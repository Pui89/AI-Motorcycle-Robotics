#!/usr/bin/env python3
"""Local-only Hugging Face OWL-ViT inference for ai-robot-motorcycle.

Uses the real Google OWL-ViT checkpoint through Transformers. It never downloads
weights or calls a hosted inference API: both processor and model load with
local_files_only=True and safetensors only. Outputs are review-only observations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

MODEL_ID = "google/owlvit-base-patch32"
MODEL_REVISION = "main"  # Override with an immutable Hub commit when pinning a local cache.
PROJECT = "ai-robot-motorcycle"
DEFAULT_LABELS = ["pedestrian","car","motorcycle","bicycle","traffic light","stop sign","road debris","pothole"]
TASK_SCOPE = "Road-scene object localization for rider advisory research. Not motorcycle-grade perception; no steering, throttle, braking, balance, or motor control."


def build_report(*, image_path: str, image_sha256: str, model_id: str,
                 revision: str, labels: list[str], threshold: float,
                 detections: list[dict[str, Any]]) -> dict[str, Any]:
    """Pure report builder; safe to test without ML dependencies or model weights."""
    if not 0.0 <= float(threshold) <= 1.0:
        raise ValueError("threshold must be in [0, 1]")
    return {
        "schema_version": "1.0",
        "project": PROJECT,
        "task": "zero-shot-object-detection",
        "model": {"id": model_id, "revision": revision},
        "input": {"image_path": image_path, "sha256": image_sha256},
        "candidate_labels": list(labels),
        "threshold": float(threshold),
        "detections": list(detections),
        "status": "MODEL_INFERENCE_REVIEW_ONLY",
        "human_review_required": True,
        "actuator_authorized": False,
        "scope": TASK_SCOPE,
        "limitations": [
            "Open-vocabulary detections can be wrong, incomplete, or overconfident.",
            "A missing detection is not evidence that an object or hazard is absent.",
            "Scores are not calibrated probabilities or validated project performance metrics.",
            "Do not use this output alone for safety-critical, enforcement, rescue, or physical-control decisions."
        ]
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=f"{PROJECT}: local-only Hugging Face OWL-ViT demo")
    parser.add_argument("image", type=Path, help="Path to a local image")
    parser.add_argument("--label", action="append", dest="labels",
                        help="Override a candidate label; repeat for multiple labels")
    parser.add_argument("--model", default=MODEL_ID, help="Hugging Face model ID or local model directory")
    parser.add_argument("--revision", default=MODEL_REVISION, help="Cached Hub revision; no network access is allowed")
    parser.add_argument("--threshold", type=float, default=0.20)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--json-out", type=Path, help="Optional JSON report output")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.image.is_file():
        print(f"Image not found: {args.image}", file=sys.stderr)
        return 2
    if not 0.0 <= args.threshold <= 1.0:
        print("--threshold must be in [0, 1]", file=sys.stderr)
        return 2
    labels = args.labels or DEFAULT_LABELS
    if not labels or any(not isinstance(x, str) or not x.strip() for x in labels):
        print("At least one non-empty candidate label is required", file=sys.stderr)
        return 2

    try:
        import torch
        from PIL import Image
        from transformers import AutoProcessor, AutoModelForZeroShotObjectDetection
    except ImportError as exc:
        print("Optional dependencies missing: install a compatible PyTorch, Transformers, and Pillow environment manually after review. Nothing is installed automatically.", file=sys.stderr)
        print(f"{type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

    if args.device == "cuda" and not torch.cuda.is_available():
        print("CUDA requested but unavailable", file=sys.stderr)
        return 2

    try:
        # Strict offline loading: no model/processor download and no hosted inference.
        processor = AutoProcessor.from_pretrained(
            args.model, revision=args.revision, local_files_only=True, trust_remote_code=False
        )
        model = AutoModelForZeroShotObjectDetection.from_pretrained(
            args.model, revision=args.revision, local_files_only=True,
            use_safetensors=True, trust_remote_code=False
        ).to(args.device).eval()
        with Image.open(args.image) as source:
            image = source.convert("RGB")
        inputs = processor(text=[labels], images=image, return_tensors="pt")
        inputs = {key: value.to(args.device) for key, value in inputs.items()}
        with torch.inference_mode():
            outputs = model(**inputs)
        target_sizes = torch.tensor([[image.height, image.width]], device=args.device)
        result = processor.post_process_object_detection(
            outputs=outputs, target_sizes=target_sizes, threshold=args.threshold
        )[0]
        detections = []
        for box, score, label_id in zip(result["boxes"], result["scores"], result["labels"]):
            coords = [round(float(v), 2) for v in box.detach().cpu().tolist()]
            detections.append({
                "label": labels[int(label_id)],
                "score": round(float(score.detach().cpu().item()), 6),
                "box_xyxy": coords
            })
        digest = hashlib.sha256(args.image.read_bytes()).hexdigest()
        report = build_report(
            image_path=str(args.image), image_sha256=digest, model_id=args.model,
            revision=args.revision, labels=labels, threshold=args.threshold,
            detections=detections
        )
    except Exception as exc:
        print(f"Local model inference failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        print("Check local model cache, revision, compatible package versions, and available RAM. The script did not attempt a download.", file=sys.stderr)
        return 1

    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    print(rendered)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(rendered + "\\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

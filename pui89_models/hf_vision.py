"""Offline-only Hugging Face vision adapters for PUI89 prototype integration.

The adapters never download model files. They can load only from an existing
local Hugging Face cache. No hosted inference API or cloud GPU is used.
"""
from __future__ import annotations

from typing import Iterable

OWLV2_MODEL_ID = "google/owlv2-base-patch16-ensemble"
DEPTH_MODEL_ID = "Intel/dpt-hybrid-midas"


def load_owlv2():
    """Load OWLv2 for open-vocabulary object proposals.

    Requires torch, transformers and Pillow to be installed separately.
    """
    try:
        from transformers import AutoProcessor, AutoModelForZeroShotObjectDetection
    except ImportError as exc:
        raise RuntimeError(
            "OWLv2 dependencies are missing. Install reviewed, compatible "
            "versions of torch and transformers only after checking local "
            "hardware, package licences and disk space."
        ) from exc

    processor = AutoProcessor.from_pretrained(
        OWLV2_MODEL_ID, local_files_only=True
    )
    model = AutoModelForZeroShotObjectDetection.from_pretrained(
        OWLV2_MODEL_ID, local_files_only=True
    )
    model.eval()
    return processor, model


def detect_objects(image, labels: Iterable[str], *, threshold: float = 0.15):
    """Return OWLv2 text-conditioned box proposals for a PIL image.

    Results are observations, not verified identities or safety decisions.
    """
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must be between 0 and 1")
    labels = [str(label).strip() for label in labels if str(label).strip()]
    if not labels:
        raise ValueError("provide at least one non-empty text label")

    import torch

    processor, model = load_owlv2()
    inputs = processor(text=[labels], images=image, return_tensors="pt")
    with torch.inference_mode():
        outputs = model(**inputs)
    target_sizes = torch.tensor([image.size[::-1]])
    result = processor.post_process_object_detection(
        outputs, threshold=threshold, target_sizes=target_sizes
    )[0]

    scores = result["scores"].detach().cpu().tolist()
    label_ids = result["labels"].detach().cpu().tolist()
    boxes = result["boxes"].detach().cpu().tolist()
    return [
        {
            "label": labels[label_id],
            "score": float(score),
            "box_xyxy": [float(v) for v in box],
            "status": "MODEL_PROPOSAL_REQUIRES_REVIEW",
        }
        for score, label_id, box in zip(scores, label_ids, boxes)
    ]


def load_dpt_hybrid():
    """Load the small Transformers-compatible Intel DPT-Hybrid checkpoint."""
    try:
        from transformers import AutoImageProcessor, AutoModelForDepthEstimation
    except ImportError as exc:
        raise RuntimeError(
            "Depth model dependencies are missing. Install reviewed, compatible "
            "versions of torch and transformers only after checking hardware, "
            "package licences and disk space."
        ) from exc

    processor = AutoImageProcessor.from_pretrained(
        DEPTH_MODEL_ID, local_files_only=True
    )
    model = AutoModelForDepthEstimation.from_pretrained(
        DEPTH_MODEL_ID, local_files_only=True
    )
    model.eval()
    return processor, model


def estimate_relative_depth(image):
    """Return a relative-depth map; values are not metric distance or water depth."""
    import torch
    import torch.nn.functional as F

    processor, model = load_dpt_hybrid()
    inputs = processor(images=image, return_tensors="pt")
    with torch.inference_mode():
        outputs = model(**inputs)
        depth = F.interpolate(
            outputs.predicted_depth.unsqueeze(1),
            size=(image.height, image.width),
            mode="bicubic",
            align_corners=False,
        ).squeeze()
    return depth.detach().cpu().numpy()


__all__ = [
    "OWLV2_MODEL_ID",
    "DEPTH_MODEL_ID",
    "load_owlv2",
    "detect_objects",
    "load_dpt_hybrid",
    "estimate_relative_depth",
]

# Hugging Face vision-model integration

**Status: prototype integration only. Model candidates are unverified, weights are not downloaded, and inference is not benchmarked. Not approved for vehicle use.**

This project now has an opt-in local adapter at [`pui89_models/hf_vision.py`](../pui89_models/hf_vision.py). It connects to real Hugging Face model checkpoints rather than placeholder model names.

## Unverified model candidates — not approved for download or vehicle use

| Checkpoint | Task | Licence shown on model card | Use in this project |
|---|---|---|---|
| [google/owlv2-base-patch16-ensemble](https://huggingface.co/google/owlv2-base-patch16-ensemble) | Text-conditioned, open-vocabulary object detection | Apache-2.0 | Candidate object localization for the project-specific research scope. |
| [Intel/dpt-hybrid-midas](https://huggingface.co/Intel/dpt-hybrid-midas) | Monocular relative-depth estimation | Apache-2.0 | Optional relative scene geometry only. |

Model-card licence labels are preliminary evidence only, not legal clearance for datasets, dependencies, upstream code, downstream uses or every project jurisdiction. Author, upstream/base-model lineage, dataset provenance and contributor provenance have not yet been independently cleared against PUI89's non-Chinese-origin preference. Keep both candidates on HOLD until that review is complete.

## Offline integration boundary — local cache only

The adapter imports without importing or downloading ML packages. It requires compatible local installations of PyTorch, Transformers and Pillow (and NumPy for the depth-map output). No package installation is performed by this repository.

1. Run the project's standard-library verification first.
2. Do not install packages as part of this prototype. First verify Python compatibility, RAM, disk space, package licences and dependency provenance.
3. The adapter is hard-locked to `local_files_only=True`; it can only use files already present in the local Hugging Face cache. There is no environment-variable or function-argument download override.
4. Any future download requires a separate user-approved change and a fresh model, licence, provenance, security and resource review.
5. Keep model weights out of Git.

Example:

```python
from PIL import Image
from pui89_models.hf_vision import detect_objects

image = Image.open("path/to/reviewed-image.jpg").convert("RGB")
proposals = detect_objects(
    image,
    labels=["person", "animal", "vehicle", "obstacle"],
    threshold=0.20,
)
print(proposals)
```

The call fails clearly if the model is not already cached. It cannot silently download anything. The detector returns candidate boxes and scores; thresholds must be calibrated on a lawful, representative, independently labelled evaluation set.

## Project-specific boundaries

- **OWLv2:** Candidate localization of road users, vehicles, signs, road-surface objects and obstacles for offline rider-advisory research only.
- **Intel DPT-Hybrid:** Optional relative scene geometry only. It cannot provide calibrated following distance, lean clearance, braking distance or riding-safety decisions.

## Important limitations

- OWLv2 is an open-vocabulary proposal model, not a project-trained detector. A text prompt does not establish that an object is present.
- Intel DPT-Hybrid produces **relative monocular depth**, not calibrated metric distance. It must not be reported as exact range, flood depth, coconut height, clearance or braking distance.
- Neither model controls motors, steering, brakes, cutters, valves, alarms, locks or other actuators.
- Preserve source, timestamp, image quality, model ID/revision, prompt, threshold, raw output, uncertainty and human-review outcome in the project's evidence records.
- Unknown, conflicting, low-quality or out-of-distribution results must remain unknown and go to human review.
- No real-world accuracy, safety, certification or product capability is claimed by adding this adapter.


## Shared AI Core integration status

The current adapter outputs remain model-proposal data. They must not be treated as trusted observations or safety decisions. The next integration change must map each proposal into the exact, versioned Shared AI Core Observation contract after reading that schema; preserve model ID and immutable revision, source image provenance, capture time, prompt, threshold, raw scores/boxes, quality flags and review state. Do not invent contract fields or silently convert model confidence into calibrated probability. Until that mapping and its contract tests exist, this is an adapter hardening step, not a completed Shared AI Core integration.

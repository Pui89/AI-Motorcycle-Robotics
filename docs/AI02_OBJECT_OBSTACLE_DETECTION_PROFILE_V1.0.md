# PUI89 AI Step-Through Scooter — AI-02 Object & Obstacle Detection Profile v1.0

**Status:** Proposed; no model, dataset, compute target or scooter integration is verified.

## Objective
Detect supported road users and immediate obstacles using the scooter's proposed forward/rear visual observations. Provide concise rider awareness with explicit uncertainty and uncovered areas. Outputs are advisory only.

## Operating domains
Evaluate forward and rear views separately. Side and rear-quarter areas remain unknown unless additional sensors are installed and validated. A front/rear camera pair is not 360-degree perception or blind-spot elimination.

## Candidate priority classes
Cars, motorcycles/scooters, bicycles, pedestrians, animals, debris, road defects where annotation supports them, cones, barriers and road-work hazards. Define ontology and priorities through requirements and rider-safety review. Retain unknown/other.

## Inputs and outputs
Consume AI-01 frames and metadata. Output class, image-space box/mask, timestamp, camera ID, model/ontology versions, confidence, uncertainty, visibility and quality. Optional tracking requires separate evaluation for vibration, motion blur and fast scene changes. Metric distance requires validated geometry or additional sensor evidence. Map through Observation, WorldState, ActionProposal and FailureReport. Never display stale detections as current or infer hazards in uncovered areas.

## Scooter-specific challenges
Test vibration, shock, lean angle, rapid scene changes, motion blur, headlamp glare, direct sunlight, rain/spray, mud, dirty lenses, night, partial occlusion and low-power/thermal constraints. Evaluate forward/rear performance separately. Rider alerts must be glanceable, brief and non-distracting.

## Evaluation
Use rights-cleared data with human-reviewed labels and splits grouped by ride/session/route/time to avoid adjacent-frame leakage. Report per-class precision/recall/F1, AP/mAP with IoU protocol, confusion matrix, false positives, missed critical objects, condition-specific performance, uncertainty, latency, CPU/RAM, energy draw and thermal behaviour. Numerical thresholds remain TBD. No gate is passed by this specification.

**Safety:** Advisory only. Rider retains steering, throttle, braking and propulsion control. Cameras do not replace mirrors or rider observation. No collision-prevention, blind-spot-elimination, adverse-weather safety or road-validation claim.
**Maturity:** Proposed profile; implementation and validation not evidenced.

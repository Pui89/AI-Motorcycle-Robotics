# PUI89 AI Step-Through Scooter — AI-01 Multi-Direction Vision Profile v1.0

**Status:** Proposed product profile. No cameras, model, compute hardware or scooter integration are established.
**Shared module:** [PUI89 Multi-Vehicle Surround Vision — Shared Module v1.0](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/architecture/PUI89_MULTI_VEHICLE_SURROUND_VISION_V1.0.md).

## 1. Purpose

Define a compact, rider-first visual awareness configuration using the shared PUI89 AI-01 capability. The scooter profile is **multi-directional vision**, not a claim of 360-degree surround coverage.

## 2. Proposed camera configuration

Initial research layout:
- CAM-F: one forward-facing camera for road context and hazards ahead.
- CAM-R: one rear-facing camera for rear context.
- Optional CAM-L / CAM-RH: side or rear-quarter cameras only if a coverage study shows meaningful benefit and mounting/power/ergonomics permit.

With only front and rear cameras, side areas remain uncovered or partially covered. Never label them as monitored blind spots or show a complete 360-degree view. Camera count, lens, field of view, resolution, frame rate, mounting and environmental rating remain TBD.

## 3. Scooter-specific engineering constraints

- Isolate vibration and shock while preserving calibration and mount integrity.
- Validate rain, spray, dust, mud, direct sun, headlamp glare and lens contamination.
- Ensure mounts and wiring do not obstruct rider view, mirrors, lights, controls, plate or required equipment.
- Define ingress protection only after the actual enclosure and assembly are tested; do not infer waterproofing from a component rating alone.
- Budget compute and camera power against the scooter's auxiliary energy system; measure standby drain and thermal behaviour.
- Design alerts for brief glanceability and low distraction; do not require complex interaction while riding.
- Essential local warnings must not depend on phone, cloud or internet connectivity.
- Inspect camera alignment and mounts after service or significant impact.

## 4. Shared AI Core interfaces

Reuse Observation, WorldState, ActionProposal and FailureReport. Include camera ID, capture/receive timestamps, calibration version, quality, freshness, confidence, uncertainty and explicit uncovered-area state. Advisory outputs may inform the rider; they may not command vehicle motion.

## 5. Verification

Test daylight, night, headlamp glare, rain/spray, dirty/blocked lens, disconnected camera, vibration-induced movement, calibration drift, timestamp skew, dropped frames, compute overload, power interruption and alert comprehension. Evaluate front/rear coverage separately and record uncovered side/rear-quarter regions.

Measure held-out precision/recall, false/missed detections, latency, resource use, energy draw, thermal behaviour and fault-detection performance. Numerical acceptance targets remain TBD pending use-case and hazard analysis.

## 6. Rider safety and evidence boundary

AI is advisory only. No autonomous steering, throttle, braking, balance or propulsion control. Cameras do not replace mirrors, rider observation or required vehicle equipment. No claim of collision prevention, blind-spot elimination, full 360-degree coverage, safe riding in adverse conditions or road validation is made.

**Maturity:** Proposed profile specified; implementation and validation not evidenced.

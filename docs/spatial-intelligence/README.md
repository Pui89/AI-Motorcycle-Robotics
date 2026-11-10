# AI Motorcycle Robotics / EasyRide: Spatial Intelligence integration profile

This project now has a project-specific spatial integration profile at
`INTEGRATION_PROFILE.json`.

## Intended use
Advisory road-surface geometry and obstacle-relative position.

## Planned tasks
- Road surface and obstacle geometry for later review
- Spatial observations linked to time and coordinate frame
- Flood-scene geometry only as a separate unvalidated research input

## Safety boundaries
- No lean, balance, traction, water-depth or rider-safety inference.
- No steering, braking, throttle or self-balancing control.
- 20 cm floodwater remains an engineering research target, not an approved riding capability.

## Shared implementation dependency
The common software interfaces are being developed in the
[PUI89 Shared AI Core Spatial Intelligence PR #26](https://github.com/Pui89/PUI89-Shared-AI-Core/pull/26).
That pull request is still a draft and has not been merged. This file records
the project-specific integration contract; it does not mean the project
currently imports or executes the shared spatial module.

Before runtime integration, require lawful sensor/data provenance, calibrated
coordinate frames, synchronized timestamps, sensor-health checks, uncertainty
handling, synthetic fault tests and project-specific human-review gates.
No physical actuation is enabled.

**Current evidence status:** profile documentation added; runtime adapter,
real sensor integration, accuracy, field performance and safety validation
remain pending. No hardware or paid service is required for this documentation
stage.

# PUI89 AI Robot Motorcycle — EasyRide Inclusive Concept

<p align="center">
  <img src="docs/EASYRIDE_CONCEPT.svg" alt="PUI89 EasyRide friendly rounded step-through AI motorcycle concept" width="100%">
</p>

**Design direction:** friendly, simple, softly rounded and approachable — with a low step-through frame, upright posture, supportive seat and easy-to-understand controls.

**Project type:** AI-enabled motorcycle research concept; software-first and simulation-first.  
**Status:** Early-stage concept and engineering foundation — not a built, tested, or road-certified vehicle.

## Mission

Develop a welcoming motorcycle concept that is easier to mount, comfortable to sit on and manageable at low speed for a broad range of adult riders. AI assistance is limited to hazard awareness, road-condition context, vehicle-health monitoring and clear advisory support. The rider remains responsible for vehicle control. No autonomous riding or physical actuation is enabled.

## EasyRide visual design

- Rounded, friendly body panels with a compact, clean silhouette.
- Low, open step-through space and a broad, low floorboard.
- Upright riding posture, supportive seat and relaxed handlebar reach.
- Clear headlamp and simple high-contrast display.
- Low-centre battery packaging as a design study, not a verified layout.
- Calm Deep Navy, pearl white, soft cyan and mint accent palette.

See the [inclusive design brief](docs/EASYRIDE_INCLUSIVE_DESIGN.md) and [concept SVG](docs/EASYRIDE_CONCEPT.svg).

## PUI89 engineering rules

- **Strict zero-cost:** no paid APIs, subscriptions, cloud GPU, paid datasets or metered services.
- **Simulation first:** no commands to physical vehicles, motors, brakes, steering or batteries.
- **Safety before features:** fail-safe behavior, human override, uncertainty reporting and hazard analysis are mandatory.
- **Evidence before claims:** distinguish implemented, simulated, proposed and independently validated capabilities.
- **Shared AI Core:** reuse PUI89 contracts and safety/evidence components; avoid duplicate core systems.
- **Security by default:** least privilege, dependency and secret checks, protected branches and review before release.
- **No unsupported performance or road-safety claims.**

## Inclusive rider-first requirements

- Make mounting and dismounting easier with a low, wide step-through opening.
- Provide upright posture, supportive seating, relaxed reach and adjustable contact points.
- Evaluate low-centre-of-gravity packaging without sacrificing strength or braking capability.
- Design readable displays, tactile controls, clear lighting and adjustable advisory alerts.
- Validate fit with diverse adult riders; never claim one size fits everyone.
- Treat ABS, traction control, hill-hold, walk-assist and reverse-assist as proposed features requiring qualified engineering and validation.

## Initial AI capability areas

1. Rider-assistance concept: hazard detection and clear warnings.
2. Vehicle health: monitored-state model for battery, electrical, thermal and component anomalies.
3. Environmental awareness: road surface, weather, visibility and nearby-object observations where lawful datasets or simulation are available.
4. Safety supervisor: confidence thresholds, stale-data detection, conflict handling, safe degradation and human override.
5. Evidence and evaluation: scenario-based tests, false-positive/false-negative tracking, latency measurement and reproducible reports.

## Development stages

1. Define requirements, hazards, operating boundaries and shared AI Core interfaces.
2. Build software-only data contracts and deterministic baseline logic.
3. Create synthetic/simulation scenarios; do not connect to a real motorcycle.
4. Add evaluation, robustness, security and regression tests.
5. Consider hardware only after documented safety reviews, legal review and qualified engineering validation.

## Weight and validation boundary

An early feasibility study may explore a 95–110 kg vehicle-mass target, excluding optional accessories. This is an unvalidated research target, not a final specification. Rider fit, structural strength, braking, stability, load capacity and regulatory requirements take priority over weight reduction.

Water resistance, fire resistance, battery safety, braking performance and durability are requirements to investigate and test — they are not verified capabilities.

## Current truth

This repository is an initial software and research scaffold. It does not contain a functioning motorcycle, validated perception model, real-time vehicle integration or certified safety system. All outputs are advisory prototypes until independently validated.

## Repository map

- `docs/PROJECT_PLAN.md` — scope, architecture and staged roadmap.
- `docs/EASYRIDE_INCLUSIVE_DESIGN.md` — rider ergonomics, inclusive design, durability and validation requirements.
- `docs/EASYRIDE_CONCEPT.svg` — original friendly EasyRide concept illustration; not production CAD.
- `docs/SAFETY_CASE.md` — hazards, safeguards and validation boundaries.
- `SECURITY.md` — vulnerability reporting and security policy.
- `tests/` — software-only tests.
- `.github/workflows/quality.yml` — dependency-light automated checks.

## License

See the repository's [LICENSE](LICENSE) file for the applicable permissions and conditions.

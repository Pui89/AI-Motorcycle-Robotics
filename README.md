# PUI89 AI Robot Motorcycle — EasyRide Inclusive Concept

**Repository:** `Pui89/ai-robot-motorcycle`  
**Project type:** Advanced AI-enabled motorcycle concept; software-first, simulation-first  
**Status:** Early-stage concept and engineering foundation — not a built, tested, or road-certified vehicle.

## Mission

Develop a friendly, low-step-through, rider-first motorcycle concept that is easier to mount, comfortable to operate, manageable at low speed, and designed for a broad range of adult riders. The AI assistance concept focuses on hazard awareness, road-condition context, vehicle-health monitoring, and clear advisory support. The rider remains responsible for control. No autonomous riding or physical actuation is enabled by this repository.\n\n**Design direction:** PUI89 EasyRide — low step-through frame, upright posture, supportive seat, adjustable rider contact points, low-centre-of-gravity packaging, simple high-contrast controls, and robust serviceable construction. See [inclusive design brief](docs/EASYRIDE_INCLUSIVE_DESIGN.md) and [concept SVG](docs/EASYRIDE_CONCEPT.svg).

## PUI89 engineering rules

- **Strict zero-cost:** no paid APIs, subscriptions, cloud GPU, paid datasets, or services that can create charges.
- **Simulation first:** no commands to physical vehicles, motors, brakes, steering, or batteries.
- **Safety before features:** fail-safe behavior, human override, uncertainty reporting, and hazard analysis are mandatory.
- **Evidence before claims:** distinguish implemented, simulated, proposed, and independently validated capabilities.
- **Shared AI Core:** reuse PUI89 contracts and safety/evidence components; do not create duplicate core systems.
- **Security by default:** least privilege, dependency and secret checks, protected branches, and review before release.
- **No unsupported performance or road-safety claims.**

## Inclusive rider-first product requirements\n\n- Make mounting and dismounting easier with a low, wide step-through opening.\n- Provide an upright posture, supportive seat, relaxed reach and adjustable contact points.\n- Evaluate low-centre-of-gravity packaging and compact, manageable mass without sacrificing strength or braking capability.\n- Design readable displays, tactile controls, clear lighting and adjustable advisory alerts.\n- Validate fit with diverse adult riders; never claim that one size fits everyone.\n- Treat ABS, traction control, hill-hold, walk-assist and reverse-assist as proposed conventional vehicle features requiring qualified engineering and validation.\n\n## Initial capability areas

1. Rider-assistance concept: hazard detection and clear warnings.
2. Vehicle health: monitored-state model for battery, electrical, thermal, and component anomalies.
3. Environmental awareness: road surface, weather, visibility, and nearby-object observations where lawful datasets or simulation are available.
4. Safety supervisor: confidence thresholds, stale-data detection, conflict handling, safe degradation, and human override.
5. Evidence and evaluation: scenario-based tests, false-positive/false-negative tracking, latency measurement, and reproducible reports.

## Development stages

1. Define requirements, hazards, operating boundaries, and shared AI Core interfaces.
2. Build software-only data contracts and deterministic baseline logic.
3. Create synthetic/simulation scenarios; do not connect to a real motorcycle.
4. Add evaluation, robustness, security, and regression tests.
5. Consider hardware only after documented safety reviews, legal review, and qualified engineering validation.

## Repository map

- `docs/PROJECT_PLAN.md` — scope, architecture, and staged roadmap.\n- `docs/EASYRIDE_INCLUSIVE_DESIGN.md` — rider ergonomics, inclusive design, durability and validation requirements.\n- `docs/EASYRIDE_CONCEPT.svg` — original conceptual illustration (not production CAD).
- `docs/SAFETY_CASE.md` — hazards, safeguards, and validation boundaries.
- `SECURITY.md` — vulnerability reporting and security policy.
- `tests/` — software-only tests.
- `.github/workflows/quality.yml` — dependency-light automated checks.

## Free AI and advanced engineering resources

Use the curated [PUI89 Free AI & Advanced Engineering Stack](docs/FREE_AI_TECH_STACK.md). It covers local AI runtimes, agentic workflows, computer vision, vehicle/robot simulation, CAD, testing and security tools. All adoption is subject to the strict zero-cost gate, exact licence review, hardware feasibility checks and simulation-only safety boundary.

## Inclusive design and weight target\n\nThe early feasibility study may explore a 95–110 kg vehicle mass target, excluding optional accessories. This is an unvalidated design target, not a final specification. Rider fit, structural strength, braking, stability, load capacity and regulatory requirements take priority over weight reduction. The concept is intended to serve a broad range of riders, but universal suitability cannot be assumed.\n\n## Current truth

This repository is an initial software and research scaffold. It does not contain a functioning motorcycle, validated perception model, real-time vehicle integration, or certified safety system. All outputs are advisory prototypes until independently validated.

## License

No license has been selected yet. Unless and until a license is added, standard copyright restrictions apply; do not assume this repository is open source.

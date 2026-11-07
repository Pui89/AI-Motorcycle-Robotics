# PUI89 AI Robot Motorcycle — EasyRide Inclusive Concept

## Project website QR codes

<table><tr><td align="center"><strong>English website</strong><br><a href="https://pui89.github.io/ai-robot-motorcycle.html"><img src="https://pui89.github.io/qr/ai-robot-motorcycle-en.png" width="160" alt="PUI89 AI Robot Motorcycle English website QR code"></a><br><a href="https://pui89.github.io/ai-robot-motorcycle.html">Open English website</a></td><td align="center"><strong>เว็บไซต์ภาษาไทย</strong><br><a href="https://pui89.github.io/ai-robot-motorcycle-th.html"><img src="https://pui89.github.io/qr/ai-robot-motorcycle-th.png" width="160" alt="QR Code เว็บไซต์ภาษาไทย PUI89 AI Robot Motorcycle"></a><br><a href="https://pui89.github.io/ai-robot-motorcycle-th.html">เปิดเว็บไซต์ภาษาไทย</a></td></tr></table>

## PUI89 product maturity snapshot — 7 November 2026

**Strategic direction: From AI Projects to AI Products.**  
**Current maturity: Grade 1–2 — Product Concept and Early Engineering Foundation.** EasyRide defines an inclusive, step-through two-wheel motorcycle direction and an initial software/research scaffold. It is not a functioning, tested or road-certified motorcycle.

| Area | Verified position |
|---|---|
| Product definition | Rider-first two-wheel concept with easy step-through access, upright posture, supportive seating and practical everyday usability. |
| Inclusive requirements | Low/open step-through, broad non-slip footboard, snag-risk reduction, readable controls and diverse adult-rider fit are design requirements requiring user testing. |
| Software and AI | Software-first and simulation-first research scaffold; opt-in model-adapter code is documented, but model inference and motorcycle-specific accuracy are not yet tested. |
| Physical product | No built motorcycle, validated braking/stability, load capacity, battery layout, weather protection or road certification is established. |

**Next product gate:** translate rider needs into measurable ergonomic and safety requirements; assess entry/exit, clothing snag hazards, centre of gravity, structural loads, braking, stability, battery/thermal protection, serviceability and regulatory constraints. Create deterministic software/simulation scenarios before considering physical integration.

**Product discipline:** the rider retains control; no autonomous riding or physical actuation is enabled. Water resistance, fire performance, durability and road safety are requirements for qualified engineering and testing, not existing capabilities. No paid API, cloud GPU, automatic model download or physical vehicle actuation is part of this update.



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
- Low, open step-through space and a broad, non-slip floorboard designed to make mounting in skirts or dresses easier.
- Smooth leg-area panels and a fully enclosed chain/belt design target to reduce clothing snag points; actual clothing clearance and safety require user testing.
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

- Make mounting and dismounting easier with a low, wide step-through opening, including for riders wearing skirts or dresses.
- Provide a broad, flat, non-slip footboard, smooth snag-resistant side covers and an enclosed chain/belt layout; test hem clearance and safe foot placement.
- Do not claim all clothing is safe: loose or long fabric can still catch in wheels or moving parts, so protective riding gear and clothing guidance remain important.
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

## Agentic AI, VLM and VLA research direction

The roadmap explores three complementary areas for rider-first assistance. These are **planned research directions**, not claims that the models or capabilities are already implemented.

### 1. Agentic AI — bounded rider-support agents
- Explore agents for organizing observations, checking data freshness, summarizing road/weather context, tracking vehicle-health evidence and preparing understandable rider advisories.
- Require explicit task boundaries, provenance, confidence, uncertainty reporting and human approval for consequential outputs.
- Keep deterministic safety gates independent of agent reasoning. Agents cannot control the motorcycle or override the rider.

### 2. Vision-Language Models (VLMs) — visual scene understanding
- Research image-and-text understanding for road-surface conditions, obstacles, signs, visibility, nearby objects and vehicle inspection observations.
- Evaluate lighting, rain, occlusion, camera placement, motion blur, domain shift, false alarms and missed hazards using licensed datasets or synthetic scenarios.
- Treat every output as an uncertain observation with source and timestamp; use clear advisory wording and preserve rider attention.

### 3. Vision-Language-Action (VLA) — mock action proposals only
- Study VLA methods in simulation to translate visual/language context into structured **non-executing** proposals, such as “increase following-distance awareness” or “ask the rider to inspect a warning”.
- Store proposals as typed **ActionProposal** records with preconditions, confidence, expected effects, risk and evidence references.
- Do not generate or execute steering, throttle, braking, acceleration, gear, motor, battery or other physical-control commands. The rider remains in control at all times.
- Any future hardware study requires a separate safety case, qualified engineering, regulatory review and validated rider testing.

**Research sequence:** shared AI Core contracts → deterministic rider-advisory baseline → synthetic/simulation scenarios → VLM evaluation → bounded agent orchestration → mock VLA proposals → robustness, usability and safety evaluation. No new model weights, packages, paid APIs, subscriptions or cloud compute are required or authorized by this roadmap.

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

## PUI89 portfolio links

- **English project page:** [PUI89 EasyRide AI Motorcycle](https://pui89.github.io/ai-robot-motorcycle.html)
- **Thai project page:** [PUI89 EasyRide AI Motorcycle — ภาษาไทย](https://pui89.github.io/ai-robot-motorcycle-th.html)
- **PUI89 main portfolio:** [https://pui89.github.io/](https://pui89.github.io/)
- **Website source repository:** [Pui89/Pui89.github.io](https://github.com/Pui89/Pui89.github.io)
- **Car companion project:** [PUI89 AI Robot Car](https://github.com/Pui89/ai-robot-car)

## License

See the repository's [LICENSE](LICENSE) file for the applicable permissions and conditions.


## Hugging Face vision models — opt-in local integration

This repository now includes real Hugging Face checkpoint adapters in [`pui89_models/hf_vision.py`](pui89_models/hf_vision.py), with project-specific usage boundaries in [`docs/HUGGING_FACE_MODEL_INTEGRATION.md`](docs/HUGGING_FACE_MODEL_INTEGRATION.md).

- **OWLv2:** `google/owlv2-base-patch16-ensemble` for text-conditioned object proposals.
- **Intel DPT-Hybrid:** `Intel/dpt-hybrid-midas` for relative scene depth where appropriate; not calibrated distance or physical depth.
- **Zero-cost default:** no packages or model weights are installed/downloaded automatically; CPU-only inference, local cache only by default, no hosted inference API or cloud GPU.
- **Evidence status:** adapter code is added; model inference and project-specific accuracy are NOT YET TESTED. Outputs remain uncertain observations for human review, never actuator commands.

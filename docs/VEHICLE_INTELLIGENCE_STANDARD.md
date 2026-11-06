# PUI89 Vehicle Intelligence Standard (PVIS)
**Standard ID:** PVIS-1.0  
**Applies to:** PUI89 AI Car and AI Motorcycle  
**Status:** Engineering standard for research and simulation; not a safety certification.

## 1. Purpose
Provide one consistent, evidence-led intelligence architecture for PUI89 road-vehicle projects. The standard governs perception, vehicle/environment state estimation, risk reasoning, advisory decisions, uncertainty, human oversight, cybersecurity, validation, and reporting. Both projects must reuse the PUI89 Shared AI Core rather than create competing copies.

## 2. Intelligence architecture
Every implementation should follow this pipeline:

1. **Sense and ingest** — accept only declared sensor/data sources; record source identity, timestamp, units, calibration state, integrity, and permissions.
2. **Validate evidence** — detect missing, malformed, stale, out-of-range, duplicated, conflicting, or potentially manipulated inputs.
3. **Perceive** — identify relevant road users, obstacles, road geometry, signs/signals, weather/visibility, and vehicle condition only where supported by available data.
4. **Estimate state** — produce a versioned WorldState with freshness, confidence/uncertainty, provenance, and known limitations.
5. **Assess risk** — estimate hazard severity, likelihood, exposure, time sensitivity, and uncertainty; do not present estimates as certainty.
6. **Propose** — produce advisory ActionProposal records with rationale, supporting evidence, confidence, expiry, and authority boundary.
7. **Apply safety gate** — reject unsupported, stale, contradictory, out-of-scope, or unsafe proposals; fail safely when evidence is inadequate.
8. **Human-facing output** — communicate the hazard, evidence, uncertainty, recommended response, and what the system cannot determine.
9. **Record and learn** — retain privacy-conscious, reproducible evaluation records; changes to models/rules require regression tests and documented review.

## 3. Shared AI Core contracts
Use the canonical PUI89 contracts and version them consistently:
- **Observation:** source, timestamp, value, units, quality, confidence, calibration, provenance.
- **WorldState:** estimated entities/conditions, timestamp, freshness, uncertainty, evidence links, limitations.
- **ActionProposal:** advisory action, rationale, evidence, confidence, expiry, required human authority, prohibited actuation.
- **FailureReport:** failure mode, severity, detection evidence, containment, recovery recommendation, unresolved risk.

Do not fork or silently redefine these contracts inside either vehicle repository. Record the compatible AI Core version/commit when integration is implemented.

## 4. Vehicle intelligence capability domains
Implement and evaluate capabilities independently; a project must not claim a capability merely because it appears in this list.

### A. Road and scene understanding
- Road boundaries, lanes, junctions, signs/signals, obstacles, road surface, visibility, and temporary hazards.
- Vulnerable road users and unusual objects, with conservative uncertainty handling.
- Weather, lighting, occlusion, glare, and sensor degradation awareness.

### B. Dynamic hazard reasoning
- Potential collision paths, closing distance/speed where measurable, blind-zone risk, unsafe following distance, sudden obstacles, and loss-of-traction indicators.
- Separate observed facts from inferred intent or predicted motion.
- Escalate uncertainty when objects are partially visible or sensor sources disagree.

### C. Vehicle health intelligence
- Monitor only available and validated signals: battery/electrical state, temperature, tire/pressure data, braking/steering diagnostics, motor/engine status, and fault codes as applicable.
- Detect abnormal trends and recommend inspection; do not claim predictive accuracy without longitudinal validation.
- Treat safety-critical faults as requiring a human/operator response.

### D. Context and driver/rider support
- Present timely, understandable warnings and route/condition context when data is available.
- Avoid distracting, excessive, ambiguous, or falsely reassuring alerts.
- Provide accessible explanation and clear escalation to the human operator.

### E. Degraded-mode intelligence
- Detect sensor failure, low confidence, stale data, communication loss, model faults, and out-of-distribution conditions.
- Reduce claims and functionality as evidence quality falls; show “unknown” rather than fabricate a state.
- Never allow degraded perception to silently increase system authority.

## 5. Authority and safety boundaries
- PVIS systems are **advisory and proposal-only** by default.
- No direct steering, throttle, braking, gear, propulsion, or other actuator control is authorized by this standard.
- No autonomous driving/riding, remote vehicle operation, or physical testing is implied.
- A human remains responsible for vehicle operation and must not be encouraged to rely solely on AI.
- Simulation results do not establish public-road safety, legal compliance, or real-world performance.
- Any future actuation research requires a separate hazard analysis, independent safety review, controlled test plan, and explicit authorization.

## 6. Cybersecurity and data integrity
- Apply least privilege, protected branches, reviewed changes, dependency pinning/review, secret scanning where available at no cost, and minimal workflow permissions.
- Never commit credentials, private keys, personal location histories, or identifiable driver/rider data.
- Validate external inputs; defend against spoofing, replay, tampering, malformed files, and compromised dependencies.
- Keep provenance and audit records for datasets, model weights, configuration, and evaluation runs.
- Do not add paid services, metered APIs, cloud GPUs, or subscriptions without explicit approval. Default development must remain zero-cost.

## 7. Environmental and electrical design inputs
For future physical prototypes, document water ingress, dust, vibration, impact, heat, cold, fire, battery thermal runaway, electrical isolation, and emergency power isolation as engineering hazards.
- Set measurable environmental requirements before selecting an enclosure or components.
- IP ratings, fire resistance, battery safety, and roadworthiness must be supported by applicable independent physical tests and certification; software documentation cannot establish them.
- Do not expose people to hazardous tests or perform uncontrolled road tests.

## 8. Verification and evidence requirements
Each capability must have:
- a written requirement and explicit operating conditions;
- representative test data with lawful licensing and provenance;
- unit, integration, regression, and negative/failure-mode tests;
- metrics with definitions, baselines, sample sizes, and limitations;
- calibration and uncertainty assessment where relevant;
- reproducible test instructions and recorded results;
- documented known failure cases and human-oversight requirements.

Test missing, noisy, stale, conflicting, corrupted, spoofed, and out-of-distribution inputs. Include false positives, false negatives, latency only when measured, and subgroup/condition performance where data supports it. Do not use a single aggregate score to conceal critical failures.

## 9. Required status labels
Use these labels in documentation and public claims:
- **Proposed** — specified but not implemented.
- **Implemented** — code exists; not necessarily validated.
- **Simulation-tested** — passed named simulation tests only.
- **Bench-tested** — tested on controlled physical equipment.
- **Field-tested** — tested in a defined real-world setting with documented controls.
- **Independently validated/certified** — only when supported by named independent evidence or certification.

Never upgrade a status without new evidence. State the version, test conditions, date, and limitations.

## 10. Mandatory project report
Every release or evaluation report must state:
1. What is known?
2. What is unknown or unobservable?
3. What changed since the previous version?
4. What failed, including near misses and unsupported cases?
5. What risk remains and who must act?
6. What is recommended next?
7. What evidence demonstrates improvement?

## 11. Project-specific extensions
- **AI Car:** add vehicle-class, cabin/occupant privacy, automotive electrical architecture, and car-specific visibility/geometry test scenarios.
- **AI Motorcycle:** add rider vulnerability, balance/lean context, two-wheel traction, road-surface contamination, protective-equipment awareness only where observable, and stricter distraction/minimal-alert design. Do not infer rider condition or intent without validated evidence.

## 12. Acceptance checklist
A feature is not ready to be described as validated unless:
- [ ] its requirement and operating domain are defined;
- [ ] data provenance and permissions are recorded;
- [ ] uncertainty and degraded modes are tested;
- [ ] safety and cybersecurity tests pass;
- [ ] regression results are reproducible;
- [ ] human authority boundaries are explicit;
- [ ] claims match the evidence and status label;
- [ ] no unapproved cost or paid dependency was introduced.

---
**PUI89 principle:** Intelligence must be evidence-grounded, uncertainty-aware, human-supervised, secure by design, and incapable of silently claiming more authority or capability than has been validated.

# Project Plan — PUI89 AI Robot Motorcycle

## 1. Product definition

A future AI-enabled motorcycle assistance platform. The first deliverable is a software-only research prototype, not a rideable vehicle or autonomous driving system.

### Intended assistance functions

- Detect and communicate possible hazards from available observations.
- Monitor modeled vehicle health and identify abnormal or missing telemetry.
- Track uncertainty, data freshness, sensor disagreement, and evidence provenance.
- Present concise recommendations to a human rider.
- Enter a conservative degraded state when inputs are missing, stale, conflicting, or unreliable.

### Explicit exclusions for the initial phase

- No autonomous steering, throttle, braking, lane changes, or riding.
- No direct connection to a real vehicle, CAN bus, ECU, battery-management system, or actuator.
- No claims of roadworthiness, collision avoidance, or certified functional safety.
- No collection or processing of personal/rider data beyond synthetic test fixtures.

## 2. Shared PUI89 AI Core integration

Reuse the shared PUI89 architecture rather than creating project-specific copies of core infrastructure. Align to these contracts:

- `Observation`: source, timestamp, observed value, quality, confidence, and provenance.
- `WorldState`: current modeled state, freshness, uncertainty, and known limitations.
- `ActionProposal`: advisory proposal only; explicit authority boundary and rationale.
- `FailureReport`: failure mode, severity, evidence, containment, and recovery recommendation.

Required cross-cutting capabilities:

- Evidence integrity and provenance.
- Uncertainty propagation and calibration records.
- Missing, noisy, stale, and conflicting evidence handling.
- Safety gates and human override.
- Reproducible benchmark and regression records.
- Clear status labels: implemented, simulated, proposed, and validated.

Do not duplicate shared components. Record the version or commit of any shared-core interface used by this project.

## 3. Initial architecture

1. Input adapters — synthetic scenario observations only.
2. Validation layer — schema, range, timestamp, provenance, and freshness checks.
3. State estimator — transparent baseline state aggregation; uncertainty retained.
4. Hazard reasoning — deterministic rules first, with traceable evidence.
5. Safety supervisor — blocks unsafe or unsupported proposals.
6. Rider information layer — warning severity, rationale, uncertainty, and recommended human action.
7. Evaluation harness — scenario replay, metrics, regression, and evidence reports.

All interfaces remain software-only. Any future hardware interface must be isolated behind an explicitly disabled adapter and a separate safety review.

## 4. Safety and security engineering

- Define operational design domain and assumptions before model development.
- Analyze hazards including false negatives, false positives, distraction, stale data, sensor failure, power loss, overheating, water ingress, fire, battery faults, tampering, and software update failure.
- Prefer fail-silent or conservative advisory behavior over confident output from poor evidence.
- Never let a model output directly command an actuator.
- Keep credentials out of source control; use least-privilege repository permissions.
- Review dependencies and licenses before adoption.
- Test malformed input, sensor disagreement, missing data, time drift, and interrupted processing.
- Treat environmental resistance as a design requirement to validate physically, not a software claim or an assumed IP rating.

## 5. Zero-cost development policy

Allowed by default: Python standard library, Git, GitHub features that are available at no charge, local synthetic fixtures, and free documentation.

Before adding any external tool, model, package, dataset, or hosted service, check:
- license and commercial-use terms;
- privacy and data provenance;
- hardware/RAM/disk requirements;
- whether a free tier can trigger billing;
- whether a standard-library alternative is sufficient.

Do not enable paid plans, paid runners, cloud compute, or metered APIs.

## 6. Roadmap and exit criteria

### Phase 0 — foundation
- [x] Establish repository scope and truth-in-claims policy.
- [x] Document safety boundaries and initial architecture.
- [ ] Align contracts with the canonical PUI89 AI Core.

### Phase 1 — software contracts
- [ ] Implement typed observation, world-state, proposal, and failure-report schemas.
- [ ] Add deterministic validation and safety-gate tests.
- [ ] Add explicit stale/missing/conflicting-data behavior.

### Phase 2 — simulation and evaluation
- [ ] Build synthetic motorcycle scenarios.
- [ ] Add hazard scenarios and repeatable replay.
- [ ] Report precision/recall where labels exist, false alarms, missed hazards, latency, and uncertainty behavior.
- [ ] Add regression thresholds with documented rationale.

### Phase 3 — research prototypes
- [ ] Evaluate perception approaches only with legally usable, documented datasets.
- [ ] Compare against deterministic baselines.
- [ ] Document limitations and failure cases.

### Phase 4 — independent engineering review
- [ ] Qualified vehicle, electrical, battery, cybersecurity, and functional-safety review.
- [ ] Legal and regulatory review for intended markets.
- [ ] Controlled test plan and independent evidence before any hardware integration.

## 7. Definition of done

A feature is not complete merely because code runs. It needs requirements, tests, traceable evidence, known limitations, security review, and documented failure behavior. Hardware or road-safety claims require appropriate independent validation.

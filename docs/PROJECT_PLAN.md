# Project Plan — PUI89 AI Robot Motorcycle

## Product definition
A future AI-enabled motorcycle assistance platform. The first deliverable is a software-only research prototype, not a rideable vehicle or autonomous riding system.

### Intended assistance functions
- Detect and communicate possible hazards from available observations.
- Monitor modeled vehicle health and identify abnormal or missing telemetry.
- Track uncertainty, freshness, sensor disagreement, and evidence provenance.
- Present concise recommendations to a human rider.
- Enter a conservative degraded state when inputs are missing, stale, conflicting, or unreliable.

### Explicit exclusions
- No autonomous steering, throttle, braking, lane changes, or riding.
- No connection to a real vehicle, CAN bus, ECU, BMS, or actuator.
- No roadworthiness, collision-avoidance, or certified functional-safety claims.
- Synthetic fixtures only in this phase; no rider personal data.

## Shared PUI89 AI Core
Reuse, do not fork, the shared Observation, WorldState, ActionProposal, and FailureReport contracts. Required capabilities: evidence integrity, uncertainty propagation, missing/noisy/stale/conflicting-data handling, safety gates, human override, reproducible benchmarks, and clear implemented/simulated/proposed/validated labels. Runtime integration remains DESIGN_ONLY_NOT_CONNECTED until adapters and cross-repository tests exist.

## Software architecture
1. Synthetic scenario input.
2. Schema, range, provenance, and freshness validation.
3. Transparent deterministic baseline.
4. Risk-state classification with traceable rationale.
5. Advisory-only safety boundary.
6. Scenario replay and regression evidence.

No physical sensor, vehicle bus, or actuator interface is included.

## Motorcycle-specific risks
- Rider fall, loss of balance, and lean-state uncertainty.
- Reduced traction, wheel slip, wet paint, gravel, mud, oil, ice, potholes, and uneven road surfaces.
- Braking and stopping-distance uncertainty; no real stopping-distance guarantee is modeled.
- Nearby vehicles, pedestrians, cyclists, blind spots, and closing hazards.
- Poor visibility, glare, rain, night conditions, and occlusion.
- Battery/electrical faults, overheating, water ingress, fire, vibration, and connector damage.
- Rider distraction from excessive, late, ambiguous, or false alerts.
- Cybersecurity, malicious inputs, sensor spoofing, and compromised updates.

## Strict zero-cost policy
Allowed by default: Python standard library, Git, synthetic fixtures, and free documentation. No paid APIs, subscriptions, paid datasets, cloud GPUs, paid runners, or metered services. Before adopting any model/package/tool, check licence, commercial-use terms, privacy, disk/RAM requirements, and billing exposure. Do not install dependencies merely for convenience.

## Roadmap and exit criteria
### Phase 0 — foundation
- [x] Define software-first scope and non-actuation boundary.
- [x] Document preliminary hazards and safety constraints.
- [x] Add synthetic rider-risk, traction, and road-surface scenarios.
- [x] Add deterministic baseline and standard-library regression tests.
- [ ] Align interface versions with canonical PUI89 AI Core.

### Phase 1 — contract and evidence maturity
- [ ] Add versioned Observation / WorldState / ActionProposal / FailureReport schemas or adapters.
- [ ] Add explicit uncertainty, provenance, and sensor-conflict fixtures.
- [ ] Generate machine-readable test reports and compare regression history.

### Phase 2 — richer simulation
- [ ] Add synthetic time-series for lean, wheel slip, braking, visibility, and hazard approach.
- [ ] Add fault injection: missing, delayed, frozen, noisy, contradictory, and spoofed observations.
- [ ] Document assumptions; illustrative thresholds must never be treated as safe limits.

### Phase 3 — research evaluation
- [ ] Evaluate perception approaches only with legally usable, documented data.
- [ ] Compare candidate models against deterministic baselines.
- [ ] Report false positives, missed hazards, calibration, latency, and limitations.

### Phase 4 — independent engineering review
- [ ] Qualified motorcycle-dynamics, vehicle, electrical, battery, cybersecurity, and functional-safety review.
- [ ] Legal/regulatory review for intended markets.
- [ ] Controlled test plan and independent evidence before hardware integration.

## Definition of done
Code execution alone is not completion. Each capability needs requirements, tests, traceable evidence, known limitations, security review, and documented failure behavior. Hardware or road-safety claims require independent validation.

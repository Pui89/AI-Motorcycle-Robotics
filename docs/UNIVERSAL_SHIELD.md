# PUI89 Universal SHIELD
**Standard:** PUI89-USS-1.0  
**Scope:** All six PUI89 projects  
**Status:** Cross-project engineering and software governance standard; not a physical safety certification.

## Mission
Protect people, animals, assets, data, and project integrity through evidence-led risk detection, prevention, warning, containment, response, and recovery. Apply the same governance and shared intelligence interfaces across all six projects without duplicating the PUI89 AI Core.

## Six-project scope
1. Coconut Harvest AI — agricultural perception and harvesting-robot concept.
2. Flood Rescue AI — flood/disaster rescue-robot concept.
3. Multimodal Narcotics Screening AI — multimodal screening decision-support and robotic concept.
4. Homeguard AI Nomad — home/environment monitoring platform and future robot concept.
5. AI Car — vehicle intelligence and driver-assistance research.
6. AI Motorcycle — rider-focused vehicle intelligence research.

## 1. Physical safety and environmental protection
Every project must maintain a hazard register covering foreseeable people/animal exposure, pinch/crush/cut/impact, entanglement, falls, collision, instability, environmental exposure, maintenance, transport, and foreseeable misuse.
- Define operating domain, exclusions, safe states, emergency stop/isolation concept, and human authority before implementation.
- Use simulation and non-actuating prototypes first. No physical actuation or field operation is implied by software readiness.
- For physical concepts, document ingress, dust, vibration, shock, impact, corrosion, UV, temperature, humidity, and structural-load requirements as applicable.
- Require controlled engineering tests before claiming any physical protection or operational capability.

## 2. Fire, water, electrical and battery protection
Maintain project-specific hazard analyses for water ingress, flooding, fire/heat, smoke, electrical shock/short circuit, overcurrent, insulation failure, battery damage, charging faults, and thermal runaway.
- Specify measurable design requirements, detection limits, containment, isolation, evacuation/withdrawal, and recovery procedures.
- Prefer fail-safe power isolation and protected energy storage in future hardware designs; do not prescribe unsafe DIY battery modifications.
- Treat water exposure and fire resistance as design/test requirements, not properties created by AI.
- Never claim an IP rating, waterproofing, fire resistance, battery safety, or certification without applicable independent physical test evidence.
- Software alerts are advisory and cannot replace certified alarms, protective equipment, emergency services, or trained responders.

## 3. Cybersecurity and anti-tampering
Apply secure-by-default controls to code, data, models, devices, and workflows:
- Least privilege for repository, workflow, device, and data access.
- Protected default branch, review before merge where feasible, and no unreviewed direct production deployment.
- Never commit tokens, passwords, private keys, personal data, or sensitive operational details.
- Validate and constrain inputs; detect malformed, replayed, spoofed, stale, conflicting, and tampered evidence.
- Record provenance and integrity metadata for datasets, model files, configuration, and test artifacts.
- Review dependencies, licenses, update provenance, and workflow permissions; pin dependencies/actions where practical.
- Use available no-cost repository security controls. Do not enable paid plans, paid scanners, metered services, or billing features.
- Define a response path: identify, contain, preserve evidence, rotate/revoke affected credentials, recover from trusted state, test, and document.

## 4. Hazard prediction and early warnings
Use a consistent risk record with hazard, affected party/asset, observed evidence, source/time, likelihood estimate, severity, exposure, uncertainty, confidence, warning threshold, recommended action, and expiry.
- Separate observed facts from inferred conditions and predictions.
- Display unknown or insufficient evidence instead of fabricating certainty.
- Escalate when evidence is stale, contradictory, low quality, out of distribution, or sensor integrity is uncertain.
- Tune warnings for both missed hazards and nuisance alerts; document false positives/negatives and operating conditions.
- Do not claim predictive accuracy until representative validation supports it.

## 5. Emergency response and recovery
Each project must document:
1. Detection and alert trigger.
2. Immediate safe-state recommendation and prohibited actions.
3. Human/operator notification and escalation route.
4. Emergency-service or trained-responder boundary where applicable.
5. Isolation/containment and protection of people and animals.
6. Evidence preservation without delaying life-safety action.
7. Recovery, inspection, restart authorization, and post-incident review.
8. Lessons learned and regression tests.

The system must never delay contacting emergency services when there is immediate danger. AI must not autonomously perform enforcement, rescue, medical, or safety-critical physical actions under this standard.

## 6. Shared AI Core integration across all six projects
Use one canonical, versioned PUI89 AI Core. Each project consumes the same contract definitions and records the compatible core version/commit. Do not fork or silently redefine shared contracts.

Required contracts:
- **Observation:** source, timestamp, value, units, quality, confidence, calibration, provenance, integrity status.
- **WorldState:** estimated state/entities, freshness, uncertainty, evidence references, operating domain, limitations.
- **ActionProposal:** advisory proposal, rationale, supporting evidence, confidence, expiry, required human authority, prohibited actuation.
- **FailureReport:** failure mode, severity, detection evidence, containment, recovery recommendation, unresolved risk.

Required shared services/interfaces:
- input validation and evidence integrity;
- provenance and audit trail;
- uncertainty propagation and calibration records;
- risk scoring with explicit assumptions;
- safety gate and proposal-only authority boundary;
- degraded-mode handling and fail-safe recommendations;
- benchmark/evaluation record format;
- consistent status and incident reporting.

A project-specific adapter may map local sensors/domains into canonical contracts; it must not create a competing core implementation.

## 7. Automated testing, benchmarks and evidence
Every repository must have a dependency-light test path and a reproducible evidence record.
- Unit, contract, integration, regression, negative, and failure-mode tests as appropriate.
- Test missing, noisy, stale, contradictory, malformed, corrupted, spoofed, and out-of-domain inputs.
- Test safety gates, authority boundaries, warning logic, emergency states, and recovery transitions.
- Record benchmark definition, dataset provenance/license, split methodology, baseline, sample size, metrics, uncertainty, limitations, environment, commit, and date.
- Keep test fixtures synthetic or lawfully sourced; do not treat unverified candidate data as training-approved.
- CI should use minimal permissions and no paid runner/service. Avoid unnecessary dependencies and downloads.
- A passing software test does not prove physical safety or real-world performance.

## 8. Strict zero-cost development
Default policy for all six projects:
- No paid APIs, subscriptions, cloud GPUs, metered services, paid datasets, or billable hosting.
- No package installation, model download, workflow expansion, or external service activation without checking licensing, resource needs, security, and cost first.
- Prefer existing code, standard-library solutions, local synthetic tests, and free native GitHub capabilities.
- No unexpected GitHub billing, paid CI minutes, or paid security features.
- If a requirement cannot be met at zero cost, document it as blocked/proposed; do not silently substitute a paid option.

## 9. Evidence and capability status
Use exact labels:
- **Proposed:** specified, not implemented.
- **Implemented:** code or design artifact exists; not necessarily validated.
- **Simulation-tested:** passed named simulation tests only.
- **Bench-tested:** controlled physical bench evidence exists.
- **Field-tested:** defined real-world test completed with documented controls.
- **Independently validated/certified:** supported by named independent evidence/certification.

Every public capability claim must state its evidence and limitations. Never infer waterproof, fireproof, secure, autonomous, real-time, roadworthy, rescue-capable, or certified status from a concept or passing software tests.

## 10. Required SHIELD review report
For every project/release, report:
- Known / verified.
- Unknown / unobservable.
- Changed since last review.
- Failures, near misses, and unsupported cases.
- Remaining risks and responsible human action.
- Recommendations and priority.
- Evidence proving improvement.
- Cost/dependency changes and security observations.

## 11. Project-specific hazard extensions
- **Coconut Harvest AI:** falling coconuts/tools, cutting and pinch zones, worker/animal exclusion, height and reach limits, tree/branch uncertainty, dropped-load containment.
- **Flood Rescue AI:** current, depth, debris, entrapment, capsizing, tether/anchor failure, battery isolation in water, rescue-person exposure, communications loss, safe withdrawal. Any depth/current capability requires measured test evidence.
- **Multimodal Narcotics Screening AI:** false positives/negatives, modality disagreement, sensor calibration, dataset bias/provenance, chain of custody, privacy, human review, and prohibition on autonomous enforcement.
- **Homeguard AI Nomad:** electrical/fire/water/mold and structural-warning uncertainty, false alarms, privacy, offline operation, safe charging, and clear emergency escalation.
- **AI Car:** collision exposure, vulnerable road users, vehicle electrical/thermal hazards, occupant privacy, degraded sensing, and no direct steering/throttle/brake control.
- **AI Motorcycle:** rider vulnerability, two-wheel stability/traction context, road-surface contamination, weather/visibility, distraction minimization, and no direct steering/throttle/brake control.

## 12. Implementation gates
A feature advances only when its gate is met:
1. **Specify:** requirement, operating domain, hazards, authority boundary, and cost review.
2. **Design:** contracts, evidence path, failure modes, safety gate, and recovery.
3. **Implement:** minimal dependency footprint, secure defaults, documentation.
4. **Test:** automated negative/regression tests and benchmark protocol.
5. **Review:** evidence, limitations, privacy/security, and human oversight.
6. **Release:** status label, change log, rollback/recovery path, and no unapproved cost.

**PUI89 SHIELD principle:** prevent harm where possible, detect uncertainty early, warn clearly, preserve human authority, recover safely, and prove every claim with evidence.

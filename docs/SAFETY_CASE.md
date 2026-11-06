# Initial Safety Case — PUI89 AI Robot Motorcycle

**Status:** Preliminary software-design record. Not a certification, safety approval, or proof of vehicle safety.

## Safety objective

The prototype must not issue direct vehicle-control commands. It may produce advisory information for research and simulation, with uncertainty and evidence visible.

## Initial hazard register

| Hazard | Example cause | Initial software/design control | Evidence required |
|---|---|---|---|
| Missed hazard | Poor visibility, model error, absent sensor | State limitations; never imply complete detection | Labeled scenario tests and missed-event analysis |
| False warning | Noise, reflections, bad thresholds | Confidence and severity handling; avoid alarm flooding | False-alarm rate by scenario |
| Stale observation | Delayed or frozen input | Timestamp/freshness validation; mark state unknown | Stale-data and time-drift tests |
| Conflicting sensors | Disagreement or calibration drift | Preserve disagreement; do not silently average away conflict | Conflict-injection tests |
| Rider distraction | Excessive or ambiguous alerts | Minimal, prioritized, human-centered advisory output | Usability review by qualified participants |
| Unsafe automation | Model proposal interpreted as command | No actuator interface; proposals are advisory only | Architecture inspection and interface tests |
| Electrical/battery hazard | Overheating, short circuit, damaged cell | No hardware control; future design requires qualified electrical and battery engineering | Independent analysis and controlled testing |
| Water ingress/fire | Environmental exposure or thermal event | Treat enclosure and materials as physical engineering requirements; software cannot establish resistance | Appropriate physical tests and certification evidence |
| Cyberattack/tampering | Malicious input, compromised dependency, unauthorized change | Input validation, least privilege, protected branches, dependency review | Security tests and audit records |
| Power/software failure | Restart, loss of power, partial update | Fail-safe software behavior; no control authority | Fault-injection and recovery tests |

## Mandatory design constraints

1. Human rider retains control and responsibility.
2. No direct throttle, brake, steering, ignition, or propulsion command path.
3. Unknown, stale, invalid, or contradictory input must be represented explicitly.
4. Every advisory output must retain rationale and supporting evidence.
5. A model's confidence score is not proof of correctness.
6. Never claim IP rating, fire resistance, battery safety, road safety, or regulatory compliance without suitable independent test evidence.
7. Any future hardware work requires qualified engineering and legal review before testing.

## Release gate

Do not describe the prototype as safe for road use, autonomous, collision-proof, waterproof, fireproof, or certified. A release candidate requires documented hazards, passing regression tests, reproducible evidence, security review, and independent domain-expert assessment.

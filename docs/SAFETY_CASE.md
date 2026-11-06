# Initial Safety Case — PUI89 AI Robot Motorcycle

**Status:** Preliminary software-design record. Not a certification, safety approval, or proof of vehicle safety.

## Safety objective
The prototype must not issue direct vehicle-control commands. It may produce advisory information for synthetic research scenarios, with rationale and limitations visible.

## Hazard register
| Hazard | Example cause | Current control | Evidence still required |
|---|---|---|---|
| Missed hazard | Occlusion, poor visibility, model error | State limitations; no complete-detection claim | Labeled scenarios and missed-event analysis |
| False warning | Noise, reflection, poor thresholds | Severity and rationale are explicit | False-alarm analysis and usability review |
| Loss of traction | Wet paint, gravel, oil, ice, worn tire | Synthetic surface/traction cases only | Validated friction model and expert review |
| Rider fall / instability | Lean, wheel slip, uneven surface | Not physically modeled or controlled | Qualified dynamics analysis and controlled test evidence |
| Close obstacle | Vehicle, pedestrian, cyclist | Synthetic obstacle-distance cases | Validated perception, timing, and human-factors evidence |
| Stale observation | Delayed or frozen input | Age validation; degraded state | Time-drift and fault-injection tests |
| Sensor disagreement | Calibration drift or spoofing | No silent averaging in future design | Multi-sensor conflict tests and calibration evidence |
| Rider distraction | Excessive or ambiguous alerts | Advisory-only output | Human-factors evaluation |
| Electrical/battery event | Short circuit, cell damage, overheating | No hardware control | Independent electrical/battery analysis and controlled tests |
| Water/fire/environment | Ingress, corrosion, thermal event | Requirements only; no IP/fire claim | Physical enclosure/material tests and applicable certification |
| Cyberattack/tampering | Malicious input, dependency compromise | Input validation, least privilege, review | Security testing and audit records |
| Power/software failure | Restart, power loss, partial update | No vehicle-control path | Fault-injection and recovery tests |

## Mandatory constraints
1. Rider retains control and responsibility.
2. No throttle, brake, steering, ignition, or propulsion command path.
3. Unknown, stale, invalid, or contradictory inputs are explicitly degraded.
4. Advisory output retains rationale and source identity.
5. Confidence is not proof of correctness.
6. Never claim IP rating, fire resistance, battery safety, road safety, or regulatory compliance without independent evidence.
7. Future hardware work requires qualified engineering and legal review before testing.

## Current evidence
- This branch adds a deterministic classifier and synthetic regression fixtures.
- Passing tests establish only expected behavior on those fixtures.
- No real sensor, motorcycle, road, rider, traction, braking, or battery validation has occurred.

## Release gate
Do not describe the project as safe for road use, autonomous, collision-proof, waterproof, fireproof, or certified. Release requires documented hazards, passing regression tests, reproducible evidence, security review, and independent domain-expert assessment.

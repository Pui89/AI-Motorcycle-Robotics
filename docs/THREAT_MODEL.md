# PUI89 AI Motorcycle / EasyRide Threat Model

**Review date:** 8 November 2026  
**Status:** Preliminary software and concept threat model. Not a vehicle cybersecurity certification or evidence of a completed security test.

## 1. Scope and security boundary

This model covers the current software, data, model, documentation, repository, and proposed advisory interfaces for PUI89 AI Motorcycle / EasyRide.

**Out of scope:** connection to a production motorcycle, ECU, CAN bus, brake/steering/throttle controller, battery management system, ignition, remote operation, or any actuator. Do not add these interfaces without a separate approved safety and security case.

Security must preserve rider safety and human authority. A compromised advisory system must not gain vehicle-control authority.

## 2. Assets to protect

- Rider-facing warnings, risk summaries, and maintenance advice.
- Observation, WorldState, ActionProposal, and FailureReport records.
- Sensor identity, timestamps, calibration, provenance, and integrity metadata.
- Datasets, labels, model weights, thresholds, configuration, and evaluation results.
- Rider privacy, trip/location information, and any future identifiable telemetry.
- Source code, dependencies, build workflows, release artifacts, repository credentials, and project history.

## 3. Threat scenarios and required mitigations

| Threat | Example | Required mitigation / safe response |
|---|---|---|
| Sensor spoofing or substitution | Fabricated obstacle, road-surface, speed, tyre, or vehicle-health signal | Authenticate source where supported; validate ranges, freshness, plausibility and provenance; mark untrusted input UNKNOWN. |
| Replay or stale observations | Old warning or safe-state record reused as current | Timestamp and sequence checks, expiry, clock-quality checks; reject replayed/stale data. |
| Sensor obstruction or degradation | Dirt, rain, vibration, glare, misalignment, damaged mount | Sensor-health and quality monitoring; explicitly degrade; do not infer a clear road. |
| Data poisoning or label manipulation | Incorrect hazard labels or manipulated training/evaluation data | Dataset provenance, licence and split records, immutable hashes, review and anomaly checks; preserve known-bad samples for regression tests. |
| Model or configuration tampering | Replaced weights, thresholds, prompt, or safety settings | Version and hash artifacts; review changes; restrict write access; reproducible evaluation; reject unknown versions. |
| Malicious or compromised dependency | Supply-chain package or action compromise | Minimise dependencies, pin versions where practical, review licences and provenance, use least-privilege workflows, update deliberately. |
| Unsafe advisory injection | Malicious content tells rider to accelerate, swerve, brake suddenly, or ignore hazards | Treat external text as untrusted data; constrain output templates; block imperative vehicle-control instructions; human review for material changes. |
| False reassurance / alert suppression | Attack or fault hides a hazard or displays “all clear” | No all-clear from missing evidence; independent negative tests; explicit unknown state; audit warning suppression and threshold changes. |
| Alert flooding / denial of service | Repeated alerts distract rider or consume resources | Rate limits, prioritisation, deduplication, bounded processing, safe degraded state; no interaction demand while moving. |
| Privacy exposure | Trip history, location, identity, images, audio or usage patterns leaked | Data minimisation, local-first design where feasible, explicit consent, retention limits, access controls, no secrets or personal data in repository. |
| Credential or repository compromise | Stolen token changes code or release | Least privilege, protected branches, reviewed changes, secret scanning where available at no cost, credential rotation and incident response. |
| Workflow compromise | Malicious CI action exfiltrates secrets or alters artifacts | Minimal workflow permissions, pinned actions where practical, no unnecessary secrets, review workflow changes, avoid paid or metered services. |
| Unsafe update or rollback | Partial update changes warnings or removes a safety gate | Versioned releases, integrity checks, staged validation, rollback to trusted version, fail closed on incomplete update. |
| GPS/network/clock manipulation | Misleading location, route, or event ordering | Treat positioning and network data as uncertain; local degradation; detect clock discontinuity; never make safety-critical control depend on connectivity. |
| Physical tampering with proposed device | Mount loosened, enclosure opened, cable damaged | Future hardware tamper/retention requirements and inspection process; no physical security claim before tests. |

## 4. Security requirements

1. **Least privilege:** repository, workflow, data, and future device permissions must be minimal.
2. **Integrity:** record provenance, version, hashes, timestamps, and calibration state for relevant inputs and artifacts.
3. **Input validation:** reject malformed, oversized, stale, replayed, contradictory, or out-of-domain inputs.
4. **Human authority:** advisory output cannot command or control steering, throttle, braking, balance, propulsion, or ignition.
5. **Fail safely:** when integrity or availability is uncertain, reduce functionality and report UNKNOWN/DEGRADED; never fabricate an all-clear.
6. **Privacy:** collect only necessary data; avoid storing identifiable location/trip histories unless justified, consented, and protected.
7. **Supply chain:** review dependency and licence changes; avoid unnecessary packages, model downloads, and external services.
8. **Repository safety:** protect default branch, review changes, avoid secrets, and use minimal CI permissions.
9. **No unexpected cost:** do not introduce paid APIs, subscriptions, cloud compute, metered scanners, or billable workflows without explicit approval.
10. **Incident response:** identify, contain, preserve relevant evidence, revoke/rotate compromised credentials, restore a trusted revision, test, and document lessons.

## 5. Verification checklist

- [ ] Missing, stale, malformed, conflicting, replayed, and spoofed observations are rejected or degraded.
- [ ] Unknown sensor identity or calibration cannot produce a confident safety claim.
- [ ] External text and model outputs cannot bypass the advisory-only boundary.
- [ ] Warning flooding and alert suppression have regression tests.
- [ ] Artifact and configuration changes are traceable to reviewed commits.
- [ ] Privacy and retention requirements are documented before collecting personal data.
- [ ] Workflow permissions and dependencies are reviewed without enabling paid services.
- [ ] Incident recovery and trusted rollback are documented.
- [ ] No vehicle-control, remote-operation, or actuator interface is present.

## 6. Residual risk and limitations

This document defines threats and expected controls; it does not prove that every mitigation is implemented or effective. No penetration test, hardware security assessment, production vehicle integration, or independent security validation is claimed. A future connected or physical prototype requires a new threat model based on its actual architecture, interfaces, components, data flows, and operating environment.

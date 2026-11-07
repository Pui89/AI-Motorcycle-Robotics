# PUI89 AI Agent and Hugging Face Integration Roadmap

**Project:** PUI89 AI Robot Motorcycle  
**Status:** Research plan only. No model is represented as installed, trained, benchmarked or validated.  
**Project-specific agent scope:** Road/weather perception, rider hazard advisories, stability-state monitoring and vehicle-health reporting. The rider retains full control; no steering, throttle or braking commands.

## Shared PUI89 agent architecture

Use the common PUI89 contracts: `WorldState`, `Observation`, `ActionProposal` and `FailureReport`.

- Perception turns supported inputs into structured observations.
- Evidence provenance records source, timestamp, sensor/modality, calibration state and integrity.
- Reasoning represents uncertainty, missing/stale data and conflicts explicitly.
- Planning produces bounded, explainable recommendations or proposals.
- Coordination routes work only to allowlisted specialist agents.
- Evaluation measures task-specific performance on held-out, reproducible datasets and scenarios.

## Hugging Face candidates

| Component | Candidate | Intended use | Decision |
|---|---|---|---|
| Agent framework | [Hugging Face smolagents](https://github.com/huggingface/smolagents) | Optional multi-step orchestration with allowlisted tools | Evaluate; framework, not a model |
| Vision-language | [Microsoft Florence-2-base](https://huggingface.co/microsoft/Florence-2-base) | Evaluate supported visual understanding tasks | First vision candidate |
| Open-vocabulary detection | [Google OWLv2 base patch16](https://huggingface.co/google/owlv2-base-patch16) | Text-conditioned object proposals | Compare on labelled project data |
| Robotics VLA | [Hugging Face SmolVLA](https://huggingface.co/lerobot/smolvla_base) | Controlled simulator research | Deferred; no physical actuation |
| Compact language model | [Microsoft Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct) | Local reasoning experiment | Deferred pending hardware fit |

Verify publisher/origin, exact model and dataset licences, model-card restrictions, dependencies, revision, weight size, RAM/VRAM and custom code before adoption. Public download availability does not establish commercial-use permission.

## Project-specific agent roles

- Road and environment perception agent: report visible objects, road context and sensor limitations.
- Hazard advisory agent: identify candidate hazards and provide evidence-linked warnings.
- Route/parking context agent: produce advisory context only; never control the vehicle.
- Stability/vehicle-health agent: assess available monitored-state inputs and report missing or out-of-range evidence.
- Evidence and evaluation agent: preserve provenance, uncertainty, false positives/negatives and failure cases.

## Zero-cost and safety defaults

- No paid APIs, subscriptions, metered inference, cloud GPUs or paid datasets.
- No automatic model or dataset downloads; never commit model weights.
- No package installation during ordinary verification.
- Keep optional adapters separate from the standard-library verification path.
- Do not enable `trust_remote_code` or execute downloaded code by default.
- No unrestricted agent code, shell, network, secret or actuator access.
- Human driver/rider retains full control. AI outputs are advisory only.
- Stop or request human review when evidence is missing, stale, conflicting, out of distribution or below a defined threshold.

## Adoption sequence

1. Validate shared contracts, provenance and uncertainty handling.
2. Add registry parsing and tests without downloading weights.
3. Define project-specific labelled benchmark fixtures and safety-relevant scenarios.
4. Compare Florence-2 and OWLv2 only on supported tasks; publish separate measured results.
5. Add smolagents only after tool allowlists, budgets, audit logs and failure handling are tested.
6. Consider SmolVLA only in a versioned simulator after a separate robotics safety review.
7. Approve any model only after licence, security, hardware and benchmark gates pass.

**Evidence status:** All model integrations in this roadmap are proposed / not yet measured. No model inference, accuracy, vehicle safety or road performance is claimed.

# PUI89 Free AI & Advanced Engineering Stack

**Policy:** strict zero-cost, local-first, non-Chinese-origin model families only, simulation-first, evidence-led. This is a curated starter list, not a claim that every listed model, hosted feature, dataset or use case is free.

## AI runtimes and model libraries
- [Ollama](https://ollama.com/) — local model runtime; MIT software licence. Model weights have separate terms.
- [llama.cpp](https://github.com/ggerganov/llama.cpp) — local inference; MIT.
- [Hugging Face Transformers](https://huggingface.co/docs/transformers) — Apache-2.0 library.
- Candidate model families to evaluate individually: Google Gemma, Microsoft Phi, Meta Llama, Mistral. Check exact release terms, attribution, acceptable-use and commercial conditions. Do not download weights until RAM/disk/compute feasibility is checked.

## Agentic AI
- [PydanticAI](https://ai.pydantic.dev/) — typed Python agents; MIT.
- [LangGraph](https://langchain-ai.github.io/langgraph/) — stateful orchestration; distinguish open-source library from hosted products.
- [smolagents](https://huggingface.co/docs/smolagents/) — lightweight agent framework; Apache-2.0.
- [CrewAI](https://www.crewai.com/) — multi-agent workflows; verify hosted/enterprise boundaries.
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) — open-source SDK; model/API inference may incur charges. No paid API use is permitted under PUI89 policy.

## AI and perception
- [PyTorch](https://pytorch.org/), [OpenCV](https://opencv.org/), [scikit-learn](https://scikit-learn.org/), [NumPy](https://numpy.org/), [pandas](https://pandas.pydata.org/), [Jupyter](https://jupyter.org/).
- OpenCV 4.5.0+ uses Apache-2.0; verify exact versions and dependencies.

## Robotics, car and motorcycle simulation
- [ROS 2 Jazzy](https://docs.ros.org/en/jazzy/), [Gazebo](https://gazebosim.org/), [CARLA](https://carla.org/), [SUMO](https://sumo.dlr.de/), [MuJoCo](https://mujoco.org/).
- Simulation only. No physical vehicle, ECU, CAN bus, steering, throttle, brake, propulsion or battery connections.

## CAD, electronics and geospatial
- [FreeCAD](https://www.freecad.org/) (LGPL), [OpenSCAD](https://openscad.org/) (GPL), [KiCad](https://www.kicad.org/) (GPL), [QGIS](https://www.qgis.org/) (GPL), [OpenStreetMap](https://www.openstreetmap.org/) data (ODbL attribution/share-alike obligations).

## Data, testing and security
- [CVAT](https://www.cvat.ai/) (verify edition/deployment terms), [FiftyOne](https://voxel51.com/fiftyone/), [pytest](https://pytest.org/), [pre-commit](https://pre-commit.com/), [OpenSSF Scorecard](https://github.com/ossf/scorecard).
- [GitHub Actions](https://docs.github.com/en/actions) is subject to plan quotas and billing settings; do not enable paid runners or exceed free allowances.

## PUI89 adoption gate
1. Verify exact software, model, dataset and plugin licences; check provenance and commercial-use conditions.
2. Confirm no hosted API, metered request, paid tier, trial conversion or telemetry requirement.
3. Check local RAM, disk, CPU/GPU and electricity implications before installation/download.
4. Prefer existing dependencies and deterministic baselines; use synthetic data first.
5. Run small offline tests, security checks and reproducible benchmarks before integration.
6. Agents may inspect, summarize and create **advisory proposals only**. No direct vehicle actuation or remote operation.
7. Label each capability as proposed, implemented, simulation-tested, bench-tested, field-tested or independently validated. Never promote a simulation result into a real-world safety claim.

## Recommended AI car / motorcycle pipeline
Synthetic sensor inputs → validation/provenance → shared PUI89 AI Core → state and hazard reasoning → agentic advisory workflow → CARLA/SUMO/Gazebo simulation → failure injection and regression tests → evidence report.

**Zero-cost warning:** free/open-source code does not make model weights, datasets, hosting, compute or all commercial uses free. Check upstream terms every time. PUI89 excludes Chinese-origin model families from this curated starter list in accordance with its sourcing preference.

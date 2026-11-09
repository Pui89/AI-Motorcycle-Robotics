"""Map synthetic motorcycle risk-baseline outputs to Shared AI Core v0.1."""
from __future__ import annotations
from datetime import datetime

SCHEMA_VERSION = "0.1.0"

def _timestamp(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("timestamp must be a non-empty ISO-8601 string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("timestamp must be valid ISO-8601") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp must include a timezone")
    return value

def build_motorcycle_v01_records(*, scenario_id, scenario_input, result,
                                 observed_at, recorded_at=None):
    """Wrap an existing deterministic synthetic result; never emits vehicle controls."""
    observed_at = _timestamp(observed_at)
    recorded_at = _timestamp(recorded_at or observed_at)
    if not isinstance(scenario_id, str) or not scenario_id.strip():
        raise ValueError("scenario_id must be a non-empty string")
    if not isinstance(scenario_input, dict) or not isinstance(result, dict):
        raise ValueError("scenario_input and result must be objects")
    if result.get("source") != "SYNTHETIC_TEST_INPUT":
        raise ValueError("only synthetic motorcycle scenario results are accepted")
    if result.get("authority") != "ADVISORY_ONLY_NO_ACTUATION":
        raise ValueError("motorcycle result must be advisory-only")
    if any(key in result for key in ("throttle", "brake", "steering", "ignition")):
        raise ValueError("vehicle control fields are forbidden")

    observation = {
        "schema_version": SCHEMA_VERSION,
        "observation_id": scenario_id,
        "observed_at": observed_at,
        "source": {"source_id": scenario_id, "source_type": "simulation", "device_or_system": "PUI89 Motorcycle synthetic risk baseline"},
        "modality": "other",
        "payload": {
            "scenario_input": scenario_input,
            "risk_result": result,
            "interpretation": "synthetic_rule_result_not_a_real_road_assessment",
        },
        "quality": {"status": "unknown", "notes": "Synthetic scenario only; no motorcycle sensor input or road test is represented."},
        "uncertainty": {"description": "Rule-based synthetic classification is not calibrated for real riding conditions."},
        "provenance": {"recorded_at": recorded_at, "dataset_or_file": "docs/simulation/MOTORCYCLE_RISK_SCENARIOS.json"},
    }
    world_state = {
        "schema_version": SCHEMA_VERSION,
        "state_id": f"motorcycle-scenario:{scenario_id}",
        "updated_at": recorded_at,
        "evidence_refs": [scenario_id],
        "entities": [{
            "entity_id": "synthetic-road-context",
            "category": "motorcycle_risk_context",
            "state": {"state": result.get("state", "UNKNOWN_DEGRADED"), "evidence_flags": result.get("evidence_flags", [])},
            "evidence_refs": [scenario_id],
        }],
        "unknowns": [
            "No real road, weather, vehicle, rider, or sensor conditions are represented.",
            "No real-world risk calibration or operational validity is established.",
        ],
        "notes": "Simulation-only state; not a riding instruction or vehicle-control signal.",
    }
    proposal = {
        "schema_version": SCHEMA_VERSION,
        "proposal_id": f"motorcycle-human-review:{scenario_id}",
        "created_at": recorded_at,
        "objective": "Request human review of the synthetic motorcycle risk scenario.",
        "world_state_ref": world_state["state_id"],
        "actions": [{
            "action_id": f"review:{scenario_id}",
            "description": "Review the synthetic risk flags and limitations as a research test case.",
            "risk_level": "unknown",
            "preconditions": [
                "Do not use this synthetic output for real riding decisions.",
                "Keep rider authority and vehicle controls entirely independent of this software record.",
            ],
            "expected_effect": "A reviewer records whether the synthetic test case behaves as specified.",
            "hazards": [
                "A synthetic classification may not represent real road conditions.",
                "No steering, throttle, braking, ignition, or other vehicle action is authorised.",
            ],
            "evidence_refs": [scenario_id],
        }],
        "authority": {"mode": "advisory_only", "human_approval_required": True, "execution_authorized": False},
        "uncertainties": [
            "No real motorcycle or rider data is used.",
            "No road safety, vehicle reliability, or model performance is validated.",
        ],
    }
    return {"observation": observation, "world_state": world_state, "action_proposal": proposal}

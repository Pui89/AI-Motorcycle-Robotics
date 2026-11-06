"""Deterministic synthetic-scenario risk baseline; never use for real riding."""
from typing import Any

VALID_SURFACES = {"dry", "wet", "gravel", "mud", "oil", "ice", "unknown"}
MAX_OBSERVATION_AGE_MS = 1000


def classify_scenario(observation: dict[str, Any]) -> dict[str, Any]:
    """Classify synthetic input conservatively. No hardware or control output."""
    required = {"surface", "traction_estimate", "visibility_m", "obstacle_distance_m", "observation_age_ms"}
    missing = sorted(required - observation.keys())
    if missing:
        return _result("UNKNOWN_DEGRADED", "Required synthetic fields are missing", missing)
    surface = observation["surface"]
    values = {k: observation[k] for k in ("traction_estimate", "visibility_m", "obstacle_distance_m", "observation_age_ms")}
    if surface not in VALID_SURFACES:
        return _result("UNKNOWN_DEGRADED", "Surface label is unsupported", ["surface"])
    for name, value in values.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return _result("UNKNOWN_DEGRADED", f"{name} is not numeric", [name])
    traction, visibility, obstacle, age = (values[k] for k in ("traction_estimate", "visibility_m", "obstacle_distance_m", "observation_age_ms"))
    if not 0 <= traction <= 1 or visibility < 0 or obstacle < 0 or age < 0:
        return _result("UNKNOWN_DEGRADED", "Value outside accepted synthetic test range", ["range_validation"])
    if age > MAX_OBSERVATION_AGE_MS:
        return _result("UNKNOWN_DEGRADED", "Synthetic observation is stale", ["observation_age_ms"])
    critical = []
    if obstacle <= 5: critical.append("very_close_obstacle")
    if traction <= 0.10: critical.append("extremely_low_traction_estimate")
    if critical: return _result("CRITICAL", "High-severity synthetic rule matched", critical)
    warnings = []
    if obstacle <= 15: warnings.append("close_obstacle")
    if traction <= 0.25: warnings.append("low_traction_estimate")
    if surface in {"ice", "oil"}: warnings.append("high_risk_surface_label")
    if warnings: return _result("WARNING", "Synthetic risk rule matched", warnings)
    advisories = []
    if surface in {"wet", "gravel", "mud"}: advisories.append("reduced_or_variable_surface_grip_possible")
    if visibility < 50: advisories.append("low_visibility")
    if advisories: return _result("ADVISORY", "Cautionary synthetic condition detected", advisories)
    return _result("NORMAL", "No configured synthetic threshold crossed", [])


def _result(state: str, rationale: str, evidence_flags: list[str]) -> dict[str, Any]:
    return {"state": state, "rationale": rationale, "evidence_flags": evidence_flags,
            "authority": "ADVISORY_ONLY_NO_ACTUATION", "source": "SYNTHETIC_TEST_INPUT"}

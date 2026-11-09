import json
import os
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from pui89_motorcycle.risk_baseline import classify_scenario
from pui89_motorcycle.shared_core_v01 import build_motorcycle_v01_records

class MotorcycleSharedCoreV01Tests(unittest.TestCase):
    def make_bundle(self):
        scenario = {
            "surface": "wet",
            "traction_estimate": 0.2,
            "visibility_m": 35,
            "obstacle_distance_m": 12,
            "observation_age_ms": 100,
        }
        result = classify_scenario(scenario)
        return build_motorcycle_v01_records(
            scenario_id="moto-synthetic-001",
            scenario_input=scenario,
            result=result,
            observed_at="2026-11-01T00:00:00Z",
            recorded_at="2026-11-01T00:00:01Z",
        )

    def test_maps_synthetic_result_to_advisory_contracts(self):
        bundle = self.make_bundle()
        self.assertEqual(bundle["observation"]["schema_version"], "0.1.0")
        self.assertEqual(bundle["observation"]["source"]["source_type"], "simulation")
        self.assertEqual(bundle["observation"]["quality"]["status"], "unknown")
        self.assertEqual(bundle["world_state"]["entities"][0]["state"]["state"], "WARNING")
        self.assertEqual(bundle["action_proposal"]["authority"]["mode"], "advisory_only")
        self.assertIs(bundle["action_proposal"]["authority"]["execution_authorized"], False)

    def test_rejects_non_synthetic_and_vehicle_control_output(self):
        scenario = {"surface":"dry"}
        result = classify_scenario(scenario)
        with self.assertRaises(ValueError):
            build_motorcycle_v01_records(scenario_id="x", scenario_input=scenario,
                                         result={**result, "source":"REAL_SENSOR"},
                                         observed_at="2026-11-01T00:00:00Z")
        with self.assertRaises(ValueError):
            build_motorcycle_v01_records(scenario_id="x", scenario_input=scenario,
                                         result={**result, "steering":0.1},
                                         observed_at="2026-11-01T00:00:00Z")

    def test_shared_core_schema_required_fields_match(self):
        schema_dir = ROOT / "schemas" / "v0.1"
        bundle = self.make_bundle()
        for key, filename in (
            ("observation","observation.schema.json"),
            ("world_state","world-state.schema.json"),
            ("action_proposal","action-proposal.schema.json"),
        ):
            schema = json.loads((schema_dir / filename).read_text(encoding="utf-8"))
            self.assertEqual(schema["properties"]["schema_version"]["const"], "0.1.0")
            self.assertTrue(set(schema["required"]).issubset(bundle[key].keys()))

if __name__ == "__main__":
    unittest.main()

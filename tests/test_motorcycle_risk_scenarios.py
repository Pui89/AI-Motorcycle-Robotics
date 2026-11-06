"""Regression tests for synthetic motorcycle scenarios only."""
import json
import unittest
from pathlib import Path
from pui89_motorcycle.risk_baseline import classify_scenario

ROOT = Path(__file__).resolve().parents[1]
SCENARIO_FILE = ROOT / "docs" / "simulation" / "MOTORCYCLE_RISK_SCENARIOS.json"

class MotorcycleScenarioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenarios = json.loads(SCENARIO_FILE.read_text(encoding="utf-8"))["scenarios"]

    def test_expected_states_and_advisory_only_authority(self):
        self.assertGreaterEqual(len(self.scenarios), 10)
        for item in self.scenarios:
            with self.subTest(scenario=item["id"]):
                result = classify_scenario(item["input"])
                self.assertEqual(result["state"], item["expected"])
                self.assertEqual(result["authority"], "ADVISORY_ONLY_NO_ACTUATION")
                self.assertEqual(result["source"], "SYNTHETIC_TEST_INPUT")

    def test_scenario_ids_are_unique(self):
        ids = [item["id"] for item in self.scenarios]
        self.assertEqual(len(ids), len(set(ids)))

    def test_missing_input_degrades(self):
        self.assertEqual(classify_scenario({"surface":"dry"})["state"], "UNKNOWN_DEGRADED")

    def test_no_vehicle_control_fields_are_returned(self):
        for item in self.scenarios:
            result = classify_scenario(item["input"])
            for key in ("throttle", "brake", "steering", "ignition"):
                self.assertNotIn(key, result)

if __name__ == "__main__":
    unittest.main()

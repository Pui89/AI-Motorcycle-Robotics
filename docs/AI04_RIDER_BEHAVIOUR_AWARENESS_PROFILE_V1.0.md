# AI-04 — Rider Behaviour Awareness Profile (Step-Through Scooter) v1.0

**Status:** Proposed product profile only; not implemented, integrated, tested, validated, or certified.

## Intended use
Provide minimal advisory context for selected riding events, with rider attention, balance, glance time and distraction risk treated as primary design constraints. Candidate events include lateral movement/turn context, closing traffic where validated, intersection approach, cyclist/pedestrian conflict cues, and degraded visibility or sensor health.

## Candidate inputs
- Forward/rear camera observations and AI-02/AI-03 outputs, only within their validated fields of view.
- Optional read-only motion context (for example speed, yaw/lean or IMU) only if a documented interface, calibration and validation exist. Do not assume these signals are installed.
- Do not infer rider gaze, fatigue, intoxication, health, emotion or fitness to ride.

## Scooter-specific hazards
Evaluate motorcycles and cars approaching from rear/side areas not covered by cameras; pedestrians stepping into the path; cyclists overtaking; filtering traffic; lane-position changes; junctions; vibration, lean, bumps, rain, spray, glare, darkness, dirt and motion blur. Unobserved side zones must remain explicitly unknown.

## Rider alerts and control boundary
Alerts must be brief, glanceable and tested to avoid visual/cognitive distraction. Never require the rider to look at a display while moving. Do not replace mirrors, direct observation, safe riding practice or statutory equipment. No automatic steering, throttle or braking; rider retains full control.

## Validation gates
Test each camera and motion input independently; validate event recognition under vibration, lean, road bumps, weather, lighting, traffic density and occlusion; measure event-level precision/recall, false alerts, missed events, latency, stale-frame handling and sensor faults; conduct rider human-factors assessment for alert comprehension and distraction. Define numeric thresholds only after hazard analysis. No thresholds are approved yet.

## Privacy and non-claims
No identity, face, emotion, voice, medical, fatigue, intoxication or fitness-to-ride inference. No cabin/rider monitoring by default. No functioning scooter, installed sensors, rider trial, road validation, collision prevention, automatic control, certification or performance is claimed.

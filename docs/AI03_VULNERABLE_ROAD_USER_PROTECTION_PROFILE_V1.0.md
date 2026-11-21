# AI-03 — Vulnerable Road User Protection Profile (Step-Through Scooter) v1.0

**Status:** Proposed product profile only; not implemented, integrated, tested, validated, or certified.

## Intended use
Advisory awareness for pedestrians, cyclists and other supported vulnerable road users in the scooter's forward and rear camera views. Rider attention, balance, glance time and distraction risk are central design constraints.

## Sensor and coverage assumptions
- Initial candidate views follow the AI-01 scooter profile: forward and rear-facing cameras.
- Do not imply side coverage or 360-degree awareness. Areas outside validated fields of view remain unknown.
- Lean angle, vibration, pitch, rapid headlamp/ambient-light changes, rain, spray, dirt, glare and camera movement can degrade image quality. Additional IMU/context inputs require documented read-only interfaces and independent validation.

## Scooter-specific hazards to evaluate
Pedestrians stepping into the path; pedestrians crossing from behind parked vehicles; cyclists overtaking or approaching from the rear; side-entry conflicts at junctions; narrow urban streets; filtering/slow traffic; kerbside activity; low-light scenes; wet-road reflections; vibration and motion blur. The system must not encourage the rider to look at a display instead of the road.

## Rider alert and control boundary
Use minimal, glanceable, prioritised alerts, with interaction designed to minimise cognitive and visual distraction. Do not replace mirrors, direct observation, safe riding practice or statutory equipment. No automatic steering, throttle or braking; rider retains full control. No claim that alerts prevent collisions.

## Scooter validation gates
Test front and rear streams separately; document blind zones; evaluate latency and frame freshness under vibration, lean, bumps, rain/spray, glare, dirt and low light. Include crossing and overtaking trajectories, partial occlusion, multiple road users and varied scene density. Report per-class precision/recall/F1, false negatives, nuisance alerts, calibration, track stability, alert comprehension and distraction/human-factors results. No numeric pass threshold is approved yet; derive thresholds from hazard analysis before testing.

## Not claimed
No functioning scooter, installed camera system, side/rear-side coverage beyond validated views, collision avoidance, automatic braking, validated detection range, rider trial, road test, regulatory approval or certification is claimed.

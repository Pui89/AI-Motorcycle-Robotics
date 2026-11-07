# AI Motorcycle / EasyRide Safety Case

**Review date:** 8 November 2026  
**Status:** Preliminary concept and software-design safety record. This is not a vehicle safety approval, roadworthiness assessment, certification, or proof of safe operation.

## 1. Safety objective and intended boundary

PUI89 AI Motorcycle / EasyRide is a human-centred, inclusive two-wheel mobility concept with potential advisory software. The current work is documentation, software research, and synthetic/simulation-oriented evaluation.

- The rider remains in control and retains responsibility for operation.
- AI outputs are advisory only and must never be represented as a substitute for rider judgement, training, protective equipment, conventional vehicle safety systems, or applicable law.
- No direct steering, throttle, braking, gear, propulsion, balance, ignition, or other actuator command path is permitted.
- No connection to a real motorcycle ECU, CAN bus, battery management system, brake controller, or actuator is in scope.
- The motorcycle is not established as built, road-tested, rider-tested, certified, or production-ready.

## 2. Motorcycle-specific hazard register

| Hazard domain | Credible causes / exposure | Required controls and evidence before any relevant claim |
|---|---|---|
| Rider fall and two-wheel instability | Low-speed manoeuvres, lean transitions, uneven loading, crosswinds, potholes, stand failure, unexpected steering input | Qualified vehicle-dynamics analysis; static and dynamic stability assessment; controlled tests by qualified personnel. No stability or balance guarantee from AI. |
| Braking and stopping | Wet/contaminated surfaces, worn tyres, load variation, brake fade, poor maintenance, unexpected obstacles | Qualified brake-system design and testing across defined loads and conditions. AI must not command or modify braking. Never assume ABS is fitted or effective without verified specification and test evidence. |
| Traction and road contamination | Rain, oil, gravel, sand, mud, painted lines, metal covers, leaves, loose debris, standing water | Define surface/condition operating limits; test tyre/vehicle behaviour through qualified engineering. Sensor-based warnings must state uncertainty and cannot guarantee grip. |
| Cornering and lean | Excess speed, changing camber, debris, poor visibility, tyre condition, unexpected road geometry | No AI lean or steering intervention. Any advisory must avoid unsupported safe-speed or safe-lean estimates; validate with representative, qualified test methods. |
| Collision and vulnerable road users | Cars, buses, pedestrians, cyclists, children, animals, blind intersections, dooring, lane changes | Conservative perception evaluation, missed-event and false-alert analysis, timing/latency measurement, human-factors review. No collision-prevention claim. |
| Rider distraction and alert overload | Dense visual displays, repeated audio alerts, confusing urgency, interaction while moving | Minimal, prioritised alerts; no required interaction while moving; adjustable presentation; distraction and comprehension studies before release. |
| Visibility and conspicuity | Night, glare, rain, fog, dirty/occluded sensors, failed lights, dark clothing | Validate lighting and visibility as vehicle-engineering requirements. Do not claim that AI sensing replaces lights, mirrors, signals, or rider observation. |
| Weather and environmental exposure | Rain, flooding, heat, cold, humidity, dust, vibration, corrosion, water ingress | Define measurable environmental requirements; enclosure, connector, vibration and corrosion tests. No IP rating, waterproofing, or all-weather-use claim without applicable independent evidence. |
| Tyres, wheels and load | Incorrect pressure, wear, puncture, damage, passenger/cargo load, loose accessories | Qualified tyre, wheel, load-rating and maintenance requirements; validate warnings against actual supported inputs. Do not infer tyre health from unavailable data. |
| Inclusive mounting and ergonomics | Footboard/step-through interference, reach mismatch, low-speed balance, clothing snag, foot entrapment | Diverse adult user trials and ergonomic review; assess mounting/dismounting, foot placement, reach, turning and stopping. Design intent does not establish universal suitability. |
| Clothing and protective equipment | Loose hems, scarves, laces, fabric near wheels/drive, unsuitable footwear or missing protective equipment | Snag/clearance review and clear rider guidance. Never infer that a garment or protective equipment is present or adequate unless validated sensing supports it. |
| Battery, electrical and fire | Cell damage, short circuit, overcurrent, charging fault, thermal runaway, wiring abrasion, crash damage | Qualified electrical/battery engineering, isolation and thermal analysis, controlled abuse and charging tests under applicable standards. No battery-safety or fire-resistance claim without evidence. |
| Crash and post-crash response | Impact, rider injury, damaged battery, blocked access, false crash alert, network loss | Define emergency escalation and privacy-conscious event handling; test detection limitations. Never delay emergency services or imply medical assessment. |
| Sensor and data failure | Vibration, occlusion, water, misalignment, calibration drift, timestamp error, stale or conflicting inputs | Source identity, freshness, calibration and integrity checks; fail to UNKNOWN/DEGRADED; test missing, noisy, stale, contradictory and spoofed inputs. |
| Communications and positioning | GPS drift, tunnel/urban canyon, mobile-network loss, clock error | Local safe degradation; never rely on cloud/network availability for essential rider control. Display uncertainty and timestamp. |
| Maintenance and modification | Unqualified repairs, incompatible parts, software updates, loose mounts, altered geometry | Document inspection and change-control requirements; qualified service boundaries; regression and post-maintenance checks. |

## 3. Mandatory safe-state and authority rules

1. No actuator commands or remote operation.
2. Missing, stale, invalid, contradictory, out-of-range, or untrusted evidence must reduce capability and show UNKNOWN/DEGRADED.
3. Do not issue confident speed, braking-distance, traction, lean-angle, collision-time, or route-safety advice unless the exact input requirements and validation evidence exist.
4. A warning must identify its source, timestamp, uncertainty, expiry, and limitation where applicable.
5. Never tell a rider to perform a risky manoeuvre based solely on AI output.
6. Do not require the rider to read, type, or interact with a display while moving.
7. Software alerts do not replace mirrors, lights, indicators, brakes, ABS/traction control where fitted, helmets, protective clothing, training, or emergency services.
8. Physical emergency stop/isolation concepts must be designed by qualified engineers; do not imply a software stop function can safely stop a moving motorcycle.
9. Never claim waterproofing, fire resistance, battery safety, roadworthiness, crash protection, regulatory compliance, or certification without applicable independent evidence.

## 4. Required validation programme

### Stage A — software and data
- Contract and schema validation for Observation, WorldState, ActionProposal, and FailureReport.
- Negative tests for missing, malformed, stale, duplicated, conflicting, spoofed, corrupted, and out-of-domain inputs.
- Evaluate false positives, false negatives, calibration, uncertainty, and subgroup/condition limitations using lawfully sourced, provenance-tracked data.
- Verify advisory-only authority and prohibit all vehicle-control interfaces.
- Test alert expiry, prioritisation, degraded mode, and recovery.

### Stage B — simulation and analytical work
- Label all simulations as synthetic or simulated.
- Define assumptions and limits for road surface, friction, lean, load, braking, visibility, weather, and other dynamics.
- Do not treat simplified simulation as proof of real motorcycle physics or rider safety.
- Obtain qualified motorcycle engineering review before relying on dynamic models.

### Stage C — physical engineering (not authorised by this record)
Any future physical prototype or rider study requires a separate approved plan, qualified engineering supervision, legal/regulatory review, risk assessment, protective controls, emergency response, and independent test evidence. No public-road test or connection to a real vehicle is authorised by this software project.

## 5. Current evidence and known gaps

- Existing safety and vehicle-intelligence documents define advisory-only boundaries and evidence labels.
- This review records motorcycle-specific hazards and validation gates; it does not demonstrate that the controls have been implemented or tested.
- No physical motorcycle, rider trial, road test, braking/traction test, battery test, environmental test, or independent certification is evidenced by this document.
- The EasyRide design brief is a concept; dimensions, mass, handling, load capacity, durability, and inclusive suitability remain unvalidated.

## 6. Release gate

Do not describe the project as road-safe, roadworthy, autonomous, self-balancing, collision-proof, waterproof, fireproof, battery-safe, universally suitable, or certified. Each public capability claim must name its evidence status, test conditions, date, and limitations.

**Principle:** protect the rider by preserving human authority, minimising distraction, exposing uncertainty, and refusing claims that exceed the evidence.

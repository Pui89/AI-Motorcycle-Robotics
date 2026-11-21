# PUI89 AI-03 — Step-Through Scooter VRU Awareness Profile v1.0

**Status:** Proposed product profile; documentation only. No functioning scooter, sensor installation, model execution, rider trial, road test or safety validation is claimed.

## Mission
Provide concise rider-facing awareness of pedestrians, children as pedestrians, cyclists and other supported vulnerable road users. The rider retains complete control of handlebar/steering, throttle and braking. The module must not encourage reliance on a camera display instead of direct observation, mirrors or safe riding practice.

## Initial view constraints
The AI-01 scooter proposal starts with forward and rear camera views. This does not provide full 360-degree coverage. Side areas, near-field blind zones, areas blocked by the rider/bodywork and anything outside the camera field of view remain unknown unless additional validated sensors cover them. No detection coverage or range is established.

## Scooter-specific hazards
- Handlebar movement, lean, vibration, bumps, acceleration and mounting flex can create blur or unstable camera geometry.
- Rider body, helmet, clothing, luggage, mirrors and vehicle structure can occlude people.
- Rain, spray, mud, dust, glare, low light, headlamp reflections and dirty lenses can degrade images.
- A small display or frequent alerts can distract the rider; audio alerts may be masked by wind, traffic or helmet use.
- A pedestrian or cyclist can enter the path from an uncovered side area; absence of a detection is not proof that the route is clear.

## Rider interaction
Prefer brief, glanceable, prioritised alerts that do not require prolonged screen viewing. Do not show complex video or dense visualisations while moving. Alert modality, mounting, volume, timing and priority require rider human-factors evaluation. Avoid startling alerts and repeated nuisance warnings. If system health is degraded, communicate unavailable/degraded status without implying safety.

## Evaluation plan
Evaluate separately at standstill, walking-speed manoeuvring and any future speed range explicitly approved by the vehicle safety case. Include pedestrians and cyclists approaching, crossing, travelling alongside, appearing from occlusion, multiple road users, day/night, rain/spray, glare, vibration, lean, camera movement, blocked lenses, dropped frames, power interruption and compute overload. Measure per-class precision/recall/F1, missed detections, false alerts, latency, tracking continuity, uncertainty calibration and abstention. Thresholds and operating limits remain TBD.

## Safety boundary and non-claims
AI-03 is advisory only. No autonomous steering, throttle, braking, balancing, collision avoidance or collision-prevention guarantee. No replacement of mirrors, rider observation, protective equipment, road rules or certified vehicle systems. No roadworthiness, detection-range or safety certification claim. Unknown coverage or uncertain observations must be shown as unknown, not safe.
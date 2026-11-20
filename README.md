# PUI89 AI Step-Through Scooter

**A rider-first, two-wheel step-through scooter concept with advisory AI awareness.**

[English project page](https://pui89.github.io/ai-robot-motorcycle.html) · [ภาษาไทย](https://pui89.github.io/ai-robot-motorcycle-th.html) · [PUI89 portfolio](https://pui89.github.io/)

![PUI89 AI Step-Through Scooter concept](docs/PUI89_AI_STEP_THROUGH_SCOOTER_CONCEPT.svg)

*Concept artwork only. It is not a functioning scooter or evidence of road testing.*

## What this product is

PUI89 AI Step-Through Scooter is a **practical two-wheel step-through mobility concept**. Easy mounting, a usable step-through floorboard and rider-first controls define the product direction. AI provides information and warnings; the rider remains responsible for riding.

**ผู้ใช้งาน:** ผู้เดินทางประจำวัน ผู้ใช้รถจักรยานยนต์ในเมือง และผู้ที่ต้องการรถแบบ Step-Through ที่ขึ้นลงสะดวก  
**ประโยชน์หลัก:** เพิ่มข้อมูลประกอบการรับรู้สภาพถนนและสุขภาพรถ โดยผู้ขับขี่ยังคงควบคุมรถเองทั้งหมด

## Product-specific functions

- Near-field awareness of vehicles, pedestrians, animals, obstacles and road context.
- Weather, visibility, road-surface and water-on-road/flood-risk warnings.
- Read-only battery, motor and vehicle-health information where supported by verified interfaces.
- Concise rider alerts and route-context assistance.
- Rider-focused ergonomics and interaction that minimise distraction.

## Rider-control boundary

AI must **not** command steering, throttle or braking. Flood-risk alerts are advisory and do not establish water-crossing ability, waterproofing or safe wading depth. The rider retains full control.

## What is not established

- No functioning scooter, vehicle integration, rider trial or road validation is established.
- No collision-prevention performance, flood-crossing ability, stability result or roadworthiness certification is claimed.
- No autonomous riding or physical actuation is in scope.

## Current development status

**Specified — rider-first two-wheel step-through requirements are documented.** No physical scooter, rider trials or road certification is established.

**Next evidence gate:** define rider use cases, vehicle architecture, sensor placement, operating limits, hazard analysis and measurable acceptance criteria before a prototype is selected or built.

## Product documentation

- [Step-Through Scooter concept illustration](docs/PUI89_AI_STEP_THROUGH_SCOOTER_CONCEPT.svg)
- [PUI89 product page](https://pui89.github.io/ai-robot-motorcycle.html)

## Shared PUI89 engineering

Cross-product architecture, evidence contracts, safety, privacy, security, recovery, device interaction and localization requirements are maintained in the [PUI89 Shared AI Core](https://github.com/Pui89/PUI89-Shared-AI-Core). Scooter-specific rider controls, mounting, vibration, weather exposure and road safety require separate validation.

Current maturity labels follow the [PUI89 Portfolio Alignment Register](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_PORTFOLIO_ALIGNMENT_REGISTER_2026-11-18.md) and [Evidence-Based Development Maturity Standard](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_DEVELOPMENT_STAGE_STANDARD.md).

## Scooter Capabilities & Functional Capacity

**Scope boundary:** PUI89 AI Step-Through Scooter is a rider-first, two-wheel step-through scooter concept with advisory AI. No functioning scooter, selected production platform or road validation is established.

### 1. Physical capacity
- Two-wheel step-through layout with a practical floorboard and rider-first controls.
- Rider capacity, passenger rating, payload, gross vehicle mass, dimensions, wheelbase, seat height, ground clearance and structural limits: **TBD** pending vehicle engineering and applicable certification.
- A previously discussed 190 kg combined rider/passenger/payload figure is **unverified** and is not a capacity rating.

### 2. Mobility capacity
- Intended for supervised road use within a future validated vehicle operating envelope.
- Define speed, turning/stability behaviour, braking performance, tyre limits, slope, ground clearance and road-surface envelope with the selected platform.
- Water exposure/flood depth, including a previously discussed 20 cm target, is **not validated** and must not be represented as safe wading capability.
- **Measured mobility and stability envelope:** TBD.

### 3. Perception capacity
- Candidate perception: nearby vehicles, pedestrians, cyclists, animals, obstacles, road surface, potholes, visibility and weather context.
- Blind-area awareness may be included only where sensor coverage and human-factors testing support it.
- Monitor rider/vehicle context only through clearly specified, permissioned and validated sensors; do not infer identity, health or intent.
- Detection coverage, range, false-alarm rate and environmental limits remain TBD.

### 4. Computing capacity
- Define local edge compute, memory, storage, latency and thermal budgets after sensor selection.
- Prioritise timely rider alerts, clear uncertainty and robust behaviour during compute faults.
- **Processor, memory and measured inference performance:** TBD.

### 5. Power capacity
- Define traction-battery and AI-system power budgets, battery-management interfaces, charging, thermal limits and low-power behaviour after platform selection.
- **Battery energy, range and charging time:** TBD.

### 6. Communication capacity
- Essential rider alerts should remain available locally without internet access.
- Define approved vehicle-local interfaces, optional phone connectivity, pairing, data permissions and loss-of-link behaviour.
- No cloud connection is required for essential safety alerts.
- **Protocols and communication range:** TBD.

### 7. Safety capacity
- AI provides advisory warnings only; rider retains full control of handlebar/steering, throttle and braking.
- No autonomous steering, throttle, braking, balance actuation or riding is in scope.
- Alert design must minimise distraction and avoid presenting uncertain hazards as confirmed events.
- No collision-prevention guarantee, roadworthiness certification or flood-crossing safety claim is made.

### 8. Maintenance capacity
- Define inspection and service for tyres, brakes, steering, suspension, battery, motor, wiring, sensors and mounting points.
- Include sensor cleaning/calibration, diagnostic records and safe replacement procedures.
- **Service intervals and validated maintenance procedures:** TBD.

### 9. Operating limits
- Concept only; no functioning scooter, rider trial, road validation, stability result or regulatory certification is established.
- Rider/payload capacity, speed, range, sensor coverage, water exposure and operating conditions remain TBD.
- The AI must not command steering, throttle or braking.

**Capacity evidence status:** Design direction documented; all numeric rider, payload, power, range and performance capacities remain TBD / not validated.


## Physical & Multimodal Sensor Privacy

PUI89 adopts the [Physical & Multimodal Sensor Privacy Standard v1.0](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/privacy/PUI89_PHYSICAL_MULTIMODAL_SENSOR_PRIVACY_STANDARD_V1.0.md) as a shared engineering requirement. Any PUI89-installed camera and microphone require physical controls. Route and motion histories are minimised and local. Privacy settings must not compromise rider-operated steering, throttle, braking or OEM safety systems.

**Evidence status:** requirements/specification only. No product-level hardware implementation or verification is claimed by this README section.


## Long-Life Battery & Energy Intelligence

PUI89 adopts the [Long-Life Battery & Energy Intelligence Standard v1.0](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/energy/PUI89_LONG_LIFE_BATTERY_ENERGY_INTELLIGENCE_STANDARD_V1.0.md) as a shared engineering requirement. Keep PUI89 auxiliary loads distinct from OEM propulsion battery protections unless integration is validated. Minimise parked standby drain and do not compromise propulsion, lighting, braking or rider controls.

Battery runtime, chemistry, capacity, cycle life, charging performance and safety compliance remain **TBD until designed and evidenced**. No unverified runtime or battery-life claim is made. The design must include an energy budget, independent BMS protections, thermal/electrical safety, service strategy and representative runtime validation.

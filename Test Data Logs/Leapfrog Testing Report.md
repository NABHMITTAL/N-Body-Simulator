Leapfrog and Time Warp Validation Test 1

  System:
  - Parent body
  - Child body
  - Moonlet

  Parent–Child orbital period:
  60 simulated seconds

  Child–Moonlet orbital period:
  10 simulated seconds

  Results:
  - No visible orbital instability
  - No body escaped
  - No collision occurred
  - No noticeable orbital deformation
  - Stable over multiple child orbital years
  - Maximum time warp remained responsive
  - No significant rendering lag


# Test 2 of Leapfrog Integration and Time-Warp Validation

## System

* Parent body
* Child body orbiting the Parent
* Moonlet 1 orbiting the Child
* Moonlet 2 orbiting the Child
* Newtonian gravity
* Synchronized leapfrog integration

## Initial Condition

* Moonlet 1 began in a stable orbit around the Child.
* Moonlet 2 was added as a second satellite of the Child.
* The simulation was first run at **10× time warp**.
* The same initial system was then rerun at **1× time warp**.

## Observation

* Moonlet 2 remained within the Child's system for approximately **27 Child orbital periods**.
* After approximately the 27th Child orbit, Moonlet 2 left the Child's system.
* During the interaction, Moonlet 1 experienced significant orbital disturbance.
* After Moonlet 2 departed, Moonlet 1 entered a stable elliptical orbit.
* The same sequence occurred when the simulation was rerun at **1× time warp**.
* Moonlet 2 escaped after approximately the same number of Child orbital periods in both runs.

## Inference

* The instability was caused by gravitational interactions within the multi-body system rather than by the displayed time-warp speed.
* The moonlets exchanged energy and angular momentum through repeated gravitational perturbations.
* Moonlet 2 eventually entered an escape trajectory.
* After Moonlet 2 left, the remaining Child–Moonlet 1 system became dynamically simpler.
* Moonlet 1 was left with a new orbital state that formed a stable elliptical orbit.
* The matching results at 1× and 10× indicate that time warp changes the rate at which simulation steps are processed without changing the underlying sequence of physics calculations.

## Verification

* The experiment was repeated using the same initial conditions.
* The first run used **10× time warp**.
* The second run used **1× time warp**.
* Moonlet 2 escaped after approximately the same Child orbital period in both runs.
* Moonlet 1 entered a stable elliptical orbit after Moonlet 2 departed in both runs.

## Conclusion

The synchronized leapfrog integrator remained stable during a complex multi-body interaction. The time-warp system produced consistent physical results at both 1× and 10× speed. Moonlet 2's escape appears to be an emergent result of gravitational interaction rather than a time-warp or integration failure. The remaining Child–Moonlet 1 system remained gravitationally stable after the ejection.



# Leapfrog and Time Warp Validation Test 3

## System:

* Parent body
* Child 1
* Moonlet 1 orbiting Child 1
* Moonlet 2 orbiting Child 1
* Child 2 orbiting the Parent

### Parent–Child 1 orbital period:

60 simulated seconds

### Child 1–Moonlet 1 orbital period:

10 simulated seconds

### Child 1–Moonlet 2 orbital period:

16 simulated seconds

## Initial Conditions:

* Child 1 orbited the Parent.
* Moonlet 1 and Moonlet 2 initially orbited Child 1.
* Child 2 orbited the Parent.
* Time warp was set to 10×.
* Previous tests had shown that 1× and 10× time warp produced consistent orbital behavior under the same initial conditions.

## Results:

* Moonlet 1 remained within the Child 1 system for approximately 45 Child 1 orbital periods.
* On Child 1 orbit 45, Moonlet 1 left the Child 1 system.
* On approximately Child 1 orbit 50, Moonlet 1 returned for a close flyby.
* During the return, Moonlet 1 followed a hyperbolic trajectory relative to Child 1.
* Moonlet 1 completed one highly elliptical orbit around Child 1.
* Moonlet 1 then immediately left the Child 1 system again.
* After Moonlet 1 left, the remaining Parent system appeared stable.
* Moonlet 1 continued to make rare close flybys of Child 1.
* The Parent–Child orbital motion appeared to follow an orbital anomaly similar to the observed Sun–Mercury system.

## Inference:

* The addition of Child 2 significantly changed the long-term behavior of the system.
* Gravitational interactions caused Moonlet 1 to transition from a bound orbit around Child 1 to an escape trajectory.
* Moonlet 1 remained dynamically associated with the larger Parent system after leaving Child 1.
* The close flyby near Child 1 orbit 50 temporarily altered Moonlet 1's trajectory into a highly elliptical orbit.
* The subsequent escape indicates that Moonlet 1 did not remain permanently captured by Child 1.
* The rare later flybys indicate repeated gravitational interactions between Moonlet 1 and Child 1.
* The apparent Parent–Child orbital anomaly may be caused by multi-body gravitational perturbations.

## Verification:

* The test was performed after Tests 1 and 2 established that 10× time warp did not independently cause orbital instability.
* The same leapfrog integration method and fixed physics timestep were used.
* The simulation remained responsive throughout the test.
* The orbital events occurred at identifiable Child 1 orbital periods.

## Conclusion:

* The leapfrog integrator remained operational during a complex five-body interaction.
* The addition of Child 2 produced significantly different long-term orbital behavior.
* Moonlet 1 escaped the Child 1 system, later returned for a close hyperbolic flyby, completed one highly elliptical orbit, and escaped again.
* Moonlet 1 remained within the larger Parent system and continued to make rare flybys of Child 1.
* The remaining Parent system appeared stable after Moonlet 1's initial escape.
* The observed orbital anomaly is a candidate for further investigation and requires quantitative measurements before being identified as a specific physical effect.





# Leapfrog and Time Warp Performance Validation Test

## System:

* Parent body
* Child A
* Moonlet A orbiting Child A
* Child B
* Moonlet B orbiting Child B
* Child C
* Moonlet C orbiting Child C
* Child D
* Moonlet D orbiting Child D
* Child E
* Moonlet E orbiting Child E
* Child F
* Moonlet F orbiting Child F
* Child G
* Moonlet G orbiting Child G
* Child H
* Moonlet H orbiting Child H

## Initial Conditions:

* The system contained 17 bodies in total.
* Eight child bodies initially orbited the Parent.
* Each child body had one moonlet.
* The bodies were initialized using circular-orbit approximations.
* Barycentric initial conditions were not applied.
* The physics timestep remained fixed at 0.01 simulated seconds.
* The same leapfrog integration method used in the previous tests was used.
* The same time-warp system and maximum substep limit were used.
* Individual bodies were observed by zooming the camera toward them.

## Results:

* The 17-body system showed visible orbital movement at 1× time warp.
* The simulation remained visually smooth at 1× time warp.
* No significant lag was observed while zoomed in on individual bodies at 1× time warp.
* Simulation lag increased as the time-warp multiplier increased.
* The lag became noticeable at approximately 1000× time warp.
* The simulation remained responsive during the test.
* The system did not experience an immediate simulation failure during the observed period.

## Inference:

* Body count alone did not cause significant lag at 1× time warp for the 17-body system.
* The increase in lag with increasing time warp indicates that the number of leapfrog physics substeps is a major performance factor.
* The simulation performs additional physics calculations before each rendered frame as time warp increases.
* The 17-body system requires repeated pairwise gravitational calculations during every leapfrog step.
* The maximum substep limit caused the physics workload to increase substantially at high time-warp values.
* The camera and individual-body rendering were unlikely to be the primary causes of the observed lag at 1× time warp.
* The test did not fully isolate the effect of body count because smaller and larger systems were not tested under identical conditions.

## Verification:

* The simulation was tested at multiple time-warp levels.
* The same physics timestep was maintained throughout the test.
* The same leapfrog integration method was used throughout the test.
* The system was visually inspected while zoomed in on individual bodies.
* The onset of noticeable lag was observed at approximately 1000× time warp.
* Previous tests had established that the leapfrog integration method remained operational during stable and complex multi-body interactions.

## Conclusion:

* The 17-body system remained smooth and responsive at 1× time warp.
* Increasing time warp increased the computational workload and produced progressively greater lag.
* Noticeable lag occurred at approximately 1000× time warp.
* The results indicate that physics substep count is a significant contributor to the performance limitation.
* Body count may contribute to the total computational cost but was not identified as the primary cause of lag at 1× time warp.
* Further tests using different body counts under identical time-warp conditions are required to quantify the effect of body count on performance.
* The absence of barycentric initial conditions limits the use of this test for long-term orbital-stability validation but does not prevent its use as an initial performance observation.

# Leapfrog and Time Warp Performance Validation Test 2

## System:

Three separate systems were tested using identical simulation settings.

### System 1

* Parent body
* Child A
* Moonlet A orbiting Child A
* Child B
* Moonlet B orbiting Child B
* Child C
* Moonlet C orbiting Child C

**Total Bodies:** 7

### System 2

* Parent body
* Child A
* Moonlet A
* Child B
* Moonlet B
* Child C
* Moonlet C
* Child D
* Moonlet D
* Child E
* Moonlet E
* Child F
* Moonlet F

**Total Bodies:** 13

### System 3

* Parent body
* Child A
* Moonlet A
* Child B
* Moonlet B
* Child C
* Moonlet C
* Child D
* Moonlet D
* Child E
* Moonlet E
* Child F
* Moonlet F
* Child G
* Moonlet G
* Child H
* Moonlet H

**Total Bodies:** 17

## Initial Conditions:

* All systems used the same leapfrog integration algorithm.
* Physics timestep remained fixed at **0.01 simulated seconds**.
* Maximum physics substep cap remained fixed at **500**.
* The renderer and simulation loop remained unchanged between tests.
* Time warp was varied while recording the measured simulation frame rate (FPS).

## Observation:

### 7 Bodies

* **1×:** Approximately **900 FPS**
* **10×:** Approximately **650 FPS**
* **100×:** Approximately **147 FPS**
* **5000×:** Approximately **32 FPS**

### 13 Bodies

* **1×:** Approximately **820 FPS**
* **10×:** Approximately **340 FPS**
* **100×:** Approximately **46 FPS**
* **1000×:** Approximately **9.5 FPS**
* **5000×:** Approximately **9.5 FPS**

### 17 Bodies

* **1×:** Approximately **750 FPS**
* **10×:** Approximately **225 FPS**
* **100×:** Approximately **27 FPS**
* **1000×:** Approximately **5.5 FPS**

## Inference:

* Increasing body count consistently reduced simulation performance.
* Increasing time warp produced a much larger performance reduction than increasing body count alone.
* The simulation remained smooth at **1×** for all tested body counts.
* Physics workload increased significantly as time warp increased because additional leapfrog integration steps were executed before each rendered frame.
* At high time warp, the simulation became physics-bound rather than rendering-bound.
* The identical FPS observed at **1000×** and **5000×** for the 13-body system indicates that the **500 substep cap** was reached and prevented any further increase in physics workload.
* The reduction in FPS between 7-, 13-, and 17-body systems is consistent with the expected increase in pairwise gravitational calculations as body count increases.

## Verification:

* The same hardware, renderer, timestep, and leapfrog implementation were used for all three systems.
* Only the number of simulated bodies and the selected time warp varied.
* FPS values were measured directly during runtime.
* The simulation remained responsive throughout all tests.

## Conclusion:

* Leapfrog integration remained operational for all tested systems.
* Performance degraded with both increasing body count and increasing time warp.
* Time warp produced the dominant increase in computational workload.
* The 500-substep cap successfully prevented additional slowdown beyond its limit, as demonstrated by identical FPS values at **1000×** and **5000×** in the 13-body system.
* The observed performance trend is consistent with the expected computational complexity of repeated pairwise gravitational calculations combined with multiple leapfrog substeps per rendered frame.
* Future optimisation efforts should focus on reducing the cost of physics calculations performed during each simulation frame rather than modifying the leapfrog integration algorithm itself.

# Leapfrog and Time Warp Performance Validation Test 3

## System

- Parent body
- Child A
- Child B
- Child C
- Child D
- Child E
- Multiple moonlets distributed among the child bodies
- Total bodies in simulation: **17**

## Initial Conditions

- All child bodies were placed in stable circular orbits around the Parent.
- Each moonlet was placed in a stable circular orbit around its respective child body.
- Physics integration used the Leapfrog (Velocity Verlet) integrator.
- Maximum physics substep cap was fixed at **500 substeps per rendered frame**.
- Performance instrumentation measured:
  - Physics time
  - Rendering time
  - Camera update time
  - Event processing time
  - Total frame time
- Tests were conducted at:
  - 1× Time Warp
  - 10× Time Warp
  - 100× Time Warp
  - 1000× Time Warp
  - 5000× Time Warp

## Results

### 1× Time Warp

- Physics: **0.5–0.9 ms**
- Rendering: **1.0–1.3 ms**
- Camera: **≈0.01 ms**
- Events: **≈0.01–0.18 ms**
- Total Frame: **1.5–2.3 ms**
- Measured FPS: **≈526–588 FPS**

Observation:
- Rendering consumed more frame time than physics.

---

### 10× Time Warp

- Physics: **3.5–6.3 ms**
- Rendering: **1.2–1.7 ms**
- Camera: **≈0.01 ms**
- Events: **≈0.01–0.13 ms**
- Total Frame: **5.1–7.8 ms**
- Measured FPS: **≈132 FPS**

Observation:
- Physics became the dominant workload.

---

### 100× Time Warp

- Physics: **36–57 ms**
- Rendering: **≈1.8 ms**
- Camera: **≈0.03 ms**
- Events: **≈0.02–0.09 ms**
- Total Frame: **38–59 ms**
- Measured FPS: **≈17 FPS**

Observation:
- Physics overwhelmingly dominated total frame time.

---

### 1000× Time Warp

- Physics: **258–286 ms**
- Rendering: **≈1.7 ms**
- Camera: **≈0.03 ms**
- Events: **≈0.26 ms**
- Total Frame: **260–288 ms**

Observation:
- Rendering and camera costs became negligible compared to physics.

---

### 5000× Time Warp

- Physics: **≈280 ms**
- Rendering: **≈1.8 ms**
- Camera: **≈0.03 ms**
- Events: **≈0.18 ms**
- Total Frame: **≈282 ms**
- Measured FPS: **≈3.6 FPS**

 Observation:
- Physics execution time remained almost identical to the 1000× test, indicating that the **500 substep cap** successfully limited additional computation.

---

## Inference

- Physics execution time scales approximately linearly with the number of Leapfrog substeps until the maximum substep cap is reached.
- Rendering, camera updates, and event processing contribute only a small fraction of total frame time at high simulation speeds.
- Once the 500-substep limit is reached, increasing Time Warp further does not significantly increase computation time.
- The measured slowdown is therefore caused by the physics workload rather than rendering or UI operations.

## Verification

- All measurements were obtained using `time.perf_counter()` instrumentation over averages of 100 frames.
- The simulation remained responsive throughout testing.
- Performance measurements were repeatable across multiple sampling intervals.
- The measured execution time at 5000× closely matched the expected cost of approximately 500 Leapfrog integrations per rendered frame.

## Conclusion

- The Leapfrog integrator and Time Warp implementation function correctly under a 17-body arbitrary system.
- The implemented 500-substep cap effectively prevents unbounded increases in computation time at extreme Time Warp values.
- Performance degradation at high Time Warp levels is attributable almost entirely to repeated physics integration.
- Future optimisation efforts should focus on reducing the cost of the Leapfrog physics step, particularly the gravitational force calculations, rather than rendering or event processing.
  


# Leapfrog Internal Performance Validation Test 1

## System

* Parent body
* Child A–H
* Moonlet A–H
* Total bodies: **17**

## Initial Conditions

* Fixed timestep (`dt`) remained constant.
* Leapfrog (Velocity Verlet) integrator used.
* Internal execution time of each Leapfrog stage was measured.
* Profiling was performed over **100 rendered frames**.
* Measurements were repeated at multiple time warp levels:
  * 1×
  * 10×
  * 100×
  * 1000×
  * 5000×

## Results

### Average execution time per Leapfrog step

| Stage | Average Time |
|--------|-------------:|
| Gravity Pass 1 | ~0.28–0.34 ms |
| Position Update | ~0.012–0.015 ms |
| Gravity Pass 2 | ~0.27–0.32 ms |
| Velocity Update | ~0.000 ms |
| **Total Leapfrog Step** | **~0.55–0.67 ms** |

### Time Warp Behaviour

* The execution time of an individual Leapfrog step remained effectively constant across all tested time warp levels.
* Increasing the time warp increased the total number of Leapfrog evaluations performed between rendered frames.
* Measured Leapfrog calls during a 100-frame profiling interval included:
  * **1×:** ~100 calls
  * **10×:** ~865–1000 calls
  * **100×:** ~5860–10000 calls
  * **1000×:** ~29600–50000 calls
  * **5000×:** 50000 calls (limited by simulation substep cap)

## Observation

* Gravity Pass 1 and Gravity Pass 2 together consumed approximately **98% of the total computation time**.
* Position updates contributed approximately **2%**.
* Velocity updates contributed a negligible amount.
* No measurable increase in the computational cost of a single Leapfrog step was observed as time warp increased.

## Inference

* The Leapfrog integrator itself is computationally stable and scales independently of simulation speed.
* Simulation slowdown at higher time warp is caused solely by executing a larger number of Leapfrog steps rather than by individual steps becoming slower.
* The dominant computational bottleneck is the repeated evaluation of gravitational forces.

## Verification

* Profiling was repeated multiple times at each tested time warp level.
* Results remained consistent across repeated measurements.
* The computational distribution between Leapfrog stages remained effectively unchanged throughout all tests.

## Conclusion

* Leapfrog implementation is computationally efficient.
* Increasing time warp does **not** increase the cost of an individual integration step.
* The primary performance bottleneck is the gravitational force calculation performed during the two gravity evaluation passes.
* Future optimisation efforts should focus on reducing the cost or number of gravitational force evaluations rather than modifying the Leapfrog integration algorithm itself.


# Leapfrog Internal Function Profiling Test 5

## Objective

Measure the execution time of each major computational component inside the Leapfrog (Velocity Verlet) integration algorithm in order to identify the primary computational bottlenecks before beginning optimization in Procedure 7.

---

## System

- Parent body
- Child A–H
- Moonlet A–H

**Total Bodies:** 17

Integrator:
- Leapfrog (Velocity Verlet)

Physics timestep:
- Fixed timestep (`dt = 0.01 s`)

Maximum substeps:
- 500

---

## Methodology

The following functions were individually instrumented using `time.perf_counter()`:

- `distance()`
- `displacement()`
- `gravitational_force()`
- `acceleration_calc()`

For each function the following values were recorded:

- Total execution time
- Number of function calls
- Average execution time per call

Measurements were performed across the following warp levels:

- 1×
- 10×
- 100×
- 1000×
- 5000×

---

## Results

### Warp Level: 1×

Average values across multiple profiling runs:

| Function | Average Time per Call |
|----------|----------------------:|
| distance() | ~0.33 µs |
| displacement() | ~0.21 µs |
| gravitational_force() | ~1.55 µs |
| acceleration_calc() | ~0.26 µs |

Average Physics Time:

- ~1.15 ms/frame

Average Total Frame Time:

- ~2.43 ms/frame

---

### Warp Level: 10×

Average values:

| Function | Average Time per Call |
|----------|----------------------:|
| distance() | ~0.31 µs |
| displacement() | ~0.19 µs |
| gravitational_force() | ~1.44 µs |
| acceleration_calc() | ~0.25 µs |

Average Physics Time:

- ~8.88 ms/frame

Average Total Frame Time:

- ~9.95 ms/frame

---

### Warp Level: 100×

Average values:

| Function | Average Time per Call |
|----------|----------------------:|
| distance() | ~0.30 µs |
| displacement() | ~0.19 µs |
| gravitational_force() | ~1.37 µs |
| acceleration_calc() | ~0.24 µs |

Average Physics Time:

- ~84.0 ms/frame

Average Total Frame Time:

- ~85.5 ms/frame

---

### Warp Level: 1000×

Average values:

| Function | Average Time per Call |
|----------|----------------------:|
| distance() | ~0.29 µs |
| displacement() | ~0.19 µs |
| gravitational_force() | ~1.36 µs |
| acceleration_calc() | ~0.23 µs |

Average Physics Time:

- ~474 ms/frame

Average Total Frame Time:

- ~476 ms/frame

---

### Warp Level: 5000×

Average values:

| Function | Average Time per Call |
|----------|----------------------:|
| distance() | ~0.295 µs |
| displacement() | ~0.186 µs |
| gravitational_force() | ~1.360 µs |
| acceleration_calc() | ~0.235 µs |

Average Physics Time:

- ~505 ms/frame

Average Total Frame Time:

- ~507 ms/frame

---

## Observations

- Average execution time per function remained nearly constant across every time warp level.
- No evidence was observed of algorithmic slowdown within any individual function as simulation speed increased.
- The increase in total physics time scaled almost entirely with the increasing number of Leapfrog integration steps executed each frame.
- `gravitational_force()` consistently consumed the greatest amount of execution time among all measured functions.
- `distance()` and `displacement()` represented the largest contributors within the force calculation pipeline.
- `acceleration_calc()` contributed comparatively little to total execution time.

---

## Inference

- The Leapfrog implementation exhibits stable computational performance independent of simulation warp level.
- The observed performance degradation at higher warp levels is caused by the increased number of Leapfrog iterations rather than slower execution of individual calculations.
- The dominant computational hotspot is the repeated evaluation of gravitational forces between body pairs.
- Further optimization efforts should prioritize reducing the computational cost and call frequency of `gravitational_force()` before attempting lower-impact optimizations elsewhere.

---

## Verification

- Identical simulation conditions were maintained throughout all measurements.
- Physics timestep remained fixed.
- Body count remained constant at 17.
- All measurements were obtained using Python's high-resolution `time.perf_counter()`.
- Multiple profiling runs were performed at each warp level to verify consistency.

---

## Conclusion

- Leapfrog internal execution time remains effectively constant across all tested warp levels.
- Physics performance scales primarily with the number of integration steps executed per rendered frame.
- `gravitational_force()` has been identified as the principal optimization target for Procedure 7.
- This test establishes the performance baseline against which all future optimization work will be measured.






# Leapfrog Optimization Validation Test 1

## Objective

Evaluate the performance impact of eliminating the separate `distance()` calculation by reusing the displacement vector and introducing `Vector2.mag_calc()` inside `gravitational_force()`.

---

## System

- Parent body
- Child A–H
- Moonlet A–H

**Total Bodies:** 17

Integrator:
- Leapfrog (Velocity Verlet)

Physics timestep:
- Fixed timestep (`dt = 0.01 s`)

Optimization Applied:

- Removed the standalone `distance()` function from the force calculation pipeline.
- Introduced `Vector2.mag_calc()` to compute the magnitude directly from the previously calculated displacement vector.
- Reused the displacement vector for both direction and magnitude calculations.

---

## Methodology

The same profiling methodology used in **Leapfrog Internal Function Profiling Test 5** was repeated after the optimization.

Measurements recorded:

- `displacement()`
- `gravitational_force()`
- `acceleration_calc()`
- Physics time per frame
- Total frame time

Primary comparison was performed at **100× Time Warp**, as Procedure 7 optimization testing standard.

---

## Results

### Warp Level: 100×

Average values across multiple profiling runs:

| Function | Before Optimization | After Optimization | Improvement |
|----------|-------------------:|------------------:|------------:|
| displacement() | ~0.186 µs | ~0.180 µs | ~3% |
| gravitational_force() | ~1.37 µs | ~1.00 µs | **~27%** |
| acceleration_calc() | ~0.235 µs | ~0.224 µs | ~5% |

Average Physics Time:

| Metric | Before | After |
|-------|-------:|------:|
| Physics | ~84.0 ms | ~76–82 ms |
| Frame | ~85.5 ms | ~68–84 ms |

---

## Observations

- The standalone `distance()` calculation was successfully removed from the force computation pipeline.
- `gravitational_force()` execution time decreased from approximately **1.37 µs** to approximately **1.00 µs** per call.
- The execution time of `displacement()` remained effectively unchanged.
- `acceleration_calc()` continued to contribute only a negligible fraction of total execution time.
- Overall physics time per frame showed a measurable reduction at the optimization benchmark warp level.

---

## Inference

- Reusing the displacement vector successfully eliminated redundant calculations previously performed by `distance()`.
- The optimization reduced duplicated coordinate subtraction and avoided constructing the separation vector twice.
- The reduction in `gravitational_force()` execution time confirms that redundant helper-function work represented a measurable computational overhead.
- Simulation behavior remained unchanged throughout testing, indicating that the optimization preserved numerical correctness.

---

## Verification

- The optimized implementation was benchmarked under the same simulation conditions as Test 5.
- Body count remained fixed at 17.
- Physics timestep remained unchanged.
- Profiling instrumentation remained identical to the previous benchmark.
- Multiple profiling runs produced consistent results.

---

## Conclusion

- Optimization 7.1 successfully reduced the computational cost of the gravitational force calculation without altering simulation behavior.
- Average `gravitational_force()` execution time decreased by approximately **27%**.
- Overall physics execution time improved while maintaining identical Leapfrog integration behavior.
- The optimization establishes the first measurable performance improvement of Procedure 7 and serves as the new performance baseline for subsequent optimizations.



# Leapfrog Optimization Test 2 — Direct Gravitational Acceleration

## Objective

Measure the performance impact of replacing the previous force → acceleration calculation chain with direct gravitational acceleration.

The optimization removes the intermediate force-to-acceleration conversion from the Leapfrog hot path.

---

## System

* **Bodies:** 17 arbitrary test bodies
* **Integrator:** Leapfrog (Velocity Verlet)
* **Time Warp:** 100×
* **Physics timestep:** `dt = 0.01`
* **Benchmark:** Multiple profiling runs

### Optimization Applied

The previous calculation:

```text
displacement
→ gravitational_force
→ acceleration_calc
→ acceleration
```

was replaced with direct gravitational acceleration:

```text
displacement
→ gravitational_acceleration
```

This eliminated the separate `acceleration_calc()` operation.

---

## Results

### Run 1

```text
========== Physics Function Profile 100x ==========

displacement()
  Calls : 683264
  Avg   : 0.184 µs

gravitational_force()
  Calls : 683264
  Avg   : 0.700 µs

Physics : 5.527 ms
Frame : 6.849 ms
==============================
```

### Run 2

```text
========== Physics Function Profile 100x ==========

displacement()
  Calls : 6123264
  Avg   : 0.180 µs

gravitational_force()
  Calls : 6123264
  Avg   : 0.677 µs

Physics : 61.934 ms
Frame : 63.827 ms
==============================
```

### Run 3

```text
========== Physics Function Profile 100x ==========

displacement()
  Calls : 11563264
  Avg   : 0.180 µs

gravitational_force()
  Calls : 11563264
  Avg   : 0.677 µs

Physics : 62.326 ms
Frame : 64.147 ms
==============================
```

---

## Comparison With Previous Baseline

Previous optimization baseline at 100×:

```text
displacement()       ≈ 0.180 µs
gravitational_force() ≈ 1.000 µs
acceleration_calc()  ≈ 0.224 µs
Physics              ≈ 76–82 ms
```

After direct acceleration optimization:

```text
displacement()              ≈ 0.181 µs
gravitational calculation   ≈ 0.678 µs
acceleration_calc()         Removed
Physics                     ≈ 62 ms
```

### Function-level improvement

The gravitational calculation decreased from approximately:

```text
1.00 µs → 0.678 µs
```

representing an improvement of approximately **32% per gravitational interaction**.

The `acceleration_calc()` function was completely removed from the hot path.

---

## Observations

* `displacement()` performance remained effectively unchanged.
* The gravitational calculation became substantially faster.
* The separate `acceleration_calc()` operation was eliminated.
* Physics execution time decreased substantially compared with the previous baseline.
* The optimization does not change the underlying Leapfrog integration method.
* The optimization preserves the same mathematical acceleration:


---

## Inference

The benchmark confirms that calculating gravitational acceleration directly is more efficient than first calculating gravitational force and subsequently dividing by the affected body's mass.

The largest gain comes from eliminating the intermediate force-to-acceleration conversion and associated arithmetic/function-call overhead.

This confirms that the force calculation path contained unnecessary work for the Leapfrog integrator.

---

## Conclusion

**Optimization 7.2 was successful.**

The direct gravitational acceleration implementation reduced the cost of the gravitational calculation by approximately **32%** and reduced overall physics execution time from roughly **76–82 ms to approximately 62 ms at 100× warp**.

The optimization is therefore retained as the new performance baseline.


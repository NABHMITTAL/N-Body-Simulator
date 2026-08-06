# Changelog

## v0.0.6 — Leapfrog Integration

### Added

- Leapfrog (Velocity Verlet) integrator.
- Stable arbitrary multi-body simulation support.
- Validation logs (`tests.md`).

### Improved

- Replaced Euler integration with Leapfrog integration.
- Stable long-term orbital propagation.
- Stable behaviour under multiple time warp levels.
- Improved numerical accuracy compared to the previous integrator.

### Current Known Issue

- High time warp levels result in significant performance degradation.
- The slowdown appears to originate from repeated gravitational force calculations during each Leapfrog step.
- Gravity solver optimisation will be addressed in the next development phase.


## v0.0.5 - Simulation Controls

### Added
- Implemented body selection system using TAB
- Added smooth camera target switching
- Added free camera mode toggle
- Implemented adjustable simulation time warp
- Added real-time simulation speed controls
- Added on-screen simulation UI
- Added current follow target indicator
- Added KSP-inspired control scheme

### Improved
- Refactored renderer and simulation communication
- Improved camera control workflow

## v0.0.4 - Camera System
### Added
- Implemented camera system
- Added free camera movement using keyboard controls
- Added camera zoom controls using mouse wheel
- Added smooth body-following camera mode
- Added world-to-screen coordinate transformation through camera

---

## v0.0.3 - Real-Time Renderer
### Added
- Implemented real-time rendering using Pygame
- Added simulation loop
- Added renderer module
- Added visualization of simulated bodies
- Added orbital motion visualization

---

## v0.0.2 - N-Body Simulation Engine
### Added
- Implemented first working N-body simulation engine
- Added Newtonian gravitational force calculations
- Added SI unit support
- Added velocity and position updates

---

## v0.0.1 - Vector Mathematics
### Added
- Implemented Vector2 class
- Added vector addition
- Added vector scaling
- Added vector division
- Added vector normalization
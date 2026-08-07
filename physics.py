import time

# DELETE AFTER TESTING
# distance_time = 0
displacement_time = 0
force_time = 0
acceleration_time = 0

# distance_calls = 0
displacement_calls = 0
force_calls = 0
acceleration_calls = 0


import math
from constants import G
from body import Body
import vector2

# def distance(body1: Body, body2: Body):

#     # DELETE AFTER TESTING
#     global distance_time, distance_calls
#     start = time.perf_counter()

#     dx = body1.position.x - body2.position.x
#     dy = body1.position.y - body2.position.y
#     dist = math.sqrt(dx**2 + dy**2)

#     # DELETE AFTER TESTING
#     distance_time += time.perf_counter() - start
#     distance_calls += 1

#     return dist

def displacement(body1: Body, body2: Body):

    # DELETE AFTER TESTING
    global displacement_time, displacement_calls
    start = time.perf_counter()

    dx = body1.position.x - body2.position.x
    dy = body1.position.y - body2.position.y
    disp = vector2.Vector2(dx, dy)

    # DELETE AFTER TESTING
    displacement_time += time.perf_counter() - start
    displacement_calls += 1

    return disp


def gravitational_force(body1: Body, body2: Body):

    # DELETE AFTER TESTING
    global force_time, force_calls
    start = time.perf_counter()

    dist = displacement(body2, body1)
    force = ((dist * (G * body1.mass * body2.mass)) / (vector2.mag_calc(dist)) ** 3)

    # DELETE AFTER TESTING
    force_time += time.perf_counter() - start
    force_calls += 1

    return force


def acceleration_calc(force: vector2, mass: float):

    # DELETE AFTER TESTING
    global acceleration_time, acceleration_calls
    start = time.perf_counter()

    acceleration = force / mass

    # DELETE AFTER TESTING
    acceleration_time += time.perf_counter() - start
    acceleration_calls += 1

    return acceleration
  
def vel_update(body:Body,dt:float):
  new_vel = body.velocity + (body.acceleration*dt)
  return new_vel

def pos_update(body:Body,dt:float):
  new_pos = body.position + (body.velocity*dt)
  return new_pos
import time

# DELETE AFTER TESTING
displacement_time = 0
force_time = 0

displacement_calls = 0
force_calls = 0


import math
from constants import G
from body import Body
import vector2


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

  
def vel_update(body:Body,dt:float):
  new_vel = body.velocity + (body.acceleration*dt)
  return new_vel

def pos_update(body:Body,dt:float):
  new_pos = body.position + (body.velocity*dt)
  return new_pos



def gravitational_acceleration(body1: Body, body2: Body):
    global force_time, force_calls
    start = time.perf_counter()

    displacement_vec = displacement(body2, body1)

    r2 = displacement_vec.x * displacement_vec.x + displacement_vec.y * displacement_vec.y
    r = math.sqrt(r2)

    acceleration = displacement_vec * (G * body2.mass / (r2 * r))
    force_time += time.perf_counter() - start
    force_calls += 1

    return acceleration

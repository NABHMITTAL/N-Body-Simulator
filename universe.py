import physics
from body import Body
from vector2 import Vector2
dt = 0.01 #time delta per frame
body_list = []

sun = Body(
  "Sun",
  1.989e30,
  Vector2(0, 0),
  Vector2(0, 0),
  20,
  "yellow"
)

earth = Body(
  "Earth",
  5.972e24,
  Vector2(1.496e11, 0),
  Vector2(0, 29780),
  8,
  "blue"
)

moon = Body(
  "Moon",
  7.35e22,
  Vector2(1.499844e11, 0),
  Vector2(0,30802),
  3,
  "gray"
)

body_list = [sun, earth, moon]


def step():

  for item in body_list:
    net_force = Vector2(0,0)
    for bodies in body_list:
      if item == bodies:
        continue
      net_force = net_force + physics.gravitational_force(item, bodies)
    item.acceleration = physics.acceleration_calc(net_force, item.mass)

  for items in body_list:
    items.velocity = physics.vel_update(items,dt)
    items.position = physics.pos_update(items,dt)

#test run
def run_sim():
  for i in range(100000):
    step()
    if i%1000 ==0:
      print(f"Step {i+1}")
      print(sun)
      print()
      print(earth)
      print()
      print(moon)
      print()

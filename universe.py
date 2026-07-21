import physics
from body import Body
from vector2 import Vector2
dt = 0.01 #time delta per frame

sun = Body(
  "Sun",
  1.989e30,
  Vector2(0, 0),
  Vector2(0, 0),
  20,
  (255,255,0)#yellow
)

earth = Body(
  "Earth",
  5.972e24,
  Vector2(1.496e11, 0),
  Vector2(0, 29780),
  8,
  (0,0,255)#blue
)

moon = Body(
  "Moon",
  7.35e22,
  Vector2(1.499844e11, 0),
  Vector2(0,30802),
  3,
  (128,128,128)#gray
)

class Universe:
  def __init__(self):
    self.bodies = [sun, earth, moon]

  def step(self,dt):
    for item in self.bodies:
      net_force = Vector2(0,0)
      for body in self.bodies:
        if item == body:
          continue
        net_force = net_force + physics.gravitational_force(item, body)
      item.acceleration = physics.acceleration_calc(net_force, item.mass)

    for items in self.bodies:
      items.velocity = physics.vel_update(items,dt)
      items.position = physics.pos_update(items,dt)


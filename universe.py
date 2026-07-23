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

# Mercury
mercury = Body(
    "Mercury",
    3.3011e23,
    Vector2(5.791e10, 0),
    Vector2(0, 47870),
    3,
    (169,169,169)
)

# Venus
venus = Body(
    "Venus",
    4.8675e24,
    Vector2(1.0821e11, 0),
    Vector2(0, 35020),
    6,
    (230,190,138)
)

# Earth
earth = Body(
    "Earth",
    5.972e24,
    Vector2(1.496e11, 0),
    Vector2(0, 29780),
    8,
    (0,255,0)
)

# Moon
moon = Body(
    "Moon",
    7.35e22,
    Vector2(1.499844e11, 0),
    Vector2(0, 30802),
    3,
    (128,128,128)
)

# Mars
mars = Body(
    "Mars",
    6.4171e23,
    Vector2(2.2794e11,0),
    Vector2(0,24077),
    4,
    (188,39,50)
)

# Phobos
phobos = Body(
    "Phobos",
    1.0659e16,
    Vector2(2.2794e11 + 9.376e6,0),
    Vector2(0,24077 + 2138),
    1,
    (140,140,140)
)

# Deimos
deimos = Body(
    "Deimos",
    1.4762e15,
    Vector2(2.2794e11 + 2.3463e7,0),
    Vector2(0,24077 + 1351),
    1,
    (170,170,170)
)

# Jupiter
jupiter = Body(
    "Jupiter",
    1.8982e27,
    Vector2(7.7857e11,0),
    Vector2(0,13070),
    16,
    (210,180,140)
)

# Io
io = Body(
    "Io",
    8.9319e22,
    Vector2(7.7857e11 + 4.217e8,0),
    Vector2(0,13070 + 17320),
    2,
    (255,230,120)
)

# Europa
europa = Body(
    "Europa",
    4.7998e22,
    Vector2(7.7857e11 + 6.711e8,0),
    Vector2(0,13070 + 13740),
    2,
    (220,220,200)
)

# Ganymede
ganymede = Body(
    "Ganymede",
    1.4819e23,
    Vector2(7.7857e11 + 1.0704e9,0),
    Vector2(0,13070 + 10880),
    3,
    (180,170,160)
)

# Callisto
callisto = Body(
    "Callisto",
    1.0759e23,
    Vector2(7.7857e11 + 1.8827e9,0),
    Vector2(0,13070 + 8200),
    3,
    (120,120,120)
)

# Saturn
saturn = Body(
    "Saturn",
    5.6834e26,
    Vector2(1.4335e12,0),
    Vector2(0,9680),
    14,
    (210,190,140)
)

# Titan
titan = Body(
    "Titan",
    1.3452e23,
    Vector2(1.4335e12 + 1.22187e9,0),
    Vector2(0,9680 + 5570),
    3,
    (255,190,120)
)

# Enceladus
enceladus = Body(
    "Enceladus",
    1.0802e20,
    Vector2(1.4335e12 + 2.37948e8,0),
    Vector2(0,9680 + 12640),
    2,
    (230,230,255)
)

# Uranus
uranus = Body(
    "Uranus",
    8.6810e25,
    Vector2(2.8725e12,0),
    Vector2(0,6800),
    12,
    (175,238,238)
)

# Titania
titania = Body(
    "Titania",
    3.527e21,
    Vector2(2.8725e12 + 4.363e8,0),
    Vector2(0,6800 + 3650),
    2,
    (190,190,210)
)

# Oberon
oberon = Body(
    "Oberon",
    3.014e21,
    Vector2(2.8725e12 + 5.835e8,0),
    Vector2(0,6800 + 3150),
    2,
    (170,170,190)
)

# Neptune
neptune = Body(
    "Neptune",
    1.02413e26,
    Vector2(4.4951e12,0),
    Vector2(0,5430),
    12,
    (65,105,225)
)

# Triton
triton = Body(
    "Triton",
    2.14e22,
    Vector2(4.4951e12 + 3.548e8,0),
    Vector2(0,5430 + 4390),
    2,
    (180,220,255)
)

class Universe:
  def __init__(self):
    self.bodies = [
    sun,

    mercury,
    venus,

    earth,
    moon,

    mars,
    phobos,
    deimos,

    jupiter,
    io,
    europa,
    ganymede,
    callisto,

    saturn,
    titan,
    enceladus,

    uranus,
    titania,
    oberon,

    neptune,
    triton
]

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


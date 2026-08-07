import physics
from body import Body
from vector2 import Vector2
dt = 0.1 #time delta per frame


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

 #Triton
triton = Body(
    "Triton",
    2.14e22,
    Vector2(4.4951e12 + 3.548e8,0),
    Vector2(0,5430 + 4390),
    2,
    (180,220,255)
)

# Parent

parent = Body(
    "Parent",
    1.0e24,
    Vector2(0, 0),
    Vector2(0, 0),
    20,
    (255, 220, 80)
)


# Child A and Moonlet A

child_a = Body(
    "Child A",
    1.0e20,
    Vector2(1.0e7, 0),
    Vector2(0, 2582.0),
    7,
    (255, 100, 100)
)

moonlet_a = Body(
    "Moonlet A",
    1.0e15,
    Vector2(1.05e7, 0),
    Vector2(0, 3738.0),
    2,
    (220, 220, 220)
)


# Child B and Moonlet B

child_b = Body(
    "Child B",
    1.0e20,
    Vector2(1.5e7, 0),
    Vector2(0, 2108.0),
    7,
    (100, 180, 255)
)

moonlet_b = Body(
    "Moonlet B",
    1.0e15,
    Vector2(1.55e7, 0),
    Vector2(0, 3264.0),
    2,
    (220, 220, 220)
)


# Child C and Moonlet C

child_c = Body(
    "Child C",
    1.0e20,
    Vector2(2.0e7, 0),
    Vector2(0, 1827.0),
    7,
    (100, 255, 150)
)

moonlet_c = Body(
    "Moonlet C",
    1.0e15,
    Vector2(2.05e7, 0),
    Vector2(0, 2983.0),
    2,
    (220, 220, 220)
)


# Child D and Moonlet D

child_d = Body(
    "Child D",
    1.0e20,
    Vector2(2.5e7, 0),
    Vector2(0, 1634.0),
    7,
    (255, 160, 80)
)

moonlet_d = Body(
    "Moonlet D",
    1.0e15,
    Vector2(2.55e7, 0),
    Vector2(0, 2790.0),
    2,
    (220, 220, 220)
)


# Child E and Moonlet E

child_e = Body(
    "Child E",
    1.0e20,
    Vector2(3.0e7, 0),
    Vector2(0, 1492.0),
    7,
    (190, 100, 255)
)

moonlet_e = Body(
    "Moonlet E",
    1.0e15,
    Vector2(3.05e7, 0),
    Vector2(0, 2648.0),
    2,
    (220, 220, 220)
)


# Child F and Moonlet F

child_f = Body(
    "Child F",
    1.0e20,
    Vector2(3.5e7, 0),
    Vector2(0, 1380.0),
    7,
    (100, 255, 240)
)

moonlet_f = Body(
    "Moonlet F",
    1.0e15,
    Vector2(3.55e7, 0),
    Vector2(0, 2536.0),
    2,
    (220, 220, 220)
)


# Child G and Moonlet G

child_g = Body(
    "Child G",
    1.0e20,
    Vector2(4.0e7, 0),
    Vector2(0, 1291.0),
    7,
    (255, 100, 200)
)

moonlet_g = Body(
    "Moonlet G",
    1.0e15,
    Vector2(4.05e7, 0),
    Vector2(0, 2447.0),
    2,
    (220, 220, 220)
)


# Child H and Moonlet H

child_h = Body(
    "Child H",
    1.0e20,
    Vector2(4.5e7, 0),
    Vector2(0, 1217.0),
    7,
    (150, 180, 255)
)

moonlet_h = Body(
    "Moonlet H",
    1.0e15,
    Vector2(4.55e7, 0),
    Vector2(0, 2373.0),
    2,
    (220, 220, 220)
)

class Universe:
  def __init__(self):
    self.bodies = [
      # sun,

      # mercury,
      # venus,

      # earth,
      # moon,

      # mars,
      # phobos,
      # deimos,

      # jupiter,
      # io,
      # europa,
      # ganymede,
      # callisto,

      # saturn,
      # titan,
      # enceladus,

      # uranus,
      # titania,
      # oberon,

      # neptune,
      # triton,
      parent,

      child_a,
      moonlet_a,

      child_b,
      moonlet_b,

      child_c,
      moonlet_c,

      child_d,
      moonlet_d,

      child_e,
      moonlet_e,

      child_f,
      moonlet_f,

      child_g,
      moonlet_g,

      child_h,
      moonlet_h

]

  def eular(self,dt):
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
      items.acceleration.x = 0
      items.acceleration.y = 0
    
  def leapFrog(self, dt):
    # ------------------------------------------------
    # 1. Calculate acceleration at the current position
    # ------------------------------------------------

    net_acceleration = Vector2(0, 0)
    for item in self.bodies:
      for body in self.bodies:
        if item == body:
          continue

        net_acceleration = (
          net_acceleration
          + physics.gravitational_acceleration(item, body)
        )

      item.old_acceleration = net_acceleration

    # ------------------------------------------------
    # 2. Update every position
    # ------------------------------------------------

    for item in self.bodies:
      item.position = (item.position + item.velocity * dt + item.old_acceleration * (0.5 * dt ** 2))

    # ------------------------------------------------
    # 3. Calculate acceleration at the new position
    # ------------------------------------------------

    net_acceleration = Vector2(0, 0)
    for item in self.bodies:
      for body in self.bodies:
        if item == body:
          continue

        net_acceleration = (
          net_acceleration
          + physics.gravitational_acceleration(item, body)
        )

      item.old_acceleration = net_acceleration

    # ------------------------------------------------
    # 4. Update every velocity
    # ------------------------------------------------

    for item in self.bodies:
      item.velocity = (item.velocity + (item.old_acceleration + item.acceleration) * (0.5 * dt))

    
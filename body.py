# Mass
# Position
# Velocity
# Radius
# Color
# Name

from vector2 import Vector2

class Body:
  def __init__(
    self, 
    name: str, 
    mass: float, 
    position: Vector2, 
    velocity: Vector2, 
    radius: float, 
    color:str
    ):

    self.mass = mass
    self.name = name
    self.position = position
    self.velocity = velocity
    self.radius = radius
    self.color = color
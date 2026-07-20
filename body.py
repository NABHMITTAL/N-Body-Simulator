# Mass
# Position
# Velocity
# Radius
# Color
# Name
#acceleration

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
    self.acceleration = 0

  def __str__(self):
    return (
      f"Name: {self.name}\n"
      f"Mass: {self.mass}\n"
      f"Position: {self.position}\n"
      f"Velocity: {self.velocity}\n"
      f"Radius: {self.radius}\n"
      f"Color: {self.color}"
    )
from body import Body

from vector2 import Vector2

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
  Vector2(150, 0),
  Vector2(0, 29.78),
  8,
  "blue"
)

moon = Body(
  "Moon",
  7.35e22,
  Vector2(151, 0),
  Vector2(0,30.8),
  3,
  "gray"
)

def __str__(self):
  return (
    f"Name: {self.name}\n"
    f"Mass: {self.mass}\n"
    f"Position: {self.position}\n"
    f"Velocity: {self.velocity}\n"
    f"Radius: {self.radius}\n"
    f"Color: {self.color}"
  )
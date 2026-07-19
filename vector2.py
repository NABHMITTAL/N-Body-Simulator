import math

class Vector2:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"({self.x}, {self.y})"
  
  def __mul__(self,scaler):
    X = self.x * scaler
    Y = self.y * scaler
    return Vector2(X,Y)


def unit_vec(vec1:Vector2, vec2: Vector2):
  dx = vec2.x-vec1.x
  dy = vec2.y-vec1.y
  magnitude = math.sqrt(dx**2 + dy**2)
  X = dx/magnitude
  Y = dy/magnitude
  return Vector2(X,Y)
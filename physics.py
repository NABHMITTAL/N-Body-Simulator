import math
from constants import G
from body import Body
import vector2

def distance(body1: Body, body2: Body):
  dx = body1.position.x - body2.position.x
  dy = body1.position.y - body2.position.y
  dist = math.sqrt(dx**2 + dy**2)
  return dist

def gravitational_force(body1: Body, body2: Body):
  force_mag = (G*body1.mass*body2.mass)/((distance(body1,body2))**2)
  force_dir = vector2.unit_vec(body1.position,body2.position)
  force = force_dir*force_mag
  return force
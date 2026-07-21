import pygame
pygame.init()
import universe  
from vector2 import Vector2

class Camera:
  def __init__(self,w,h):
    self.position = Vector2(0,0)
    self.zoom = 3.5e-9
    self.follow_target = None
    self.move_speed = 1e8
    self.zoom_speed = 1.1
    self.width = w
    self.height = h

  
  def world_to_screen(self,position):
    scale_x = (position.x - self.position.x) * self.zoom
    scale_y = (position.y - self.position.y)* self.zoom
    screen_x = scale_x + self.width/2
    screen_y = scale_y + self.height/2
    return (int(screen_x), int(screen_y))
  
  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      self.position.y = self.position.y - (1*self.move_speed)
      
    if keys[pygame.K_s]:
      self.position.y = self.position.y + (1*self.move_speed)
    
    if keys[pygame.K_d]:
      self.position.x = self.position.x + (1*self.move_speed)
    
    if keys[pygame.K_a]:
      self.position.x = self.position.x - (1*self.move_speed)
    if keys[pygame.K_f]:
      self.follow_target = universe.earth
    if keys[pygame.K_g]:
      self.follow_target = None
    

    if self.follow_target != None:
      distance = self.follow_target.position - self.position
      move_strength = distance*0.04
      self.position = self.position + move_strength

class Renderer:

  def __init__(self):
    info = pygame.display.Info()
    self.width = info.current_w
    self.height = info.current_h
    self.color = (0,0,0)
    self.state = True
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.camera = Camera(self.width, self.height)
    pygame.display.set_caption("N-Body Simulator")


  def process_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.state = False
      if event.type == pygame.MOUSEWHEEL:
        if event.y > 0:
          self.camera.zoom *= self.camera.zoom_speed
        if event.y < 0:
          self.camera.zoom /= self.camera.zoom_speed


  def draw(self,world:universe.Universe):
    self.screen.fill(self.color)
    for body in world.bodies:
      position = self.camera.world_to_screen(body.position)
      pygame.draw.circle(
        self.screen,
        body.color, 
        position, 
        body.radius
      )
    pygame.display.update()
  



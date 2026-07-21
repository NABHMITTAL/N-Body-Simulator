import pygame
pygame.init()
import universe


class Renderer:
  def __init__(self):
    info = pygame.display.Info()
    self.width = info.current_w
    self.height = info.current_h
    self.color = (0,0,0)
    self.state = True
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.dist_scale = 3.5e-9
    pygame.display.set_caption("N-Body Simulator")


  def draw(self,world:universe.Universe):
    self.screen.fill(self.color)
    for body in world.bodies:
      position = self.world_to_screen(body.position)
      pygame.draw.circle(
        self.screen,
        body.color, 
        position, 
        body.radius
      )
    pygame.display.update()


  def world_to_screen(self,position):
    scale_x = position.x * self.dist_scale
    scale_y = position.y * self.dist_scale
    screen_x = scale_x + self.width/2
    screen_y = scale_y + self.height/2

    return (int(screen_x), int(screen_y))
  
  def process_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.state = False
                                   
  
  

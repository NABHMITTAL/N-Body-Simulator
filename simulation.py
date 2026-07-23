from universe import Universe
import renderer


class Simulation:
  def __init__(self):
    self.universe = Universe()
    self.renderer = renderer.Renderer()
    self.selected_body_index = 0
    self.renderer.camera.follow_target = self.universe.bodies[self.selected_body_index]

    self.selected_body = 0

    self.dt = 0.01
    self.time_scale_index = 0
    self.time_scales = [1,10,100,1000,5000,10000,50000,100000,1000000,10000000]

  def check_events(self):
    #switch body
    if self.renderer.switch_body_requested:
      self.selected_body_index += 1
      if self.selected_body_index >= len(self.universe.bodies):
          self.selected_body_index = 0  
      self.renderer.camera.follow_target = self.universe.bodies[self.selected_body_index]
      self.renderer.switch_body_requested = False

    #change time
    if self.renderer.time_up_requested:
      if self.time_scale_index<9:
        self.time_scale_index+= 1
        self.renderer.time_up_requested = False
    if self.renderer.time_down_requested:
      if self.time_scale_index>0:
        self.time_scale_index-= 1
        self.renderer.time_down_requested = False
    if self.renderer.time_to_one:
        self.time_scale_index = 0
        self.renderer.time_to_one = False

  def run(self):
    while self.renderer.state:

      self.renderer.process_events()
      self.check_events()
      sim_dt = self.dt * self.time_scales[self.time_scale_index]
      self.renderer.camera.update()
      self.universe.step(sim_dt)
      self.renderer.draw(self.universe, self.time_scales[self.time_scale_index])
      print(self.renderer.camera.zoom)
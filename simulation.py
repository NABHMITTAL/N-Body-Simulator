from universe import Universe
from renderer import Renderer


class Simulation:
  def __init__(self):
    self.universe = Universe()
    self.renderer = Renderer()

    self.dt = 0.01
    self.time_scale = 100000

  def run(self):
    while self.renderer.state:
      sim_dt = self.dt * self.time_scale
      self.renderer.process_events()
      self.universe.step(sim_dt)
      self.renderer.draw(self.universe)
from manim import *

class Bus:
  def __init__(self, position=[0,0,0]):
     self.position = position
     self.contents = None

  def get_bus(self):
      return self

  def put_in_bus(self, data):
      self.contents = data

  def read_from_bus(self):
    return data
  
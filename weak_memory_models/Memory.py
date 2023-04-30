from manim import *

class Memory:
  def __init__(self, contents, position=[0,0,0]):
     self.position = position
    #  self.rectangle = Rectangle(color=BLUE, fill_opacity=1).move_to(position)
     self.contents = contents

  def get_memory(self):
      return self

  def do_memory_operation(self, op):
      i = Bus.read_from_bus()
      if (i[0] == 'r'):
        val = read(i[1])
        Bus.put_in_bus(val)
      elif (i[0] == 'w'):
        write(i[1], i[2])

  def read(self, location):
    return contents[location]
  
  def write(self, location, value):
    contents[location] = value

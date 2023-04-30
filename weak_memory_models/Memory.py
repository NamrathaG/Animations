from manim import *

class Memory:
  def __init__(self, contents, position=[0,0,0]):
     self.position = position
     self.contents = contents

  def get_memory(self):
      return self

  # def do_memory_operation(self, op):
  #     i = Bus.read_from_bus()
  #     if (i[0] == 'r'):
  #       val = read(i[1])
  #       Bus.put_in_bus(val)
  #     elif (i[0] == 'w'):
  #       write(i[1], i[2])

  def get_contents(self):
     return self.contents
  
  def read(self, location):
    return self.contents[location]
  
  def write(self, location, value):
    self.contents[location] = value

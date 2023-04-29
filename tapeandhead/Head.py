from manim import *

class Head:
  def __init__(self, table, position=(1,1)):
     self.location = position
     self.table = table
     self.arrow = Arrow(start=UP, end=DOWN, color=GOLD).scale(0.5)
     self.arrow.next_to(table.get_cell(position), UP)

  def get_head(self):
      return self

#   def find_cell(self, cell): 
#       for 

  def move_right(self):
      newloc = (self.location[0], self.location[1]+1)
      self.location = newloc

  def move_left(self):
      newloc = (self.location[0], self.location[1]-1)
      self.location = newloc
    #   self.arrow.next_to(self.table.get_cell(newloc), UP)
    #   self.play(self.arrow.animate.next_to(self.table.get_cell(newloc),UP))


      
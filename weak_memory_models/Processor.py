from manim import *

class Processor:
  def __init__(self, pid, position=[0,0,0], instructions=[]):
     self.location = position
     self.pid = pid
     self.instructions = instructions
     self.pc = 0
    #  self.arrow = Arrow(start=UP, end=DOWN, color=GOLD).scale(0.5) # program counter
    #  self.arrow.next_to(table.get_cell(position), UP)

  def get_proc(self):
      return self

#   def issue_instruction(self):
#       i = instructions[pc]
#       put_in_bus(i)
#       self.pc = self.pc + 1
  
  def create_program_list(self):
    program_list = []
    for i in self.instructions:
        if i[0] == 'r':
            if i[2] == None:
               program_list.append(["read(" + i[1]+")"])
            else:
               program_list.append(["read(" + i[1]+ ", " + str(i[2])+")"])
        elif i[0] == 'w':
            program_list.append(["write(" + i[1]+ ", " + str(i[2])+")"])
    return (program_list)
      
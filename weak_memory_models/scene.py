from manim import *
from Memory import *
from Bus import *
from Processor import *

"""
TODO
1. position all of the components
2. put_in_bus
3. update_memory
4. bus_to_proc
5. bus_to_memory
6. update proc read return value
"""


# tapeList = ["b","b","1","1","1","b","b","b","b"]
# tape = Table([tapeList], include_outer_lines=True)
# tape.get_vertical_lines()[0].set_color(BLACK)
# tape.get_vertical_lines()[1].set_color(BLACK)
# headObj = Head(tape, position=(1,3))


#Initialize processors
proc1_o = Processor(pid = 1, instructions= [('r','x', None, None), ('w', 'x', 2, None), ('r', 'y', None, None)])
proc1_a = Table(proc1_o.create_program_list(),col_labels=[Text("P1")])
proc1_a.add(SurroundingRectangle(proc1_a.get_rows()[1]))
proc1_a.get_horizontal_lines().set_color(BLACK)


proc2_o = Processor(pid = 1, instructions= [('r','y', None, None), ('w', 'x', 6, None), ('w', 'y', 3, None)])
proc2_a = Table(proc2_o.create_program_list(),col_labels=[Text("P2")])
proc2_a.add(SurroundingRectangle(proc2_a.get_rows()[1]))
proc2_a.get_horizontal_lines().set_color(BLACK)


proc3_o = Processor(pid = 1, instructions= [('r','y', None, None), ('w', 'x', 6, None), ('w', 'y', 3, None)])
proc3_a = Table(proc3_o.create_program_list(),col_labels=[Text("P2")])
proc3_a.add(SurroundingRectangle(proc3_a.get_rows()[1]))
proc3_a.get_horizontal_lines().set_color(BLACK)

processors_group = Group(proc1_a, proc2_a, proc3_a).scale(0.5).arrange_in_grid(rows=1, buff=1).move_to([0,2,0])

#Initialize bus
bus_o = Bus()
bus_a = Table([[""]], include_outer_lines=True).next_to(processors_group, DOWN).scale(0.5)


#Initialize memory
contents_m = {"x" : 2, "y": 3}
mem_o = Memory(contents_m)
mem_a = Table([[key +": " +str(value) for key, value in contents_m.items()]], include_outer_lines=True).next_to(bus_a, DOWN).scale(0.5)



class WeakMemoryModels(Scene):

    # class head:
    def update_memory(self, location, value):
        global mem_a
        mem_o.write(location, value)
        mem_a_new = Table([[key +": " +str(value) for key, value in mem_o.get_contents().items()]], include_outer_lines=True).next_to(bus_a, DOWN).scale(0.5)
        self.play(Transform(mem_a,mem_a_new))
        self.remove(mem_a)
        self.add(mem_a_new)
        mem_a  = mem_a_new

    def put_in_bus(self, value):
        global bus_a
        bus_o.put_in_bus(value)
        bus_a_new = Table([[value]], row_labels=[Text("Bus")], include_outer_lines=True).next_to(processors_group, DOWN).scale(0.5)
        self.play(Transform(bus_a, bus_a_new))
        self.remove(bus_a)
        self.add(bus_a_new)
        bus_a  = bus_a_new
        # headObj.move_right()
        # head = headObj.get_head()
        # pos = head.location
        # cell = tape.get_cell(pos)
        # arrow = head.arrow
        # self.play(arrow.animate.next_to(cell,UP))

    # def write_to_tape(self, alpha):
    #     global tape
    #     global tapeList
    #     curr_head_pos = headObj.location
    #     print(curr_head_pos)
    #     tapeList[curr_head_pos[1]-1] = alpha
    #     print(tapeList)
    #     tape2 = Table([tapeList], include_outer_lines=True)
    #     tape2.get_vertical_lines()[0].set_color(BLACK)
    #     tape2.get_vertical_lines()[1].set_color(BLACK)
    #     self.play(Transform(tape,tape2))
    #     self.remove(tape)
    #     self.add(tape2)
    #     tape = tape2

    # def tell_me_what_to_do(self, program, state, curr_alpha):
    #     return program["delta"][state][curr_alpha]

    def construct(self):


        


        self.add(processors_group, bus_a, mem_a)
        self.update_memory('x', 17)
        self.update_memory('x', 10)
        self.put_in_bus("read(x)")
        self.put_in_bus("write(y)")
        # program = {
        #     "initial" :"q0",
        #     "final" : ["q3"],
        #     "delta" : {"q0":
        #               {
        #               "1":["q0", "x", "R" ], 
        #               "b": ["q1", "b", "L"]
        #               },
        #             "q1":
        #              {
        #                "1":["q1", "1", "L"],
        #                "x":["q2", "1", "R"],
        #                "b":["q3", "b", "R"]
        #              },  
        #              "q2":
        #              {
        #                  "1":["q2", "1", "R"],
        #                  "b":["q1", "1", "L"]
        #              }
        #            }
        #         }

        # control_state = program["initial"]
        # while(control_state not in program["final"]):
        #     loc = headObj.location
        #     ent = str(tape.get_entries(loc).lines_text.original_text)
            
        #     # try:
        #     #     l = program["delta"][control_state][ent]
        #     # except Exception:
        #     #     break
        #     l = program["delta"][control_state][ent]
        #     control_state = l[0]
        #     self.write_to_tape(l[1])
        #     if (l[2] == "L"):
        #         self.move_left()
        #     else:
        #         self.move_right()
          
          
            


        # loc = headObj.location
        # cell = tape.get_cell(loc)
        # pprint
        # print()
        # self.move_right()
        # self.move_left()
        # self.write_to_tape("k")
        # self.move_right()
        # self.write_to_tape("x")
        # self.move_right()
        # self.write_to_tape("y")
        # self.wait(1)
        

        # head = headObj.get_head()

        # headObj.move_right()

        # ent = tape.get_entries()
        # for item in ent:
        #         print(item.
        # cell_last = tape.get_cell((1,4))
        # cell_first = tape.get_cell((1,1))
        # cell_2 = tape.get_cell(cell_first.get_center)

        # for i in [(1,1),(1,2),(1,3),(1,4)]:
        #     if cell_first == tape.get_cell((i)):
        #           print("yes found it")

        # print(cell_first.get)
        # print(cell_first.points)
        # print(cell_first.get)
        # print(cell_first)

        # headObj = Head(cell_first)
        # head = headObj.get_head()
        # self.add(tape, head)

        # head.next_to(cell_first, UP)
        # head_location = cell_first
        # t0.get_vertical_lines()[1].set_color(BLACK)
        

        # arrow_1.move_to(cell, UP)
        # self.add(tape,head)
        # self.play(head.animate.next_to(cell_last,UP))
        # self.wait(1)
         
        # self.play(Create(Arrow(start=UP, end=DOWN, color=GOLD).next_to(cell,UP)))
        
        # self.add(circle, square, triangle)
        # self.wait(1)

        
        
        
        
        
        # circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        # square = Square()  # create a square
        # square.rotate(PI / 4)  # rotate `a certain amount

        # self.play(Create(square))  # animate the creation of the square
        # self.play(Transform(square, circle))  # interpolate the square into the circle
        # self.play(FadeOut(square))  # fade out animation


        # rectangle = Rectangle()  # create a circle
        # rect1 = Rectangle(width=4.0, height=1.0, grid_xstep=1.0)
        # head = Arrow(start=UP, end=DOWN, color=GOLD)
        # arrow_1.next_to(rect1, UP)

        # self.add(rect1)
        # self.add(arrow_1)
        # what do I want
        # 1. I need to write in the squares
        # 2. I also need to move the arrow to the squares
        # 3. Remove the right boundary of the rectangle
        # print("Hello")
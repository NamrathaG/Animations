from manim import *
from Head import *

"""
TODO
1. (q0, a on tape1, b on tape2) = (q1, change to a' on tape1, change to b' on tape2, L, R)

"""

tapeLists = [["b","b","1","1","1","b","b","b","b"], ["b","b","b","b","b","b","b","b","b"]]
tapes= [Table([tapeLists[0]], include_outer_lines=True), Table([tapeLists[1]], include_outer_lines=True)]
tapes[0].get_vertical_lines()[0].set_color(BLACK)
tapes[0].get_vertical_lines()[1].set_color(BLACK)
tapes[1].get_vertical_lines()[0].set_color(BLACK)
tapes[1].get_vertical_lines()[1].set_color(BLACK)
tapes[0].shift(UP*2).scale(0.7)
tapes[1].next_to(tapes[0], DOWN, buff=1).scale(0.7)

heads = [Head(tapes[0], position=(1,3)), Head(tapes[1], position=(1,3)) ]

class TapeAndHead(Scene):

    # class head:
    def move_left(self, tape_no):
        heads[tape_no].move_left()
        head = heads[tape_no].get_head()
        pos = head.location
        cell = tapes[tape_no].get_cell(pos)
        arrow = head.arrow
        self.play(arrow.animate.next_to(cell,UP))

    def move_right(self, tape_no):
        heads[tape_no].move_right()
        head = heads[tape_no].get_head()
        pos = head.location
        cell = tapes[tape_no].get_cell(pos)
        arrow = head.arrow
        self.play(arrow.animate.next_to(cell,UP))

    def write_to_tape(self, tape_no, alpha):
        global tapes
        global tapeLists
        curr_head_pos = heads[tape_no].location
        tapeLists[tape_no][curr_head_pos[1]-1] = alpha
        tape2 = Table([tapeLists[tape_no]], include_outer_lines=True)
        tape2.get_vertical_lines()[0].set_color(BLACK)
        tape2.get_vertical_lines()[1].set_color(BLACK)
        if (tape_no == 1):
            tape2.next_to(tapes[0], DOWN, buff=1).scale(0.7)
        else:
            tape2.shift(UP*2).scale(0.7)
        self.play(Transform(tapes[tape_no],tape2))
        self.remove(tapes[tape_no])
        self.add(tape2)
        tapes[tape_no] = tape2


    def construct(self):


        self.add(tapes[0], tapes[1], heads[0].get_head().arrow, heads[1].get_head().arrow)
        self.move_left(0)
        self.write_to_tape(0,"x")
        self.move_right(1)
        self.write_to_tape(1,"y")
        self.move_left(0)
        self.write_to_tape(0,"x")
        self.move_right(1)
        self.write_to_tape(1,"y")
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
          
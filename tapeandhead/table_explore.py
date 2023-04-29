from manim import *
from pprint import pprint



class TableExplore(Scene):

    # class head:


    # def move_left(self, head):
          

    def construct(self):
      
        tape_list = ["x", "y", "y", "z"]
        tape = Table([tape_list], include_outer_lines=True)
        self.add(tape)
        # tape_list2 = ["x", "x", "y", "z"]
        # tape2 = Table([tape_list2], include_outer_lines=True)
        cell = tape.get_cell((1,1))
        ent = tape.get_entries((1,1)).lines_text.original_text
        # arrow = Arrow(start=UP, end=DOWN, color=GOLD)
        # self.play(tape.animate.set_value([["a","b","c","d"]]))
        pprint(vars(ent))
        # self.play(arrow.animate.next_to(tape.get_cell((1,3)),UP))


        # self.play(Transform(tape, tape2))
        # self.wait(1)
        # self.add(tape)
        # cell = tape.get_cell((1,2))
        # cell.set_color(BLUE)
        # ent = tape.get_entries_without_labels()
        # colors = [BLUE, GREEN, YELLOW, RED]
        # pprint(vars(ent[0]))
        # # ent[0].set
        # for k in range(len(colors)):
        #                 ent[k].                        
        # self.add(tape,cell)
        # pprint(vars(tape))
        # cell1 = tape.get_cell((1,2))


        # paragraph = Paragraph('this is a awesome', 'paragraph',
        #               'With \nNewlines', '\tWith Tabs',
        #               '  With Spaces', 'With Alignments',
        #               'center', 'left', 'right')

        # text1 = Text("Hello", slant=ITALIC)
        # pprint(vars(cell1))
        # ent = tape.get_entries()
        # # pprint(vars(ent))
        # sos = ent.submobjects
        # # pprint(vars(sos[0]))
        # lt = sos[0].lines_text
        # pprint(vars(lt))
        # lt.original_text = "h"
        # self.add(tape)
        # print(paragraph.original_text)
        # print(text1.chars[0])
        # print(paragraph)
        # for p in paragraph.chars:
        #     print(p.
        # ent = tape.get_entries((1,1))
        # print(ent)
        # for item in ent:

        # for row in tape:
        #     print(row)
                
    
        
        
        
    
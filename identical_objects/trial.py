from manim import *
import random

def random_derangement(n):
        while True:
            v = [i for i in range(n)]
            for j in range(n - 1, -1, -1):
                p = random.randint(0, j)
                if v[p] == j:
                    break
                else:
                    v[j], v[p] = v[p], v[j]
            else:
                if v[0] != 0:
                    return tuple(v)

class Indications(Scene):



    def construct(self):



        # lbl = Tex(r"Circum-\\scribe").scale(2)

        lbl = Square().set_color(BLACK)
        self.add(lbl)
        self.play(Circumscribe(lbl))
        self.play(Circumscribe(lbl, Circle))
        self.play(Circumscribe(lbl, fade_out=True))
        self.play(Circumscribe(lbl, time_width=2))
        self.play(Circumscribe(lbl, Circle, True))


        grid = NumberPlane()
        grid = NumberPlane()
        grid_title = Tex("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        # text = Text("Colors").scale(2)
        # for letter in text:
        #     letter.set_color(random_bright_color())


        # tex = Tex("Wiggle").scale(3)
        # # self.play(Wiggle(tex), Indicate(tex))
        # # self.wait()

        # self.play(ApplyWave(
        #     tex,
        #     direction=RIGHT,
        #     time_width=0.5,
        #     amplitude=0.3
        # ))
        # dcol= []
        # text = Text("distinct").scale(2)
        # for letter in text:
        #     dcol.append(random_bright_color())


        # m1 = MarkupText(f'6 <b> <span fgcolor= "{dcol[0]}">d</span><span fgcolor= "{dcol[1]}">i</span><span fgcolor= "{dcol[2]}">s</span><span fgcolor= "{dcol[3]}">t</span><span fgcolor= "{dcol[4]}">i</span><span fgcolor= "{dcol[5]}">n</span><span fgcolor= "{dcol[6]}">c</span><span fgcolor= "{dcol[7]}">t</span></b> <span fgcolor="{RED}">Hello</span> tiles')
        # m2 = MarkupText(f'5 <b>distinct</b> <span fgcolor="{BLUE}">World</span> tiles').next_to(m1, DOWN)

        # self.play(Write(m1))
        # self.play(Write(m2))
        # self.play(Flash(m1))
        
        # m1 = MarkupText(f'Identical Objects Rule').scale(1).shift(UP)
        # m2 = MarkupText(f'In probability problems, there are no collections of identical objects;').next_to(m1, DOWN).scale(0.7)
        # m3 = MarkupText(f'all objects are <span fgcolor="{YELLOW}">distinguishable</span>').next_to(m2, DOWN).scale(0.7)
        # # paragraph = Paragraph(MarkupText(f'6 <b>identical</b> Hello tiles'), '5 identical World tiles')

        # self.play(Write(m1))
        # self.play(Write(m2))
        # self.play(Write(m3))

        # m3 = MarkupText(f'Tile addresses')

        # m4 = MarkupText(f'11 <b>distinct</b> tiles')

        self.wait(3)
        # w1 = Text("Hello", color=RED).scale(0.7)
        # t1 = Rectangle(width=2.0, height=1.0).set_fill(GRAY, opacity=0.2).scale(0.6)
        # w2 = Text("World", color=BLUE).scale(0.7)
        # t2 = Rectangle(width=2.0, height=1.0).set_fill(GRAY, opacity=0.2).scale(0.6)


        # vg1 = VGroup(col1, rect1)
        # vg2 = VGroup(col2, rect2)

        # text1 = MathTex(r"P(")
        # text2 = MathTex(r")")

        # self.add(text1, vg1.next_to(text1, RIGHT), vg2.next_to(vg1, RIGHT), text2.next_to(vg2, RIGHT))

        
        # # self.play(Write(text1), Create(vg1), Create(vg2), Write(text2))

        # self.wait(4)
    
        
        
        # col1 = Text("Hello", color=RED).move_to([0,0,0]).scale(0.8)
        # emptytext1 = Text("?")
        # rect1 = Rectangle(width=2.0, height=1.0).move_to([0,0,0]).set_fill(GRAY, opacity=0.2).scale(0.8)
        # col2 = Text("World", color=BLUE).move_to([2,0,0]).scale(0.8)
        # rect2 = Rectangle(width=2.0, height=1.0).move_to([2,0,0]).set_fill(GRAY, opacity=0.2).scale(0.8)
        # emptytext2 = Text("?").move_to([2,0,0])
        
        # first = VGroup()
        # second = VGroup()
        # first.add(rect1, col1)
        # second.add(rect2, col2)
        # self.add(rect1, col1, col2, rect2)
        # self.play(rect1.animate.flip(), Transform(col1, emptytext1), rect2.animate.flip(), Transform(col2, emptytext2))
        # # self.play(rect.animate.shift(RIGHT*2), rect2.animate.shift(LEFT*2), col.animate.shift(RIGHT*2), col2.animate.shift(LEFT*2))
        # self.play(first.animate.shift(RIGHT*2), second.animate.shift(LEFT*2))
        # self.wait(2)

        # col = Text("Hello", color=RED).move_to([0,0,0]).scale(0.8)
        # circle = Circle().set_fill(RED)
        # self.play(Create(circle))
        # self.play(circle.animate.flip())
        # self.play(ApplyMethod(circle.flip()))
        # self.wait(1)
        
        #########$$$$$$$$$
        # coordinates  = [[-1,2,0],  [0,2,0], [1,2,0], [-1,1,0], [0, 1, 0], [1, 1, 0], [-1, 0, 0],  [0,0,0] , [1, 0 , 0], [-1,-1,0], [0,-1,0]]
        # colors  = [RED, RED, RED, RED, RED, RED, BLUE, BLUE, BLUE, BLUE, BLUE]
        # word = ["Hello", "Hello", "Hello", "Hello", "Hello", "Hello", "World", "World", "World", "World", "World"]
        # positions = [0,1,2,3,4,5,6,7,8,9,10]
        # box_of_wt = VGroup()
        # box_of_words = VGroup()
        # box_of_tiles = VGroup()
    
        # index = 0
        # box = Rectangle(width=3, height=4).move_to([0,0.5,0])
        # text1 = MarkupText(f'6 identical <span fgcolor="{RED}">Hello</span>tiles and 5 identical <span fgcolor="{BLUE}">World</span> tiles').shift(UP).shift(UP).shift(UP)
        # self.play(Create(box))
        # self.play(Write(text1))

        # words = [Text(wor, color=col).scale(0.3).move_to(cor) for cor, col, wor in zip(coordinates, colors, word)]
        # questionmarks = [Text("?").scale(0.3).move_to(cor) for cor in coordinates]
        # rectangles = [Rectangle().set_fill(GRAY, opacity=0.2).scale(0.2).move_to(cor) for cor, col in zip(coordinates, colors)]
       
        # for w,r in zip(words,rectangles): 
        #     k = VGroup()
        #     k.add(r,w)
        #     box_of_wt.add(k)
        #     box_of_words.add(w)
        #     box_of_tiles.add(r)
        

        # self.play(*[Create(b) for b in box_of_tiles], run_time = 2)
        # self.add(*[b for b in box_of_words])

        # self.play(*[b.animate.flip() for b in box_of_tiles], *[Transform(a, b) for a, b in zip(box_of_words, questionmarks)])
        
        # # random.shuffle(positions)
        # positions = random_derangement(11)
        # self.play(*[b.animate.move_to(coordinates[i]) for b, i in zip(box_of_wt, positions) ])
       
        # self.wait(5)
        #####$$$$$$$$$$$$$$$$$$$$


        # self.play(*[Create(b) for b in box_of_circles], run_time =1)
        # self.play(*[b.animate.flip() for b in box_of_circles])
        # self.play(*)
        # self.wait(5)
        # Possible_outcomes = [[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]]

        # y = 2.8
        # x = 4
        # for outcome in Possible_outcomes:
        #     pos1 = [x, y, 0]
        #     pos2 = [x+1, y , 0]
        #     pos3 = [x+2, y, 0]
            
        #     circle1 = Circle().set_color(RED if outcome[0] else BLUE).scale(0.18).move_to(pos1).set_style(fill_opacity = 1)
        #     circle2 = Circle().set_color(RED if outcome[1] else BLUE).scale(0.18).move_to(pos2).set_style(fill_opacity = 1)
        #     circle3 = Circle().set_color(RED if outcome[2] else BLUE).scale(0.18).move_to(pos3).set_style(fill_opacity = 1)
        #     self.add(circle1)
        #     self.add(circle2)
        #     self.add(circle3)
        #     y = y - 0.8



        
        # self.play(Create(Rectangle(width=4, height=1).move_to([5,3.5,0])), Create(Rectangle(width=4, height=1).move_to([5,-3.5,0])), run_time=2)
        # ellipse_1 = Ellipse(width=4.0, height=7.9, color=BLUE_B).move_to([5, 0,0])
        # self.play(Create(ellipse_1))

        # self.wait(5)

        # text = MarkupText(f'P(<span fgcolor="{RED}">RRR</span>) > P(<span fgcolor="{BLUE}">BBB</span>)')
        # self.play(Write(text), run_time=2)


        # indications = [ApplyWave,Circumscribe,Flash,FocusOn,Indicate,ShowPassingFlash,Wiggle]
        # names = [Tex(i.__name__).scale(3) for i in indications]
        # self.wait(1)
        # self.add(Circle().move_to([0,0,0]))
        # self.wait(1) 
        # self.add(Circle().move_to([1,0,0]))
        # self.wait(1)
        # colors = [DARK_BROWN, BLUE_E, BLUE_D, BLUE_A, TEAL_B, GREEN_B, YELLOW_E]
        # radius = [1 + rad * 0.1 for rad in range(len(colors))]

        # circles_group = VGroup()

        # # zip(radius, color) makes the iterator [(radius[i], color[i]) for i in range(radius)]
        # circles_group.add(*[Circle(radius=rad, stroke_width=10, color=col)
        #                     for rad, col in zip(radius, colors)])
        # circleslist = [Circle(radius=rad, stroke_width=10, color=col) for rad, col in zip(radius, colors)]
   
        # self.play(*[Create(l) for l in circleslist], run_time =5)
        # self.wait(5)
        
        # for k in circleslist: 
        #     self.remove(k)
        

        # t = Text("hello there")
        # self.play(Write(t))
        # box = Group()
        # integer1 =  Integer(number=1).move_to([0,0,0]).scale(0.75)
        # integer2 = Integer(number =2 ).move_to([1,0,0]).scale(0.75)
        # box.add(integer1)
        # box.add(integer2)

        # # t = Text("hello there")
        # self.play(Indicate(box[0]), Indicate(box[1]))
        # self.wait(2)
        # self.add(names[0])
        # for i in range(len(names)):
        #     if indications[i] is Flash:
        #         self.play(Flash(UP))
        #     elif indications[i] is ShowPassingFlash:
        #         self.play(ShowPassingFlash(Underline(names[i])))
        #     else:
        #         self.play(indications[i](names[i]))
        #     self.play(AnimationGroup(
        #         FadeOut(names[i], shift=UP*1.5),
        #         FadeIn(names[(i+1)%len(names)], shift=UP*1.5),
        #     ))
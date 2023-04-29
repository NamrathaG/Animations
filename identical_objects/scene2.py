from manim import *
from itertools import permutations 
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

class MobjectExample(Scene):
    def construct(self):

        coordinates  = [[-1, 2, 0],  [0, 2, 0], [1, 2, 0], [-1, 1, 0], [0, 1, 0], [1, 1, 0], [-1, 0, 0], [0, 0, 0] , [1, 0 , 0], [-1, -1, 0], [0, -1, 0]]
        colors  = [RED, RED, RED, RED, RED, RED, BLUE, BLUE, BLUE, BLUE, BLUE]
        word = ["Hello", "Hello", "Hello", "Hello", "Hello", "Hello", "World", "World", "World", "World", "World"]
        indices = [0,1,2,3,4,5,6,7,8,9,10]
        Possible_outcomes = [[0,0], [0,1], [1,0], [1,1]]
        box_of_wt = VGroup()
        box_of_words = VGroup()
        box_of_tiles = VGroup()
    
        box = Rectangle(width=3, height=4).move_to([0,0.5,0])
        text1 = MarkupText(f'6 identical <span fgcolor="{RED}">Hello</span> tiles and 5 identical <span fgcolor="{BLUE}">World</span> tiles').shift(UP).shift(UP).shift(UP).scale(0.7)
        self.play(Create(box))
        self.play(Write(text1))

        words = [Text(wor, color=col).scale(0.3).move_to(cor) for cor, col, wor in zip(coordinates, colors, word)]
        questionmarks = [Text("?").scale(0.3).move_to(cor) for cor in coordinates]
        tiles = [Rectangle().set_fill(GRAY, opacity=0.2).scale(0.2).move_to(cor).set_stroke(width=1) for cor, col in zip(coordinates, colors)]
       
        for w,r in zip(words,tiles): 
            k = VGroup()
            k.add(r,w)
            box_of_wt.add(k)
            box_of_words.add(w)
            box_of_tiles.add(r)
        

        # self.play(*[Create(b) for b in box_of_tiles], run_time = 2)
        # self.add(*[b for b in box_of_words])

        self.play(*[Write(b) for b in box_of_words], *[Create(b) for b in box_of_tiles])
        
        self.wait(2)
        self.play(*[b.animate.flip() for b in box_of_tiles], *[Transform(a, b) for a, b in zip(box_of_words, questionmarks)])
        self.wait(2)
        # random.shuffle(indices)
        shuffled_indices = random_derangement(11)
        self.play(*[b.animate.move_to(coordinates[i]) for b, i in zip(box_of_wt, shuffled_indices) ], run_time =1)
        random.shuffle(indices)
        self.play(*[b.animate.move_to(coordinates[i]) for b, i in zip(box_of_wt, indices) ], run_time =1)

       
        self.wait(5)


        #$$$$$$

        w1 = Text("Hello", color=RED).scale(0.3)
        t1 = Rectangle().set_fill(GRAY, opacity=0.2).scale(0.2).set_stroke(width=1)
        w2 = Text("World", color=BLUE).scale(0.3)
        t2 = Rectangle().set_fill(GRAY, opacity=0.2).scale(0.2).set_stroke(width=1)


       

        part1 = Text("P(").scale(0.7).next_to(box,DOWN, buff=0.5).align_to(box, LEFT)
        vg1 = VGroup(t1, w1).next_to(part1, RIGHT, buff = 0.08)
        vg2 = VGroup(t2, w2).next_to(vg1, RIGHT, buff = 0.06)
        part2 = Text(") = ?").scale(0.7).next_to(vg2, RIGHT, buff = 0.08)

        self.play(Write(part1))
        self.play(Create(vg1))
        self.play(Create(vg2))
        self.play(Write(part2))
        

        self.wait(2)


        # text2 = MarkupText(f'P(<span fgcolor="{RED}">Hello</span><span fgcolor="{BLUE}">World</span>) = ?').next_to(box,DOWN, buff=0.5).scale(0.7)
        # self.play(Write(text2))
        
        # self.wait(2)



        """
        Let's look at all the possible outcomes. 
        
        """
        y = 1.5
        x = 4
        for outcome in Possible_outcomes:
            pos1 = [x, y, 0]
            pos2 = [x+1, y , 0]
            pos3 = [x+2, y, 0]
            

            words = [Text(wor, color=col).scale(0.3).move_to(cor) for cor, col, wor in zip(coordinates, colors, word)]
            
            tile1 = Rectangle().set_fill(GRAY, opacity=0.2).scale(0.2).move_to(pos1).set_stroke(width=1)
            tile2 = Rectangle().set_fill(GRAY, opacity=0.2).scale(0.2).move_to(pos2).set_stroke(width=1)
            word1 = Text("Hello" if outcome[0] else "World").set_color(RED if outcome[0] else BLUE).scale(0.3).move_to(pos1)
            word2 = Text("Hello" if outcome[1] else "World").set_color(RED if outcome[1] else BLUE).scale(0.3).move_to(pos2)
            self.play(Create(tile1), Write(word1))
            self.play(Create(tile2), Write(word2))
            y = y - 1


        """
        TODO: Write pick1 and pick2 on the sample space
        """
       

        """
        Removing box, text1 and text2
        """
        for a in box_of_wt:
             self.remove(a)
        
        self.remove(text1, part1, vg1, vg2, part2, box)

        self.wait(2)

        
        ts = MarkupText(f'S be the sample space').shift(UP*3).shift(LEFT*4).scale(0.7)
        te = MarkupText(f'E be the event that we get <span fgcolor="{RED}">Hello</span><span fgcolor="{BLUE}">World</span>').scale(0.7)
        

        ellipse_1 = Ellipse(width=3, height=5, color=PINK).move_to([4.5, 0,0])
        self.play(Create(ellipse_1))


        samplespace_text = Text(f"S").move_to([3,2,0]).scale(0.8)
        self.play(Write(samplespace_text), Write(ts))
        
        ellipse_2 = Ellipse(width=2.3, height=1, color=PINK).move_to([4.5, -0.5, 0])
        self.play(Create(ellipse_2))

        samplespace_text = Text(f"E").move_to([3.6,0,0]).scale(0.5)
        self.play(Write(samplespace_text), Write(te.next_to(ts, DOWN).align_to(ts,LEFT)))


        self.wait(5)


        """
        Since probability is no. of favourable cases divede by total no. of cases
        We get 1 / 4. 
        Is that it then? Well turns out this is actually not the right answer.
        """

        

        t1 = MathTex(r"\text{P(E)}").shift(LEFT*3)
        t2 = MathTex(r"= \frac{\text{n(E)}}{\text{n(S)}}").next_to(t1)  
        t3 = MathTex(r"= \frac{1}{4}").next_to(t2, DOWN).align_to(t2,LEFT)   
        cross1 = Cross(t3)    

        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Create(cross1))
        self.wait(5)

        # """
        # This looks to be right, so what could have gone wrong.
        # Pause for a moment and see if you can figure it out.
        # """
        # #Pause screen
        
        self.remove(ts, te, t1,t2,t3, cross1)
        pause_text = Text("Where did we go wrong?").shift(LEFT).shift(LEFT)
        self.play(Write(pause_text) , run_time = 2)
        self.wait(5)
        self.clear()

        """
        Okay so the devil is in the details. 
        """
        t1 = MathTex(r"\text{Probability} = \frac{\text{number of favorable cases}}{\text{total number of cases}}^*")   
        t2 = MarkupText(f'<sup>*</sup> Each case must be <span fgcolor="{YELLOW}">equally likely</span>').scale(0.5)

        
        # asterisk1 = Text("*").move_to([4.6,0.7,0])
        # asterisk2 = Text("*").move_to([])
       
        self.play(Write(t1), run_time = 3)
        self.wait(1)
        self.play(Write(t2.next_to(t1, DOWN, buff=0.5)), run_time = 3)
        # self.play(Write(asterisk1))
        self.wait(2)

        self.clear()


        y = 1.5
        x = 4
        for outcome in Possible_outcomes:
            pos1 = [x, y, 0]
            pos2 = [x+1, y , 0]
            pos3 = [x+2, y, 0]
            

            words = [Text(wor, color=col).scale(0.3).move_to(cor) for cor, col, wor in zip(coordinates, colors, word)]
            
            tile1 = Rectangle().set_fill(GRAY, opacity=0.2).scale(0.2).move_to(pos1).set_stroke(width=1)
            tile2 = Rectangle().set_fill(GRAY, opacity=0.2).scale(0.2).move_to(pos2).set_stroke(width=1)
            word1 = Text("Hello" if outcome[0] else "World").set_color(RED if outcome[0] else BLUE).scale(0.3).move_to(pos1)
            word2 = Text("Hello" if outcome[1] else "World").set_color(RED if outcome[1] else BLUE).scale(0.3).move_to(pos2)
            self.add(tile1, word1)
            self.add(tile2, word2)
            y = y - 1
        

        ellipse_1 = Ellipse(width=3, height=5, color=PINK).move_to([4.5, 0,0])
        samplespace_text = Text("S").move_to([3,2,0]).scale(0.8)
        self.add(ellipse_1, samplespace_text)

        ellipse_up = Ellipse(width=2.2, height=1, color=PINK).move_to([4.5, 1.5, 0])
        self.play(Create(ellipse_up))
        t_up = Text("H").move_to([3.6,1,0]).scale(0.5)
        self.play(Write(t_up))

        ellipse_down = Ellipse(width=2.2, height=1, color=PINK).move_to([4.5, -1.5, 0])
        self.play(Create(ellipse_down))
        t_down = Text("W").move_to([3.6,-1,0]).scale(0.5)
        self.play(Write(t_down))

        self.wait(2)

        text = Text(f'P(H) > P(W)')
        self.play(Write(text), run_time=2)

        self.clear()


        """
        Okay here's one. Instead of choosing a ball if we consider our sample space to be the 
        position in the box to which our hand goes. Now this all are equally likely because we are not allowed to be looking
        so every position in the box has equal opportunity to be touched by our hand. 
        If you noticed we did not label the last bottom right corner position because, there is no ball in that position, if at all our
        hand goes over there we are going to reposition to reach a ball. so that position is not going to be chosen.
        So the only positions that are going to be chosen by our hand are the ones labeled. You can consider the numbers as addresses of each
        of the balls.
        """
        box_of_circles2 = Group()
        box_of_integers2 = Group()
        box = Rectangle(width=3, height=4).move_to([0,0.5,0])
        self.play(Create(box))
        tileloctext = Text("Tile locations").next_to(box, DOWN, buff = 0.5).scale(0.7)
        self.play(Write(tileloctext))
        count = 1
        for c in coordinates:
           integer =  Integer(number=count).move_to(c).scale(0.75)
           circle = Circle().set_color(WHITE).scale(0.2).set_style(fill_opacity = 0,stroke_width=1).move_to(c)
           box_of_integers2.add(integer)
           box_of_circles2.add(circle)
           self.play(Create(circle), Create(integer), run_time = 0.5)
           count = count + 1 
        
        """
        Possible outcomes
        """

        positions_list = [1,2,3,4,5,6,7,8,9,10,11]
        Possible_outcomes2 = permutations(positions_list, 2) 
        

        y = 3.5
        x = 4
        count = 0
        for outcome in Possible_outcomes2:
            if count == 14:
                break  
            position1 = [x, y, 0]
            position2 = [x+1, y , 0]

            integer1 =  Integer(number=outcome[0]).move_to(position1).scale(0.75)
            circle1 = Circle().set_color(WHITE).scale(0.2).set_style(fill_opacity = 0,stroke_width=1).move_to(position1)
            
            integer2 =  Integer(number=outcome[1]).move_to(position2).scale(0.75)
            circle2 = Circle().set_color(WHITE).scale(0.2).set_style(fill_opacity = 0,stroke_width=1).move_to(position2)
            

            if count < 4: 
               self.play(Create(circle1), Create(integer1), Create(circle2), Create(integer2), run_time = 0.5)
               self.play(Indicate(box_of_integers2[outcome[0]-1]), Indicate( box_of_integers2[outcome[1]-1]), Indicate(box_of_circles2[outcome[0]-1]), Indicate( box_of_circles2[outcome[1]-1]))

            else :
               self.play(Create(circle1), Create(integer1), Create(circle2), Create(integer2), run_time = 0.1)
               self.play(Indicate(box_of_integers2[outcome[0]-1]), Indicate( box_of_integers2[outcome[1]-1]), Indicate(box_of_circles2[outcome[0]-1]), Indicate( box_of_circles2[outcome[1]-1]), run_time=0.1)

            y = y - 0.5
            count = count +1

        self.play(Write(Text("...").move_to([x,y,0])))


        for a in box_of_circles2:
             self.remove(a)

        for a in box_of_integers2:
             self.remove(a)
        self.remove(box, tileloctext)


        p1 = [3,3.5,0]
        p2 = [3,-3.5,0]
        brace = BraceBetweenPoints(p1,p2) 
        self.play(Create(brace))
        self.play(Write(Text("?").next_to(brace, LEFT)))

        self.wait(5)


        
        """
        Better way to calculate total possible outcomes
        """
        pick1 = Line([-3,0,0], [-2,0,0])
        pick1_text = MarkupText(f"1<sup>st</sup> pick").next_to(pick1, DOWN).scale(0.5)
        choices1 = Integer(11).next_to(pick1, UP)
        pick2 = Line([-1.5, 0, 0] , [-0.5, 0,0])
        pick2_text = MarkupText(f"2<sup>nd</sup> pick").next_to(pick2, DOWN).scale(0.5)
        choices2 = Integer(10).next_to(pick2, UP)
        self.play(Create(pick1), Create(pick2))
        self.play(Write(pick1_text), Write(pick2_text))
        times1 = MathTex(r"\times").move_to([-1.75, 0.4,0])
        self.play(Create(choices1), run_time=1)
        self.wait(1)
        self.play(Create(choices2), run_time=1)
        self.wait(1)
        self.play(Write(times1))
        
        self.remove(pick1)
        self.remove(pick1_text)
        self.remove(choices1)
        self.remove(pick2)
        self.remove(pick2_text)
        self.remove(choices2)
        self.remove(times1)
        

        """
        Similarly better way to calculate favourable outcomes
        """

        pick1 = Line([-3,0,0], [-2,0,0]).set_color(RED)
        pick1_text = MarkupText(f"1<sup>st</sup> pick").next_to(pick1, DOWN).scale(0.5)
        choices1 = Integer(6).next_to(pick1, UP)
        pick2 = Line([-1.5, 0, 0] , [-0.5, 0,0]).set_color(BLUE)
        pick2_text = MarkupText(f"2<sup>nd</sup> pick").next_to(pick2, DOWN).scale(0.5)
        choices2 = Integer(5).next_to(pick2, UP)
        self.play(Create(pick1), Create(pick2))
        self.play(Write(pick1_text), Write(pick2_text))
        self.play(Create(choices1), run_time=1)
        self.wait(1)
        self.play(Create(choices2), run_time=1)
        self.wait(1)
        self.play(Write(MathTex(r"\times").move_to([-1.75, 0.4 ,0])))
        
        self.clear()

        """
        Final answer
        """
        answer1 = MathTex(r"P(E) &= \frac{6 \times 5 }{11 \times 10 } \\ &= \frac{30}{110} \\ &= \frac{3}{11}")

        self.play(Write(answer1), run_time=3)


        self.clear()


        titlescale = 0.5
        ob = -5
        coordinates1  = [[ob-1, 2, 0],  [ob+0, 2, 0], [ob+1, 2, 0], [ob-1, 1, 0], [ob+0, 1, 0], [ob+1, 1, 0], [ob-1, 0, 0], [ob+0, 0, 0] , [ob+1, 0 , 0], [ob-1, -1, 0], [ob+0, -1, 0]]
        colors  = [RED, RED, RED, RED, RED, RED, BLUE, BLUE, BLUE, BLUE, BLUE]
        word = ["Hello", "Hello", "Hello", "Hello", "Hello", "Hello", "World", "World", "World", "World", "World"]
        indices = [0,1,2,3,4,5,6,7,8,9,10]
        Possible_outcomes = [[0,0], [0,1], [1,0], [1,1]]
        box_of_wt = VGroup()
        box_of_words = VGroup()
        box_of_tiles = VGroup()
    
        box = Rectangle(width=3, height=4).move_to([ob+0,0.5,0])
        self.play(Create(box))

        words = [Text(wor, color=col).scale(0.3).move_to(cor) for cor, col, wor in zip(coordinates1, colors, word)]
        tiles = [Rectangle().set_fill(GRAY, opacity=0.2).scale(0.2).move_to(cor).set_stroke(width=1) for cor, col in zip(coordinates1, colors)]
       
        for w,r in zip(words,tiles): 
            k = VGroup()
            k.add(r,w)
            box_of_wt.add(k)
            box_of_words.add(w)
            box_of_tiles.add(r)
        

        self.play(*[Create(b) for b in box_of_tiles], *[Write(b) for b in box_of_words])


        m1 = MarkupText(f'6 <b>identical</b> <span fgcolor="{RED}">Hello</span> tiles').next_to(box, DOWN).scale(titlescale)
        m2 = MarkupText(f'5 <b>identical</b> <span fgcolor="{BLUE}">World</span> tiles').next_to(m1, DOWN).scale(titlescale)

        self.play(Write(m1))
        self.play(Write(m2))

     
        self.wait(3)

        # """
        # Need to play an arrow over here
        # """

        plus1 = Text("+", color=GOLD).move_to([-2.5,0.5,0]).scale(1.7)
        self.play(Write(plus1))
        


        ob = 0
        coordinates2  = [[ob-1, 2, 0],  [ob+0, 2, 0], [ob+1, 2, 0], [ob-1, 1, 0], [ob+0, 1, 0], [ob+1, 1, 0], [ob-1, 0, 0], [ob+0, 0, 0] , [ob+1, 0 , 0], [ob-1, -1, 0], [ob+0, -1, 0]]

        box_of_circles2 = Group()
        box_of_integers2 = Group()
        box = Rectangle(width=3, height=4).move_to([ob+0,0.5,0])
        self.play(Create(box))
        count = 1
        for c in coordinates2:
           integer =  Integer(number=count).move_to(c).scale(0.75)
           circle = Circle().set_color(WHITE).scale(0.2).set_style(fill_opacity = 0,stroke_width=1).move_to(c)
           box_of_integers2.add(integer)
           box_of_circles2.add(circle)
           count = count + 1 
        
        self.play(*[Create(b) for b in box_of_circles2], *[Write(b) for b in box_of_integers2])
        
    
        m1 = MarkupText(f'Tile locations').next_to(box, DOWN).scale(titlescale)

        self.play(Write(m1))

        """
        Need to play an arrow over here
        """

        arrow_1 = Arrow(start=[1.5,0.5,0], end=[3.5,0.5,0], color=GOLD)
        self.play(Create(arrow_1) , run_time = 2)
        


     

       
        ob = 5
        coordinates1  = [[ob-1, 2, 0],  [ob+0, 2, 0], [ob+1, 2, 0], [ob-1, 1, 0], [ob+0, 1, 0], [ob+1, 1, 0], [ob-1, 0, 0], [ob+0, 0, 0] , [ob+1, 0 , 0], [ob-1, -1, 0], [ob+0, -1, 0]]
        colors  = [RED, RED, RED, RED, RED, RED, BLUE, BLUE, BLUE, BLUE, BLUE]
        word = ["Hello", "Hello", "Hello", "Hello", "Hello", "Hello", "World", "World", "World", "World", "World"]
        indices = [0,1,2,3,4,5,6,7,8,9,10]
        Possible_outcomes = [[0,0], [0,1], [1,0], [1,1]]
        box_of_wt = VGroup()
        box_of_words = VGroup()
        box_of_tiles = VGroup()
    
        box = Rectangle(width=3, height=4).move_to([ob+0,0.5,0])
        self.play(Create(box))

        words = [Text(wor, color=col).scale(0.3).move_to(cor) for cor, col, wor in zip(coordinates1, colors, word)]
        tiles = [Rectangle().set_fill(GRAY, opacity=0.2).scale(0.2).move_to(cor).set_stroke(width=1) for cor, col in zip(coordinates1, colors)]
       
        for w,r in zip(words,tiles): 
            k = VGroup()
            k.add(r,w)
            box_of_wt.add(k)
            box_of_words.add(w)
            box_of_tiles.add(r)
        

        self.play(*[Create(b) for b in box_of_tiles], *[Create(b) for b in box_of_words])

        icoord = []
     
        
        leftshift = 0.3
        upshift = 0.1

        for c in coordinates1:
            icoord.append([c[0] - leftshift, c[1]+ upshift, 0])
            

        box_of_circles2 = Group()
        box_of_integers2 = Group()
        count = 1
        for c in icoord:
           integer =  Integer(number=count).move_to(c).scale(0.3)
           circle = Circle().set_color(WHITE).scale(0.1).set_style(fill_opacity = 0,stroke_width=1).move_to(c)
           box_of_integers2.add(integer)
           box_of_circles2.add(circle)
           count = count + 1

        self.play(*[Create(b) for b in box_of_circles2], *[Write(b) for b in box_of_integers2])
            
    
        m1 = MarkupText(f'6 <b>distinct</b> <span fgcolor="{RED}">Hello</span> tiles').next_to(box, DOWN).scale(titlescale)
        m2 = MarkupText(f'5 <b>distinct</b> <span fgcolor="{BLUE}">World</span> tiles').next_to(m1, DOWN).scale(titlescale)

        self.play(Write(m1))
        self.play(Write(m2))

    
        

        
        square1 = Rectangle(width=1, height=1).move_to([-5.68,-2.3, 0]).set_stroke(width=0)
        square2 = Rectangle(width=1, height=1).move_to([4.38, -2.3, 0]).set_stroke(width=0)

       
        
        # square1 = Rectangle(width=1.23, height=1).move_to([-5.68,-2.3, 0]).set_stroke(width=0)
        # square2 = Rectangle(width=1.1, height=1).move_to([4.38, -2.3, 0]).set_stroke(width=0)


        # square1 = Dot().move_to([-5.7,-2.3, 0])
        # square2 = Dot().move_to([4.4, -2.3, 0])


        self.add(square1)
        self.add(square2)

        self.play(Circumscribe(square1, Circle), time_width = 2)
        self.wait(1)
        self.play(Circumscribe(square2, Circle), time_width = 2)
        # self.play(Circumscribe(square1, Circle))
        # self.play(Circumscribe(square1, fade_out=True))
        # self.play(Circumscribe(square1, time_width=2))
        # self.play(Circumscribe(square1, Circle, True))

        self.wait(2)


        self.clear()


        m1 = MarkupText(f'Identical Objects Rule').scale(1).shift(UP)
        m2 = MarkupText(f'In probability problems, there are no collections of identical objects;').next_to(m1, DOWN).scale(0.7)
        m3 = MarkupText(f'all objects are <span fgcolor="{YELLOW}">distinguishable</span>').next_to(m2, DOWN).scale(0.7)
        # paragraph = Paragraph(MarkupText(f'6 <b>identical</b> Hello tiles'), '5 identical World tiles')

        self.play(Write(m1))
        self.play(Write(m2))
        self.play(Write(m3))

        self.wait(2)
from manim import *

class Shapes(Scene):
    def construct(self):
        # circle = Circle()
        # square = Square()
        # triangle = Triangle()

        # self.play(ApplyMethod(circle.shift, LEFT))
        # self.play(ApplyMethod(circle.shift, RIGHT))
        # self.play(ApplyMethod(circle.shift, RIGHT))
        # self.play(ApplyMethod(circle.shift, LEFT))
        
        # ar = Arrow(start=[0,0,0], end=[2, 3, 0], color=YELLOW)
        # ar2 = Arrow(start=[0,0,0], end= [3,3,0], color= YELLOW)
        # self.add(ar)
        # # self.add(ar2)
        # self.play(Transform(ar,ar2))
        # self.remove(ar)
        # self.add(ar2)
        # self.wait(1)


        # d1,d2=Dot(color=BLUE, ),Dot(color=GREEN)
        # dg=VGroup(d1,d2).arrange(RIGHT,buff=1)
        l1=Line([0,0,0], [0,2,0]).set_color(RED)
        # x=ValueTracker(0)
        # y=ValueTracker(0)
        # d2.add_updater(lambda z: z.set_x(x.get_value()))
        # d1.add_updater(lambda z: z.set_x(x.get_value()))
        # d2.add_updater(lambda z: z.set_y(y.get_value()))
        # l1.add_updater(lambda z: z.become(Line([0,0,0],[1 + x.get_value(), 2, 0])))
        self.add(l1)
        self.play(Rotate(l1, angle= 90, about_point=ORIGIN))
        # self.play(ApplyMethod(l1.rotate_about_origin, -45))
        
        # self.play(x.animate.set_value(5))
        # self.play(y.animate.set_value(4))
        self.wait()
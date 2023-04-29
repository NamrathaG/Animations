from manim import *

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        self.play(ApplyMethod(circle.shift, LEFT) )
        self.play(ApplyMethod(circle.shift, RIGHT) )
        self.play(ApplyMethod(circle.shift, RIGHT) )
        self.play(ApplyMethod(circle.shift, LEFT) )
        self.wait(1)
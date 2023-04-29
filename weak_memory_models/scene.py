from manim import *


class SquareToCircle(Scene):
    def construct(self):
        square1 = Square(color=BLUE, fill_opacity=1)
        square2 = Square(color=BLUE, fill_opacity=1)
        # circle = Circle()  # create a circle
        # circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        # square = Square()  # create a square
        # square.rotate(PI / 4)  # rotate a certain amount

        self.add(square1)
        self.add(square2)
        # self.play(Create(square))  # animate the creation of the square
        # self.play(Transform(square, circle))  # interpolate the square into the circle
        # self.play(FadeOut(square))  # fade out animation
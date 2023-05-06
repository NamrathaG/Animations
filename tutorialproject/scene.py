from manim import *


class SquareToCircle(Scene):
    def construct(self):
        # Scene.interactive_embed(self)
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        # self.embed()
        # Scene.wait_until(self, Scene.on_key_press)
        # self.play(Transform(square, circle))  # interpolate the square into the circle
        # self.play(FadeOut(square))  # fade out animation
from manim import *
from pprint import pprint

class ValueTrackerExample(Scene):
            def construct(self):
                number_line = NumberLine(include_numbers=True)
                pointer = Vector(DOWN)
                label = MathTex("x").add_updater(lambda m: m.next_to(pointer, UP))

                tracker = ValueTracker(0)
                pointer.add_updater(
                    lambda m: m.next_to(
                                number_line.n2p(tracker.get_value()),
                                UP
                            )
                )
                self.add(number_line, pointer,label)
                # tracker += 1.5
                # self.wait(5)
                # tracker -= 4
                # self.wait(0.5)
                self.play(tracker.animate.set_value(5)),
                self.wait(0.5)
                self.play(tracker.animate.set_value(3))
                self.play(tracker.animate.increment_value(-2))
                self.wait(0.5)
from manim import *

class MoveAlongPathExample(Scene):
    def construct(self):
        # d1 = Dot().set_color(ORANGE)
        s1 = Sq
        t1 = Text("hello")
        l1 = Line([0,3,0], [3,0,0])
        elbow_2 = Elbow(width=2.0)
        l2 = VMobject()
        self.add(t1, l1)
        # l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))
        self.play(MoveAlongPath(t1, l1), rate_func=linear)
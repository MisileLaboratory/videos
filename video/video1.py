from manim import *
from intro import intro
from library import create_textbox

class MisileLab(Scene):
    def construct(self):
        intro(self)
        # self.wait(12)

        groups = [create_textbox("Binary", GRAY), create_textbox("Programming language", GRAY), create_textbox("Assembly", GRAY)]

        groups[0].move_to([-4.5, 0, 0])
        self.play(Create(groups[0]))

        groups[1].move_to([-1, 0, 0])
        self.play(Create(groups[1]))

        groups[2].move_to([2.5, 0, 0])
        self.play(Create(groups[2]))

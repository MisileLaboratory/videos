from manim import *

class MisileLab(Scene):
    def construct(self):
        default_time = 1.0

        self.play(Write(Text("Misile"), lag_ratio=2))
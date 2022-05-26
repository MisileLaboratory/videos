from manim import *

def intro(scene: Scene):
    text = MarkupText(f'println!<span fgcolor="{PURPLE}">(</span><span fgcolor="{BLUE}">"Misile"</span><span fgcolor="{PURPLE}">)</span><span fgcolor="{WHITE}">;</span>', color=RED)
    scene.play(Write(text, lag_ratio=2))
    scene.wait(1)
    scene.play(FadeOut(text))

class Intro(Scene):
    def construct(self):
        intro(self)
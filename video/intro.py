from manim import *

def intro(scene: Scene):
    text = Text("Misile")
    scene.play(Write(text, lag_ratio=2))
    scene.wait(1)
    scene.play(FadeOut(text))
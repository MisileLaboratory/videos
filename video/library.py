from manim import *

def create_textbox(string: str, color):
    result = VGroup()
    text = Text(string).scale(0.5)
    box = Rectangle(height=text.height + 0.5, width=text.width + 0.5, fill_color=color, fill_opacity=0.5, stroke_color=color)
    text.move_to(box.get_center())
    result.add(box, text)
    return result
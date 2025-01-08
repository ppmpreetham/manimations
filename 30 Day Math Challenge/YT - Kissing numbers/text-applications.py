from manim import *

class TextAppScene(Scene):
    def construct(self):
        text1 = Text("Coding Theory", font_size=32)
        text2 = Text("Data Compression", font_size=32)

        self.play(Write(text1))
        self.wait(1)
        
        self.play(Transform(text1, text2))
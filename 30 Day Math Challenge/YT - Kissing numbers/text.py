from manim import *

class TextScene(Scene):
    def construct(self):
        kissing1 = Text("Kissing(1) = 2", font_size=32)
        kissing2 = Text("Kissing(2) = 6", font_size=32)
        kissing3 = Text("Kissing(3) = 12", font_size=32)
        kissing4 = Text("Kissing(4) = 24", font_size=32)
        kissing5 = Text("Kissing(8) = 240", font_size=32)
        kissing6 = Text("Kissing(24) = 196,560", font_size=32)
        
        # Animation sequence
        self.play(FadeIn(kissing1))
        self.wait(1)
        
        self.play(Transform(kissing1, kissing2))
        self.wait(1)
        
        self.play(Transform(kissing1, kissing3))
        self.wait(1)
        
        self.play(Transform(kissing1, kissing4))
        self.wait(1)
        
        self.play(Transform(kissing1, kissing5))
        self.wait(1)
        
        self.play(Transform(kissing1, kissing6))
        self.wait(2)
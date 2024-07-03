from manim import *

class AdditionScene(Scene):
    def construct(self):
        one = Text("1")
        plus = Text("+").next_to(one, RIGHT)
        two = Text("2").next_to(plus, RIGHT)
        equals = Text("=").next_to(two, RIGHT)
        three = Text("3").next_to(equals, RIGHT)
        
        self.play(Write(one))
        self.wait(1)
        
        self.play(Write(plus))
        self.wait(1)
        
        self.play(Write(two))
        self.wait(1)
        
        self.play(Write(equals))
        self.wait(1)
        
        self.play(Write(three))
        self.wait(1)

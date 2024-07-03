from manim import *

class VectorAdditionScene(Scene):
    def construct(self):
        vec1 = Matrix([[1], [2], [3]], left_bracket="(", right_bracket=")")
        plus = Text("+").next_to(vec1, RIGHT)
        vec2 = Matrix([[0], [1], [0]], left_bracket="(", right_bracket=")").next_to(plus, RIGHT)
        equals = Text("=").next_to(vec2, RIGHT)
        vec3 = Matrix([[1], [3], [3]], left_bracket="(", right_bracket=")").next_to(equals, RIGHT)
        
        vec1.move_to(LEFT * 3)
        plus.next_to(vec1, RIGHT)
        vec2.next_to(plus, RIGHT)
        equals.next_to(vec2, RIGHT)
        vec3.next_to(equals, RIGHT)
        
        self.play(Write(vec1))
        self.wait(1)
        
        self.play(Write(plus))
        self.wait(1)
        
        self.play(Write(vec2))
        self.wait(1)
        
        self.play(Write(equals))
        self.wait(1)
        
        self.play(Write(vec3))
        self.wait(1)

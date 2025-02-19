from manim import *

class xavierProofText(Scene):
    def construct(self):
        text1 = MathTex("f(x) = \\frac{1}{b-a}")
        self.play(Write(text1))
        self.wait(2)
        
        text2 = MathTex("f(x) = \\frac{1}{a-(-a)}")
        self.play(FadeOut(text1), FadeIn(text2))
        self.wait(2)
        
        text3 = MathTex("f(x) = \\frac{1}{2a}")
        self.play(FadeOut(text2), FadeIn(text3))
        self.wait(2)
        
        text4 = MathTex("\\mu = \\frac{-a+a}{2}")
        self.play(FadeOut(text3), FadeIn(text4))
        self.wait(2)
        
        text5 = MathTex("\\mu = 0")
        self.play(FadeOut(text4), FadeIn(text5))
        self.wait(2)
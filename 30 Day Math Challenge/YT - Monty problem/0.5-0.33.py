from manim import *

class FractionArrow(Scene):
    def construct(self):

        text_1_2 = Text("1/3", font_size=72)
        text_1_3 = Text("2/3", font_size=72)
        
        text_1_2.to_edge(LEFT)
        text_1_3.to_edge(RIGHT)
        
        arrow = Arrow(start=text_1_2.get_right(), end=text_1_3.get_left())

        self.play(FadeIn(text_1_2))
        self.wait(2)
        self.play(Create(arrow))
        self.play(FadeIn(text_1_3))

        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.media_width = "100%"
    config.verbosity = "WARNING"
    scene = FractionArrow()
    scene.render()
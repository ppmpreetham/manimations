from manim import *

class FlipSymbol(Scene):
    def construct(self):
        left_arrow = Arrow(start=RIGHT, end=LEFT)
        right_arrow = Arrow(start=LEFT, end=RIGHT)
    
        left_arrow.shift(UP)
        right_arrow.shift(DOWN)
        
        self.play(Create(left_arrow), Create(right_arrow))
        
        self.play(
            left_arrow.animate.shift(DOWN * 2),
            right_arrow.animate.shift(UP * 2)
        )
        
        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.media_width = "100%"
    config.verbosity = "WARNING"
    scene = FlipSymbol()
    scene.render()
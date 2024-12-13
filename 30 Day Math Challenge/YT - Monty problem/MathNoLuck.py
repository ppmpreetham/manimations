from manim import *

class MathNotLuck(Scene):
    def construct(self):
        
        text = Text("it's math, not luck", font_size=72)
        self.play(FadeIn(text))
        
        self.play(
            text.animate.set_color(BLUE),
            run_time=2
        )
        
        self.play(
            text.animate.shift(UP * 2),
            run_time=2
        )
        
        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.media_width = "100%"
    config.verbosity = "WARNING"
    scene = MathNotLuck()
    scene.render()
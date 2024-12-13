from manim import *

class FiftyFifty(Scene):
    def construct(self):
        fifty_fifty_text = Text("50-50", font_size=144)
        self.play(FadeIn(fifty_fifty_text))
        self.play(
            fifty_fifty_text.animate.scale(1.5).rotate(PI / 4),
            run_time=2
        )
        self.play(
            fifty_fifty_text.animate.set_color(YELLOW),
            run_time=2
        )
        self.play(
            fifty_fifty_text.animate.shift(UP * 2),
            run_time=2
        )
        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.media_width = "100%"
    config.verbosity = "WARNING"
    scene = FiftyFifty()
    scene.render()
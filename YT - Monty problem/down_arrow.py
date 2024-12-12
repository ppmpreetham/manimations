from manim import *

class DownArrow(Scene):
    def construct(self):
        down_arrow = Arrow(start=UP, end=DOWN)
        self.play(Create(down_arrow))
        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.media_width = "100%"
    config.verbosity = "WARNING"
    scene = DownArrow()
    scene.render()
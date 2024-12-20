from manim import *

class KissingNumbers1D(Scene):
    def construct(self):
        central_sphere = Circle(radius=0.5, color=BLUE).set_fill(BLUE, opacity=0.5)
        left_sphere = Circle(radius=0.5, color=GREEN).set_fill(GREEN, opacity=0.5).shift(LEFT)
        right_sphere = Circle(radius=0.5, color=GREEN).set_fill(GREEN, opacity=0.5).shift(RIGHT)

        left_contact = Dot(LEFT * 0.5, color=RED)
        right_contact = Dot(RIGHT * 0.5, color=RED)

        # Labels
        central_label = Text("Central", font_size=24).next_to(central_sphere, UP)
        left_label = Text("1", font_size=24).next_to(left_sphere, UP)
        right_label = Text("2", font_size=24).next_to(right_sphere, UP)

        # Animation sequence
        self.play(Create(central_sphere))
        self.play(Write(central_label))
        self.play(
            Create(left_sphere),
            Create(right_sphere)
        )
        self.play(
            Write(left_label),
            Write(right_label)
        )
        self.play(
            Create(left_contact),
            Create(right_contact)
        )
        
        # Flashing part ahahaha
        self.play(
            Flash(left_contact),
            Flash(right_contact)
        )
        self.wait(2)
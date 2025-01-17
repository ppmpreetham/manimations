from manim import *
import numpy as np

class CoffeeCupToDonut(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Coffee Cup
        coffee_cup = Surface(
            lambda u, v: np.array([
                (1 + 0.5 * v) * np.cos(u),
                (1 + 0.5 * v) * np.sin(u),
                v
            ]),
            u_range=[0, TAU], v_range=[-1, 1],
            resolution=(60, 60),
            color=RED_B
        )

        # Donut
        donut = Surface(
            lambda u, v: np.array([
                (2 + np.cos(v)) * np.cos(u),
                (2 + np.cos(v)) * np.sin(u),
                np.sin(v)
            ]),
            u_range=[0, TAU], v_range=[0, TAU],
            resolution=(30, 30),
            color=BLUE_B
        )

        self.add(coffee_cup)
        self.play(Create(coffee_cup))
        self.wait(1)

        # Morph
        self.play(Transform(coffee_cup, donut), run_time=3)
        self.wait(1)

        self.play(FadeOut(coffee_cup))

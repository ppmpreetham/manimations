from manim import *
import numpy as np

class torusRotation(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

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
        
        self.add(donut)
        self.play(Rotate(donut,angle=TAU, axis=UP, run_time=4))
        self.wait(1)
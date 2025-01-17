from manim import *
import numpy as np

class StretchSquish(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        cube = Cube()
        self.add(cube)
        self.play(cube.animate.scale([2, 1, 1]))
        self.wait(1)
        self.play(cube.animate.scale([0.25, 1, 1]))
        self.wait(1)
        self.play(Rotate(cube, angle=PI/4, axis=RIGHT))
        self.play(Rotate(cube, angle=PI/4, axis=UP))
        self.wait(1)
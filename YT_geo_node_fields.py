from manim import *

class RotatedSquareWithLabels(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes)
        
        square = Square(side_length=2, fill_color=BLUE, fill_opacity=0.5)
        square.rotate(PI / 4, axis=RIGHT)
        square.rotate(PI / 4, axis=UP)
        square.rotate(PI / 4, axis=OUT)
        self.add(square)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(12)

if __name__ == "__main__":
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 60
    config.quality = "high"

    scene = RotatedSquareWithLabels()
    scene.render()

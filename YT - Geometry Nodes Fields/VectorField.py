from manim import *

class VectorField3D(ThreeDScene):
    def construct(self):
        def vector_field_func(point):
            x, y, z = point[:3]
            return np.exp(np.array([x, y, z]))

        axes = ThreeDAxes()

        for x in range(-5, 6):
            for y in range(-5, 6):
                for z in range(-5, 6):
                    point = np.array([x, y, z])
                    field_value = vector_field_func(point)
                    field_value_text = Text(f"{field_value}", font_size=24).scale(0.2)
                    field_value_text.move_to(point)
                    self.add(field_value_text)

        self.add(axes)

        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(10)
        self.stop_ambient_camera_rotation()

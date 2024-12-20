from manim import *
import numpy as np

class KissingNumbers3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # axes
        axes = ThreeDAxes(x_range=[-3,3], y_range=[-3,3], z_range=[-3,3])
        self.add(axes)
        
        central_sphere = Sphere(radius=1, color=BLUE).set_fill(BLUE, opacity=0.5)
        
        # icosahedral arrangement
        phi = (1 + np.sqrt(5)) / 2
        positions = [
            [0, 1, phi], [0, -1, phi], [0, 1, -phi], [0, -1, -phi],
            [1, phi, 0], [-1, phi, 0], [1, -phi, 0], [-1, -phi, 0],
            [phi, 0, 1], [-phi, 0, 1], [phi, 0, -1], [-phi, 0, -1]
        ]
        
        scaled_positions = [np.array(pos) * 2 / np.sqrt(1 + phi*phi) for pos in positions]
        
        # kissing spheres
        kissing_spheres = VGroup()
        contact_points = VGroup()
        
        for pos in scaled_positions:
            sphere = Sphere(radius=1, color=GREEN).set_fill(GREEN, opacity=0.5)
            sphere.move_to(pos)
            kissing_spheres.add(sphere)
            
            # contact point
            contact = Dot3D(pos/2, color=RED, radius=0.05)
            contact_points.add(contact)
        
        self.play(Create(central_sphere))
        self.play(AnimationGroup(*[Create(sphere) for sphere in kissing_spheres],
                                lag_ratio=0.1))
        self.play(Create(contact_points))
        
        # Flashes
        self.play(AnimationGroup(*[Flash(point) for point in contact_points],
                                lag_ratio=0.1))
        
        # camera
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)

if __name__ == "__main__":
    with tempconfig({"quality": "high_quality", "preview": True}):
        scene = KissingNumbers3D()
        scene.render()
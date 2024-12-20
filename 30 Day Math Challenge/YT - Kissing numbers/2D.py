from manim import *
import numpy as np

class KissingNumbers2D(Scene):
    def construct(self):
        # axes
        x_line = Line(LEFT * 3, RIGHT * 3, color=GRAY)
        y_line = Line(UP * 3, DOWN * 3, color=GRAY)
        
        # Central circle
        central_circle = Circle(radius=1, color=BLUE).set_fill(BLUE, opacity=0.5)
        
        # Kissing circles setup
        angles = np.linspace(0, 2*PI, 6, endpoint=False)
        positions = [
            np.array([2*np.cos(angle), 2*np.sin(angle), 0])
            for angle in angles
        ]
        
        kissing_circles = VGroup()
        for pos in positions:
            circle = Circle(radius=1, color=GREEN).set_fill(GREEN, opacity=0.5)
            circle.move_to(pos)
            kissing_circles.add(circle)
        
        # Labels setup
        labels = VGroup()
        for i, pos in enumerate(positions):
            label = Text(str(i + 1), font_size=24).move_to(pos)
            labels.add(label)
        
        # Contact points setup
        contact_points = VGroup()
        for pos in positions:
            point = Dot(pos/2, color=RED, radius=0.05)
            contact_points.add(point)
        
        # Animation sequence
        self.play(Create(x_line), Create(y_line))
        self.play(Create(central_circle))
        self.play(AnimationGroup(*[Create(circle) for circle in kissing_circles], 
                                lag_ratio=0.1))
        self.play(Write(labels))
        self.play(Create(contact_points))
        self.play(
            AnimationGroup(*[Flash(point) for point in contact_points],
                          lag_ratio=0.1)
        )      
        self.wait(2)
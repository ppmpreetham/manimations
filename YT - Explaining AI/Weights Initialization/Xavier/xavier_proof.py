from manim import *
import numpy as np

class VarianceUniformDistribution(Scene):
    def construct(self):
        a = 3
        
        title = Text("Variance of a Uniform Distribution")
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={
                "color": BLUE,
                "include_tip": True,
                "include_numbers": True
            }
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")
        new_graph = axes.plot(lambda x: 1/(2*a) if (-a <= x <= a) else 0, color=YELLOW, discontinuities=[-a,a])
        
        self.play(Create(axes), Write(labels))
        self.play(Create(new_graph))

        point_left = Dot(axes.c2p(-a, 0), color=RED)
        point_right = Dot(axes.c2p(a, 0), color=RED)
        point_top = Dot(axes.c2p(0, 1/(2*a)), color=RED)
        self.play(Create(point_left), Create(point_right))
        self.play(Flash(point_left), Flash(point_right), Write(Text("-a").next_to(axes.c2p(-a, 0), UP)), Write(Text("a").next_to(axes.c2p(a, 0), UP)))
        self.play(Create(point_top), Flash(point_top), Write(MathTex("\\frac{1}{2a}").next_to(axes.c2p(0, 0.5/a), UP+RIGHT)))
        area = axes.get_area(new_graph, x_range=[-a, a], color=BLUE, opacity=0.3)
        self.play(FadeIn(area))
        self.wait(2)

        # Scale everything down
        self.play(axes.animate.scale(0.5), labels.animate.scale(0.5), new_graph.animate.scale(0.5), point_left.animate.scale(0.5), point_right.animate.scale(0.5), point_top.animate.scale(0.5), area.animate.scale(0.5))
        self.wait(2)
from manim import *
import numpy as np
from scipy.stats import norm

class NormalDistribution(Scene):
    def construct(self):
        
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={
                "color": BLUE,
                "include_tip": True,
                "numbers_to_exclude": []
            },
            x_axis_config={
                "numbers_to_include": np.arange(-4, 5, 1),
                "numbers_with_elongated_ticks": np.arange(-4, 5, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 0.6, 0.1),
                "decimal_number_config": {"num_decimal_places": 1}
            },
        ).scale(1.0)  
        
        
        axes.center()
        
        
        x_label = axes.get_x_axis_label("x").scale(0.6)  
        y_label = axes.get_y_axis_label("f(x)").scale(0.6)  

        
        normal_graph = axes.plot(
            lambda x: norm.pdf(x, 0, 1),
            color=RED,
            x_range=[-4, 4],
        )

        
        graph_label = MathTex(
            "f(x) = \\frac{1}{\\sqrt{2\\pi}} e^{-\\frac{x^2}{2}}"
        ).scale(0.6)  
        graph_label.to_corner(UR).shift(LEFT * 0.5 + DOWN * 0.5)

        
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=2
        )
        self.play(Create(normal_graph), run_time=1.5)
        self.play(Write(graph_label), run_time=1.5)

        
        total_area = axes.get_area(
            normal_graph,
            x_range=[-4, 4],
            color=BLUE_C,
            opacity=0.3
        )
        self.play(FadeIn(total_area))

        
        area_label = MathTex("\\text{Total Area} = 1").scale(0.6)  
        area_label.next_to(graph_label, DOWN, buff=0.2)  
        self.play(Write(area_label))
        self.wait(1)

        
        probability_tracker = ValueTracker(-4)
        prob_area = always_redraw(
            lambda: axes.get_area(
                normal_graph,
                x_range=[-4, probability_tracker.get_value()],
                color=GREEN_C,
                opacity=0.5
            )
        )

        
        prob_label = always_redraw(
            lambda: MathTex(
                f"P(X \\leq {probability_tracker.get_value():.2f}) = {norm.cdf(probability_tracker.get_value()):.3f}"
            ).scale(0.6).to_corner(UL).shift(DOWN * 0.2)  
        )

        
        v_line = always_redraw(
            lambda: axes.get_vertical_line(
                axes.c2p(probability_tracker.get_value(), 0),
                line_config={"color": YELLOW}
            )
        )

        
        self.play(
            FadeIn(prob_area),
            FadeIn(v_line),
            FadeIn(prob_label)
        )

        
        self.play(
            probability_tracker.animate.set_value(2),
            run_time=4,
            rate_func=linear
        )
        self.wait(1)

        
        self.play(
            probability_tracker.animate.set_value(-1),
            run_time=2
        )
        self.wait(1)

        
        self.play(
            probability_tracker.animate.set_value(4),
            run_time=2
        )
        self.wait(2)
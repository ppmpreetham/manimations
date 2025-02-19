from manim import *
import numpy as np

class VarianceUniformDistributionExample(Scene):
    def construct(self):
        a = 3  # Initial value of 'a'
        
        title = Text("Variance of a Uniform Distribution")
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Initial Axes Setup
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[0, 0.5, 0.1],  # Default y-axis range
            axis_config={"color": BLUE, "include_tip": True, "include_numbers": True}
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        # Function to generate graph based on 'a'
        def get_graph(a_val):
            return axes.plot(lambda x: 1/(2*a_val) if (-a_val <= x <= a_val) else 0, 
                             color=YELLOW, 
                             discontinuities=[-a_val, a_val], 
                             use_smoothing=False)

        # Function to generate area under the curve
        def get_area(a_val):
            return axes.get_area(get_graph(a_val), x_range=[-a_val, a_val], color=BLUE, opacity=0.3)

        # Display dynamic text labels
        a_value_text = MathTex(f"a = {a}").to_corner(UR)
        left_coord_text = MathTex(f"(-{a}, 0)").next_to(axes.c2p(-a, 0), DOWN)
        right_coord_text = MathTex(f"({a}, 0)").next_to(axes.c2p(a, 0), DOWN)
        top_coord_text = MathTex(f"\\left(0, \\frac{{1}}{{2({a})}}\\right)").next_to(axes.c2p(0, 0.5/a), UP+RIGHT)

        self.play(Write(a_value_text), Write(left_coord_text), Write(right_coord_text), Write(top_coord_text))

        # Initial graph and area
        graph = get_graph(a)
        area = get_area(a)

        self.play(Create(graph), FadeIn(area))

        # Function to animate 'a' changing smoothly
        def update_a(new_a):
            nonlocal a
            a = new_a

            # Adjust Y-axis dynamically when a = 1
            new_y_range = [0, 1.2, 0.2] if a == 1 else [0, 0.5, 0.1]  
            new_axes = Axes(
                x_range=[-6, 6, 1],
                y_range=new_y_range,
                axis_config={"color": BLUE, "include_tip": True, "include_numbers": True}
            )
            new_labels = new_axes.get_axis_labels(x_label="x", y_label="y")
            new_graph = get_graph(a)
            new_area = get_area(a)

            # Update text labels
            new_a_value_text = MathTex(f"a = {a}").to_corner(UR)
            new_left_coord_text = MathTex(f"(-{a}, 0)").next_to(axes.c2p(-a, 0), DOWN)
            new_right_coord_text = MathTex(f"({a}, 0)").next_to(axes.c2p(a, 0), DOWN)
            new_top_coord_text = MathTex(f"\\left(0, \\frac{{1}}{{2({a})}}\\right)").next_to(axes.c2p(0, 0.5/a), UP+RIGHT)

            # Animate transformations
            self.play(
                Transform(axes, new_axes),
                Transform(labels, new_labels),
                Transform(graph, new_graph),
                Transform(area, new_area),
                Transform(a_value_text, new_a_value_text),
                Transform(left_coord_text, new_left_coord_text),
                Transform(right_coord_text, new_right_coord_text),
                Transform(top_coord_text, new_top_coord_text),
                run_time=3  # Increased duration to 3 seconds
            )

        # Change 'a' values: 3 → 5 → 1 (y-axis scales) → 3 (y-axis back)
        update_a(5)
        update_a(1)  # y-axis expands
        update_a(3)  # y-axis returns

        # Show distance between -a and a as 2a
        brace = BraceBetweenPoints(axes.c2p(-a, 0), axes.c2p(a, 0), DOWN)
        brace_text = MathTex("2a").next_to(brace, DOWN)
        self.play(Create(brace), Write(brace_text))
        self.wait(1)

        # Multiply 1/(2a) and 2a to get 1
        equation = MathTex("\\frac{1}{2a} \\times 2a = 1").to_edge(LEFT+UP)
        self.play(Write(equation))
        self.wait(2)

from manim import *
import numpy as np

class UniformDistributionEnhanced(Scene):
    def construct(self):
        
        self.camera.background_color = BLACK

        
        axes = Axes(
            x_range=[-1, 6],
            y_range=[0, 1.5],
            axis_config={
                "include_tip": True,
                "color": BLUE_B,
                "stroke_width": 2,
            }
        ).add_coordinates(color=BLUE_C)
        
        
        x_label = Text("x", font="Times New Roman").scale(0.8).next_to(axes.x_axis, RIGHT)
        y_label = Text("y", font="Times New Roman").scale(0.8).next_to(axes.y_axis, UP)
        
        
        title = Text("Uniform Distribution", font="Times New Roman")
        title.to_edge(UP)
        title.set_color(BLUE_A)
        
        
        self.play(
            Create(axes, run_time=1.5),
            Write(x_label),
            Write(y_label),
            Write(title)
        )
        self.wait(1)
        
        
        point_a = np.array([1, 0, 0])
        point_b = np.array([4, 0, 0])
        
        
        height = 1/(point_b[0] - point_a[0])
        rectangle = Rectangle(
            width=(point_b[0] - point_a[0])*axes.get_x_unit_size(),
            height=height*axes.get_y_unit_size(),
            fill_color=BLUE,
            fill_opacity=0,
            stroke_color=BLUE_A,
            stroke_width=2
        )
        rectangle.move_to(
            axes.coords_to_point(
                (point_b[0] + point_a[0])/2,
                height/2,
                0
            )
        )
        
        
        self.play(Create(rectangle, run_time=1.5))
        self.wait(1)

        
        self.play(
            axes.animate.set_opacity(0.3),
            run_time=0.5
        )
        
        
        dot_a = Dot(axes.coords_to_point(*point_a), color=YELLOW)
        dot_b = Dot(axes.coords_to_point(*point_b), color=YELLOW)
        
        
        glow_a = Dot(
            axes.coords_to_point(*point_a),
            color=YELLOW,
            radius=0.2
        ).set_opacity(0.3)
        glow_b = Dot(
            axes.coords_to_point(*point_b),
            color=YELLOW,
            radius=0.2
        ).set_opacity(0.3)
        
        label_a = MathTex("a").next_to(dot_a, DOWN).set_color(YELLOW)
        label_b = MathTex("b").next_to(dot_b, DOWN).set_color(YELLOW)
        
        
        flash_a = Flash(
            dot_a,
            color=YELLOW,
            flash_radius=0.3,
            num_lines=20,
            rate_func=smooth
        )
        flash_b = Flash(
            dot_b,
            color=YELLOW,
            flash_radius=0.3,
            num_lines=20,
            rate_func=smooth
        )
        
        
        self.play(
            FadeIn(glow_a, scale=3),
            FadeIn(glow_b, scale=3),
            run_time=0.5
        )
        self.play(
            Create(dot_a),
            Create(dot_b),
            Write(label_a),
            Write(label_b)
        )
        self.play(flash_a, flash_b)
        self.wait(1)
        
        
        prob_text = Text(
            "For uniform distribution,\nall values between a and b\nhave equal probability",
            font="Times New Roman",
            font_size=28,
            color=BLUE_A
        ).next_to(title, DOWN, buff=0.5)
        
        self.play(Write(prob_text))
        self.wait(1.5)
        
        
        self.play(
            rectangle.animate.set_fill(opacity=0.3),
            run_time=1.5
        )
        self.wait(1)
        
        
        area_eq = MathTex(
            r"\text{Area}", r"=", r"1", r"=", r"(b-a)", r"\times", r"h"
        ).set_color_by_tex_to_color_map({
            r"\text{Area}": BLUE_A,
            r"(b-a)": YELLOW,
            r"h": GREEN
        }).next_to(prob_text, DOWN)
        
        self.play(Write(area_eq))
        self.wait(1)
        
        
        height_eq = MathTex(
            r"h", r"=", r"f(x)", r"=", r"\frac{1}{b-a}"
        ).set_color_by_tex_to_color_map({
            r"h": GREEN,
            r"f(x)": GREEN,
            r"\frac{1}{b-a}": YELLOW
        }).next_to(area_eq, DOWN)
        
        self.play(Write(height_eq))
        self.wait(1.5)
        
        
        piecewise = MathTex(
            r"f(x) = \begin{cases} "
            r"\frac{1}{b-a} & \text{if } a \leq x \leq b \\" 
            r"0 & \text{otherwise}"
            r"\end{cases}"
        ).set_color(BLUE_A)
        
        
        piecewise.move_to(ORIGIN).shift(UP * 0.5)
        
        
        self.play(
            FadeOut(prob_text),
            FadeOut(area_eq),
            FadeOut(height_eq),
            run_time=1
        )
        
        self.play(Write(piecewise))
        self.wait(1)
        
        
        def uniform_dist(x):
            if point_a[0] <= x <= point_b[0]:
                return height
            return 0
        
        graph = axes.plot(
            uniform_dist,
            x_range=[axes.x_range[0], axes.x_range[1]],
            color=YELLOW,
            stroke_width=3
        )
        
        
        graph_glow = axes.plot(
            uniform_dist,
            x_range=[axes.x_range[0], axes.x_range[1]],
            color=YELLOW,
            stroke_width=10,
            stroke_opacity=0.3
        )
        
        
        self.play(
            axes.animate.set_opacity(1),
            FadeOut(piecewise),
            run_time=0.5
        )
        
        self.play(
            Create(graph_glow),
            Create(graph),
            run_time=2
        )
        
        self.wait(2)
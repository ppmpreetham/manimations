from manim import *
import numpy as np

class XavierInitialization(Scene):
    def construct(self):
        
        self.camera.background_color = BLACK
        
        
        init_methods_text = [
            Text(f"{method}", font="CMU Serif").scale(0.7)
            for method, _ in [
                ("Random Normal", None),
                ("Zeros", None),
                ("Ones", None),
                ("Xavier/Glorot", None),
                ("He", None),
                ("Uniform", None),
                ("LeCun", None),
            ]
        ]
        
        
        init_methods_group = VGroup(*init_methods_text).arrange(DOWN, buff=0.5)
        init_methods_group.to_edge(LEFT, buff=1)
        
        
        self.play(Write(init_methods_group), run_time=2)
        
        
        xavier_text = init_methods_text[3]
        
        
        highlight_rect = BackgroundRectangle(
            xavier_text,
            color=BLUE_E,
            fill_opacity=0.3,
            buff=0.2
        )
        
        
        self.play(
            FadeIn(highlight_rect),
            xavier_text.animate.set_color(WHITE),
            *[FadeOut(text) for i, text in enumerate(init_methods_text) if i != 3]
        )
        
        
        self.play(
            VGroup(highlight_rect, xavier_text).animate.move_to(UP * 2.5).scale(1.5)
        )
        
        
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE},
            tips=False
        ).scale(0.6)
        
        
        tanh_graph = axes.plot(
            lambda x: np.tanh(x),
            color=BLUE
        )
        
        
        tanh_label = Text("tanh(x)", font="CMU Serif", color=BLUE).scale(0.6)
        tanh_label.next_to(axes, RIGHT)
        
        
        graph_group = VGroup(axes, tanh_graph, tanh_label).move_to(DOWN * 0.5)
        
        
        self.play(
            Create(axes),
            Create(tanh_graph),
            Write(tanh_label)
        )

        
        self.wait(2)

        
        sigmoid_graph = axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            color=GREEN
        )
        
        
        sigmoid_label = Text("sigmoid(x)", font="CMU Serif", color=GREEN).scale(0.6)
        sigmoid_label.next_to(axes, RIGHT)
        
        
        self.play(
            Transform(tanh_graph, sigmoid_graph),
            Transform(tanh_label, sigmoid_label)
        )

        
        self.play(
            graph_group.animate.scale(0.5).to_edge(LEFT, buff=1)
        )

        
        formula = MathTex(
            r"\text{Var}(W) = \frac{2}{n_{in} + n_{out}}",
            color=BLUE
        )
        formula.to_edge(RIGHT, buff=1)
        
        self.play(Write(formula))
        
        
        self.wait(2)

        
        self.wait(1)

        
        self.play(
            FadeOut(graph_group),
            FadeOut(VGroup(highlight_rect, xavier_text))
        )

        
        self.play(
            formula.animate.scale(2).move_to(ORIGIN)
        )

        
        question = Text("Where does this come from?", font="CMU Serif", color=WHITE).scale(0.8)
        question.next_to(formula, DOWN, buff=0.5)
        self.play(Write(question))

        
        explanation = Text(
            "The 2 comes from the symmetry.\n"
            "It ensures that the variance of the activations remains stable across layers,\n"
            "which helps the network learn efficiently during training.\n"
            "We initialize the weights randomly and want the variance of the activations\n"
            "to be the same as the variance of the inputs.",
            font="CMU Serif",
            color=WHITE
        ).scale(0.5)
        explanation.next_to(question, DOWN, buff=0.5)
        self.play(Write(explanation))

        
        self.wait(2)
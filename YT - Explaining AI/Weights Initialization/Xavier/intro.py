from manim import *
import numpy as np

class Intro(Scene):
    def construct(self):
        
        a_text = Text("Dense(units = 25, activation = 'relu')")
        b_text = Text("Dense(units = 15, activation = 'relu')")
        c_text = Text("Dense(units = 10, activation = 'softmax')")
        
        
        self.play(Write(a_text))
        self.play(ReplacementTransform(a_text, b_text))
        self.play(ReplacementTransform(b_text, c_text))
        self.wait(1)
        
        
        units_part = Text("10", color=YELLOW).scale(1)
        units_part.next_to(c_text, RIGHT, buff=0.1)
        
        self.play(
            c_text.animate.set_opacity(0.3),
            FadeIn(units_part)
        )
        self.wait(1)

        
        init_methods = [
            ("Random Normal", np.random.normal(0, 0.1, 10)),
            ("Zeros", np.zeros(10)),
            ("Ones", np.ones(10)),
            ("Xavier/Glorot", np.random.normal(0, np.sqrt(2.0/25), 10)),
            ("He", np.random.normal(0, np.sqrt(2.0/25), 10)),
            ("Uniform", np.random.uniform(-0.1, 0.1, 10)),
            ("LeCun", np.random.normal(0, np.sqrt(1.0/25), 10))
        ]

        
        weight_group = VGroup()
        name_group = VGroup()
        for i, (name, weights) in enumerate(init_methods):
            weight_values = Text(
                f"[{', '.join([f'{w:.2f}' for w in weights[:10]])}]",
                font_size=24
            )
            method_text = Text(f"{name}: [{', '.join([f'{w:.2f}' for w in weights[:10]])}]", font_size=24, color=BLUE)
            row = VGroup(weight_values).arrange(RIGHT)
            row.shift(DOWN * (i * 0.6 + 1))
            name_row = VGroup(method_text).arrange(RIGHT)
            name_row.shift(DOWN * (i * 0.6 + 1))
            weight_group.add(row)
            name_group.add(name_row)

        weight_group.center()
        name_group.center()

        
        self.play(
            c_text.animate.to_edge(UP),
            units_part.animate.to_edge(UP)
        )
        
        for row in weight_group:
            self.play(Write(row))
            self.wait(0.5)
        
        self.wait(3)

        
        for weight_row, name_row in zip(weight_group, name_group):
            self.play(Transform(weight_row, name_row))
            self.wait(0.5)
        
        self.wait(2)
        
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])
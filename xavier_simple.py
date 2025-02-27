from manim import *
import numpy as np

class XavierInitialization(Scene):
    def construct(self):
        # Introduction
        self.show_title()
        
        # Problem statement
        self.show_problem()
        
        # Forward pass analysis
        self.show_forward_pass()
        
        # Backward pass analysis
        self.show_backward_pass()
        
        # Combined result
        self.show_final_result()
        
        # Visualize distributions
        self.show_distributions()
        
        # Conclusion
        self.show_conclusion()
    
    def show_title(self):
        title = Text("Xavier Initialization", font_size=60)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.5).to_corner(UL))
    
    def show_problem(self):
        # Simple diagram of a neural network
        nn_layers = 4
        neurons_per_layer = [4, 5, 5, 3]
        
        network = VGroup()
        neuron_groups = []
        
        # Create neurons
        for i, n_neurons in enumerate(neurons_per_layer):
            layer = VGroup()
            for j in range(n_neurons):
                neuron = Circle(radius=0.2, color=WHITE, fill_opacity=0)
                neuron.move_to([i*2, (n_neurons-1)*0.5 - j*1.0, 0])
                layer.add(neuron)
            network.add(layer)
            neuron_groups.append(layer)
        
        # Add connections between layers
        for i in range(nn_layers - 1):
            for neuron1 in neuron_groups[i]:
                for neuron2 in neuron_groups[i+1]:
                    line = Line(
                        neuron1.get_center(), 
                        neuron2.get_center(),
                        stroke_width=1,
                        stroke_opacity=0.5
                    )
                    network.add(line)
        
        # Center the network
        network.move_to(ORIGIN)
        
        # Problem statement
        problem = Text("Problem: How should we initialize weights?", font_size=36)
        problem.to_edge(UP)
        
        self.play(
            Write(problem),
            Create(network)
        )
        self.wait(1)
        
        # Illustrate the issues
        too_small = Text("Too small → Vanishing gradients", font_size=28, color=RED)
        too_large = Text("Too large → Exploding gradients", font_size=28, color=ORANGE)
        
        too_small.next_to(problem, DOWN)
        too_large.next_to(too_small, DOWN)
        
        self.play(Write(too_small))
        self.wait(0.5)
        self.play(Write(too_large))
        self.wait(1)
        
        self.network = network
        self.play(
            FadeOut(problem),
            FadeOut(too_small),
            FadeOut(too_large),
            network.animate.scale(0.7).to_edge(LEFT)
        )
    
    def show_forward_pass(self):
        title = Text("Forward Pass Analysis", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create a simple neuron model for forward pass
        in_neurons = 3
        in_layer = VGroup()
        for i in range(in_neurons):
            neuron = Circle(radius=0.2, color=WHITE, fill_opacity=0)
            neuron.move_to([-2, (in_neurons-1) - i*1.0, 0])
            in_layer.add(neuron)
        
        out_neuron = Circle(radius=0.2, color=WHITE, fill_opacity=0)
        out_neuron.move_to([2, 0, 0])
        
        connections = VGroup()
        for n in in_layer:
            line = Line(n.get_center(), out_neuron.get_center(), stroke_width=1)
            connections.add(line)
        
        # Labels
        input_labels = VGroup()
        for i, n in enumerate(in_layer):
            label = MathTex(f"x_{i+1}")
            label.next_to(n, LEFT)
            input_labels.add(label)
        
        output_label = MathTex("y")
        output_label.next_to(out_neuron, RIGHT)
        
        weight_labels = VGroup()
        for i, c in enumerate(connections):
            label = MathTex(f"W_{i+1}")
            midpoint = (c.get_start() + c.get_end()) / 2
            direction = normalize(c.get_end() - c.get_start())
            normal = np.array([-direction[1], direction[0], 0])
            label.move_to(midpoint + normal * 0.3)
            weight_labels.add(label)
        
        forward_model = VGroup(in_layer, out_neuron, connections, input_labels, output_label, weight_labels)
        forward_model.scale(0.8).shift(RIGHT*3 + UP*1)
        
        self.play(Create(forward_model))
        self.wait(1)
        
        # Equations
        eq1 = MathTex(r"y = \sum_{i=1}^{n_{in}} W_i x_i")
        eq2 = MathTex(r"\text{Var}(y) = \sum_{i=1}^{n_{in}} \text{Var}(W_i x_i)")
        eq3 = MathTex(r"\text{Var}(y) = n_{in} \cdot \text{Var}(W) \cdot \text{Var}(x)")
        eq4 = MathTex(r"\text{For stable variance: } \text{Var}(y) = \text{Var}(x)")
        eq5 = MathTex(r"\text{Therefore: } \text{Var}(W) = \frac{1}{n_{in}}")
        
        equations = VGroup(eq1, eq2, eq3, eq4, eq5).arrange(DOWN, aligned_edge=LEFT)
        equations.next_to(title, DOWN).shift(LEFT * 3)
        
        for eq in equations:
            self.play(Write(eq))
            self.wait(0.5)
        
        # Highlight the result
        box_forward = SurroundingRectangle(eq5, color=YELLOW)
        self.play(Create(box_forward))
        self.wait(1)
        
        self.forward_result = eq5
        
        self.play(
            FadeOut(title),
            FadeOut(forward_model),
            FadeOut(VGroup(*equations[:-1])),
            FadeOut(box_forward),
            eq5.animate.to_edge(UP)
        )
    
    def show_backward_pass(self):
        title = Text("Backward Pass Analysis", font_size=36)
        title.next_to(self.forward_result, DOWN)
        self.play(Write(title))
        
        # Create a simple neuron model for backward pass
        out_neurons = 3
        out_layer = VGroup()
        for i in range(out_neurons):
            neuron = Circle(radius=0.2, color=WHITE, fill_opacity=0)
            neuron.move_to([2, (out_neurons-1) - i*1.0, 0])
            out_layer.add(neuron)
        
        in_neuron = Circle(radius=0.2, color=WHITE, fill_opacity=0)
        in_neuron.move_to([-2, 0, 0])
        
        connections = VGroup()
        for n in out_layer:
            line = Line(in_neuron.get_center(), n.get_center(), stroke_width=1)
            connections.add(line)
        
        # Labels
        output_labels = VGroup()
        for i, n in enumerate(out_layer):
            label = MathTex(f"y_{i+1}")
            label.next_to(n, RIGHT)
            output_labels.add(label)
        
        input_label = MathTex("x")
        input_label.next_to(in_neuron, LEFT)
        
        weight_labels = VGroup()
        for i, c in enumerate(connections):
            label = MathTex(f"W_{i+1}")
            midpoint = (c.get_start() + c.get_end()) / 2
            direction = normalize(c.get_end() - c.get_start())
            normal = np.array([-direction[1], direction[0], 0])
            label.move_to(midpoint + normal * 0.3)
            weight_labels.add(label)
        
        backward_model = VGroup(in_neuron, out_layer, connections, output_labels, input_label, weight_labels)
        backward_model.scale(0.8).shift(RIGHT*3 + UP*1)
        
        self.play(Create(backward_model))
        self.wait(1)
        
        # Gradient labels
        gradient_labels = VGroup()
        for i, n in enumerate(out_layer):
            label = MathTex(r"\frac{\partial L}{\partial y_" + f"{i+1}" + "}")
            label.scale(0.7).next_to(n, RIGHT, buff=0.8)
            gradient_labels.add(label)
        
        gradient_arrows = VGroup()
        for i, (label, neuron) in enumerate(zip(gradient_labels, out_layer)):
            arrow = Arrow(label.get_left(), neuron.get_right(), buff=0.1, color=RED)
            gradient_arrows.add(arrow)
        
        self.play(
            Write(gradient_labels),
            Create(gradient_arrows)
        )
        self.wait(0.5)
        
        # Equations
        eq1 = MathTex(r"\frac{\partial L}{\partial x} = \sum_{i=1}^{n_{out}} W_i \frac{\partial L}{\partial y_i}")
        eq2 = MathTex(r"\text{Var}\left(\frac{\partial L}{\partial x}\right) = n_{out} \cdot \text{Var}(W) \cdot \text{Var}\left(\frac{\partial L}{\partial y}\right)")
        eq3 = MathTex(r"\text{For stable gradients: } \text{Var}\left(\frac{\partial L}{\partial x}\right) = \text{Var}\left(\frac{\partial L}{\partial y}\right)")
        eq4 = MathTex(r"\text{Therefore: } \text{Var}(W) = \frac{1}{n_{out}}")
        
        equations = VGroup(eq1, eq2, eq3, eq4).arrange(DOWN, aligned_edge=LEFT)
        equations.next_to(title, DOWN).shift(LEFT * 3)
        
        for eq in equations:
            self.play(Write(eq))
            self.wait(0.5)
        
        # Highlight the result
        box_backward = SurroundingRectangle(eq4, color=BLUE)
        self.play(Create(box_backward))
        self.wait(1)
        
        self.backward_result = eq4
        
        self.play(
            FadeOut(title),
            FadeOut(backward_model),
            FadeOut(gradient_labels),
            FadeOut(gradient_arrows),
            FadeOut(VGroup(*equations[:-1])),
            FadeOut(box_backward),
            eq4.animate.next_to(self.forward_result, DOWN)
        )
    
    def show_final_result(self):
        title = Text("Combining the Constraints", font_size=36)
        title.next_to(self.backward_result, DOWN)
        self.play(Write(title))
        
        # Combining equations
        eq1 = MathTex(r"\text{Forward: } \text{Var}(W) = \frac{1}{n_{in}}")
        eq2 = MathTex(r"\text{Backward: } \text{Var}(W) = \frac{1}{n_{out}}")
        eq3 = MathTex(r"\text{Compromise: } \text{Var}(W) = \frac{1}{2}\left(\frac{1}{n_{in}} + \frac{1}{n_{out}}\right)")
        eq4 = MathTex(r"\text{Var}(W) = \frac{n_{in} + n_{out}}{2 \cdot n_{in} \cdot n_{out}}")
        eq5 = MathTex(r"\text{Var}(W) = \frac{2}{n_{in} + n_{out}}")
        
        equations = VGroup(eq1, eq2, eq3, eq4, eq5).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        equations.next_to(title, DOWN)
        
        self.play(
            TransformMatchingTex(self.forward_result.copy(), eq1),
            TransformMatchingTex(self.backward_result.copy(), eq2)
        )
        self.wait(0.5)
        
        balance = Text("Balance between forward and backward constraints", font_size=24)
        balance.next_to(eq2, RIGHT, buff=1)
        self.play(Write(balance))
        self.wait(0.5)
        
        self.play(Write(eq3))
        self.wait(0.5)
        self.play(Write(eq4))
        self.wait(0.5)
        self.play(Write(eq5))
        
        # Highlight final result
        final_box = SurroundingRectangle(eq5, color=GREEN)
        self.play(Create(final_box))
        self.wait(1)
        
        self.final_result = eq5
        
        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(self.forward_result),
            FadeOut(self.backward_result),
            FadeOut(balance),
            FadeOut(VGroup(*equations[:-1])),
            FadeOut(final_box),
            eq5.animate.to_edge(UP)
        )
    
    def show_distributions(self):
        title = Text("Visualizing Weight Distributions", font_size=36)
        title.next_to(self.final_result, DOWN)
        self.play(Write(title))
        
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 1, 0.2],
            x_length=8,
            y_length=4,
            axis_config={"include_tip": False}
        )
        
        axes_labels = axes.get_axis_labels(x_label="w", y_label="p(w)")
        axes_group = VGroup(axes, axes_labels)
        axes_group.next_to(title, DOWN)
        
        self.play(Create(axes_group))
        self.wait(0.5)
        
        # Create distributions
        n_in = 100
        n_out = 100
        
        # Xavier standard deviation
        xavier_std = np.sqrt(2 / (n_in + n_out))
        
        # Normal distribution curves
        def normal_pdf(x, mu, sigma):
            return np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
        
        # Xavier normal
        xavier_curve = axes.plot(
            lambda x: normal_pdf(x, 0, xavier_std),
            color=GREEN
        )
        
        # Too small
        small_std = xavier_std * 0.3
        small_curve = axes.plot(
            lambda x: normal_pdf(x, 0, small_std),
            color=RED
        )
        
        # Too large
        large_std = xavier_std * 3
        large_curve = axes.plot(
            lambda x: normal_pdf(x, 0, large_std),
            color=ORANGE
        )
        
        # Legend
        legend = VGroup(
            VGroup(Square(side_length=0.2, fill_opacity=1, color=GREEN), 
                   Text("Xavier", font_size=20)).arrange(RIGHT, buff=0.2),
            VGroup(Square(side_length=0.2, fill_opacity=1, color=RED), 
                   Text("Too Small", font_size=20)).arrange(RIGHT, buff=0.2),
            VGroup(Square(side_length=0.2, fill_opacity=1, color=ORANGE), 
                   Text("Too Large", font_size=20)).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        legend.to_edge(RIGHT).shift(UP)
        
        # Show curves one by one
        self.play(Create(xavier_curve), Write(legend[0]))
        self.wait(0.5)
        self.play(Create(small_curve), Write(legend[1]))
        self.wait(0.5)
        self.play(Create(large_curve), Write(legend[2]))
        self.wait(1)
        
        # Show formula for standard deviation
        formula = MathTex(r"\sigma = \sqrt{\frac{2}{n_{in} + n_{out}}}")
        formula.next_to(axes_group, DOWN)
        
        self.play(Write(formula))
        self.wait(1)
        
        self.play(
            FadeOut(title),
            FadeOut(axes_group),
            FadeOut(xavier_curve),
            FadeOut(small_curve),
            FadeOut(large_curve),
            FadeOut(legend),
            FadeOut(formula),
            FadeOut(self.final_result)
        )
    
    def show_conclusion(self):
        title = Text("Xavier/Glorot Initialization", font_size=48)
        self.play(Write(title))
        self.wait(0.5)
        
        summary = VGroup(
            MathTex(r"\text{Var}(W) = \frac{2}{n_{in} + n_{out}}"),
            Text("Normal Distribution:", font_size=28),
            MathTex(r"W \sim \mathcal{N}\left(0, \sqrt{\frac{2}{n_{in} + n_{out}}}\right)"),
            Text("Uniform Distribution:", font_size=28),
            MathTex(r"W \sim \mathcal{U}\left[-\sqrt{\frac{6}{n_{in} + n_{out}}}, \sqrt{\frac{6}{n_{in} + n_{out}}}\right]"),
        ).arrange(DOWN, buff=0.5)
        
        summary.next_to(title, DOWN)
        
        for item in summary:
            self.play(Write(item))
            self.wait(0.5)
        
        conclusion = Text(
            "Balances signal flow in forward and backward passes\n"
            "Prevents vanishing and exploding gradients\n"
            "Enables effective training of deep networks",
            font_size=28
        )
        
        conclusion.next_to(summary, DOWN, buff=0.7)
        self.play(Write(conclusion))
        self.wait(1)
        
        credit = Text(
            "Xavier Glorot & Yoshua Bengio (2010)\n"
            "'Understanding the difficulty of training deep feedforward neural networks'",
            font_size=24
        )
        credit.to_edge(DOWN)
        
        self.play(Write(credit))
        self.wait(2)
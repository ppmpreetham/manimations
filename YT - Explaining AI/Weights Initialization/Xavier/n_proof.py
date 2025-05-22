from manim import *
import numpy as np

class GlorotInitializationProof(Scene):
    def construct(self):
        self.setup_scene()
        self.show_forward_pass()
        self.show_backward_pass()
        self.show_combined_constraint()
        self.demonstrate_experimentally()
        self.conclude()
        
    def setup_scene(self):
        self.title = Text("Xavier/Glorot Initialization Proof", font_size=42)
        subtitle = Text("Why Var(W) = 2/(n_in + n_out)?", font_size=32)
        subtitle.next_to(self.title, DOWN)
        
        self.play(Write(self.title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(
            self.title.animate.scale(0.6).to_corner(UL),
            FadeOut(subtitle)
        )
        
    def show_forward_pass(self):
        self.section_title = Text("Forward Pass Analysis", color=BLUE).scale(0.8)
        self.section_title.to_edge(UP)
        self.play(Write(self.section_title))
        
        # Create a simple network visualization
        self.network = self.create_network_diagram()
        self.play(Create(self.network))
        
        # Linear transformation equation
        eq1 = MathTex(r"y = Wx", font_size=36)
        eq1.next_to(self.network, DOWN, buff=0.5)
        self.play(Write(eq1))
        self.wait(1)
        
        # Variance analysis
        var_steps = VGroup(
            MathTex(r"\text{Var}(y_j) = \text{Var}\left(\sum_{i=1}^{n_{in}} W_{ji} x_i\right)", font_size=30),
            MathTex(r"\text{For independent } W_{ji} \text{ and } x_i \text{ with } E[x_i]=0:", font_size=30),
            MathTex(r"\text{Var}(y_j) = \sum_{i=1}^{n_{in}} \text{Var}(W_{ji}) \text{Var}(x_i)", font_size=30),
            MathTex(r"\text{Assuming } \text{Var}(x_i) = 1 \text{ and uniform } \text{Var}(W_{ji}) = \sigma_w^2:", font_size=30),
            MathTex(r"\text{Var}(y_j) = n_{in} \cdot \sigma_w^2", font_size=30),
            MathTex(r"\text{For preserving variance: } \text{Var}(y_j) = \text{Var}(x_i) = 1", font_size=30),
            MathTex(r"\text{Therefore: } \sigma_w^2 = \frac{1}{n_{in}}", font_size=30)
        )
        
        var_steps.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        var_steps.next_to(eq1, DOWN, buff=0.5)
        
        for step in var_steps:
            self.play(Write(step))
            self.wait(0.5)
            
        self.forward_result = var_steps[-1]
        self.forward_box = SurroundingRectangle(self.forward_result, color=BLUE)
        self.play(Create(self.forward_box))
        
        # Visual representation of variance preservation
        self.forward_viz = self.show_variance_visualization("forward")
        
        cleanup_group = VGroup(*var_steps[:-1], eq1)
        self.play(FadeOut(cleanup_group))
        
    def show_backward_pass(self):
        backward_title = Text("Backward Pass Analysis", color=RED).scale(0.8)
        backward_title.to_edge(UP)
        
        self.play(FadeOut(self.forward_viz))  # Remove forward visualization
        self.play(ReplacementTransform(self.section_title, backward_title))
        self.section_title = backward_title
        
        # Gradient flow equation
        eq1 = MathTex(r"\frac{\partial L}{\partial x} = W^T \frac{\partial L}{\partial y}", font_size=36)
        eq1.next_to(self.network, DOWN, buff=0.5)
        self.play(Write(eq1))
        self.wait(1)
        
        # Variance analysis for backward pass
        var_steps = VGroup(
            MathTex(r"\text{Var}\left(\frac{\partial L}{\partial x_i}\right) = \text{Var}\left(\sum_{j=1}^{n_{out}} W_{ji} \frac{\partial L}{\partial y_j}\right)", font_size=30),
            MathTex(r"\text{For independent } W_{ji} \text{ and } \frac{\partial L}{\partial y_j}:", font_size=30),
            MathTex(r"\text{Var}\left(\frac{\partial L}{\partial x_i}\right) = \sum_{j=1}^{n_{out}} \text{Var}(W_{ji}) \text{Var}\left(\frac{\partial L}{\partial y_j}\right)", font_size=30),
            MathTex(r"\text{Assuming } \text{Var}\left(\frac{\partial L}{\partial y_j}\right) = 1 \text{ and uniform } \text{Var}(W_{ji}) = \sigma_w^2:", font_size=30),
            MathTex(r"\text{Var}\left(\frac{\partial L}{\partial x_i}\right) = n_{out} \cdot \sigma_w^2", font_size=30),
            MathTex(r"\text{For stable gradients: } \text{Var}\left(\frac{\partial L}{\partial x_i}\right) = \text{Var}\left(\frac{\partial L}{\partial y_j}\right) = 1", font_size=30),
            MathTex(r"\text{Therefore: } \sigma_w^2 = \frac{1}{n_{out}}", font_size=30)
        )
        
        var_steps.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        var_steps.next_to(eq1, DOWN, buff=0.5)
        
        for step in var_steps:
            self.play(Write(step))
            self.wait(0.5)
            
        self.backward_result = var_steps[-1]
        self.backward_box = SurroundingRectangle(self.backward_result, color=RED)
        self.play(Create(self.backward_box))
        
        # Visual representation of gradient variance preservation
        self.backward_viz = self.show_variance_visualization("backward")
        
        cleanup_group = VGroup(*var_steps[:-1], eq1)
        self.play(FadeOut(cleanup_group))
        
    def show_combined_constraint(self):
        combined_title = Text("Combining Forward & Backward Constraints", color=PURPLE).scale(0.8)
        combined_title.to_edge(UP)
        
        self.play(FadeOut(self.backward_viz))  # Remove visualization
        self.play(ReplacementTransform(self.section_title, combined_title))
        self.section_title = combined_title
        
        # Move the two constraints side by side
        forward_group = VGroup(self.forward_result, self.forward_box)
        backward_group = VGroup(self.backward_result, self.backward_box)
        
        self.play(
            forward_group.animate.to_edge(LEFT).shift(RIGHT * 2 + UP),
            backward_group.animate.to_edge(RIGHT).shift(LEFT * 2 + UP)
        )
        
        # Highlighting the conflict
        conflict = Text("These two constraints conflict!", color=YELLOW, font_size=28)
        conflict.next_to(VGroup(forward_group, backward_group), DOWN)
        self.play(Write(conflict))
        self.wait(1)
        
        # Proposing the compromise - Xavier/Glorot solution
        solution_text = Text("Xavier/Glorot solution: balance both constraints", font_size=32)
        solution_text.next_to(conflict, DOWN)
        self.play(Write(solution_text))
        self.wait(1)
        
        # Mathematical compromise
        compromise = VGroup(
            MathTex(r"\text{Average of the constraints:} \quad \sigma_w^2 = \frac{1}{2}\left(\frac{1}{n_{in}} + \frac{1}{n_{out}}\right)", font_size=32),
            MathTex(r"\text{For similar layer sizes, approximately:} \quad \sigma_w^2 \approx \frac{1}{n_{in}}", font_size=32),
            MathTex(r"\text{A more symmetric solution:} \quad \sigma_w^2 = \frac{2}{n_{in} + n_{out}}", font_size=32)
        )
        
        compromise.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        compromise.next_to(solution_text, DOWN, buff=0.5)
        
        for step in compromise:
            self.play(Write(step))
            self.wait(0.75)
        
        # Highlight final result
        final_box = SurroundingRectangle(compromise[-1], color=PURPLE)
        self.play(Create(final_box))
        self.wait(1)
        
        # For clarity, isolate the result
        self.final_result = MathTex(r"\boxed{\text{Var}(W) = \frac{2}{n_{in} + n_{out}}}", font_size=48, color=PURPLE)
        self.final_result.move_to(ORIGIN)
        
        self.play(
            FadeOut(forward_group),
            FadeOut(backward_group),
            FadeOut(conflict),
            FadeOut(solution_text),
            FadeOut(compromise),
            FadeOut(final_box),
            Write(self.final_result)
        )
        self.wait(2)
        
    def demonstrate_experimentally(self):
        experiment_title = Text("Experimental Verification", font_size=36)
        experiment_title.to_edge(UP)
        self.play(
            self.title.animate.scale(0.8).to_corner(UL),  # Main title
            ReplacementTransform(self.section_title, experiment_title)  # Section title
        )
        self.section_title = experiment_title
        
        # Move final result up
        self.play(self.final_result.animate.scale(0.7).next_to(experiment_title, DOWN))
        
        # Create neural network for experimental demonstration
        exp_network = self.create_experimental_network()
        exp_network.scale(0.9).next_to(self.final_result, DOWN, buff=0.5)
        self.play(Create(exp_network))
        
        # Create histograms for distribution comparison
        histograms = self.create_distribution_comparison()
        histograms.scale(0.8).next_to(exp_network, DOWN, buff=0.5)
        self.play(Create(histograms))
        
        # Annotations
        annotations = VGroup(
            Text("Standard Normal Init: Variance increases/decreases with depth", font_size=24, color=RED),
            Text("Xavier/Glorot Init: Variance stable across all layers", font_size=24, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT)
        annotations.next_to(histograms, DOWN)
        
        self.play(Write(annotations))
        self.wait(2)

        # Store for cleanup
        self.exp_content = VGroup(exp_network, histograms, annotations)

    def conclude(self):
        conclusion = Text(
            "Xavier/Glorot initialization maintains stable signal\n"
            "variance throughout both forward and backward passes,\n"
            "enabling faster and more reliable training.",
            font_size=36
        )
        
        # Clear everything except title
        cleanup_objects = VGroup(
            self.section_title,
            self.final_result,
            self.exp_content,
            self.network
        )
        
        self.play(
            FadeOut(cleanup_objects),
            FadeIn(conclusion)
        )
        self.wait(2)
        
        final_formula = MathTex(r"\boxed{\text{Var}(W) = \frac{2}{n_{in} + n_{out}}}", font_size=48, color=PURPLE)
        final_formula.next_to(conclusion, DOWN, buff=0.5)
        self.play(Write(final_formula))
        self.wait(1)
        
        practical_note = Text(
            "Practically: Initialize W ~ Uniform(-√(6/(n_in+n_out)), √(6/(n_in+n_out)))\n"
            "Or W ~ Normal(0, √(2/(n_in+n_out)))",
            font_size=28
        )
        practical_note.next_to(final_formula, DOWN, buff=0.5)
        self.play(Write(practical_note))
        self.wait(3)

    def create_network_diagram(self):
        layers_sizes = [4, 5, 3]
        network = VGroup()
        
        # Create layers
        layers = []
        max_neurons = max(layers_sizes)
        layer_width = 2.5
        
        for i, size in enumerate(layers_sizes):
            layer = VGroup()
            for j in range(size):
                neuron = Circle(radius=0.2, color=WHITE)
                y_pos = (j - (size-1)/2) * 0.5
                neuron.move_to([i * layer_width - layer_width, y_pos, 0])
                layer.add(neuron)
            layers.append(layer)
            network.add(layer)
        
        # Create connections between layers
        for i in range(len(layers) - 1):
            for n1 in layers[i]:
                for n2 in layers[i+1]:
                    conn = Line(n1.get_center(), n2.get_center(), stroke_width=1)
                    network.add(conn)
                    
        # Add labels
        n_in = Text("n_in", font_size=24).next_to(layers[0], DOWN, buff=0.3)
        n_out = Text("n_out", font_size=24).next_to(layers[-1], DOWN, buff=0.3)
        network.add(n_in, n_out)
        
        # Add weight matrix label
        w_label = Text("W", font_size=32)
        w_label.move_to([(layers[0].get_center()[0] + layers[1].get_center()[0])/2, 
                          (max(layers_sizes)-1)/2 * 0.5 + 0.5, 0])
        network.add(w_label)
        
        return network
    
    def show_variance_visualization(self, pass_type):
        # Create a visualization showing signal/gradient flow and variance
        
        if pass_type == "forward":
            colors = [BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E]
            title = Text("Forward Signal Flow Visualization", font_size=24)
            var_text = "Signal Variance"
        else:
            colors = [RED_A, RED_B, RED_C, RED_D, RED_E]
            title = Text("Backward Gradient Flow Visualization", font_size=24)
            var_text = "Gradient Variance"
        
        # Create visualization panel
        panel = VGroup()
        
        # Create variance indicators for three types of initialization
        bad_init_low = self.create_variance_evolution("decrease", colors, var_text)
        bad_init_high = self.create_variance_evolution("increase", colors, var_text)
        good_init = self.create_variance_evolution("stable", colors, var_text)
        
        # Add labels
        bad_init_low_label = Text("Too small weights", font_size=20, color=colors[0])
        bad_init_high_label = Text("Too large weights", font_size=20, color=colors[-1])
        good_init_label = Text("Xavier/Glorot init", font_size=20, color=GREEN)
        
        bad_init_low_label.next_to(bad_init_low, RIGHT)
        bad_init_high_label.next_to(bad_init_high, RIGHT)
        good_init_label.next_to(good_init, RIGHT)
        
        # Arrange visualizations
        viz_group = VGroup(
            title,
            VGroup(bad_init_low, bad_init_low_label).arrange(RIGHT),
            VGroup(bad_init_high, bad_init_high_label).arrange(RIGHT),
            VGroup(good_init, good_init_label).arrange(RIGHT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        viz_group.scale(0.8).to_edge(DOWN)
        panel.add(viz_group)
        
        self.play(FadeIn(panel))
        return panel
    
    def create_variance_evolution(self, trend, colors, title_text):
        var_group = VGroup()
        
        # Title
        title = Text(title_text, font_size=22)
        var_group.add(title)
        
        # Create bars showing variance at each layer
        num_layers = 5
        bar_width = 0.2
        bar_spacing = 0.1
        max_height = 0.8
        
        bars = VGroup()
        
        if trend == "decrease":
            heights = [max_height * (0.9**i) for i in range(num_layers)]
        elif trend == "increase":
            heights = [max_height * (1.1**i) for i in range(num_layers)]
        else:  # stable
            heights = [max_height * 0.8] * num_layers
            
        for i, height in enumerate(heights):
            if trend == "stable":
                color = GREEN
            else:
                color = colors[min(i, len(colors)-1)]
                
            bar = Rectangle(
                width=bar_width,
                height=height,
                fill_opacity=0.8,
                color=color,
                stroke_width=1
            )
            bar.move_to([i * (bar_width + bar_spacing), height/2, 0])
            bars.add(bar)
        
        # Add layer labels
        labels = VGroup()
        for i in range(num_layers):
            label = Text(f"L{i+1}", font_size=16)
            label.next_to(bars[i], DOWN, buff=0.1)
            labels.add(label)
            
        var_group.add(bars, labels)
        var_group.arrange(DOWN)
        
        return var_group
        
    def create_experimental_network(self):
        # Create a visual of a deeper neural network for experimental demonstration
        layers = [3, 5, 7, 5, 3]
        network = VGroup()
        
        # Create neurons
        x_spacing = 1.0
        y_spacing = 0.5
        
        # Create layers of neurons
        all_neurons = []
        for l_idx, layer_size in enumerate(layers):
            layer_neurons = []
            for n_idx in range(layer_size):
                neuron = Circle(radius=0.15, color=WHITE, fill_opacity=0)
                y_pos = (n_idx - (layer_size-1)/2) * y_spacing
                x_pos = l_idx * x_spacing * 1.5
                neuron.move_to([x_pos, y_pos, 0])
                layer_neurons.append(neuron)
                network.add(neuron)
            all_neurons.append(layer_neurons)
        
        # Add connections
        for l_idx in range(len(layers) - 1):
            for n1 in all_neurons[l_idx]:
                for n2 in all_neurons[l_idx + 1]:
                    conn = Line(
                        n1.get_center(), 
                        n2.get_center(), 
                        stroke_width=0.5,
                        stroke_opacity=0.5
                    )
                    network.add(conn)
        
        # Add labels
        network.add(Text("Input", font_size=20).next_to(all_neurons[0][1], LEFT))
        network.add(Text("Output", font_size=20).next_to(all_neurons[-1][1], RIGHT))
        
        return network
    
    def create_distribution_comparison(self):
        # Create histograms comparing distribution with different initialization strategies
        
        group = VGroup()
        
        # Two rows: top for standard normal, bottom for glorot
        standard_row = self.create_histograms("standard", RED)
        glorot_row = self.create_histograms("glorot", GREEN)
        
        standard_label = Text("Standard Normal Init", font_size=22, color=RED)
        glorot_label = Text("Xavier/Glorot Init", font_size=22, color=GREEN)
        
        standard_group = VGroup(standard_label, standard_row).arrange(DOWN, buff=0.2)
        glorot_group = VGroup(glorot_label, glorot_row).arrange(DOWN, buff=0.2)
        
        group = VGroup(standard_group, glorot_group).arrange(DOWN, buff=0.5)
        
        return group
        
    def create_histograms(self, init_type, color):
        # Create a row of histograms representing activation distributions
        histograms = VGroup()
        num_layers = 4
        
        for i in range(num_layers):
            if init_type == "standard":
                # For standard init - variance increases with depth
                var = 1.0 * (1.5**i)
                height = 1.0 * (0.8**i)
            else:  # glorot init
                # For glorot init - stable variance
                var = 1.0
                height = 0.95
            
            # Create bell curve
            hist = self.create_bell_curve(var, height, color)
            histograms.add(hist)
            
        histograms.arrange(RIGHT, buff=0.3)
        return histograms
    
    def create_bell_curve(self, variance, height, color):
        # Create a bell curve (normal distribution) visualization
        
        curve = VMobject(color=color, fill_opacity=0.5, stroke_width=2)
        
        std_dev = np.sqrt(variance)
        x_min, x_max = -3 * std_dev, 3 * std_dev
        dx = 0.1
        
        points = []
        x_vals = np.arange(x_min, x_max + dx, dx)
        for x in x_vals:
            y = height * np.exp(-0.5 * (x / std_dev) ** 2)
            points.append([x, y, 0])
            
        # Add baseline points
        points.append([x_max, 0, 0])
        points.append([x_min, 0, 0])
        
        curve.set_points_as_corners(points)
        
        # Add variance text
        var_text = Text(f"σ² = {variance:.1f}", font_size=16, color=color)
        var_text.next_to(curve, UP, buff=0.1)
        
        layer_group = VGroup(curve, var_text)
        
        # Add layer label
        layer_num = len(self.create_bell_curve.__dict__.get('_layer_count', [])) + 1
        self.create_bell_curve.__dict__.setdefault('_layer_count', []).append(1)
        
        label = Text(f"Layer {layer_num % 4 + 1}", font_size=16)
        label.next_to(curve, DOWN, buff=0.1) 
        layer_group.add(label)
        
        # Scale to reasonable size
        layer_group.scale(0.5)
        
        return layer_group
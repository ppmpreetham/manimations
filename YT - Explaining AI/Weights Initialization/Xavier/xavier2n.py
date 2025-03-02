from manim import *
import numpy as np

class XavierInitializationScene(Scene):
    def construct(self):
        self.setup_scene()
        self.show_problem()
        self.forward_pass_analysis()
        self.backward_pass_analysis()
        self.combine_constraints()
        self.visualize_distributions()
        self.compare_initializations()
        self.conclusion()
    
    def setup_scene(self):
        # Title
        title = Text("Xavier Initialization", font_size=60)
        subtitle = Text("Understanding the mathematics behind weight initialization", 
                        font_size=32).next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(
            title.animate.scale(0.5).to_corner(UL),
            FadeOut(subtitle)
        )
        self.wait(1)
    
    def show_problem(self):
        # Neural network visual
        n_in = 4
        hidden = 5
        n_out = 3
        
        network = self.create_network(n_in, hidden, n_out)
        network.move_to(ORIGIN)
        
        self.play(Create(network))
        self.wait(1)
        
        # Problem statement
        problem = VGroup(
            Text("Problem: How should we initialize weights?", font_size=36),
            Text("Too small: Vanishing gradients", font_size=28, color=RED),
            Text("Too large: Exploding gradients", font_size=28, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(UP)
        
        self.play(Write(problem[0]))
        self.wait(1)
        
        # Demonstrate signal flow with poor initialization
        # Vanishing signal
        signal_path = self.highlight_path(network)
        vanishing_signal = self.create_signal(diminishing=True)
        
        self.play(Write(problem[1]))
        self.play(MoveAlongPath(vanishing_signal, signal_path), run_time=3)
        self.play(FadeOut(vanishing_signal))
        self.wait(1)
        
        # Exploding signal
        exploding_signal = self.create_signal(diminishing=False)
        self.play(Write(problem[2]))
        self.play(MoveAlongPath(exploding_signal, signal_path), run_time=2)
        self.play(FadeOut(exploding_signal))
        
        self.network = network
        self.problem_text = problem
        self.wait(1)
    
    def forward_pass_analysis(self):
        self.play(
            FadeOut(self.problem_text),
            self.network.animate.scale(0.7).to_edge(LEFT)
        )
        
        # Forward pass title
        forward_title = Text("Forward Pass Analysis", font_size=40).to_edge(UP)
        self.play(Write(forward_title))
        
        # Equations for forward pass
        eq1 = MathTex(r"y_j = \sum_{i=1}^{n_{in}} W_{ji} \cdot x_i")
        eq2 = MathTex(r"\text{Var}(y_j) = \sum_{i=1}^{n_{in}} \text{Var}(W_{ji} \cdot x_i)")
        eq3 = MathTex(r"\text{Var}(y_j) = n_{in} \cdot \text{Var}(W) \cdot \text{Var}(x)")
        eq4 = MathTex(r"\text{For stable variance: } \text{Var}(y) = \text{Var}(x)")
        eq5 = MathTex(r"\text{Therefore: } \text{Var}(W) = \frac{1}{n_{in}}")
        
        equations = VGroup(eq1, eq2, eq3, eq4, eq5).arrange(DOWN, aligned_edge=LEFT).next_to(forward_title, DOWN).shift(RIGHT*2)
        
        # Animate equations one by one
        self.play(Write(eq1))
        self.wait(1)
        
        # Visualize forward signal with variance
        in_neurons = VGroup(*[Dot() for _ in range(4)]).arrange(DOWN, buff=0.5)
        out_neuron = Dot().shift(RIGHT*3)
        
        connections = VGroup(*[Line(in_neuron.get_center(), out_neuron.get_center()) 
                             for in_neuron in in_neurons])
        
        neuron_labels = VGroup(
            MathTex("x_1"), MathTex("x_2"), MathTex("x_3"), MathTex("x_4"),
            MathTex("y_j")
        )
        
        for i, label in enumerate(neuron_labels[:-1]):
            label.next_to(in_neurons[i], LEFT)
            
        neuron_labels[-1].next_to(out_neuron, RIGHT)
        
        small_network = VGroup(in_neurons, out_neuron, connections, neuron_labels)
        small_network.to_edge(RIGHT).shift(DOWN*0.5)
        
        self.play(Create(small_network))
        
        # Highlight each connection and indicate weight variance
        weight_labels = VGroup(*[MathTex("W_{j" + str(i+1) + "}").scale(0.7).next_to(connections[i], UP, buff=0.1) 
                                for i in range(len(connections))])
        
        self.play(Write(weight_labels))
        self.wait(1)
        
        # Visualize variance propagation
        self.play(Write(eq2))
        self.wait(0.5)
        self.play(Write(eq3))
        self.wait(1)
        
        # Show desired outcome
        self.play(Write(eq4))
        self.wait(0.5)
        self.play(Write(eq5))
        
        # Highlight the key result
        box = SurroundingRectangle(eq5, color=YELLOW)
        self.play(Create(box))
        self.wait(1)
        
        self.forward_result = eq5
        self.forward_box = box
        
        self.play(
            FadeOut(small_network),
            FadeOut(weight_labels),
            FadeOut(equations[:-1]),
            FadeOut(forward_title),
            eq5.animate.to_edge(UP)
        )
        self.wait(1)
    
    def backward_pass_analysis(self):
        # Backward pass title
        backward_title = Text("Backward Pass Analysis", font_size=40).next_to(self.forward_result, DOWN)
        self.play(Write(backward_title))
        
        # Equations for backward pass
        eq1 = MathTex(r"\frac{\partial L}{\partial x_i} = \sum_{j=1}^{n_{out}} W_{ji} \cdot \frac{\partial L}{\partial y_j}")
        eq2 = MathTex(r"\text{Var}\left(\frac{\partial L}{\partial x_i}\right) = n_{out} \cdot \text{Var}(W) \cdot \text{Var}\left(\frac{\partial L}{\partial y}\right)")
        eq3 = MathTex(r"\text{For stable variance: } \text{Var}\left(\frac{\partial L}{\partial x}\right) = \text{Var}\left(\frac{\partial L}{\partial y}\right)")
        eq4 = MathTex(r"\text{Therefore: } \text{Var}(W) = \frac{1}{n_{out}}")
        
        equations = VGroup(eq1, eq2, eq3, eq4).arrange(DOWN, aligned_edge=LEFT).next_to(backward_title, DOWN)
        
        # Visualize backprop with small network
        out_neurons = VGroup(*[Dot() for _ in range(3)]).arrange(DOWN, buff=0.5)
        in_neuron = Dot().shift(LEFT*3)
        
        connections = VGroup(*[Line(in_neuron.get_center(), out_neuron.get_center()) 
                             for out_neuron in out_neurons])
        
        neuron_labels = VGroup(
            MathTex("x_i"),
            MathTex("y_1"), MathTex("y_2"), MathTex("y_3")
        )
        
        neuron_labels[0].next_to(in_neuron, LEFT)
        for i, label in enumerate(neuron_labels[1:]):
            label.next_to(out_neurons[i], RIGHT)
            
        small_network = VGroup(in_neuron, out_neurons, connections, neuron_labels)
        small_network.to_edge(RIGHT)
        
        # Animate equations
        self.play(Write(eq1))
        self.play(Create(small_network))
        self.wait(1)
        
        # Gradient arrows
        gradient_arrows = VGroup(*[
            Arrow(
                start=out_neurons[i].get_center() + RIGHT*0.5,
                end=out_neurons[i].get_center() + RIGHT*1.5,
                color=RED
            ).scale(0.7) for i in range(3)
        ])
        
        gradient_labels = VGroup(*[
            MathTex(r"\frac{\partial L}{\partial y_" + str(i+1) + "}").scale(0.7).next_to(gradient_arrows[i], RIGHT, buff=0.1)
            for i in range(3)
        ])
        
        self.play(
            Create(gradient_arrows),
            Write(gradient_labels)
        )
        
        # Backward flow
        back_arrows = VGroup(*[
            Arrow(
                start=connections[i].get_start() + LEFT*0.1,
                end=connections[i].get_start() + LEFT*1.0,
                color=RED
            ).scale(0.7) for i in range(3)
        ])
        
        final_grad = MathTex(r"\frac{\partial L}{\partial x_i}").next_to(back_arrows[1], LEFT)
        
        self.play(Write(eq2))
        self.wait(0.5)
        
        self.play(
            Create(back_arrows),
            Write(final_grad)
        )
        self.wait(1)
        
        self.play(Write(eq3))
        self.play(Write(eq4))
        
        # Highlight the key result
        backward_box = SurroundingRectangle(eq4, color=BLUE)
        self.play(Create(backward_box))
        self.wait(1)
        
        self.backward_result = eq4
        self.backward_box = backward_box
        
        self.play(
            FadeOut(small_network),
            FadeOut(gradient_arrows),
            FadeOut(gradient_labels),
            FadeOut(back_arrows),
            FadeOut(final_grad),
            FadeOut(equations[:-1]),
            FadeOut(backward_title),
            eq4.animate.next_to(self.forward_result, DOWN)
        )
        self.wait(1)
    
    def combine_constraints(self):
        # Title for combining constraints
        combine_title = Text("Balancing Forward & Backward Constraints", font_size=36).next_to(self.backward_result, DOWN)
        self.play(Write(combine_title))
        
        # Combining the two constraints
        eq1 = MathTex(r"\text{Forward: } \text{Var}(W) = \frac{1}{n_{in}}")
        eq2 = MathTex(r"\text{Backward: } \text{Var}(W) = \frac{1}{n_{out}}")
        eq3 = MathTex(r"\text{Compromise: } \text{Var}(W) = \frac{1}{2}\left(\frac{1}{n_{in}} + \frac{1}{n_{out}}\right)")
        eq4 = MathTex(r"\text{Var}(W) = \frac{n_{out} + n_{in}}{2 \cdot n_{in} \cdot n_{out}}")
        eq5 = MathTex(r"\text{Var}(W) = \frac{2}{n_{in} + n_{out}}")
        
        equations = VGroup(eq1, eq2, eq3, eq4, eq5).arrange(DOWN, aligned_edge=LEFT).next_to(combine_title, DOWN)
        
        self.play(
            TransformMatchingTex(self.forward_result.copy(), eq1),
            TransformMatchingTex(self.backward_result.copy(), eq2)
        )
        self.wait(0.5)
        
        left_pan = Circle(radius=0.5, fill_opacity=0.2, color=BLUE)
        right_pan = Circle(radius=0.5, fill_opacity=0.2, color=RED)
        
        fulcrum = Triangle().scale(0.3).rotate(PI)
        beam = Line(left_pan.get_center() + UP*0.5, right_pan.get_center() + UP*0.5)
        
        left_pan.next_to(beam, LEFT+DOWN)
        right_pan.next_to(beam, RIGHT+DOWN)
        fulcrum.next_to(beam, DOWN, buff=0)
        
        scale = VGroup(beam, fulcrum, left_pan, right_pan)
        scale.scale(0.8).to_edge(RIGHT)
        
        scale_text1 = MathTex(r"\frac{1}{n_{in}}").next_to(left_pan, DOWN)
        scale_text2 = MathTex(r"\frac{1}{n_{out}}").next_to(right_pan, DOWN)
        
        scale_group = VGroup(scale, scale_text1, scale_text2)

        
        self.play(FadeIn(scale_group))
        self.wait(0.5)
        
        # Show compromise
        self.play(Write(eq3))
        self.wait(1)
        
        # Algebraic steps
        self.play(Write(eq4))
        self.wait(0.5)
        self.play(Write(eq5))
        
        # Box the final result
        final_box = SurroundingRectangle(eq5, color=GREEN)
        self.play(Create(final_box))
        self.wait(1)
        
        self.final_result = eq5
        self.final_box = final_box
        
        self.play(
            FadeOut(self.forward_result),
            FadeOut(self.forward_box),
            FadeOut(self.backward_result),
            FadeOut(self.backward_box),
            FadeOut(equations[:-1]),
            FadeOut(scale_group),
            FadeOut(combine_title),
            eq5.animate.to_edge(UP)
        )
        self.wait(1)
    
    def visualize_distributions(self):
        # Title for distribution visualization
        dist_title = Text("Visualizing Weight Distributions", font_size=36).next_to(self.final_result, DOWN)
        self.play(Write(dist_title))
        
        # Create axes for weight distribution
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 1, 0.25],
            x_length=6,
            y_length=3,
            axis_config={"include_tip": False}
        )
        
        axes_labels = axes.get_axis_labels(x_label="w", y_label="p(w)")
        axes_group = VGroup(axes, axes_labels).next_to(dist_title, DOWN)
        
        self.play(Create(axes_group))
        
        # Create distributions for different initializations
        n_in, n_out = 100, 100  # Example values
        
        # Xavier Uniform distribution
        xavier_std = np.sqrt(2 / (n_in + n_out))
        xavier_scale = xavier_std * np.sqrt(3)  # For uniform distribution: std = scale*sqrt(1/3)
        
        def xavier_uniform(x):
            # Uniform distribution scaled appropriately
            mask = (x >= -xavier_scale) & (x <= xavier_scale)
            return mask * (1 / (2 * xavier_scale))
        
        # Xavier Normal distribution
        def xavier_normal(x):
            return (1 / (xavier_std * np.sqrt(2 * np.pi))) * np.exp(-(x**2) / (2 * xavier_std**2))
        
        # Too small initialization
        small_std = xavier_std * 0.3
        def small_init(x):
            return (1 / (small_std * np.sqrt(2 * np.pi))) * np.exp(-(x**2) / (2 * small_std**2))
        
        # Too large initialization
        large_std = xavier_std * 3
        def large_init(x):
            return (1 / (large_std * np.sqrt(2 * np.pi))) * np.exp(-(x**2) / (2 * large_std**2))
        
        # Plot distributions
        xavier_norm_plot = axes.plot(lambda x: xavier_normal(x), color=GREEN)
        xavier_uniform_plot = axes.plot(lambda x: xavier_uniform(x), color=BLUE)
        small_plot = axes.plot(lambda x: small_init(x), color=RED)
        large_plot = axes.plot(lambda x: large_init(x), color=ORANGE)
        
        # Legend
        legend = VGroup(
            VGroup(Square(side_length=0.2, color=GREEN), Text("Xavier Normal", font_size=20)).arrange(RIGHT, buff=0.2),
            VGroup(Square(side_length=0.2, color=BLUE), Text("Xavier Uniform", font_size=20)).arrange(RIGHT, buff=0.2),
            VGroup(Square(side_length=0.2, color=RED), Text("Too Small", font_size=20)).arrange(RIGHT, buff=0.2),
            VGroup(Square(side_length=0.2, color=ORANGE), Text("Too Large", font_size=20)).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT)
        
        # Show Xavier Normal
        self.play(Create(xavier_norm_plot))
        self.play(FadeIn(legend[0]))
        self.wait(0.5)
        
        # Show Xavier Uniform
        self.play(Create(xavier_uniform_plot))
        self.play(FadeIn(legend[1]))
        self.wait(0.5)
        
        # Show what happens with too small/large initializations
        self.play(Create(small_plot))
        self.play(FadeIn(legend[2]))
        self.wait(0.5)
        
        self.play(Create(large_plot))
        self.play(FadeIn(legend[3]))
        self.wait(1)
        
        # Formula for standard deviation
        std_formula = MathTex(r"\sigma = \sqrt{\frac{2}{n_{in} + n_{out}}}")
        std_formula.next_to(legend, DOWN, buff=0.5)
        
        self.play(Write(std_formula))
        self.wait(1)
        
        self.dist_plots = VGroup(xavier_norm_plot, xavier_uniform_plot, small_plot, large_plot)
        self.dist_legend = legend
        self.dist_axes = axes_group
        self.std_formula = std_formula
        self.dist_title = dist_title
    
    def compare_initializations(self):
        # Clear previous visualizations
        self.play(
            FadeOut(self.dist_plots),
            FadeOut(self.dist_legend),
            FadeOut(self.dist_axes),
            FadeOut(self.std_formula),
            FadeOut(self.dist_title),
            FadeOut(self.final_box)
        )
        
        # Comparison title
        compare_title = Text("Comparing Initializations in Action", font_size=36).next_to(self.final_result, DOWN)
        self.play(Write(compare_title))
        
        # Create a deep network for visualization
        layers = [4, 6, 8, 6, 3]
        networks = VGroup(*[self.create_network(layers[0], layers[1:-1], layers[-1]) for _ in range(3)])
        
        titles = VGroup(
            Text("Xavier Init", color=GREEN, font_size=24),
            Text("Small Init", color=RED, font_size=24),
            Text("Large Init", color=ORANGE, font_size=24)
        )
        
        # Arrange networks side by side
        for i, (network, title) in enumerate(zip(networks, titles)):
            network.scale(0.5)
            title.next_to(network, UP)
            network_group = VGroup(network, title)
            network_group.move_to([-4 + i*4, -1, 0])
        
        self.play(
            *[Create(network) for network in networks],
            *[Write(title) for title in titles]
        )
        self.wait(1)
        
        # Show signal flow in each network
        paths = [self.highlight_path(network) for network in networks]
        
        # Create signals with different behaviors
        signals = [
            self.create_signal(diminishing=False, exploding=False, color=GREEN),  # Xavier - stable
            self.create_signal(diminishing=True, exploding=False, color=RED),     # Small - vanishing
            self.create_signal(diminishing=False, exploding=True, color=ORANGE)   # Large - exploding
        ]
        
        # Animate signals through networks
        self.play(
            *[MoveAlongPath(signal, path) for signal, path in zip(signals, paths)],
            run_time=3
        )
        self.wait(1)
        
        # Show histograms of activations at different layers
        histograms = self.create_layered_histograms()
        histograms.next_to(networks, DOWN, buff=1)
        
        self.play(Create(histograms))
        self.wait(2)
        
        self.networks = networks
        self.network_titles = titles
        self.histograms = histograms
        self.compare_title = compare_title
    
    def conclusion(self):
        # Clear previous visualizations
        self.play(
            FadeOut(self.networks),
            FadeOut(self.network_titles),
            FadeOut(self.histograms),
            FadeOut(self.compare_title)
        )
        
        # Final summary
        summary = VGroup(
            Text("Summary:", font_size=36),
            MathTex(r"\text{Var}(W) = \frac{2}{n_{in} + n_{out}}"),
            Text("For uniform distribution:", font_size=28),
            MathTex(r"W \sim U\left[-\sqrt{\frac{6}{n_{in} + n_{out}}}, \sqrt{\frac{6}{n_{in} + n_{out}}}\right]"),
            Text("For normal distribution:", font_size=28),
            MathTex(r"W \sim N\left(0, \sqrt{\frac{2}{n_{in} + n_{out}}}\right)")
        ).arrange(DOWN, buff=0.4).next_to(self.final_result, DOWN, buff=1)
        
        self.play(Write(summary[0]))
        self.play(Write(summary[1]))
        self.wait(0.5)
        self.play(Write(summary[2]))
        self.play(Write(summary[3]))
        self.wait(0.5)
        self.play(Write(summary[4]))
        self.play(Write(summary[5]))
        self.wait(1)
        
        # Final credits
        credits = Text(
            "Xavier/Glorot Initialization\n"
            "Proposed by Xavier Glorot & Yoshua Bengio (2010)\n"
            "'Understanding the difficulty of training deep feedforward neural networks'",
            font_size=24
        ).to_edge(DOWN)
        
        self.play(Write(credits))
        self.wait(2)
    
    # Helper methods
    def create_network(self, n_in, hidden_layers, n_out):
        if isinstance(hidden_layers, int):
            hidden_layers = [hidden_layers]
            
        layers = [n_in] + hidden_layers + [n_out]
        
        network = VGroup()
        all_neurons = []
        
        # Create neurons for each layer
        for i, n_neurons in enumerate(layers):
            layer_neurons = VGroup(*[Dot() for _ in range(n_neurons)])
            layer_neurons.arrange(DOWN, buff=0.5)
            if i > 0:
                layer_neurons.next_to(all_neurons[-1], RIGHT, buff=2)
            all_neurons.append(layer_neurons)
            network.add(layer_neurons)
        
        # Connect neurons between adjacent layers
        connections = VGroup()
        for i in range(len(layers) - 1):
            for neuron1 in all_neurons[i]:
                for neuron2 in all_neurons[i+1]:
                    connection = Line(
                        neuron1.get_center(),
                        neuron2.get_center(),
                        stroke_opacity=0.5,
                        stroke_width=1
                    )
                    connections.add(connection)
        
        network.add(connections)
        return network
    
    def highlight_path(self, network):
        # Find a path through the network
        # The issue is here - network contains both dots and connections, but we're 
        # incorrectly filtering by checking if an object is a Dot
        dots = []
        for mobject in network:
            if isinstance(mobject, VGroup):
                for submobject in mobject:
                    if isinstance(submobject, Dot):
                        dots.append(submobject)

        # Group dots into layers
        layers = []
        if dots:  # Add this check to handle empty dots list
            current_layer = []
            x_coord = dots[0].get_center()[0]

            for dot in dots:
                if abs(dot.get_center()[0] - x_coord) < 0.1:
                    current_layer.append(dot)
                else:
                    layers.append(current_layer)
                    current_layer = [dot]
                    x_coord = dot.get_center()[0]

            if current_layer:
                layers.append(current_layer)

        # Select one neuron from each layer for the path
        path_neurons = [layer[len(layer)//2] for layer in layers]

        # Create the path
        path = VMobject()
        points = [neuron.get_center() for neuron in path_neurons]
        path.set_points_as_corners(points)

        return path
    
    def create_signal(self, diminishing=False, exploding=False, color=WHITE):
        if diminishing:
            signal = Circle(radius=0.2, color=color, fill_opacity=0.8)
            signal.add_updater(lambda m, dt: m.scale(0.99))
        elif exploding:
            signal = Circle(radius=0.2, color=color, fill_opacity=0.8)
            signal.add_updater(lambda m, dt: m.scale(1.01))
        else:
            signal = Circle(radius=0.2, color=color, fill_opacity=0.8)
        
        return signal
    
    def create_layered_histograms(self):
        # Create visualization of activation distributions across layers
        group = VGroup()
        
        layer_titles = ["Layer 1", "Layer 2", "Layer 3", "Output"]
        
        for i, title in enumerate(layer_titles):
            # Xavier (stable)
            xavier_hist = self.create_histogram(
                values=np.random.normal(0, 1, 1000), 
                color=GREEN,
                height=1,
                width=1.2
            )
            
            # Small init (shrinking)
            small_values = np.random.normal(0, 1, 1000) * (0.5 ** i)
            small_hist = self.create_histogram(
                values=small_values, 
                color=RED,
                height=1,
                width=1.2
            )
            
            # Large init (expanding)
            large_values = np.random.normal(0, 1, 1000) * (1.5 ** i)
            large_hist = self.create_histogram(
                values=large_values, 
                color=ORANGE,
                height=1,
                width=1.2
            )
            
            layer_group = VGroup(
                xavier_hist, small_hist, large_hist,
                Text(title, font_size=16)
            ).arrange(DOWN, buff=0.2)
            
            group.add(layer_group)
        
        group.arrange(RIGHT, buff=0.7)
        return group
    
    def create_histogram(self, values, bins=20, color=WHITE, height=2, width=3):
        # Create a simple histogram visualization
        hist, bin_edges = np.histogram(values, bins=bins, density=True)
        
        # Scale histogram
        hist = hist / np.max(hist) * height
        
        # Create rectangles for bars
        bars = VGroup()
        for i in range(len(hist)):
            bar = Rectangle(
                height=hist[i],
                width=width/bins,
                fill_opacity=0.7,
                fill_color=color,
                stroke_width=1,
                stroke_color=WHITE
            )
            bar.move_to([bin_edges[i]*width/2, hist[i]/2, 0], aligned_edge=DOWN+LEFT)
            bars.add(bar)
        
        result = VGroup(bars)
        result.scale(0.3)  # Scale down to fit in scene
        return result

class FinalSummaryScene(Scene):
    def construct(self):
        title = Text("Xavier Initialization", font_size=60).to_edge(UP)
        
        formula = MathTex(r"\text{Var}(W) = \frac{2}{n_{in} + n_{out}}").scale(1.5)
        
        implementations = VGroup(
            Text("Normal distribution:", font_size=32),
            MathTex(r"W \sim N\left(0, \sqrt{\frac{2}{n_{in} + n_{out}}}\right)"),
            Text("Uniform distribution:", font_size=32),
            MathTex(r"W \sim U\left[-\sqrt{\frac{6}{n_{in} + n_{out}}}, \sqrt{\frac{6}{n_{in} + n_{out}}}\right]")
        ).arrange(DOWN)
        
        VGroup(formula, implementations).arrange(DOWN, buff=1)
        
        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(formula))
        self.wait(1)
        
        for item in implementations:
            self.play(Write(item))
            self.wait(0.5)
        
        self.wait(2)
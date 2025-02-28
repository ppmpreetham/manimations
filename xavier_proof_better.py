from manim import *
import numpy as np

class XavierInitialization(Scene):
    def construct(self):
        # Title sequence
        title = Text("Xavier Initialization", font_size=48)
        subtitle = Text("Maintaining Variance Across Neural Network Layers", font_size=32)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Introduction to Neural Network Layer
        self.introduce_neural_network_layer()
        
        # Explain Linear Transformation in a Layer
        self.explain_linear_transformation()
        
        # Visualize Variance of Activations
        self.visualize_variance()
        
        # Show why 2/n_in is used instead of 1/n_in
        self.explain_factor_two()
        
        # Conclusion and summary
        self.conclusion()

    def introduce_neural_network_layer(self):
        # Create a simple neural network diagram
        nn_layers = self.create_network_layers()
        
        self.play(Create(nn_layers))
        self.wait(1)
        
        # Highlight the specific layer we're focusing on
        focus_rect = SurroundingRectangle(nn_layers[1], color=YELLOW, buff=0.2)
        layer_text = Text("Focus on a single layer", font_size=32).to_edge(UP)
        
        self.play(Create(focus_rect), Write(layer_text))
        self.wait(2)
        
        # Explain input and output dimensions
        input_dim = MathTex(r"x \in \mathbb{R}^{n_{\text{in}}}", font_size=36)
        output_dim = MathTex(r"y \in \mathbb{R}^{n_{\text{out}}}", font_size=36)
        
        input_dim.next_to(nn_layers[0], LEFT, buff=1)
        output_dim.next_to(nn_layers[1], RIGHT, buff=1)
        
        input_arrow = Arrow(input_dim, nn_layers[0], buff=0.1)
        output_arrow = Arrow(nn_layers[1], output_dim, buff=0.1)
        
        self.play(Write(input_dim), Write(output_dim))
        self.play(Create(input_arrow), Create(output_arrow))
        self.wait(2)
        
        self.play(
            FadeOut(input_arrow), FadeOut(output_arrow),
            FadeOut(focus_rect), FadeOut(layer_text),
            FadeOut(nn_layers), FadeOut(input_dim), FadeOut(output_dim)
        )
    
    def create_network_layers(self):
        # Create a neural network with 3 layers
        layers_group = VGroup()
        n_layers = 3
        n_neurons = [4, 5, 3]  # Number of neurons in each layer
        
        for i in range(n_layers):
            layer = VGroup()
            for j in range(n_neurons[i]):
                neuron = Circle(radius=0.2, color=BLUE, fill_opacity=0.5)
                neuron.move_to([3 * i - 3, j - (n_neurons[i] - 1)/2, 0])
                layer.add(neuron)
            layers_group.add(layer)
        
        # Add connections between layers
        for i in range(n_layers - 1):
            for n1 in layers_group[i]:
                for n2 in layers_group[i+1]:
                    conn = Line(n1.get_center(), n2.get_center(), stroke_opacity=0.5, stroke_width=1)
                    layers_group.add(conn)
        
        return layers_group

    def explain_linear_transformation(self):
        # Create the section title
        section_title = Text("Linear Transformation in a Layer", font_size=40)
        self.play(Write(section_title))
        self.wait(1.5)
        self.play(section_title.animate.to_edge(UP))
        
        # Show the linear transformation equation y = Wx + b
        eq = MathTex(r"y = W x + b", font_size=42)
        self.play(Write(eq))
        self.wait(1)
        
        # Explain the components of the equation
        w_desc = MathTex(r"W \text{ is the weight matrix of size } n_{\text{out}} \times n_{\text{in}}", font_size=32)
        x_desc = MathTex(r"x \text{ is the input vector of size } n_{\text{in}}", font_size=32)
        b_desc = MathTex(r"b \text{ is the bias vector (for simplicity, assume } b = 0 \text{)}", font_size=32)
        
        descriptions = VGroup(w_desc, x_desc, b_desc).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        descriptions.next_to(eq, DOWN, buff=0.8)
        
        self.play(Write(descriptions))
        self.wait(2)
        
        # Simplify to y = Wx
        eq_simple = MathTex(r"y = W x", font_size=42)
        eq_simple.move_to(eq)
        self.play(Transform(eq, eq_simple))
        self.wait(1.5)
        
        # Clean up for the next section
        self.play(
            FadeOut(descriptions),
            FadeOut(section_title),
            FadeOut(eq_simple),
            FadeOut(eq)
        )
        # Keep eq for the next part
        
    def visualize_variance(self):
        # Create the section title
        section_title = Text("Variance of Activations", font_size=40)
        section_title.to_edge(UP)
        self.play(Write(section_title))
        
        # Create a geometric visualization of the transformation
        # Here we'll represent our input and output spaces
        
        # Create the input space (2D for visualization)
        n_in = 2
        input_axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4,
            y_length=4,
            axis_config={"include_tip": True}
        )
        input_axes.to_edge(LEFT, buff=1.5)
        input_label = Text("Input Space", font_size=24).next_to(input_axes, DOWN)
        
        # Create the output space
        n_out = 2
        output_axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4,
            y_length=4,
            axis_config={"include_tip": True}
        )
        output_axes.to_edge(RIGHT, buff=1.5)
        output_label = Text("Output Space", font_size=24).next_to(output_axes, DOWN)
        
        self.play(
            Create(input_axes),
            Create(output_axes),
            Write(input_label),
            Write(output_label)
        )
        
        # Get equation from previous section and move it
        eq = MathTex(r"y = W x", font_size=36)
        eq.move_to(ORIGIN)
        self.play(ReplacementTransform(self.mobjects[-5], eq))  # Transform the equation kept from the previous section
        
        # Draw random points in the input space (unit variance)
        np.random.seed(42)  # For reproducibility
        n_points = 30
        points_x = np.random.normal(0, 1, n_points)  # Mean 0, variance 1
        points_y = np.random.normal(0, 1, n_points)  # Mean 0, variance 1
        
        # Create dots for input space
        input_dots = VGroup()
        for i in range(n_points):
            dot = Dot(input_axes.c2p(points_x[i], points_y[i]), color=BLUE, radius=0.05)
            input_dots.add(dot)
        
        self.play(Create(input_dots))
        
        # Define the inverse variance as a scaling factor
        variance_eq = MathTex(r"\text{Var}(x) = \sigma_x^2", font_size=32)
        variance_eq.next_to(input_axes, UP)
        self.play(Write(variance_eq))
        
        # Explain the aim: preserving variance
        aim_text = Text("Goal: Preserve the variance of activations", font_size=24)
        aim_text.next_to(eq, UP, buff=3.1)
        self.play(Write(aim_text))
        self.wait(1.5)
        
        # Now demonstrate three cases of weight initialization
        
        # Case 1: Weights too large (variance increases)
        w_large = [[2.0, 0.0], [0.0, 2.0]]  # Scaling matrix
        transformed_points_large = [np.dot(w_large, [points_x[i], points_y[i]]) for i in range(n_points)]
        
        # Create dots for output space
        output_dots_large = VGroup()
        for i in range(n_points):
            dot = Dot(output_axes.c2p(transformed_points_large[i][0], transformed_points_large[i][1]), 
                     color=RED, radius=0.05)
            output_dots_large.add(dot)
        
        # Show transformation with large weights
        w_large_eq = MathTex(r"W \text{ with large values}", font_size=28)
        w_large_eq.set_color(RED)
        w_large_eq.next_to(output_axes, UP)
        
        self.play(
            Create(output_dots_large),
            Write(w_large_eq)
        )
        self.wait(1)
        
        # Highlight the increased variance
        var_large_text = Text("Variance increases", font_size=24, color=RED)
        var_large_text.next_to(output_label, DOWN, buff=0.5)
        self.play(Write(var_large_text))
        self.wait(1.5)
        self.play(
            FadeOut(output_dots_large),
            FadeOut(w_large_eq),
            FadeOut(var_large_text)
        )
        
        # Case 2: Weights too small (variance decreases)
        w_small = [[0.2, 0.0], [0.0, 0.2]]  # Scaling matrix
        transformed_points_small = [np.dot(w_small, [points_x[i], points_y[i]]) for i in range(n_points)]
        
        # Create dots for output space
        output_dots_small = VGroup()
        for i in range(n_points):
            dot = Dot(output_axes.c2p(transformed_points_small[i][0], transformed_points_small[i][1]), 
                     color=GREEN, radius=0.05)
            output_dots_small.add(dot)
        
        # Show transformation with small weights
        w_small_eq = MathTex(r"W \text{ with small values}", font_size=28)
        w_small_eq.set_color(GREEN)
        w_small_eq.next_to(output_axes, UP)
        
        self.play(
            Create(output_dots_small),
            Write(w_small_eq)
        )
        self.wait(1)
        
        # Highlight the decreased variance
        var_small_text = Text("Variance decreases", font_size=24, color=GREEN)
        var_small_text.next_to(output_label, DOWN, buff=0.5)
        self.play(Write(var_small_text))
        self.wait(1.5)
        self.play(
            FadeOut(output_dots_small),
            FadeOut(w_small_eq),
            FadeOut(var_small_text)
        )
        
        # Case 3: Xavier initialization (variance preserved)
        scale = np.sqrt(2/n_in)
        w_xavier = [[scale, 0], [0, scale]]  # Xavier scaling
        transformed_points_xavier = [np.dot(w_xavier, [points_x[i], points_y[i]]) for i in range(n_points)]
        
        # Create dots for output space
        output_dots_xavier = VGroup()
        for i in range(n_points):
            dot = Dot(output_axes.c2p(transformed_points_xavier[i][0], transformed_points_xavier[i][1]), 
                     color=YELLOW, radius=0.05)
            output_dots_xavier.add(dot)
        
        # Show transformation with Xavier initialization
        w_xavier_eq = MathTex(r"W \text{ with Xavier initialization: } \sigma_w^2 = \frac{2}{n_{\text{in}}}", font_size=28)
        w_xavier_eq.set_color(YELLOW)
        w_xavier_eq.next_to(output_axes, UP)
        
        self.play(
            Create(output_dots_xavier),
            Write(w_xavier_eq)
        )
        self.wait(1)
        
        # Highlight the preserved variance
        var_xavier_text = Text("Variance preserved", font_size=24, color=YELLOW)
        var_xavier_text.next_to(output_label, DOWN, buff=0.5)
        self.play(Write(var_xavier_text))
        self.wait(2)
        
        # Show the theoretical calculation
        theoretical_title = Text("Theoretical Justification", font_size=32)
        theoretical_title.next_to(section_title, DOWN, buff=0.5)
        
        # Clean up some elements for the next explanation
        self.play(
            FadeOut(input_dots), FadeOut(output_dots_xavier),
            FadeOut(input_label), FadeOut(output_label),
            FadeOut(input_axes), FadeOut(output_axes),
            FadeOut(variance_eq), FadeOut(w_xavier_eq),
            FadeOut(var_xavier_text), FadeOut(aim_text), 
            FadeOut(eq)
        )
        
        self.play(Write(theoretical_title))
        
        # Calculate variance equation
        var_eq1 = MathTex(r"\text{Var}(y) = \text{Var}(Wx)", font_size=36)
        var_eq2 = MathTex(r"\text{Var}(y) = W \, \text{Var}(x) \, W^T", font_size=36)
        var_eq3 = MathTex(r"\text{Var}(y) = \sigma_x^2 \cdot WW^T", font_size=36)
        
        equations = VGroup(var_eq1, var_eq2, var_eq3).arrange(DOWN, buff=0.7)
        equations.next_to(theoretical_title, DOWN, buff=0.7)
        
        self.play(Write(var_eq1))
        self.wait(1)
        self.play(ReplacementTransform(var_eq1, var_eq2))
        self.wait(1)
        self.play(ReplacementTransform(var_eq1, var_eq3))
        self.wait(2)
        
        # Clean up for next section
        self.play(
            FadeOut(section_title),
            FadeOut(theoretical_title),
            FadeOut(equations)
        )

    def explain_factor_two(self):
        # Create section title
        section_title = Text("Why Use a Factor of 2?", font_size=40)
        section_title.to_edge(UP)
        self.play(Write(section_title))
        self.wait(1)
        
        # Create explanation text
        explanation = Text(
            "For symmetric activation functions like tanh or sigmoid,\n"
            "the factor of 2 compensates for the reduction in variance\n"
            "that occurs during backpropagation.",
            font_size=32, line_spacing=1.2
        )
        explanation.next_to(section_title, DOWN, buff=0.8)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # Show activation functions
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8,
            y_length=4,
            axis_config={"include_tip": True}
        )
        axes.move_to(DOWN * 1.5)
        
        # Plot tanh function
        tanh_function = axes.plot(
            lambda x: np.tanh(x),
            color=BLUE
        )
        tanh_label = Text("tanh(x)", font_size=24, color=BLUE)
        tanh_label.next_to(tanh_function, UP + RIGHT)
        
        self.play(Create(axes), Create(tanh_function), Write(tanh_label))
        self.wait(1.5)
        
        # Highlight the gradient effect
        x_value = 2.5
        point = axes.c2p(x_value, np.tanh(x_value))
        dot = Dot(point, color=YELLOW)
        
        # Compute the tangent line
        gradient = 1 - np.tanh(x_value)**2  # Derivative of tanh
        tangent_line = axes.plot(
            lambda x: gradient * (x - x_value) + np.tanh(x_value),
            x_range=[x_value-1.5, x_value+1.5],
            color=YELLOW
        )
        
        gradient_text = MathTex(
            r"\text{Gradient} = 1 - \tanh^2(x) < 1 \text{ (for } x \neq 0 \text{)}",
            font_size=28
        )
        gradient_text.set_color(YELLOW)
        gradient_text.to_edge(DOWN, buff=0.5)
        
        self.play(Create(dot), Create(tangent_line), Write(gradient_text))
        self.wait(2)
        
        # Show the factor 2 compensating
        compensation_text = Text(
            "The factor 2 compensates for this gradient shrinkage",
            font_size=28, color=YELLOW
        )
        compensation_text.next_to(gradient_text, UP, buff=0.5)
        
        self.play(Write(compensation_text))
        self.wait(2)
        
        # Xavier variance formula with the factor 2
        xavier_eq = MathTex(
            r"\sigma_W^2 = \frac{2}{n_{\text{in}}} \Rightarrow \text{Var}(y) \approx \text{Var}(x)",
            font_size=36
        )
        xavier_eq.next_to(explanation, DOWN, buff=1.0)
        
        self.play(
            FadeOut(axes), FadeOut(tanh_function), FadeOut(tanh_label),
            FadeOut(dot), FadeOut(tangent_line), FadeOut(gradient_text),
            FadeOut(compensation_text), FadeOut(explanation)
        )
        
        self.play(Write(xavier_eq))
        self.wait(2)
        
        # Clean up for conclusion
        self.play(
            FadeOut(section_title),
            FadeOut(xavier_eq)
        )

    def conclusion(self):
        # Title for conclusion
        title = Text("Conclusion", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Summary points
        points = [
            "Xavier initialization helps maintain variance across layers",
            "Weight variance set to 2/n_in prevents vanishing/exploding gradients",
            "The factor 2 accounts for nonlinear activation functions",
            "Stable training leads to faster convergence and better models"
        ]
        
        bullet_points = VGroup()
        
        for i, point in enumerate(points):
            bullet = Text("• " + point, font_size=28)
            bullet.move_to(UP * (1 - i * 0.8))
            bullet_points.add(bullet)
        
        for bullet in bullet_points:
            self.play(Write(bullet))
            self.wait(1)
        
        # Show final formula
        final_formula = MathTex(
            r"W \sim \mathcal{N}\left(0, \frac{2}{n_{\text{in}}}\right)",
            font_size=40
        )
        final_formula.next_to(bullet_points, DOWN, buff=1.0)
        
        self.play(Write(final_formula))
        self.wait(1)
        
        # Add a box around the final formula
        box = SurroundingRectangle(final_formula, color=YELLOW, buff=0.2)
        self.play(Create(box))
        self.wait(2)
        
        # Final animation - fade everything except the title and show a thank you message
        thank_you = Text("Thanks for watching!", font_size=36, color=BLUE)
        thank_you.next_to(title, DOWN, buff=1.0)
        
        self.play(
            FadeOut(bullet_points),
            FadeOut(final_formula),
            FadeOut(box),
            Write(thank_you)
        )
        self.wait(3)
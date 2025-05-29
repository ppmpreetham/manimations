from manim import *
import numpy as np

class QLearning(Scene):
    def construct(self):
        BLUE = "#3498db"
        ORANGE = "#e67e22"
        GREEN = "#2ecc71"
        PURPLE = "#9b59b6"
        
        # Title
        title = Text("Q-Learning Algorithm", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Q-table visualization
        table_title = Text("Q-Table", font_size=24, color=BLUE)
        table_title.move_to(UP * 2 + LEFT * 4)
        
        # Create a simple Q-table
        states = ["S1", "S2", "S3"]
        actions = ["↑", "↓", "←", "→"]
        
        # Table headers
        headers = VGroup()
        state_header = Text("State", font_size=16, color=WHITE)
        state_header.move_to(LEFT * 5 + UP * 1)
        headers.add(state_header)
        
        for i, action in enumerate(actions):
            action_header = Text(action, font_size=16, color=WHITE)
            action_header.move_to(LEFT * 3.5 + i * 0.8 * RIGHT + UP * 1)
            headers.add(action_header)
        
        # Q-values (initially random, will update)
        q_values = np.random.uniform(-0.5, 0.5, (3, 4))
        q_texts = VGroup()
        
        for i, state in enumerate(states):
            state_text = Text(state, font_size=16, color=WHITE)
            state_text.move_to(LEFT * 5 + (0.5 - i * 0.5) * UP)
            q_texts.add(state_text)
            
            for j in range(4):
                q_val = Text(f"{q_values[i][j]:.1f}", font_size=14, color=WHITE)
                q_val.move_to(LEFT * 3.5 + j * 0.8 * RIGHT + (0.5 - i * 0.5) * UP)
                q_texts.add(q_val)
        
        self.play(Write(table_title))
        self.play(Write(headers))
        self.play(Write(q_texts))
        
        # Q-learning update equation
        equation = MathTex(
            r"Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + \gamma \max_{a'} Q(s',a') - Q(s,a) \right]",
            font_size=24,
            color=PURPLE
        )
        equation.to_edge(DOWN)
        self.play(Write(equation))
        
        # Highlight parts of equation
        alpha_box = SurroundingRectangle(equation[0][13:15], color=ORANGE)
        alpha_label = Text("Learning Rate", font_size=16, color=ORANGE)
        alpha_label.next_to(alpha_box, UP)
        
        gamma_box = SurroundingRectangle(equation[0][19:21], color=GREEN)
        gamma_label = Text("Discount Factor", font_size=16, color=GREEN)
        gamma_label.next_to(gamma_box, DOWN)
        
        self.play(Create(alpha_box), Write(alpha_label))
        self.wait(1)
        self.play(Create(gamma_box), Write(gamma_label))
        self.wait(1)
        
        # Animate Q-value update
        # Highlight one Q-value
        highlight_rect = Rectangle(width=0.7, height=0.4, color=YELLOW, stroke_width=3)
        highlight_rect.move_to(LEFT * 3.5 + 2 * 0.8 * RIGHT + 0.5 * UP)
        
        self.play(Create(highlight_rect))
        
        # Show update
        old_val = q_values[0][2]
        new_val = old_val + 0.1 * (1.0 + 0.9 * 0.5 - old_val)  # Example update
        
        # Animate the change
        self.play(
            q_texts[6].animate.set_color(YELLOW),  # Highlight changing value
            run_time=1
        )
        
        new_text = Text(f"{new_val:.1f}", font_size=14, color=YELLOW)
        new_text.move_to(q_texts[6].get_center())
        
        self.play(Transform(q_texts[6], new_text))
        self.wait(2)
from manim import *
import numpy as np

class PolicyGradient(Scene):
    def construct(self):
        BLUE = "#3498db"
        ORANGE = "#e67e22"
        GREEN = "#2ecc71"
        PURPLE = "#9b59b6"
        
        # Title
        title = Text("Policy Gradient Methods", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Policy as probability distribution
        policy_title = Text("Policy π(a|s)", font_size=24, color=BLUE)
        policy_title.move_to(UP * 2)
        self.play(Write(policy_title))
        
        # Create action probability bars
        actions = ["↑", "↓", "←", "→"]
        probabilities = [0.1, 0.2, 0.3, 0.4]  # Initial policy
        
        bars = VGroup()
        prob_texts = VGroup()
        
        for i, (action, prob) in enumerate(zip(actions, probabilities)):
            # Action label
            action_text = Text(action, font_size=24, color=WHITE)
            action_text.move_to(LEFT * 3 + i * 1.5 * RIGHT + DOWN * 0.5)
            
            # Probability bar
            bar = Rectangle(width=0.8, height=prob * 3, color=BLUE, fill_opacity=0.7)
            bar.move_to(action_text.get_center() + UP * (prob * 1.5))
            
            # Probability text
            prob_text = Text(f"{prob:.1f}", font_size=16, color=WHITE)
            prob_text.next_to(bar, UP)
            
            bars.add(VGroup(action_text, bar))
            prob_texts.add(prob_text)
        
        self.play(Create(bars))
        self.play(Write(prob_texts))
        
        # Show policy update
        update_title = Text("Policy Update", font_size=20, color=GREEN)
        update_title.to_edge(LEFT).shift(DOWN * 2)
        self.play(Write(update_title))
        
        # Gradient ascent equation
        equation = MathTex(
            r"\theta \leftarrow \theta + \alpha \nabla_\theta J(\theta)",
            font_size=24,
            color=PURPLE
        )
        equation.next_to(update_title, DOWN)
        self.play(Write(equation))
        
        # Simulate policy improvement
        # Let's say action "→" gets positive reward, so we increase its probability
        new_probabilities = [0.05, 0.15, 0.2, 0.6]  # Shift probability to →
        
        improvement_text = Text("After positive reward for →", font_size=16, color=GREEN)
        improvement_text.next_to(equation, DOWN)
        self.play(Write(improvement_text))
        
        # Animate the probability change
        for i, (old_prob, new_prob) in enumerate(zip(probabilities, new_probabilities)):
            # Update bar height
            new_bar = Rectangle(width=0.8, height=new_prob * 3, color=BLUE, fill_opacity=0.7)
            new_bar.move_to(bars[i][0].get_center() + UP * (new_prob * 1.5))
            
            # Update probability text
            new_prob_text = Text(f"{new_prob:.1f}", font_size=16, color=WHITE)
            new_prob_text.next_to(new_bar, UP)
            
            self.play(
                Transform(bars[i][1], new_bar),
                Transform(prob_texts[i], new_prob_text),
                run_time=1
            )
        
        # Highlight the increased probability
        highlight = SurroundingRectangle(bars[3], color=GREEN, stroke_width=4)
        self.play(Create(highlight))
        
        explanation = Text("Higher probability for rewarded action", 
                         font_size=16, color=GREEN)
        explanation.next_to(highlight, RIGHT)
        self.play(Write(explanation))
        
        self.wait(3)
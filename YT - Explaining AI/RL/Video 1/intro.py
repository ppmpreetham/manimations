from manim import *

class ReinforcementLearningIntro(Scene):
    def construct(self):
        # Create states as circles
        state_A = Circle(radius=0.5, color=BLUE, fill_opacity=0.5).shift(LEFT*2)
        state_B = Circle(radius=0.5, color=GREEN, fill_opacity=0.5).shift(RIGHT*2)
        
        # Labels for states
        label_A = Text("S₀", font_size=36).move_to(state_A.get_center())
        label_B = Text("S₁", font_size=36).move_to(state_B.get_center())
        
        # Arrow for transition
        arrow = Arrow(start=state_A.get_right(), end=state_B.get_left(), color=YELLOW)
        
        # Reward label
        reward = Text("+1", font_size=24, color=YELLOW).next_to(arrow, UP)
        
        # Title
        title = Text("Reinforcement Learning", font_size=48).to_edge(UP)
        
        self.add(title)
        
        # Create the animation sequence
        self.play(Write(title))
        self.play(Create(state_A), Create(label_A))
        self.wait(0.5)
        self.play(Create(state_B), Create(label_B))
        self.wait(0.5)
        
        # Show action and reward
        self.play(Create(arrow))
        self.play(Write(reward))
        
        # Highlight state transition
        self.play(state_A.animate.set_fill(BLUE, opacity=0.2))
        self.play(state_B.animate.set_fill(GREEN, opacity=0.8))
        
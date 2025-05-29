from manim import *
import numpy as np

class RewardsAndValues(Scene):
    def construct(self):
        BLUE = "#3498db"
        GREEN = "#2ecc71"
        RED = "#e74c3c"
        YELLOW = "#f1c40f"
        
        # Title
        title = Text("Rewards & Value Function", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create simplified 3x3 grid
        grid_size = 3
        cell_size = 1.2
        
        grid = VGroup()
        value_texts = VGroup()
        
        # Value function values (example)
        values = np.array([
            [0.1, 0.3, 1.0],   # Top row
            [0.05, -1.0, 0.7], # Middle row  
            [0.02, 0.1, 0.5]   # Bottom row
        ])
        
        for i in range(grid_size):
            for j in range(grid_size):
                cell = Square(side_length=cell_size, color=WHITE, stroke_width=2)
                cell.move_to(np.array([j * cell_size - cell_size, 
                                     cell_size - i * cell_size, 0]))
                
                # Color based on value
                value = values[i][j]
                if value > 0.5:
                    cell.set_fill(GREEN, opacity=value * 0.7)
                elif value < 0:
                    cell.set_fill(RED, opacity=abs(value) * 0.7)
                else:
                    cell.set_fill(YELLOW, opacity=value * 0.7)
                
                grid.add(cell)
                
                # Add value text
                value_text = Text(f"{value:.1f}", font_size=20, color=BLACK)
                value_text.move_to(cell.get_center())
                value_texts.add(value_text)
        
        self.play(Create(grid))
        self.play(Write(value_texts))
        
        # Add goal marker
        goal_star = Star(5, outer_radius=0.3, color=YELLOW, fill_opacity=1)
        goal_star.move_to(np.array([1.2, 1.2, 0]))  # Top right
        self.play(Create(goal_star))
        
        # Add obstacle marker
        obstacle_x = Text("X", font_size=30, color=WHITE)
        obstacle_x.move_to(np.array([0, 0, 0]))  # Center
        self.play(Write(obstacle_x))
        
        # Explanation
        explanation = VGroup(
            Text("Value Function V(s):", font_size=24, color=BLUE),
            Text("• Green: High value (close to goal)", font_size=18, color=GREEN),
            Text("• Red: Negative value (obstacle)", font_size=18, color=RED),
            Text("• Yellow: Low value (far from goal)", font_size=18, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT)
        explanation.to_edge(RIGHT)
        
        self.play(Write(explanation))
        self.wait(3)
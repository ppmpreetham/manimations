from manim import *
import numpy as np

class GridWorld(Scene):
    def construct(self):
        BLUE = "#3498db"
        ORANGE = "#e67e22"
        GREEN = "#2ecc71"
        RED = "#e74c3c"
        
        # Create grid
        grid_size = 4
        cell_size = 1
        
        grid = VGroup()
        for i in range(grid_size):
            for j in range(grid_size):
                cell = Square(side_length=cell_size, color=WHITE, stroke_width=2)
                cell.move_to(np.array([j * cell_size - 1.5, 1.5 - i * cell_size, 0]))
                grid.add(cell)
        
        self.play(Create(grid))
        
        # Add goal state
        goal = Square(side_length=cell_size, color=GREEN, fill_opacity=0.7)
        goal.move_to(np.array([1.5, -1.5, 0]))  # Bottom right
        goal_text = Text("GOAL", font_size=20, color=WHITE)
        goal_text.move_to(goal.get_center())
        
        # Add obstacle
        obstacle = Square(side_length=cell_size, color=RED, fill_opacity=0.7)
        obstacle.move_to(np.array([0.5, 0.5, 0]))  # Middle
        obstacle_text = Text("X", font_size=30, color=WHITE)
        obstacle_text.move_to(obstacle.get_center())
        
        # Add agent
        agent = Circle(radius=0.3, color=ORANGE, fill_opacity=0.9)
        agent.move_to(np.array([-1.5, 1.5, 0]))  # Top left
        
        self.play(FadeIn(goal), Write(goal_text))
        self.play(FadeIn(obstacle), Write(obstacle_text))
        self.play(Create(agent))
        
        # Show random exploration
        title = Text("Random Exploration", font_size=32, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Random moves
        positions = [
            np.array([-1.5, 1.5, 0]),   # Start
            np.array([-0.5, 1.5, 0]),  # Right
            np.array([-0.5, 0.5, 0]),  # Down (blocked)
            np.array([-0.5, 1.5, 0]),  # Back up
            np.array([-1.5, 1.5, 0]),  # Left
            np.array([-1.5, 0.5, 0]),  # Down
            np.array([-0.5, 0.5, 0]),  # Right (blocked)
            np.array([-1.5, 0.5, 0]),  # Back
        ]
        
        for i, pos in enumerate(positions[1:], 1):
            if np.array_equal(pos, np.array([-0.5, 0.5, 0])):  # Blocked position
                # Show collision
                self.play(agent.animate.move_to(pos), run_time=0.3)
                self.play(agent.animate.set_fill(RED), run_time=0.2)
                self.play(agent.animate.set_fill(ORANGE), 
                         agent.animate.move_to(positions[i-1]), run_time=0.3)
            else:
                self.play(agent.animate.move_to(pos), run_time=0.5)
        
        self.wait(2)
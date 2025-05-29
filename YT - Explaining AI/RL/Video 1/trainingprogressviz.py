from manim import *
import numpy as np

class TrainingProgress(Scene):
    def construct(self):
        BLUE = "#3498db"
        GREEN = "#2ecc71"
        ORANGE = "#e67e22"
        RED = "#e74c3c"
        
        # Title
        title = Text("RL Training Progress", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create axes for reward curve
        axes = Axes(
            x_range=[0, 100, 20],
            y_range=[-50, 50, 25],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": np.arange(0, 101, 20)},
            y_axis_config={"numbers_to_include": np.arange(-50, 51, 25)},
        )
        
        axes_labels = axes.get_axis_labels(
            x_label="Episode", y_label="Reward"
        )
        
        self.play(Create(axes), Write(axes_labels))
        
        # Generate training curve data (typical RL learning curve)
        episodes = np.linspace(0, 100, 100)
        # Noisy improvement curve
        base_curve = 40 * (1 - np.exp(-episodes / 30)) - 40
        noise = np.random.normal(0, 8, 100)
        rewards = base_curve + noise
        
        # Create the curve progressively
        points = [axes.coords_to_point(ep, reward) for ep, reward in zip(episodes, rewards)]
        
        # Draw curve progressively
        curve = VMobject()
        curve.set_points_as_corners([points[0], points[0]])
        curve.set_stroke(GREEN, width=3)
        
        self.play(Create(curve))
        
        # Animate curve growth
        for i in range(1, len(points), 2):  # Every other point for speed
            new_curve = VMobject()
            new_curve.set_points_as_corners(points[:i+1])
            new_curve.set_stroke(GREEN, width=3)
            self.play(Transform(curve, new_curve), run_time=0.1)
        
        # Add phases annotation
        phases = VGroup(
            Text("Exploration", font_size=16, color=ORANGE),
            Text("Learning", font_size=16, color=BLUE),
            Text("Convergence", font_size=16, color=GREEN)
        )
        
        # Position phase labels
        phases[0].move_to(axes.coords_to_point(15, -30))
        phases[1].move_to(axes.coords_to_point(50, 0))
        phases[2].move_to(axes.coords_to_point(85, 30))
        
        # Draw phase regions
        exploration_region = Rectangle(
            width=2.5, height=4, color=ORANGE, fill_opacity=0.2
        ).move_to(axes.coords_to_point(15, 0))
        
        learning_region = Rectangle(
            width=3, height=4, color=BLUE, fill_opacity=0.2
        ).move_to(axes.coords_to_point(50, 0))
        
        convergence_region = Rectangle(
            width=2.5, height=4, color=GREEN, fill_opacity=0.2
        ).move_to(axes.coords_to_point(85, 0))
        
        self.play(
            FadeIn(exploration_region),
            FadeIn(learning_region),
            FadeIn(convergence_region)
        )
        self.play(Write(phases))
        
        # Add moving average line
        window = 10
        moving_avg = np.convolve(rewards, np.ones(window)/window, mode='valid')
        avg_episodes = episodes[window-1:]
        avg_points = [axes.coords_to_point(ep, avg) for ep, avg in zip(avg_episodes, moving_avg)]
        
        avg_curve = VMobject()
        avg_curve.set_points_as_corners(avg_points)
        avg_curve.set_stroke(RED, width=4)
        
        avg_label = Text("Moving Average", font_size=16, color=RED)
        avg_label.to_edge(RIGHT).shift(UP * 2)
        
        self.play(Create(avg_curve), Write(avg_label))
        
        # Final summary
        summary = VGroup(
            Text("Key Observations:", font_size=18, color=WHITE),
            Text("• High variance early (exploration)", font_size=14, color=ORANGE),
            Text("• Gradual improvement (learning)", font_size=14, color=BLUE),
            Text("• Stabilization (convergence)", font_size=14, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT)
        summary.to_edge(DOWN)
        
        self.play(Write(summary))
        self.wait(3)
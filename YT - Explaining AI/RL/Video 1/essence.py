from manim import *
import numpy as np

class RLEssenceTutorial(Scene):
    def construct(self):
        # 3b1b style colors
        BLUE = "#3498db"
        ORANGE = "#e67e22"
        GREEN = "#2ecc71"
        PURPLE = "#9b59b6"
        RED = "#e74c3c"
        YELLOW = "#f1c40f"
        GRAY = "#7f8c8d"
        
        # ========== PART 1: Hook with Real-World Examples ==========
        self.show_real_world_examples()
        self.wait(2)
        self.clear()
        
        # ========== PART 2: What is RL? ==========
        self.show_rl_definition()
        self.wait(2)
        self.clear()
        
        # ========== PART 3: Core Components ==========
        self.show_core_components()
        self.wait(2)
        self.clear()
        
        # ========== PART 4: Simple Example - Baby Learning to Walk ==========
        self.show_baby_walking_example()
        self.wait(2)
        self.clear()
        
        # ========== PART 5: Dog Training Example ==========
        self.show_dog_training_example()
        self.wait(2)
        self.clear()
        
        # ========== PART 6: Game Playing Example ==========
        self.show_game_playing_example()
        self.wait(2)
        self.clear()
        
        # ========== PART 7: The Learning Loop ==========
        self.show_learning_loop()
        self.wait(2)
        self.clear()
        
        # ========== PART 8: Key Insights ==========
        self.show_key_insights()
        self.wait(3)

    def show_real_world_examples(self):
        BLUE = "#3498db"
        GREEN = "#2ecc71"
        ORANGE = "#e67e22"
        
        # Title
        title = Text("Reinforcement Learning is Everywhere", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        
        # Examples grid
        examples = [
            ("🎮", "Game AI", "AlphaGo, Chess, Dota 2"),
            ("🚗", "Self-Driving Cars", "Navigation, Parking"),
            ("🏭", "Robotics", "Assembly, Manipulation"),
            ("💰", "Finance", "Trading, Portfolio Management"),
            ("🏥", "Healthcare", "Drug Discovery, Treatment"),
            ("🎯", "Recommendation", "Netflix, YouTube, Amazon")
        ]
        
        example_groups = VGroup()
        
        for i, (emoji, title_text, desc) in enumerate(examples):
            row = i // 3
            col = i % 3
            
            # Position
            pos = np.array([col * 4 - 4, 1 - row * 2.5, 0])
            
            # Emoji (large)
            emoji_text = Text(emoji, font_size=60)
            emoji_text.move_to(pos + UP * 0.5)
            
            # Title
            title_obj = Text(title_text, font_size=20, color=GREEN)
            title_obj.move_to(pos)
            
            # Description
            desc_obj = Text(desc, font_size=14, color=ORANGE)
            desc_obj.move_to(pos + DOWN * 0.5)
            
            group = VGroup(emoji_text, title_obj, desc_obj)
            example_groups.add(group)
        
        # Animate examples appearing
        self.play(FadeOut(title))
        for group in example_groups:
            self.play(FadeIn(group), run_time=0.5)
        
        # Highlight the pattern
        pattern_text = Text("What do they all have in common?", font_size=32, color=BLUE)
        pattern_text.to_edge(DOWN)
        self.play(Write(pattern_text))
        
        self.wait(2)

    def show_rl_definition(self):
        BLUE = "#3498db"
        GREEN = "#2ecc71"
        ORANGE = "#e67e22"
        PURPLE = "#9b59b6"
        
        # Main title
        title = Text("Reinforcement Learning", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Definition
        definition = VGroup(
            Text("Learning through", font_size=32, color=GREEN),
            Text("Trial and Error", font_size=40, color=ORANGE, weight=BOLD),
            Text("with Rewards and Punishments", font_size=24, color=PURPLE)
        ).arrange(DOWN)
        
        self.play(Write(definition[0]))
        self.play(Write(definition[1]))
        self.play(Write(definition[2]))
        
        # Comparison with other learning types
        comparison_title = Text("How is it different?", font_size=24, color=BLUE)
        comparison_title.move_to(DOWN * 1.5)
        self.play(Write(comparison_title))
        
        # Three columns
        supervised = VGroup(
            Text("Supervised Learning", font_size=18, color=GREEN),
            Text("Learn from examples", font_size=14, color=WHITE),
            Text("Teacher provides", font_size=14, color=WHITE),
            Text("correct answers", font_size=14, color=WHITE)
        ).arrange(DOWN)
        supervised.move_to(LEFT * 4 + DOWN * 3)
        
        unsupervised = VGroup(
            Text("Unsupervised Learning", font_size=18, color=ORANGE),
            Text("Find hidden patterns", font_size=14, color=WHITE),
            Text("No teacher,", font_size=14, color=WHITE),
            Text("discover structure", font_size=14, color=WHITE)
        ).arrange(DOWN)
        unsupervised.move_to(DOWN * 3)
        
        reinforcement = VGroup(
            Text("Reinforcement Learning", font_size=18, color=PURPLE),
            Text("Learn from experience", font_size=14, color=WHITE),
            Text("Environment provides", font_size=14, color=WHITE),
            Text("rewards/punishments", font_size=14, color=WHITE)
        ).arrange(DOWN)
        reinforcement.move_to(RIGHT * 4 + DOWN * 3)
        
        self.play(Write(supervised))
        self.play(Write(unsupervised))
        self.play(Write(reinforcement))
        
        # Highlight RL
        highlight = SurroundingRectangle(reinforcement, color=PURPLE, stroke_width=3)
        self.play(Create(highlight))
        
        self.wait(2)

    def show_core_components(self):
        BLUE = "#3498db"
        ORANGE = "#e67e22"
        GREEN = "#2ecc71"
        YELLOW = "#f1c40f"
        PURPLE = "#9b59b6"
        
        title = Text("The RL Framework", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Large environment box
        env_box = RoundedRectangle(width=8, height=5, color=BLUE, corner_radius=0.3)
        env_box.set_fill(BLUE, opacity=0.1)
        env_label = Text("ENVIRONMENT", font_size=24, color=BLUE, weight=BOLD)
        env_label.move_to(env_box.get_top() + DOWN * 0.5)
        
        # Agent circle (larger and more prominent)
        agent = Circle(radius=0.8, color=ORANGE)
        agent.set_fill(ORANGE, opacity=0.8)
        agent.move_to(env_box.get_center() + LEFT * 2.5)
        agent_label = Text("AGENT", font_size=20, color=WHITE, weight=BOLD)
        agent_label.move_to(agent.get_center())
        
        self.play(Create(env_box), Write(env_label))
        self.play(Create(agent), Write(agent_label))
        
        # Actions (multiple arrows for emphasis)
        action_arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                agent.get_right() + UP * (i-1) * 0.3,
                agent.get_right() + RIGHT * 2 + UP * (i-1) * 0.3,
                color=GREEN, stroke_width=8
            )
            action_arrows.add(arrow)
        
        action_label = Text("ACTIONS", font_size=20, color=GREEN, weight=BOLD)
        action_label.next_to(action_arrows, UP)
        
        # Examples of actions
        action_examples = VGroup(
            Text("• Move left/right", font_size=14, color=GREEN),
            Text("• Buy/sell stock", font_size=14, color=GREEN),
            Text("• Turn steering wheel", font_size=14, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT)
        action_examples.next_to(action_label, DOWN)
        
        self.play(Create(action_arrows), Write(action_label))
        self.play(Write(action_examples))
        
        # States (curved arrow from environment to agent)
        state_curve = CurvedArrow(
            env_box.get_center() + RIGHT * 1.5 + UP * 1,
            agent.get_top() + RIGHT * 0.3,
            color=YELLOW, stroke_width=8
        )
        state_label = Text("STATE", font_size=20, color=YELLOW, weight=BOLD)
        state_label.next_to(state_curve, UP)
        
        # State examples
        state_examples = VGroup(
            Text("• Player position", font_size=14, color=YELLOW),
            Text("• Stock prices", font_size=14, color=YELLOW),
            Text("• Car speed & location", font_size=14, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT)
        state_examples.next_to(state_label, DOWN)
        
        self.play(Create(state_curve), Write(state_label))
        self.play(Write(state_examples))
        
        # Rewards (curved arrow back to agent)
        reward_curve = CurvedArrow(
            env_box.get_center() + RIGHT * 1.5 + DOWN * 1,
            agent.get_bottom() + RIGHT * 0.3,
            color=PURPLE, stroke_width=8
        )
        reward_label = Text("REWARD", font_size=20, color=PURPLE, weight=BOLD)
        reward_label.next_to(reward_curve, DOWN)
        
        # Reward examples
        reward_examples = VGroup(
            Text("• +100 for winning", font_size=14, color=PURPLE),
            Text("• +$1000 profit", font_size=14, color=PURPLE),
            Text("• -10 for crash", font_size=14, color=PURPLE)
        ).arrange(DOWN, aligned_edge=LEFT)
        reward_examples.next_to(reward_label, UP)
        
        self.play(Create(reward_curve), Write(reward_label))
        self.play(Write(reward_examples))
        
        # Animate the interaction cycle
        self.wait(1)
        cycle_text = Text("The Learning Cycle", font_size=24, color=WHITE)
        cycle_text.to_edge(RIGHT).shift(DOWN * 2)
        self.play(Write(cycle_text))
        
        # Pulse the arrows in sequence
        for _ in range(3):
            self.play(action_arrows.animate.set_stroke(width=12), run_time=0.4)
            self.play(action_arrows.animate.set_stroke(width=8), run_time=0.2)
            self.play(state_curve.animate.set_stroke(width=12), run_time=0.4)
            self.play(state_curve.animate.set_stroke(width=8), run_time=0.2)
            self.play(reward_curve.animate.set_stroke(width=12), run_time=0.4)
            self.play(reward_curve.animate.set_stroke(width=8), run_time=0.2)
        
        self.wait(2)

    def show_baby_walking_example(self):
        BLUE = "#3498db"
        ORANGE = "#e67e22"
        GREEN = "#2ecc71"
        RED = "#e74c3c"
        
        title = Text("Example 1: Baby Learning to Walk", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Baby figure (simple stick figure)
        head = Circle(radius=0.3, color=ORANGE, fill_opacity=1)
        body = Line(ORIGIN, DOWN * 1.5, color=ORANGE, stroke_width=6)
        left_arm = Line(UP * 0.5, UP * 0.5 + LEFT * 0.7 + DOWN * 0.3, color=ORANGE, stroke_width=4)
        right_arm = Line(UP * 0.5, UP * 0.5 + RIGHT * 0.7 + DOWN * 0.3, color=ORANGE, stroke_width=4)
        left_leg = Line(DOWN * 1.5, DOWN * 1.5 + LEFT * 0.5 + DOWN * 0.8, color=ORANGE, stroke_width=4)
        right_leg = Line(DOWN * 1.5, DOWN * 1.5 + RIGHT * 0.5 + DOWN * 0.8, color=ORANGE, stroke_width=4)
        
        baby = VGroup(head, body, left_arm, right_arm, left_leg, right_leg)
        baby.move_to(LEFT * 4)
        
        # Ground line
        ground = Line(LEFT * 6, RIGHT * 6, color=GREEN, stroke_width=4)
        ground.move_to(DOWN * 3)
        
        self.play(Create(baby), Create(ground))
        
        # Attempt 1: Fall down
        fall_text = Text("Attempt 1: Try to walk", font_size=20, color=BLUE)
        fall_text.to_edge(RIGHT).shift(UP * 2)
        self.play(Write(fall_text))
        
        # Wobble and fall
        self.play(baby.animate.rotate(PI/6), run_time=0.5)
        self.play(baby.animate.rotate(-PI/3), run_time=0.5)
        self.play(baby.animate.rotate(PI/2).shift(DOWN * 0.5), run_time=0.7)
        
        # Negative reward
        sad_face = Text("😢", font_size=40)
        sad_face.next_to(baby, UP)
        reward_text = Text("Reward: -1 (fell down)", font_size=16, color=RED)
        reward_text.next_to(sad_face, RIGHT)
        
        self.play(Write(sad_face), Write(reward_text))
        self.wait(1)
        
        # Reset baby
        self.play(FadeOut(sad_face), FadeOut(reward_text), FadeOut(fall_text))
        baby.rotate(-PI/2).shift(UP * 0.5)
        self.play(baby.animate.move_to(LEFT * 4))
        
        # Attempt 2: Better balance
        better_text = Text("Attempt 50: Better balance", font_size=20, color=BLUE)
        better_text.to_edge(RIGHT).shift(UP * 2)
        self.play(Write(better_text))
        
        # Small wobble but stay upright
        self.play(baby.animate.rotate(PI/12), run_time=0.3)
        self.play(baby.animate.rotate(-PI/12), run_time=0.3)
        self.play(baby.animate.rotate(0), run_time=0.3)
        
        # Small positive reward
        neutral_face = Text("😐", font_size=40)
        neutral_face.next_to(baby, UP)
        small_reward = Text("Reward: +0.1 (stayed up)", font_size=16, color=GREEN)
        small_reward.next_to(neutral_face, RIGHT)
        
        self.play(Write(neutral_face), Write(small_reward))
        self.wait(1)
        
        # Reset again
        self.play(FadeOut(neutral_face), FadeOut(small_reward), FadeOut(better_text))
        
        # Attempt 3: First step!
        step_text = Text("Attempt 200: First step!", font_size=20, color=BLUE)
        step_text.to_edge(RIGHT).shift(UP * 2)
        self.play(Write(step_text))
        
        # Take a step forward
        self.play(baby.animate.shift(RIGHT * 1), run_time=1)
        
        # Big positive reward
        happy_face = Text("😊", font_size=40)
        happy_face.next_to(baby, UP)
        big_reward = Text("Reward: +10 (took a step!)", font_size=16, color=GREEN)
        big_reward.next_to(happy_face, RIGHT)
        
        self.play(Write(happy_face), Write(big_reward))
        
        # Learning summary
        summary = VGroup(
            Text("What the baby learned:", font_size=20, color=BLUE),
            Text("• Falling = bad (negative reward)", font_size=16, color=RED),
            Text("• Staying upright = okay (small reward)", font_size=16, color=ORANGE),
            Text("• Moving forward = great! (big reward)", font_size=16, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT)
        summary.to_edge(DOWN).shift(LEFT * 2)
        
        self.play(Write(summary))
        self.wait(3)

    def show_dog_training_example(self):
        BLUE = "#3498db"
        ORANGE = "#e67e22"
        GREEN = "#2ecc71"
        RED = "#e74c3c"
        PURPLE = "#9b59b6"
        
        title = Text("Example 2: Training a Dog", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Dog (simple representation)
        dog_body = Ellipse(width=2, height=1, color=ORANGE, fill_opacity=0.8)
        dog_head = Circle(radius=0.4, color=ORANGE, fill_opacity=0.8)
        dog_head.next_to(dog_body, RIGHT, buff=0)
        dog_tail = Arc(radius=0.5, start_angle=0, angle=PI/2, color=ORANGE, stroke_width=6)
        dog_tail.next_to(dog_body, LEFT)
        
        dog = VGroup(dog_body, dog_head, dog_tail)
        dog.move_to(LEFT * 3)
        
        # Owner (stick figure)
        owner_head = Circle(radius=0.2, color=BLUE, fill_opacity=1)
        owner_body = Line(ORIGIN, DOWN * 1, color=BLUE, stroke_width=4)
        owner_arm = Line(UP * 0.3, UP * 0.3 + RIGHT * 0.8, color=BLUE, stroke_width=4)
        owner = VGroup(owner_head, owner_body, owner_arm)
        owner.move_to(RIGHT * 3)
        
        self.play(Create(dog), Create(owner))
        
        # Command
        command_text = Text("SIT!", font_size=24, color=BLUE, weight=BOLD)
        command_text.next_to(owner, UP)
        self.play(Write(command_text))
        
        # Dog's possible actions
        actions_title = Text("Dog's Actions:", font_size=20, color=PURPLE)
        actions_title.to_edge(LEFT).shift(UP * 1)
        
        actions = VGroup(
            Text("• Sit", font_size=16, color=GREEN),
            Text("• Lie down", font_size=16, color=ORANGE),
            Text("• Run away", font_size=16, color=RED),
            Text("• Jump", font_size=16, color=ORANGE)
        ).arrange(DOWN, aligned_edge=LEFT)
        actions.next_to(actions_title, DOWN)
        
        self.play(Write(actions_title), Write(actions))
        
        # Scenario 1: Dog sits
        scenario1 = Text("Scenario 1: Dog sits", font_size=18, color=GREEN)
        scenario1.to_edge(RIGHT).shift(UP * 2)
        self.play(Write(scenario1))
        
        # Dog sits (compress vertically)
        sitting_dog = dog.copy()
        sitting_dog.scale([1, 0.6, 1])
        self.play(Transform(dog, sitting_dog))
        
        # Positive reward
        treat = Circle(radius=0.1, color=ORANGE, fill_opacity=1)
        treat.move_to(owner.get_center() + LEFT * 0.5)
        treat_path = Arc(radius=2, start_angle=PI, angle=-PI/2)
        treat_path.move_to(owner.get_center() + LEFT * 1)
        
        self.play(MoveAlongPath(treat, treat_path), run_time=1)
        
        reward1 = Text("🦴 Treat! (+10)", font_size=20, color=GREEN)
        reward1.next_to(dog, DOWN)
        self.play(Write(reward1))
        
        self.wait(1)
        self.play(FadeOut(reward1), FadeOut(treat), FadeOut(scenario1))
        
        # Reset dog
        self.play(Transform(dog, VGroup(dog_body, dog_head, dog_tail)))
        
        # Scenario 2: Dog runs away
        scenario2 = Text("Scenario 2: Dog runs away", font_size=18, color=RED)
        scenario2.to_edge(RIGHT).shift(UP * 2)
        self.play(Write(scenario2))
        
        # Dog runs
        self.play(dog.animate.shift(LEFT * 2), run_time=1)
        
        # No reward (or negative)
        no_reward = Text("No treat 😞 (0)", font_size=20, color=RED)
        no_reward.next_to(dog, DOWN)
        self.play(Write(no_reward))
        
        self.wait(1)
        
        # Learning outcome
        learning_box = Rectangle(width=8, height=2, color=BLUE, fill_opacity=0.1)
        learning_box.to_edge(DOWN)
        
        learning_text = VGroup(
            Text("Learning Outcome:", font_size=20, color=BLUE, weight=BOLD),
            Text("Dog learns: Sitting after 'SIT' command = treat", font_size=16, color=GREEN),
            Text("Running away after 'SIT' command = no treat", font_size=16, color=RED)
        ).arrange(DOWN)
        learning_text.move_to(learning_box.get_center())
        
        self.play(Create(learning_box), Write(learning_text))
        self.wait(3)

    def show_game_playing_example(self):
        BLUE = "#3498db"
        ORANGE = "#e67e22"
        GREEN = "#2ecc71"
        RED = "#e74c3c"
        YELLOW = "#f1c40f"
        
        title = Text("Example 3: AI Playing Pac-Man", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Simple Pac-Man maze
        maze_walls = VGroup()
        
        # Outer walls
        top_wall = Rectangle(width=6, height=0.2, color=BLUE, fill_opacity=1)
        top_wall.move_to(UP * 2)
        bottom_wall = Rectangle(width=6, height=0.2, color=BLUE, fill_opacity=1)
        bottom_wall.move_to(DOWN * 2)
        left_wall = Rectangle(width=0.2, height=4, color=BLUE, fill_opacity=1)
        left_wall.move_to(LEFT * 3)
        right_wall = Rectangle(width=0.2, height=4, color=BLUE, fill_opacity=1)
        right_wall.move_to(RIGHT * 3)
        
        # Inner walls
        inner_wall1 = Rectangle(width=1, height=0.2, color=BLUE, fill_opacity=1)
        inner_wall1.move_to(LEFT * 1 + UP * 0.5)
        inner_wall2 = Rectangle(width=1, height=0.2, color=BLUE, fill_opacity=1)
        inner_wall2.move_to(RIGHT * 1 + DOWN * 0.5)
        
        maze_walls.add(top_wall, bottom_wall, left_wall, right_wall, inner_wall1, inner_wall2)
        
        # Pac-Man (yellow circle)
        pacman = Circle(radius=0.2, color=YELLOW, fill_opacity=1)
        pacman.move_to(LEFT * 2 + UP * 1)
        
        # Dots
        dots = VGroup()
        dot_positions = [
            LEFT * 1 + UP * 1,
            ORIGIN + UP * 1,
            RIGHT * 1 + UP * 1,
            LEFT * 1,
            ORIGIN,
            RIGHT * 1,
            LEFT * 1 + DOWN * 1,
            ORIGIN + DOWN * 1,
            RIGHT * 1 + DOWN * 1
        ]
        
        for pos in dot_positions:
            dot = Circle(radius=0.05, color=WHITE, fill_opacity=1)
            dot.move_to(pos)
            dots.add(dot)
        
        # Ghost
        ghost_body = Rectangle(width=0.4, height=0.4, color=RED, fill_opacity=1)
        ghost_body.move_to(RIGHT * 2 + DOWN * 1)
        ghost = ghost_body
        
        self.play(Create(maze_walls))
        self.play(Create(pacman), Create(dots), Create(ghost))
        
        # Show possible actions
        actions_text = Text("Possible Actions: ↑ ↓ ← →", font_size=20, color=ORANGE)
        actions_text.to_edge(RIGHT).shift(UP * 2)
        self.play(Write(actions_text))
        
        # Action 1: Move right (collect dot)
        action1_text = Text("Action: Move Right →", font_size=16, color=GREEN)
        action1_text.to_edge(RIGHT).shift(UP * 1)
        self.play(Write(action1_text))
        
        target_dot = dots[0]  # First dot
        self.play(pacman.animate.move_to(target_dot.get_center()))
        self.play(FadeOut(target_dot))
        
        reward1_text = Text("Reward: +10 (ate dot)", font_size=16, color=GREEN)
        reward1_text.next_to(action1_text, DOWN)
        self.play(Write(reward1_text))
        
        self.wait(1)
        self.play(FadeOut(action1_text), FadeOut(reward1_text))
        
        # Action 2: Move toward ghost (bad!)
        action2_text = Text("Action: Move Down ↓", font_size=16, color=RED)
        action2_text.to_edge(RIGHT).shift(UP * 1)
        self.play(Write(action2_text))
        
        # Move toward ghost
        self.play(pacman.animate.move_to(LEFT * 1 + UP * 0.5))
        self.play(pacman.animate.move_to(LEFT * 1))
        
        # Collision effect - Fixed star creation
        explosion = RegularPolygon(n=6, color=RED, fill_opacity=0.8)
        explosion.scale(0.5)
        explosion.move_to(pacman.get_center())
        self.play(Transform(pacman, explosion))
        
        reward2_text = Text("Reward: -100 (died!)", font_size=16, color=RED)
        reward2_text.next_to(action2_text, DOWN)
        self.play(Write(reward2_text))
        
        self.wait(1)
        
        # Learning summary table
        summary_title = Text("AI Learning Summary", font_size=24, color=BLUE)
        summary_title.to_edge(DOWN).shift(UP * 2)
        
        summary_table = VGroup(
            Text("State", font_size=16, color=WHITE),
            Text("Action", font_size=16, color=WHITE),
            Text("Reward", font_size=16, color=WHITE),
            Text("Learning", font_size=16, color=WHITE),
        ).arrange(RIGHT, buff=1)
        summary_table.next_to(summary_title, DOWN)
        
        row1 = VGroup(
            Text("Near dot", font_size=14, color=GREEN),
            Text("Move to dot", font_size=14, color=GREEN),
            Text("+10", font_size=14, color=GREEN),
            Text("Good move!", font_size=14, color=GREEN),
        ).arrange(RIGHT, buff=1)
        row1.next_to(summary_table, DOWN)
        
        row2 = VGroup(
            Text("Near ghost", font_size=14, color=RED),
            Text("Move to ghost", font_size=14, color=RED),
            Text("-100", font_size=14, color=RED),
            Text("Avoid this!", font_size=14, color=RED),
        ).arrange(RIGHT, buff=1)
        row2.next_to(row1, DOWN)
        
        self.play(Write(summary_title))
        self.play(Write(summary_table))
        self.play(Write(row1))
        self.play(Write(row2))
        
        self.wait(3)

    def show_learning_loop(self):
        BLUE = "#3498db"
        ORANGE = "#e67e22"
        GREEN = "#2ecc71"
        PURPLE = "#9b59b6"
        YELLOW = "#f1c40f"
        
        title = Text("The RL Learning Loop", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create circular flow diagram
        center = ORIGIN
        radius = 2
        
        # States as circles around the loop
        positions = [
            center + radius * UP,                    # Observe
            center + radius * (RIGHT + UP) / np.sqrt(2),    # Decide  
            center + radius * RIGHT,                 # Act
            center + radius * (RIGHT + DOWN) / np.sqrt(2),  # Receive
            center + radius * DOWN,                  # Learn
            center + radius * (LEFT + DOWN) / np.sqrt(2),   # Update
            center + radius * LEFT,                  # Improve
            center + radius * (LEFT + UP) / np.sqrt(2),     # Repeat
        ]
        
        steps = [
            ("1. OBSERVE", "State", YELLOW),
            ("2. DECIDE", "Policy", ORANGE),
            ("3. ACT", "Action", GREEN),
            ("4. RECEIVE", "Reward", PURPLE),
            ("5. LEARN", "Experience", BLUE),
            ("6. UPDATE", "Knowledge", ORANGE),
            ("7. IMPROVE", "Strategy", GREEN),
            ("8. REPEAT", "Cycle", YELLOW),
        ]
        
        step_objects = VGroup()
        
        for i, ((step_name, description, color), pos) in enumerate(zip(steps, positions)):
            # Step circle
            step_circle = Circle(radius=0.5, color=color, fill_opacity=0.3)
            step_circle.move_to(pos)
            
            # Step number and name
            step_text = VGroup(
                Text(step_name, font_size=14, color=color, weight=BOLD),
                Text(description, font_size=12, color=WHITE)
            ).arrange(DOWN, buff=0.1)
            step_text.move_to(step_circle.get_center())
            
            step_group = VGroup(step_circle, step_text)
            step_objects.add(step_group)
        
        # Create arrows between steps
        arrows = VGroup()
        for i in range(len(positions)):
            start_pos = positions[i]
            end_pos = positions[(i + 1) % len(positions)]
            
            # Calculate arrow start and end points on circle circumference
            direction = (end_pos - start_pos) / np.linalg.norm(end_pos - start_pos)
            arrow_start = start_pos + 0.5 * direction
            arrow_end = end_pos - 0.5 * direction
            
            arrow = Arrow(arrow_start, arrow_end, color=WHITE, stroke_width=4)
            arrows.add(arrow)
        
        # Animate the loop
        for i, (step_obj, arrow) in enumerate(zip(step_objects, arrows)):
            self.play(Create(step_obj), run_time=0.5)
            self.play(GrowArrow(arrow), run_time=0.3)
        
        # Highlight the cycle by pulsing
        self.wait(1)
        for _ in range(2):
            for step_obj in step_objects:
                self.play(
                    step_obj[0].animate.set_stroke(width=6),
                    run_time=0.1
                )
                self.play(
                    step_obj[0].animate.set_stroke(width=2),
                    run_time=0.1
                )
        
        # Key insight
        insight_box = Rectangle(width=10, height=1.5, color=BLUE, fill_opacity=0.1)
        insight_box.to_edge(DOWN)
        
        insight_text = VGroup(
            Text("Key Insight:", font_size=20, color=BLUE, weight=BOLD),
            Text("The agent gets better over time by repeating this loop!", font_size=16, color=WHITE)
        ).arrange(DOWN)
        insight_text.move_to(insight_box.get_center())
        
        self.play(Create(insight_box), Write(insight_text))
        self.wait(3)

    def show_key_insights(self):
        BLUE = "#3498db"
        GREEN = "#2ecc71"
        ORANGE = "#e67e22"
        RED = "#e74c3c"
        PURPLE = "#9b59b6"
        YELLOW = "#f1c40f"
        
        title = Text("Key Insights About RL", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Insight 1: Trial and Error
        insight1_title = Text("1. Learning Through Trial and Error", font_size=24, color=GREEN)
        insight1_title.move_to(UP * 2)
        
        insight1_desc = VGroup(
            Text("• No teacher telling the agent what to do", font_size=16, color=WHITE),
            Text("• Agent discovers good actions by trying them", font_size=16, color=WHITE),
            Text("• Mistakes are part of learning!", font_size=16, color=ORANGE)
        ).arrange(DOWN, aligned_edge=LEFT)
        insight1_desc.next_to(insight1_title, DOWN, aligned_edge=LEFT)
        
        self.play(Write(insight1_title))
        self.play(Write(insight1_desc))
        self.wait(2)
        
        # Insight 2: Delayed Rewards
        insight2_title = Text("2. Rewards Can Be Delayed", font_size=24, color=PURPLE)
        insight2_title.next_to(insight1_desc, DOWN, buff=0.5)
        
        # Chess example visualization
        chess_example = VGroup(
            Text("Chess Example:", font_size=16, color=WHITE, weight=BOLD),
            Text("• Move piece now → No immediate reward", font_size=14, color=ORANGE),
            Text("• Many moves later → Win the game! (+100)", font_size=14, color=GREEN),
            Text("• Challenge: Which early moves helped win?", font_size=14, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT)
        chess_example.next_to(insight2_title, DOWN, aligned_edge=LEFT)
        
        self.play(Write(insight2_title))
        self.play(Write(chess_example))
        self.wait(2)
        
        # Insight 3: Exploration vs Exploitation
        insight3_title = Text("3. Explore vs Exploit Dilemma", font_size=24, color=ORANGE)
        insight3_title.next_to(chess_example, DOWN, buff=0.5)
        
        # Restaurant analogy
        restaurant_box = Rectangle(width=8, height=2, color=ORANGE, fill_opacity=0.1)
        restaurant_box.next_to(insight3_title, DOWN)
        
        restaurant_text = VGroup(
            Text("Restaurant Analogy:", font_size=16, color=WHITE, weight=BOLD),
            Text("Exploit: Keep ordering your favorite dish (known good reward)", font_size=14, color=GREEN),
            Text("Explore: Try a new dish (might be better or worse)", font_size=14, color=ORANGE),
            Text("Balance: Sometimes stick with favorites, sometimes try new things", font_size=14, color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT)
        restaurant_text.move_to(restaurant_box.get_center())
        
        self.play(Write(insight3_title))
        self.play(Create(restaurant_box), Write(restaurant_text))
        self.wait(2)
        
        # Final message
        final_box = Rectangle(width=10, height=1.5, color=BLUE, fill_opacity=0.2)
        final_box.to_edge(DOWN)
        
        final_text = VGroup(
            Text("Reinforcement Learning is everywhere around us!", font_size=20, color=BLUE, weight=BOLD),
            Text("From babies learning to walk to AI mastering games", font_size=16, color=WHITE)
        ).arrange(DOWN)
        final_text.move_to(final_box.get_center())
        
        self.play(Create(final_box), Write(final_text))
        
        # Fixed sparkle effect - using simple circles instead of invalid stars
        sparkles = VGroup()
        for _ in range(20):
            sparkle = Circle(radius=0.05, color=YELLOW, fill_opacity=0.8)
            sparkle.move_to(
                np.array([
                    np.random.uniform(-6, 6),
                    np.random.uniform(-3, 3),
                    0
                ])
            )
            sparkles.add(sparkle)
        
        self.play(FadeIn(sparkles))
        self.play(FadeOut(sparkles))
        self.wait(3)
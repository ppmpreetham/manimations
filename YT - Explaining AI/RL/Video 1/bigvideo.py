from manim import *
import numpy as np

class OpeningHook(Scene):
    def construct(self):
        # Child learning to walk with mathematical overlay
        self.camera.background_color = "#0f0f23"
        
        # Create a simple representation of learning process
        grid = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )
        
        # Child figure (simple stick figure)
        child_body = Line(ORIGIN, UP*0.8, color=WHITE, stroke_width=3)
        child_head = Circle(radius=0.15, color=WHITE).next_to(child_body, UP, buff=0.05)
        child_arms = Line(LEFT*0.3, RIGHT*0.3, color=WHITE, stroke_width=2).move_to(child_body.get_center() + UP*0.3)
        child_legs = VGroup(
            Line(ORIGIN, DOWN*0.5 + LEFT*0.2, color=WHITE, stroke_width=2),
            Line(ORIGIN, DOWN*0.5 + RIGHT*0.2, color=WHITE, stroke_width=2)
        ).move_to(child_body.get_bottom())
        
        child = VGroup(child_body, child_head, child_arms, child_legs)
        child.scale(0.8).move_to(LEFT*3)
        
        # Mathematical symbols overlay
        math_symbols = VGroup(
            MathTex(r"s", color=BLUE),
            MathTex(r"a", color=GREEN),
            MathTex(r"r", color=YELLOW),
            MathTex(r"\pi", color=RED)
        ).arrange(RIGHT, buff=0.8).move_to(RIGHT*2)
        
        # Animations
        self.add(grid)
        self.play(FadeIn(child), run_time=2)
        
        # Simulate stumbling
        for i in range(3):
            self.play(
                child.animate.rotate(15*DEGREES).shift(RIGHT*0.3 + DOWN*0.1),
                run_time=0.5
            )
            self.play(
                child.animate.rotate(-15*DEGREES).shift(UP*0.1),
                run_time=0.3
            )
            self.wait(0.2)
        
        # Transform to mathematical representation
        self.play(
            FadeIn(math_symbols),
            child.animate.scale(0.5).set_opacity(0.5),
            run_time=2
        )
        
        self.wait(3)
        
        # Final equation reveal
        main_equation = MathTex(
            r"V^{\pi}(s) = \mathbb{E}_{\pi}[G | S_0 = s]",
            color=WHITE,
            font_size=48
        ).move_to(DOWN*2)
        
        self.play(Write(main_equation), run_time=3)
        self.wait(2)

class GridWorldIntro(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create 4x4 grid
        grid_size = 4
        cell_size = 0.8
        
        # Grid lines
        grid_lines = VGroup()
        for i in range(grid_size + 1):
            # Vertical lines
            line = Line(
                start=[i*cell_size - grid_size*cell_size/2, -grid_size*cell_size/2, 0],
                end=[i*cell_size - grid_size*cell_size/2, grid_size*cell_size/2, 0],
                color=BLUE_E,
                stroke_width=2
            )
            grid_lines.add(line)
            
            # Horizontal lines
            line = Line(
                start=[-grid_size*cell_size/2, i*cell_size - grid_size*cell_size/2, 0],
                end=[grid_size*cell_size/2, i*cell_size - grid_size*cell_size/2, 0],
                color=BLUE_E,
                stroke_width=2
            )
            grid_lines.add(line)
        
        # Agent (blue dot)
        agent = Dot(color=BLUE, radius=0.15)
        agent.move_to([-grid_size*cell_size/2 + cell_size/2, -grid_size*cell_size/2 + cell_size/2, 0])
        
        # Reward squares
        goal_square = Square(side_length=cell_size*0.8, color=GREEN, fill_opacity=0.7)
        goal_square.move_to([grid_size*cell_size/2 - cell_size/2, grid_size*cell_size/2 - cell_size/2, 0])
        goal_text = Text("+10", color=WHITE, font_size=20).move_to(goal_square.get_center())
        
        penalty_square = Square(side_length=cell_size*0.8, color=RED, fill_opacity=0.7)
        penalty_square.move_to([cell_size/2, -grid_size*cell_size/2 + cell_size/2, 0])
        penalty_text = Text("-5", color=WHITE, font_size=20).move_to(penalty_square.get_center())
        
        # Build scene
        self.play(Create(grid_lines), run_time=2)
        self.play(FadeIn(agent), run_time=1)
        self.play(
            FadeIn(goal_square), Write(goal_text),
            FadeIn(penalty_square), Write(penalty_text),
            run_time=2
        )
        
        # Show possible movements
        arrows = VGroup()
        directions = [UP, DOWN, LEFT, RIGHT]
        colors = [YELLOW, YELLOW, YELLOW, YELLOW]
        
        for direction, color in zip(directions, colors):
            if self.is_valid_move(agent.get_center(), direction, cell_size, grid_size):
                arrow = Arrow(
                    start=agent.get_center(),
                    end=agent.get_center() + direction * cell_size * 0.6,
                    color=color,
                    stroke_width=3,
                    max_tip_length_to_length_ratio=0.3
                )
                arrows.add(arrow)
        
        self.play(Create(arrows), run_time=2)
        self.wait(2)
        
        # Show agent movement
        path = [RIGHT, UP, UP, RIGHT]
        total_reward = 0
        
        reward_tracker = DecimalNumber(0, color=WHITE, num_decimal_places=0)
        reward_text = Text("Total Reward: ", color=WHITE, font_size=24)
        reward_display = VGroup(reward_text, reward_tracker).arrange(RIGHT)
        reward_display.to_edge(UP)
        
        self.play(Write(reward_display))
        
        for move in path:
            self.play(FadeOut(arrows), run_time=0.5)
            new_pos = agent.get_center() + move * cell_size
            
            # Check if hitting reward/penalty
            if np.allclose(new_pos, goal_square.get_center(), atol=0.1):
                total_reward += 10
                reward_popup = Text("+10", color=GREEN, font_size=32)
            elif np.allclose(new_pos, penalty_square.get_center(), atol=0.1):
                total_reward -= 5
                reward_popup = Text("-5", color=RED, font_size=32)
            else:
                reward_popup = Text("0", color=GRAY, font_size=24)
            
            reward_popup.move_to(new_pos + UP*0.5)
            
            self.play(
                agent.animate.move_to(new_pos),
                FadeIn(reward_popup),
                reward_tracker.animate.set_value(total_reward),
                run_time=1
            )
            self.play(FadeOut(reward_popup), run_time=0.5)
            
            # Show new possible moves
            arrows = VGroup()
            for direction, color in zip(directions, colors):
                if self.is_valid_move(agent.get_center(), direction, cell_size, grid_size):
                    arrow = Arrow(
                        start=agent.get_center(),
                        end=agent.get_center() + direction * cell_size * 0.6,
                        color=color,
                        stroke_width=3,
                        max_tip_length_to_length_ratio=0.3
                    )
                    arrows.add(arrow)
            
            if len(path) > 1:  # Don't show arrows on last move
                self.play(Create(arrows), run_time=0.5)
                path = path[1:]
        
        self.wait(3)
    
    def is_valid_move(self, pos, direction, cell_size, grid_size):
        new_pos = pos + direction * cell_size
        boundary = grid_size * cell_size / 2
        return (-boundary + cell_size/2 <= new_pos[0] <= boundary - cell_size/2 and
                -boundary + cell_size/2 <= new_pos[1] <= boundary - cell_size/2)

class StatesAndActions(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Title
        title = Text("States and Actions", color=WHITE, font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Show different examples of states
        examples = VGroup()
        
        # Chess board state
        chess_squares = VGroup()
        for i in range(3):
            for j in range(3):
                color = WHITE if (i+j) % 2 == 0 else GRAY
                square = Square(side_length=0.2, color=color, fill_opacity=0.8)
                square.move_to([i*0.2 - 0.2, j*0.2 - 0.2, 0])
                chess_squares.add(square)
        
        chess_piece = Text("♔", color=BLACK, font_size=16).move_to(chess_squares[4].get_center())
        chess_example = VGroup(chess_squares, chess_piece)
        chess_label = Text("Chess Position", color=WHITE, font_size=16)
        chess_group = VGroup(chess_example, chess_label).arrange(DOWN, buff=0.3)
        
        # Robot configuration
        robot_body = Rectangle(width=0.4, height=0.6, color=BLUE, fill_opacity=0.7)
        robot_arm1 = Line(ORIGIN, RIGHT*0.3, color=RED, stroke_width=4).move_to(robot_body.get_top())
        robot_arm2 = Line(ORIGIN, UP*0.2, color=RED, stroke_width=4).move_to(robot_arm1.get_end())
        robot_example = VGroup(robot_body, robot_arm1, robot_arm2)
        robot_label = Text("Robot Joint Angles", color=WHITE, font_size=16)
        robot_group = VGroup(robot_example, robot_label).arrange(DOWN, buff=0.3)
        
        # Economic indicators
        econ_graph = VGroup()
        points = [[-0.2, -0.1, 0], [-0.1, 0.1, 0], [0, 0.05, 0], [0.1, 0.2, 0], [0.2, 0.15, 0]]
        for i in range(len(points)-1):
            line = Line(points[i], points[i+1], color=GREEN, stroke_width=3)
            econ_graph.add(line)
        
        axes = VGroup(
            Line([-0.3, -0.2, 0], [0.3, -0.2, 0], color=WHITE),
            Line([-0.3, -0.2, 0], [-0.3, 0.3, 0], color=WHITE)
        )
        econ_example = VGroup(econ_graph, axes)
        econ_label = Text("Economic State", color=WHITE, font_size=16)
        econ_group = VGroup(econ_example, econ_label).arrange(DOWN, buff=0.3)
        
        examples.add(chess_group, robot_group, econ_group)
        examples.arrange(RIGHT, buff=1.5).scale(0.8)
        examples.move_to(UP*0.5)
        
        # Animate examples
        for example in examples:
            self.play(FadeIn(example), run_time=1.5)
            self.wait(0.5)
        
        # Mathematical abstraction
        math_text = MathTex(r"s \in S", color=BLUE, font_size=48)
        math_text.move_to(DOWN*1.5)
        
        self.play(
            examples.animate.scale(0.7).set_opacity(0.5),
            Write(math_text),
            run_time=2
        )
        
        # Show actions
        action_title = Text("Actions from each state:", color=WHITE, font_size=24)
        action_title.move_to(DOWN*2.5)
        
        self.play(Write(action_title))
        
        # Action arrows
        action_arrows = VGroup()
        for example in examples:
            center = example.get_center()
            for angle in [0, PI/2, PI, 3*PI/2]:
                arrow = Arrow(
                    start=center,
                    end=center + 0.3 * np.array([np.cos(angle), np.sin(angle), 0]),
                    color=YELLOW,
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.4
                )
                action_arrows.add(arrow)
        
        self.play(Create(action_arrows), run_time=2)
        
        # Mathematical representation of actions
        action_math = MathTex(r"a \in A(s)", color=GREEN, font_size=36)
        action_math.move_to(DOWN*3.2)
        
        self.play(Write(action_math))
        self.wait(3)

class RewardsAndTransitions(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create state-action-reward diagram
        state_s = Circle(radius=0.5, color=BLUE, fill_opacity=0.3)
        state_s_label = MathTex("s", color=WHITE, font_size=32).move_to(state_s.get_center())
        state_s_group = VGroup(state_s, state_s_label).move_to(LEFT*3)
        
        action_a = Square(side_length=0.8, color=GREEN, fill_opacity=0.3)
        action_a_label = MathTex("a", color=WHITE, font_size=32).move_to(action_a.get_center())
        action_a_group = VGroup(action_a, action_a_label).move_to(ORIGIN)
        
        # Multiple possible outcomes
        outcomes = VGroup()
        rewards = ["+1", "-1", "+5"]
        next_states = ["s'_1", "s'_2", "s'_3"]
        probs = ["0.5", "0.3", "0.2"]
        
        for i, (reward, next_state, prob) in enumerate(zip(rewards, next_states, probs)):
            y_pos = 1.5 - i * 1.5
            
            # Reward
            reward_circle = Circle(radius=0.3, color=YELLOW, fill_opacity=0.5)
            reward_text = Text(reward, color=WHITE, font_size=20)
            reward_group = VGroup(reward_circle, reward_text).move_to(RIGHT*2 + UP*y_pos)
            
            # Next state
            next_state_circle = Circle(radius=0.4, color=BLUE, fill_opacity=0.3)
            next_state_text = MathTex(next_state, color=WHITE, font_size=24)
            next_state_group = VGroup(next_state_circle, next_state_text).move_to(RIGHT*4.5 + UP*y_pos)
            
            # Probability
            prob_text = Text(f"p={prob}", color=WHITE, font_size=16).move_to(RIGHT*3.25 + UP*(y_pos + 0.5))
            
            # Arrows
            arrow1 = Arrow(
                start=action_a_group.get_right(),
                end=reward_group.get_left(),
                color=WHITE,
                stroke_width=2
            )
            arrow2 = Arrow(
                start=reward_group.get_right(),
                end=next_state_group.get_left(),
                color=WHITE,
                stroke_width=2
            )
            
            outcome = VGroup(reward_group, next_state_group, prob_text, arrow1, arrow2)
            outcomes.add(outcome)
        
        # Build scene
        self.play(FadeIn(state_s_group), run_time=1)
        self.wait(0.5)
        
        # Arrow from state to action
        state_action_arrow = Arrow(
            start=state_s_group.get_right(),
            end=action_a_group.get_left(),
            color=WHITE,
            stroke_width=3
        )
        
        self.play(
            Create(state_action_arrow),
            FadeIn(action_a_group),
            run_time=1.5
        )
        self.wait(1)
        
        # Show outcomes one by one
        for outcome in outcomes:
            self.play(FadeIn(outcome), run_time=1.5)
            self.wait(0.5)
        
        # Mathematical representation
        math_eq = MathTex(
            r"P(r, s' | s, a)",
            color=WHITE,
            font_size=40
        ).move_to(DOWN*2.5)
        
        description = Text(
            "Probability of reward r and next state s', given state s and action a",
            color=GRAY,
            font_size=20
        ).move_to(DOWN*3.2)
        
        self.play(Write(math_eq), run_time=2)
        self.play(Write(description), run_time=2)
        self.wait(3)

class TrajectorySequence(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Timeline visualization
        timeline = Line(LEFT*5, RIGHT*5, color=WHITE, stroke_width=3)
        timeline.move_to(DOWN*1)
        
        # Time markers
        time_markers = VGroup()
        for i in range(6):
            marker = Line(UP*0.1, DOWN*0.1, color=WHITE).move_to(LEFT*5 + RIGHT*2*i + DOWN*1)
            time_label = MathTex(f"t_{i}", color=GRAY, font_size=16).next_to(marker, DOWN, buff=0.2)
            time_markers.add(VGroup(marker, time_label))
        
        self.play(Create(timeline))
        self.play(Create(time_markers), run_time=2)
        
        # States, actions, and rewards
        elements = VGroup()
        
        for i in range(5):
            x_pos = LEFT*4 + RIGHT*2*i
            
            # State
            state = Circle(radius=0.25, color=BLUE, fill_opacity=0.5)
            state_label = MathTex(f"s_{i}", color=WHITE, font_size=16)
            state_group = VGroup(state, state_label).move_to(x_pos + UP*1.5)
            
            # Action (if not last)
            if i < 4:
                action = Square(side_length=0.4, color=GREEN, fill_opacity=0.5)
                action_label = MathTex(f"a_{i}", color=WHITE, font_size=16)
                action_group = VGroup(action, action_label).move_to(x_pos + RIGHT*1 + UP*0.5)
                
                # Reward
                reward = Circle(radius=0.2, color=YELLOW, fill_opacity=0.5)
                reward_label = MathTex(f"r_{i+1}", color=WHITE, font_size=14)
                reward_group = VGroup(reward, reward_label).move_to(x_pos + RIGHT*2 + UP*1.5)
                
                # Arrows
                state_action_arrow = Arrow(
                    start=state_group.get_bottom(),
                    end=action_group.get_top(),
                    color=WHITE,
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.3
                )
                action_reward_arrow = Arrow(
                    start=action_group.get_right(),
                    end=reward_group.get_left(),
                    color=WHITE,
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.3
                )
                
                step_elements = VGroup(state_group, action_group, reward_group, 
                                     state_action_arrow, action_reward_arrow)
            else:
                step_elements = state_group
            
            elements.add(step_elements)
        
        # Animate sequence
        for i, element in enumerate(elements):
            if i == 0:
                self.play(FadeIn(element), run_time=1)
            else:
                # Add connecting arrow from previous reward to current state
                prev_reward = elements[i-1][-3]  # reward group from previous step
                curr_state = element[0] if isinstance(element, VGroup) else element
                
                connecting_arrow = Arrow(
                    start=prev_reward.get_right(),
                    end=curr_state.get_left(),
                    color=ORANGE,
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.3
                )
                
                self.play(
                    Create(connecting_arrow),
                    FadeIn(element),
                    run_time=1.5
                )
            self.wait(0.5)
        
        # Mathematical representation
        math_sequence = MathTex(
            r"s_0 \xrightarrow{a_0} r_1, s_1 \xrightarrow{a_1} r_2, s_2 \xrightarrow{a_2} r_3, s_3 \ldots",
            color=WHITE,
            font_size=28
        ).move_to(DOWN*3)
        
        self.play(Write(math_sequence), run_time=3)
        self.wait(3)

class PolicyVisualization(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create grid for policy visualization
        grid_size = 3
        cell_size = 1.2
        
        # Grid states
        states = VGroup()
        for i in range(grid_size):
            for j in range(grid_size):
                x = (i - grid_size//2) * cell_size
                y = (j - grid_size//2) * cell_size
                
                state_circle = Circle(radius=0.4, color=BLUE, fill_opacity=0.3)
                state_circle.move_to([x, y, 0])
                states.add(state_circle)
        
        self.play(Create(states), run_time=2)
        
        # Show policy as probability distributions
        arrows_groups = VGroup()
        
        for state in states:
            center = state.get_center()
            
            # Four possible actions (up, down, left, right)
            directions = [UP, DOWN, LEFT, RIGHT]
            probabilities = [0.4, 0.1, 0.3, 0.2]  # Example probabilities
            colors = [RED, GREEN, BLUE, YELLOW]
            
            state_arrows = VGroup()
            for direction, prob, color in zip(directions, probabilities, colors):
                # Arrow length proportional to probability
                arrow_length = prob * 0.8
                arrow = Arrow(
                    start=center,
                    end=center + direction * arrow_length,
                    color=color,
                    stroke_width=4,
                    max_tip_length_to_length_ratio=0.3
                )
                
                # Probability label
                prob_text = Text(f"{prob:.1f}", color=color, font_size=14)
                prob_text.move_to(center + direction * (arrow_length + 0.3))
                
                state_arrows.add(arrow, prob_text)
            
            arrows_groups.add(state_arrows)
        
        # Animate policy
        for arrows in arrows_groups:
            self.play(Create(arrows), run_time=1)
            self.wait(0.2)
        
        # Mathematical definition
        policy_eq = MathTex(
            r"\pi(a|s) = P(A = a | S = s)",
            color=WHITE,
            font_size=36
        ).move_to(DOWN*3)
        
        self.play(Write(policy_eq), run_time=2)
        
        # Show different policy types
        self.wait(1)
        policy_types = Text("Policy Types:", color=WHITE, font_size=24).move_to(UP*3)
        
        random_policy = Text("• Random: Equal probability for all actions", 
                           color=GRAY, font_size=18).move_to(UP*2.5)
        deterministic_policy = Text("• Deterministic: Probability 1 for one action, 0 for others", 
                                  color=GRAY, font_size=18).move_to(UP*2.2)
        
        self.play(Write(policy_types))
        self.play(Write(random_policy))
        self.play(Write(deterministic_policy))
        self.wait(3)

class ReturnAndDiscount(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Show reward sequence
        rewards = [2, 5, -1, 3, 1, 4, 2]
        
        # Timeline
        timeline = Line(LEFT*5, RIGHT*5, color=WHITE, stroke_width=2)
        self.play(Create(timeline))
        
        # Reward visualization
        reward_objects = VGroup()
        positions = np.linspace(-4, 4, len(rewards))
        
        for i, (reward, pos) in enumerate(zip(rewards, positions)):
            # Reward circle
            color = GREEN if reward > 0 else RED
            circle = Circle(radius=0.25, color=color, fill_opacity=0.7)
            circle.move_to([pos, 1, 0])
            
            # Reward value
            reward_text = Text(str(reward), color=WHITE, font_size=16)
            reward_text.move_to(circle.get_center())
            
            # Time label
            time_text = MathTex(f"r_{i+1}", color=WHITE, font_size=14)
            time_text.move_to([pos, -0.5, 0])
            
            reward_group = VGroup(circle, reward_text, time_text)
            reward_objects.add(reward_group)
        
        # Animate rewards appearing
        for reward_obj in reward_objects:
            self.play(FadeIn(reward_obj), run_time=0.5)
        
        # Simple sum first
        simple_sum = MathTex(
            r"G = r_1 + r_2 + r_3 + r_4 + \ldots",
            color=WHITE,
            font_size=32
        ).move_to(DOWN*2)
        
        self.play(Write(simple_sum))
        self.wait(2)
        
        # Show the problem with infinite sums
        infinity_concern = Text("What if the sequence never ends?", 
                              color=YELLOW, font_size=24).move_to(DOWN*2.8)
        
        self.play(Write(infinity_concern))
        self.wait(2)
        
        # Introduce discount factor
        self.play(FadeOut(simple_sum), FadeOut(infinity_concern))
        
        discount_eq = MathTex(
            r"G = r_1 + \gamma r_2 + \gamma^2 r_3 + \gamma^3 r_4 + \ldots",
            color=WHITE,
            font_size=32
        ).move_to(DOWN*2)
        
        self.play(Write(discount_eq))
        
        # Show discount factor values
        gamma_text = Text("γ (discount factor): 0 ≤ γ ≤ 1", 
                         color=BLUE, font_size=24).move_to(DOWN*2.8)
        
        self.play(Write(gamma_text))
        
        # Visual representation of discounting
        gamma_value = 0.8
        discounted_rewards = VGroup()
        
        for i, reward_obj in enumerate(reward_objects):
            # Calculate discounted value
            discounted_value = rewards[i] * (gamma_value ** i)
            
            # Show original and discounted values
            original_pos = reward_obj.get_center()
            
            # Discounted reward (smaller, faded)
            disc_circle = Circle(radius=0.25 * (gamma_value ** i), 
                               color=reward_obj[0].color, 
                               fill_opacity=0.7 * (gamma_value ** i))
            disc_circle.move_to(original_pos + DOWN*1.5)
            
            disc_text = Text(f"{discounted_value:.1f}", 
                           color=WHITE, 
                           font_size=int(16 * (gamma_value ** (i/2))))
            disc_text.move_to(disc_circle.get_center())
            
            disc_group = VGroup(disc_circle, disc_text)
            discounted_rewards.add(disc_group)
        
        # Animate discounting effect
        for i, disc_reward in enumerate(discounted_rewards):
            self.play(
                TransformFromCopy(reward_objects[i][0], disc_reward[0]),
                TransformFromCopy(reward_objects[i][1], disc_reward[1]),
                run_time=0.8
            )
        
        self.wait(3)
        
        # Show convergence property
        convergence_text = Text("Now infinite sums converge!", 
                              color=GREEN, font_size=24).move_to(DOWN*3.5)
        
        self.play(Write(convergence_text))
        self.wait(2)

class ValueFunctionReveal(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create grid world
        grid_size = 4
        cell_size = 1.0
        
        # Create states
        states = VGroup()
        state_positions = []
        
        for i in range(grid_size):
            for j in range(grid_size):
                x = (i - grid_size//2 + 0.5) * cell_size
                y = (j - grid_size//2 + 0.5) * cell_size
                
                state_circle = Circle(radius=0.3, color=BLUE, fill_opacity=0.3)
                state_circle.move_to([x, y, 0])
                states.add(state_circle)
                state_positions.append([x, y, 0])
        
        self.play(Create(states), run_time=2)
        
        # Define value function values (example)
        values = [
            [1.0, 2.5, 4.0, 5.5],
            [0.5, 1.8, 3.2, 4.8],
            [0.2, 1.2, 2.5, 4.0],
            [0.0, 0.8, 1.5, 2.8]
        ]
        
        # Value function equation
        value_eq = MathTex(
            r"V^{\pi}(s) = \mathbb{E}_{\pi}[G | S_0 = s]",
            color=WHITE,
            font_size=36
        ).move_to(UP*3)
        
        self.play(Write(value_eq))
        
        # Show value function as heat map
        value_objects = VGroup()
        max_value = max(max(row) for row in values)
        
        for i, state in enumerate(states):
            row = i // grid_size
            col = i % grid_size
            value = values[row][col]
            
            # Color intensity based on value
            intensity = value / max_value
            color = interpolate_color(BLUE, RED, intensity)
            
            # Update state color
            new_state = Circle(radius=0.35, color=color, fill_opacity=0.8)
            new_state.move_to(state.get_center())
            
            # Value text
            value_text = Text(f"{value:.1f}", color=WHITE, font_size=16)
            value_text.move_to(state.get_center())
            
            value_group = VGroup(new_state, value_text)
            value_objects.add(value_group)
        
        # Animate value function reveal
        for i, (old_state, new_value_obj) in enumerate(zip(states, value_objects)):
            self.play(
                Transform(old_state, new_value_obj[0]),
                FadeIn(new_value_obj[1]),
                run_time=0.3
            )
        
        # Explanation text
        explanation = VGroup(
            Text("Value Function Properties:", color=WHITE, font_size=24),
            Text("• Higher values = better long-term prospects", color=GRAY, font_size=18),
            Text("• Considers all future rewards from this state", color=GRAY, font_size=18),
            Text("• Depends on the policy π being followed", color=GRAY, font_size=18)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanation.move_to(DOWN*2.5)
        
        for line in explanation:
            self.play(Write(line), run_time=1)
            self.wait(0.5)
        
        self.wait(3)

class FinalConnection(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Show all components together
        title = Text("The Mathematical Framework of Learning", 
                    color=WHITE, font_size=32).move_to(UP*3.5)
        
        self.play(Write(title))
        
        # Create component boxes
        components = VGroup()
        
        # States
        states_box = Rectangle(width=2.5, height=1.5, color=BLUE)
        states_text = VGroup(
            Text("States", color=WHITE, font_size=20),
            MathTex(r"s \in S", color=BLUE, font_size=16)
        ).arrange(DOWN, buff=0.2).move_to(states_box.get_center())
        states_group = VGroup(states_box, states_text).move_to(LEFT*4 + UP*1.5)
        
        # Actions
        actions_box = Rectangle(width=2.5, height=1.5, color=GREEN)
        actions_text = VGroup(
            Text("Actions", color=WHITE, font_size=20),
            MathTex(r"a \in A(s)", color=GREEN, font_size=16)
        ).arrange(DOWN, buff=0.2).move_to(actions_box.get_center())
        actions_group = VGroup(actions_box, actions_text).move_to(LEFT*1 + UP*1.5)
        
        # Rewards
        rewards_box = Rectangle(width=2.5, height=1.5, color=YELLOW)
        rewards_text = VGroup(
            Text("Rewards", color=WHITE, font_size=20),
            MathTex(r"r \in \mathbb{R}", color=YELLOW, font_size=16)
        ).arrange(DOWN, buff=0.2).move_to(rewards_box.get_center())
        rewards_group = VGroup(rewards_box, rewards_text).move_to(RIGHT*2 + UP*1.5)
        
        # Policy
        policy_box = Rectangle(width=2.5, height=1.5, color=RED)
        policy_text = VGroup(
            Text("Policy", color=WHITE, font_size=20),
            MathTex(r"\pi(a|s)", color=RED, font_size=16)
        ).arrange(DOWN, buff=0.2).move_to(policy_box.get_center())
        policy_group = VGroup(policy_box, policy_text).move_to(LEFT*4 + DOWN*0.5)
        
        # Return
        return_box = Rectangle(width=2.5, height=1.5, color=ORANGE)
        return_text = VGroup(
            Text("Return", color=WHITE, font_size=20),
            MathTex(r"G = \sum \gamma^t r_t", color=ORANGE, font_size=14)
        ).arrange(DOWN, buff=0.2).move_to(return_box.get_center())
        return_group = VGroup(return_box, return_text).move_to(LEFT*1 + DOWN*0.5)
        
        # Value Function
        value_box = Rectangle(width=2.5, height=1.5, color=PURPLE)
        value_text = VGroup(
            Text("Value Function", color=WHITE, font_size=18),
            MathTex(r"V^{\pi}(s) = \mathbb{E}[G]", color=PURPLE, font_size=14)
        ).arrange(DOWN, buff=0.2).move_to(value_box.get_center())
        value_group = VGroup(value_box, value_text).move_to(RIGHT*2 + DOWN*0.5)
        
        components.add(states_group, actions_group, rewards_group, 
                      policy_group, return_group, value_group)
        
        # Animate components
        for component in components:
            self.play(FadeIn(component), run_time=1)
            self.wait(0.3)
        
        # Show connections
        connections = VGroup()
        
        # States to Actions
        arrow1 = Arrow(states_group.get_right(), actions_group.get_left(), 
                      color=WHITE, stroke_width=2)
        connections.add(arrow1)
        
        # Actions to Rewards
        arrow2 = Arrow(actions_group.get_right(), rewards_group.get_left(), 
                      color=WHITE, stroke_width=2)
        connections.add(arrow2)
        
        # Policy influences Actions
        arrow3 = Arrow(policy_group.get_top(), actions_group.get_bottom(), 
                      color=WHITE, stroke_width=2)
        connections.add(arrow3)
        
        # Rewards to Return
        arrow4 = Arrow(rewards_group.get_bottom(), return_group.get_top(), 
                      color=WHITE, stroke_width=2)
        connections.add(arrow4)
        
        # Return to Value Function
        arrow5 = Arrow(return_group.get_right(), value_group.get_left(), 
                      color=WHITE, stroke_width=2)
        connections.add(arrow5)
        
        self.play(Create(connections), run_time=3)
        
        # Final insight
        insight = Text(
            "This framework captures the essence of rational decision-making!",
            color=GOLD,
            font_size=24
        ).move_to(DOWN*2.8)
        
        self.play(Write(insight), run_time=3)
        self.wait(3)
        
        # Tease next video
        tease = Text(
            "Next: How do we actually compute these value functions?",
            color=GRAY,
            font_size=20
        ).move_to(DOWN*3.5)
        
        self.play(Write(tease), run_time=2)
        self.wait(2)
from manim import *
import numpy as np

class ConceptualZoomOut(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Start with a single agent in a grid
        agent = Dot(color=BLUE, radius=0.15)
        grid = self.create_small_grid()
        
        self.play(FadeIn(grid), FadeIn(agent))
        self.wait(1)
        
        # Zoom out to show it's part of a larger universe
        for scale_factor in [0.7, 0.5, 0.3, 0.2]:
            # Scale down current view
            current_group = VGroup(grid, agent)
            self.play(
                current_group.animate.scale(scale_factor).move_to(ORIGIN),
                run_time=1.5
            )
            
            # Add more grids around it
            if scale_factor <= 0.5:
                surrounding_grids = VGroup()
                positions = [LEFT*3, RIGHT*3, UP*2.5, DOWN*2.5]
                for pos in positions:
                    new_grid = self.create_small_grid().scale(scale_factor).move_to(pos)
                    new_agent = Dot(color=BLUE, radius=0.15*scale_factor).move_to(pos)
                    surrounding_grids.add(new_grid, new_agent)
                
                self.play(FadeIn(surrounding_grids), run_time=1)
        
        # Add cosmic text
        universe_text = Text("The mathematical framework scales infinitely", 
                           color=GOLD, font_size=20).move_to(DOWN*3.5)
        self.play(Write(universe_text), run_time=2)
        self.wait(2)
    
    def create_small_grid(self):
        grid = VGroup()
        for i in range(4):
            # Vertical lines
            line = Line(DOWN*0.8, UP*0.8, color=BLUE_E, stroke_width=1)
            line.move_to(LEFT*1.2 + RIGHT*0.8*i)
            grid.add(line)
            # Horizontal lines  
            line = Line(LEFT*1.2, RIGHT*1.2, color=BLUE_E, stroke_width=1)
            line.move_to(DOWN*0.8 + UP*0.8*i)
            grid.add(line)
        return grid

class MathematicalBeauty(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create flowing mathematical symbols
        symbols = [
            MathTex(r"s", color=BLUE, font_size=48),
            MathTex(r"a", color=GREEN, font_size=48),
            MathTex(r"r", color=YELLOW, font_size=48),
            MathTex(r"\pi", color=RED, font_size=48),
            MathTex(r"V", color=PURPLE, font_size=48),
            MathTex(r"\mathbb{E}", color=ORANGE, font_size=48)
        ]
        
        # Arrange in a circle
        radius = 2.5
        for i, symbol in enumerate(symbols):
            angle = i * 2 * PI / len(symbols)
            symbol.move_to(radius * np.array([np.cos(angle), np.sin(angle), 0]))
        
        # Animate symbols appearing with rotation
        for symbol in symbols:
            self.play(
                FadeIn(symbol),
                symbol.animate.rotate(PI/4),
                run_time=0.8
            )
        
        # Create connecting flow lines
        flow_lines = VGroup()
        for i in range(len(symbols)):
            start_symbol = symbols[i]
            end_symbol = symbols[(i + 1) % len(symbols)]
            
            # Curved line between symbols
            line = CurvedArrow(
                start_symbol.get_center(),
                end_symbol.get_center(),
                color=WHITE,
                stroke_width=2,
                angle=PI/6
            )
            flow_lines.add(line)
        
        self.play(Create(flow_lines), run_time=3)
        
        # Center equation emerges
        center_eq = MathTex(
            r"Intelligence",
            color=GOLD,
            font_size=36
        ).move_to(ORIGIN)
        
        self.play(Write(center_eq), run_time=2)
        
        # Pulse effect
        for _ in range(3):
            self.play(
                VGroup(*symbols, flow_lines, center_eq).animate.scale(1.1),
                run_time=0.5
            )
            self.play(
                VGroup(*symbols, flow_lines, center_eq).animate.scale(1/1.1),
                run_time=0.5
            )
        
        self.wait(2)

class UncertaintyVisualization(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create probability clouds
        agent = Dot(color=BLUE, radius=0.2)
        self.add(agent)
        
        # Show multiple possible outcomes from one action
        outcomes = VGroup()
        probabilities = [0.4, 0.3, 0.2, 0.1]
        positions = [UP*2, RIGHT*2, DOWN*2, LEFT*2]
        
        for prob, pos in zip(probabilities, positions):
            # Create probability cloud
            cloud = VGroup()
            n_dots = int(prob * 50)  # Number of dots proportional to probability
            
            for _ in range(n_dots):
                dot = Dot(
                    color=YELLOW,
                    radius=0.02,
                    fill_opacity=prob
                )
                # Random position around the target
                random_offset = np.random.normal(0, 0.3, 2)
                dot.move_to(pos + random_offset[0]*RIGHT + random_offset[1]*UP)
                cloud.add(dot)
            
            outcomes.add(cloud)
            
            # Add probability label
            prob_label = Text(f"{prob:.1f}", color=WHITE, font_size=24)
            prob_label.move_to(pos + normalize(pos) * 0.5)
            outcomes.add(prob_label)
        
        # Animate uncertainty
        self.play(FadeIn(outcomes), run_time=3)
        
        # Show expected value calculation
        expected_text = MathTex(
            r"\mathbb{E}[X] = \sum p_i \cdot x_i",
            color=WHITE,
            font_size=32
        ).move_to(DOWN*3)
        
        self.play(Write(expected_text), run_time=2)
        self.wait(2)

class SequentialDecisionChain(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create chain of decisions
        chain_length = 6
        positions = [LEFT*4 + RIGHT*1.5*i for i in range(chain_length)]
        
        states = VGroup()
        actions = VGroup()
        arrows = VGroup()
        
        for i, pos in enumerate(positions):
            # State
            state = Circle(radius=0.25, color=BLUE, fill_opacity=0.7)
            state_label = MathTex(f"s_{i}", color=WHITE, font_size=14)
            state_group = VGroup(state, state_label).move_to(pos)
            states.add(state_group)
            
            # Action (except for last state)
            if i < chain_length - 1:
                action = Square(side_length=0.3, color=GREEN, fill_opacity=0.7)
                action_label = MathTex(f"a_{i}", color=WHITE, font_size=12)
                action_group = VGroup(action, action_label).move_to(pos + RIGHT*0.75)
                actions.add(action_group)
                
                # Arrows
                arrow1 = Arrow(
                    start=state_group.get_right(),
                    end=action_group.get_left(),
                    color=WHITE,
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.3
                )
                
                arrow2 = Arrow(
                    start=action_group.get_right(),
                    end=positions[i+1] + LEFT*0.25,
                    color=WHITE,
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.3
                )
                
                arrows.add(arrow1, arrow2)
        
        # Animate the chain building
        self.play(FadeIn(states[0]), run_time=0.5)
        
        for i in range(chain_length - 1):
            self.play(
                Create(arrows[2*i]),     # State to action arrow
                FadeIn(actions[i]),      # Action
                run_time=0.8
            )
            self.play(
                Create(arrows[2*i + 1]), # Action to next state arrow
                FadeIn(states[i + 1]),   # Next state
                run_time=0.8
            )
        
        # Add time dimension
        time_axis = Line(LEFT*5, RIGHT*5, color=GRAY, stroke_width=1).move_to(DOWN*2)
        time_labels = VGroup()
        for i in range(chain_length):
            label = Text(f"t={i}", color=GRAY, font_size=12)
            label.move_to(positions[i] + DOWN*2.5)
            time_labels.add(label)
        
        self.play(Create(time_axis), Write(time_labels), run_time=2)
        
        # Highlight the sequential nature
        sequential_text = Text("Each decision affects all future possibilities", 
                             color=YELLOW, font_size=18).move_to(UP*2.5)
        self.play(Write(sequential_text), run_time=2)
        self.wait(2)

class PolicyEvolution(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create a 3x3 state grid
        grid_size = 3
        cell_size = 1.0
        
        states = VGroup()
        for i in range(grid_size):
            for j in range(grid_size):
                x = (i - 1) * cell_size
                y = (j - 1) * cell_size
                
                state = Circle(radius=0.3, color=BLUE, fill_opacity=0.3)
                state.move_to([x, y, 0])
                states.add(state)
        
        self.play(Create(states), run_time=1)
        
        # Show policy evolution over time
        policies = [
            # Random policy (iteration 0)
            [(0.25, 0.25, 0.25, 0.25) for _ in range(9)],
            # Slightly better (iteration 1)
            [(0.4, 0.2, 0.2, 0.2), (0.3, 0.4, 0.15, 0.15), (0.2, 0.6, 0.1, 0.1),
             (0.3, 0.2, 0.3, 0.2), (0.25, 0.25, 0.25, 0.25), (0.15, 0.4, 0.15, 0.3),
             (0.2, 0.1, 0.6, 0.1), (0.15, 0.15, 0.4, 0.3), (0.1, 0.1, 0.6, 0.2)],
            # Much better (iteration 2)
            [(0.7, 0.1, 0.1, 0.1), (0.1, 0.7, 0.1, 0.1), (0.1, 0.8, 0.05, 0.05),
             (0.6, 0.1, 0.2, 0.1), (0.1, 0.6, 0.1, 0.2), (0.05, 0.7, 0.05, 0.2),
             (0.5, 0.05, 0.4, 0.05), (0.05, 0.05, 0.7, 0.2), (0.05, 0.05, 0.8, 0.1)]
        ]
        
        policy_arrows = VGroup()
        
        for iteration, policy in enumerate(policies):
            # Clear previous arrows
            if policy_arrows:
                self.play(FadeOut(policy_arrows), run_time=0.5)
                policy_arrows = VGroup()
            
            # Show iteration number
            iteration_text = Text(f"Policy Iteration {iteration}", 
                                color=WHITE, font_size=24).move_to(UP*2.5)
            if iteration == 0:
                self.play(Write(iteration_text))
            else:
                self.play(Transform(iteration_text, Text(f"Policy Iteration {iteration}", 
                                                       color=WHITE, font_size=24).move_to(UP*2.5)))
            
            # Create arrows for this policy
            directions = [UP, DOWN, LEFT, RIGHT]
            colors = [RED, GREEN, BLUE, YELLOW]
            
            for state_idx, state in enumerate(states):
                state_policy = policy[state_idx]
                center = state.get_center()
                
                for dir_idx, (direction, prob, color) in enumerate(zip(directions, state_policy, colors)):
                    if prob > 0.05:  # Only show significant probabilities
                        arrow_length = prob * 0.6
                        arrow = Arrow(
                            start=center,
                            end=center + direction * arrow_length,
                            color=color,
                            stroke_width=max(1, int(prob * 8)),
                            max_tip_length_to_length_ratio=0.3
                        )
                        policy_arrows.add(arrow)
            
            self.play(Create(policy_arrows), run_time=2)
            self.wait(1.5)
        
        # Final message
        final_text = Text("Policy converges to optimal behavior", 
                         color=GOLD, font_size=20).move_to(DOWN*2.5)
        self.play(Write(final_text), run_time=2)
        self.wait(2)

class StateValueHeatmap(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create grid
        grid_size = 6
        cell_size = 0.8
        
        # Define a value function (distance from goal)
        goal_pos = (4, 4)  # Goal at top-right
        values = []
        
        for i in range(grid_size):
            row = []
            for j in range(grid_size):
                # Manhattan distance from goal, inverted
                distance = abs(i - goal_pos[0]) + abs(j - goal_pos[1])
                value = max(0, 10 - distance)
                row.append(value)
            values.append(row)
        
        # Normalize values for color mapping
        max_val = max(max(row) for row in values)
        
        # Create heatmap
        heatmap = VGroup()
        for i in range(grid_size):
            for j in range(grid_size):
                x = (i - grid_size/2 + 0.5) * cell_size
                y = (j - grid_size/2 + 0.5) * cell_size
                
                value = values[i][j]
                intensity = value / max_val if max_val > 0 else 0
                
                # Color from blue (low) to red (high)
                color = interpolate_color(BLUE_D, RED, intensity)
                
                cell = Square(
                    side_length=cell_size * 0.9,
                    color=color,
                    fill_opacity=0.8,
                    stroke_width=1,
                    stroke_color=WHITE
                )
                cell.move_to([x, y, 0])
                
                # Value text
                value_text = Text(f"{value:.0f}", color=WHITE, font_size=14)
                value_text.move_to(cell.get_center())
                
                heatmap.add(cell, value_text)
        
        # Animate heatmap building
        self.play(FadeIn(heatmap), run_time=3)
        
        # Add goal marker
        goal_marker = Star(color=GOLD, fill_opacity=1).scale(0.3)
        goal_x = (goal_pos[0] - grid_size/2 + 0.5) * cell_size
        goal_y = (goal_pos[1] - grid_size/2 + 0.5) * cell_size
        goal_marker.move_to([goal_x, goal_y, 0])
        
        self.play(FadeIn(goal_marker), run_time=1)
        
        # Add explanation
        explanation = Text("Value function: Expected return from each state", 
                          color=WHITE, font_size=18).move_to(DOWN*3)
        self.play(Write(explanation), run_time=2)
        self.wait(2)

class ActionSpaceVisualization(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Central state
        central_state = Circle(radius=0.4, color=BLUE, fill_opacity=0.7)
        state_label = MathTex("s", color=WHITE, font_size=24).move_to(central_state.get_center())
        state_group = VGroup(central_state, state_label)
        
        self.play(FadeIn(state_group))
        
        # Show different types of action spaces
        
        # Discrete actions
        discrete_title = Text("Discrete Action Space", color=GREEN, font_size=20).move_to(UP*2.5)
        self.play(Write(discrete_title))
        
        discrete_actions = VGroup()
        directions = [UP, DOWN, LEFT, RIGHT, UP+LEFT, UP+RIGHT, DOWN+LEFT, DOWN+RIGHT]
        action_labels = ["↑", "↓", "←", "→", "↖", "↗", "↙", "↘"]
        
        for direction, label in zip(directions, action_labels):
            action_circle = Circle(radius=0.2, color=GREEN, fill_opacity=0.5)
            action_circle.move_to(direction * 1.5)
            action_text = Text(label, color=WHITE, font_size=16).move_to(action_circle.get_center())
            
            arrow = Arrow(
                start=central_state.get_center(),
                end=action_circle.get_center(),
                color=GREEN,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.3
            )
            
            discrete_actions.add(action_circle, action_text, arrow)
        
        self.play(Create(discrete_actions), run_time=3)
        self.wait(2)
        
        # Transform to continuous
        continuous_title = Text("Continuous Action Space", color=ORANGE, font_size=20)
        continuous_title.move_to(UP*2.5)
        
        self.play(Transform(discrete_title, continuous_title))
        
        # Create continuous action space (circle of possibilities)
        continuous_circle = Circle(radius=2, color=ORANGE, stroke_width=3, fill_opacity=0.1)
        
        # Sample some continuous actions
        sample_actions = VGroup()
        for i in range(16):
            angle = i * 2 * PI / 16
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            
            arrow = Arrow(
                start=central_state.get_center(),
                end=central_state.get_center() + direction * 1.8,
                color=ORANGE,
                stroke_width=1,
                max_tip_length_to_length_ratio=0.2
            )
            sample_actions.add(arrow)
        
        self.play(
            Transform(discrete_actions, VGroup(continuous_circle, sample_actions)),
            run_time=3
        )
        
        # Add mathematical notation
        continuous_math = MathTex(
            r"a \in \mathbb{R}^n",
            color=ORANGE,
            font_size=32
        ).move_to(DOWN*2.5)
        
        self.play(Write(continuous_math), run_time=2)
        self.wait(2)

class RewardShaping(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create a path from start to goal
        path_points = [
            LEFT*4 + DOWN*2,
            LEFT*2 + DOWN*1,
            ORIGIN,
            RIGHT*2 + UP*1,
            RIGHT*4 + UP*2
        ]
        
        # Create states along path
        states = VGroup()
        for i, point in enumerate(path_points):
            if i == 0:
                color = BLUE  # Start
                label = "Start"
            elif i == len(path_points) - 1:
                color = GOLD  # Goal
                label = "Goal"
            else:
                color = GRAY  # Intermediate
                label = f"s_{i}"
            
            state = Circle(radius=0.3, color=color, fill_opacity=0.7)
            state.move_to(point)
            text = Text(label, color=WHITE, font_size=12).move_to(point)
            states.add(VGroup(state, text))
        
        self.play(FadeIn(states), run_time=2)
        
        # Show different reward structures
        reward_scenarios = [
            # Sparse rewards
            {
                "title": "Sparse Rewards",
                "rewards": [0, 0, 0, 0, 100],
                "color": RED
            },
            # Dense rewards
            {
                "title": "Dense Rewards", 
                "rewards": [0, 10, 20, 50, 100],
                "color": GREEN
            },
            # Shaped rewards
            {
                "title": "Shaped Rewards",
                "rewards": [0, 5, 15, 35, 100],
                "color": BLUE
            }
        ]
        
        for scenario in reward_scenarios:
            title = Text(scenario["title"], color=scenario["color"], font_size=24)
            title.move_to(UP*3)
            
            reward_display = VGroup()
            for i, reward in enumerate(scenario["rewards"]):
                reward_text = Text(f"+{reward}", color=scenario["color"], font_size=16)
                reward_text.move_to(path_points[i] + DOWN*0.8)
                reward_display.add(reward_text)
            
            if scenario == reward_scenarios[0]:
                self.play(Write(title), Write(reward_display), run_time=2)
            else:
                self.play(
                    Transform(title, title),
                    Transform(reward_display, reward_display),
                    run_time=2
                )
            
            self.wait(1.5)
        
        # Add insight
        insight = Text("Reward design shapes learning behavior", 
                      color=WHITE, font_size=18).move_to(DOWN*3.5)
        self.play(Write(insight), run_time=2)
        self.wait(2)

class TemporalAbstraction(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Show hierarchical decision making
        
        # High-level decisions
        high_level = VGroup()
        high_states = ["Home", "Work", "Store", "Gym"]
        positions = [LEFT*3, LEFT*1, RIGHT*1, RIGHT*3]
        
        for state, pos in zip(high_states, positions):
            circle = Circle(radius=0.5, color=BLUE, fill_opacity=0.3)
            circle.move_to(pos + UP*2)
            text = Text(state, color=WHITE, font_size=16).move_to(circle.get_center())
            high_level.add(VGroup(circle, text))
        
        self.play(FadeIn(high_level), run_time=2)
        
        # High-level arrows
        high_arrows = VGroup()
        for i in range(len(positions) - 1):
            arrow = Arrow(
                start=positions[i] + RIGHT*0.5 + UP*2,
                end=positions[i+1] + LEFT*0.5 + UP*2,
                color=BLUE,
                stroke_width=3
            )
            high_arrows.add(arrow)
        
        self.play(Create(high_arrows), run_time=1.5)
        
        # Zoom into one high-level action (going to work)
        zoom_box = Rectangle(width=6, height=1.5, color=YELLOW, stroke_width=3)
        zoom_box.move_to(DOWN*0.5)
        
        self.play(Create(zoom_box), run_time=1)
        
        # Low-level details of "going to work"
        low_level = VGroup()
        low_actions = ["Walk to\nbus stop", "Wait for\nbus", "Board\nbus", "Exit at\nwork stop", "Walk to\noffice"]
        low_positions = [LEFT*2.5, LEFT*1.25, ORIGIN, RIGHT*1.25, RIGHT*2.5]
        
        for action, pos in zip(low_actions, low_positions):
            square = Square(side_length=0.6, color=GREEN, fill_opacity=0.3)
            square.move_to(pos + DOWN*0.5)
            text = Text(action, color=WHITE, font_size=10).move_to(square.get_center())
            low_level.add(VGroup(square, text))
        
        self.play(FadeIn(low_level), run_time=2)
        
        # Low-level arrows
        low_arrows = VGroup()
        for i in range(len(low_positions) - 1):
            arrow = Arrow(
                start=low_positions[i] + RIGHT*0.3 + DOWN*0.5,
                end=low_positions[i+1] + LEFT*0.3 + DOWN*0.5,
                color=GREEN,
                stroke_width=2
            )
            low_arrows.add(arrow)
        
        self.play(Create(low_arrows), run_time=1.5)
        
        # Add hierarchy labels
        high_label = Text("High-level Policy", color=BLUE, font_size=16).move_to(LEFT*4 + UP*2)
        low_label = Text("Low-level Policy", color=GREEN, font_size=16).move_to(LEFT*4 + DOWN*0.5)
        
        self.play(Write(high_label), Write(low_label), run_time=1.5)
        
        # Mathematical representation
        hierarchy_math = MathTex(
            r"\pi_{high}(s) \rightarrow \pi_{low}(s, g)",
            color=WHITE,
            font_size=24
        ).move_to(DOWN*2.5)
        
        self.play(Write(hierarchy_math), run_time=2)
        self.wait(2)

class ExplorationVisualization(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create a landscape with unknown rewards
        landscape = VGroup()
        
        # Create hills and valleys
        x_range = np.linspace(-5, 5, 50)
        y_values = 2 * np.sin(x_range) + 0.5 * np.sin(3 * x_range) + 0.2 * np.sin(7 * x_range)
        
        # Normalize to screen coordinates
        points = []
        for i, (x, y) in enumerate(zip(x_range, y_values)):
            points.append([x, y, 0])
        
        landscape_curve = VMobject()
        landscape_curve.set_points_as_corners(points)
        landscape_curve.set_color(WHITE)
        
        self.play(Create(landscape_curve), run_time=2)
        
        # Add fog of war (unknown regions)
        fog_regions = VGroup()
        for i in range(len(points) - 1):
            if i % 3 == 0:  # Partially reveal landscape
                continue
            
            fog_rect = Rectangle(
                width=0.3,
                height=4,
                color=GRAY,
                fill_opacity=0.7
            )
            fog_rect.move_to([points[i][0], 0, 0])
            fog_regions.add(fog_rect)
        
        self.play(FadeIn(fog_regions), run_time=1.5)
        
        # Show explorer agent
        explorer = Dot(color=BLUE, radius=0.15)
        explorer.move_to([-4, 0, 0])
        
        self.play(FadeIn(explorer), run_time=0.5)
        
        # Exploration vs exploitation
        exploitation_path = [-4, -3.5, -3, -2.5]  # Safe, known path
        exploration_path = [-2, 0, 2, 4]  # Risky, unknown path
        
        # Show exploitation first
        exploit_text = Text("Exploitation: Use known information", 
                          color=GREEN, font_size=18).move_to(UP*3)
        self.play(Write(exploit_text), run_time=1)
        
        for x in exploitation_path:
            self.play(explorer.animate.move_to([x, 0, 0]), run_time=0.8)
        
        self.wait(1)
        
        # Now show exploration
        explore_text = Text("Exploration: Discover new possibilities", 
                          color=YELLOW, font_size=18)
        explore_text.move_to(UP*3)
        
        self.play(Transform(exploit_text, explore_text), run_time=1)
        
        # Remove fog as agent explores
        for i, x in enumerate(exploration_path):
            self.play(explorer.animate.move_to([x, 0, 0]), run_time=0.8)
            
            # Remove nearby fog
            fog_to_remove = VGroup()
            for fog in fog_regions:
                if abs(fog.get_center()[0] - x) < 1:
                    fog_to_remove.add(fog)
            
            if fog_to_remove:
                self.play(FadeOut(fog_to_remove), run_time=0.5)
        
        # Balance equation
        balance_eq = MathTex(
            r"\epsilon\text{-greedy: } \begin{cases} \text{explore} & \text{with prob } \epsilon \\ \text{exploit} & \text{with prob } 1-\epsilon \end{cases}",
            color=WHITE,
            font_size=20
        ).move_to(DOWN*3)
        
        self.play(Write(balance_eq), run_time=3)
        self.wait(2)
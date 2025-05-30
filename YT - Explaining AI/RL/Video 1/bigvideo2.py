from manim import *
import numpy as np

class ChildToMathematicalAgent(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Start with child figure
        child_body = Line(ORIGIN, UP*0.8, color=WHITE, stroke_width=3)
        child_head = Circle(radius=0.15, color=WHITE).next_to(child_body, UP, buff=0.05)
        child_arms = Line(LEFT*0.3, RIGHT*0.3, color=WHITE, stroke_width=2).move_to(child_body.get_center() + UP*0.3)
        child_legs = VGroup(
            Line(ORIGIN, DOWN*0.5 + LEFT*0.2, color=WHITE, stroke_width=2),
            Line(ORIGIN, DOWN*0.5 + RIGHT*0.2, color=WHITE, stroke_width=2)
        ).move_to(child_body.get_bottom())
        
        child = VGroup(child_body, child_head, child_arms, child_legs)
        child.scale(0.8).move_to(LEFT*3)
        
        # Create grid world that will appear
        grid_size = 4
        cell_size = 0.8
        grid_lines = VGroup()
        
        for i in range(grid_size + 1):
            # Vertical lines
            line = Line(
                start=[i*cell_size - grid_size*cell_size/2, -grid_size*cell_size/2, 0],
                end=[i*cell_size - grid_size*cell_size/2, grid_size*cell_size/2, 0],
                color=BLUE_E,
                stroke_width=2,
                stroke_opacity=0
            )
            grid_lines.add(line)
            
            # Horizontal lines
            line = Line(
                start=[-grid_size*cell_size/2, i*cell_size - grid_size*cell_size/2, 0],
                end=[grid_size*cell_size/2, i*cell_size - grid_size*cell_size/2, 0],
                color=BLUE_E,
                stroke_width=2,
                stroke_opacity=0
            )
            grid_lines.add(line)
        
        grid_lines.move_to(RIGHT*2)
        
        # Mathematical agent (blue dot)
        agent = Dot(color=BLUE, radius=0.15, fill_opacity=0)
        agent.move_to(RIGHT*2 + LEFT*grid_size*cell_size/2 + RIGHT*cell_size/2 + DOWN*grid_size*cell_size/2 + UP*cell_size/2)
        
        # Start with child
        self.add(child)
        self.wait(1)
        
        # Transform child to abstract representation
        self.play(
            child.animate.scale(0.5).set_color(BLUE).set_opacity(0.7),
            run_time=2
        )
        
        # Fade in grid
        self.play(
            grid_lines.animate.set_stroke(opacity=1),
            run_time=2
        )
        
        # Child becomes mathematical agent
        self.play(
            Transform(child, agent),
            run_time=2
        )
        
        # Agent appears as blue dot
        self.play(
            agent.animate.set_fill(opacity=1),
            FadeOut(child),
            run_time=1
        )
        
        self.wait(2)

class RandomMovementWithQuestions(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create grid
        grid_size = 4
        cell_size = 0.8
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
        
        # Agent
        agent = Dot(color=BLUE, radius=0.15)
        start_pos = [-grid_size*cell_size/2 + cell_size/2, -grid_size*cell_size/2 + cell_size/2, 0]
        agent.move_to(start_pos)
        
        self.add(grid_lines, agent)
        
        # Random movements with question marks
        directions = [UP, DOWN, LEFT, RIGHT]
        question_marks = VGroup()
        
        for i in range(8):  # 8 random moves
            # Show question mark before each move
            question = Text("?", color=YELLOW, font_size=48)
            question.move_to(agent.get_center() + UP*0.8)
            
            self.play(FadeIn(question), run_time=0.5)
            
            # Random direction
            direction = np.random.choice(directions)
            new_pos = agent.get_center() + direction * cell_size
            
            # Check boundaries
            if (-grid_size*cell_size/2 + cell_size/2 <= new_pos[0] <= grid_size*cell_size/2 - cell_size/2 and
                -grid_size*cell_size/2 + cell_size/2 <= new_pos[1] <= grid_size*cell_size/2 - cell_size/2):
                
                self.play(
                    agent.animate.move_to(new_pos),
                    question.animate.set_opacity(0.3),
                    run_time=0.8
                )
            else:
                # Bounce back if hitting boundary
                self.play(
                    agent.animate.shift(direction * 0.1).shift(-direction * 0.1),
                    question.animate.set_color(RED),
                    run_time=0.8
                )
            
            question_marks.add(question)
            self.wait(0.3)
        
        # Keep some question marks visible to show confusion
        self.wait(2)

class MultipleStateExamples(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Chess board example
        chess_example = self.create_chess_board()
        chess_example.scale(0.6).move_to(LEFT*4 + UP*1)
        chess_label = Text("Chess Position", color=WHITE, font_size=18).next_to(chess_example, DOWN)
        chess_group = VGroup(chess_example, chess_label)
        
        # Robot configuration
        robot_example = self.create_robot()
        robot_example.scale(0.8).move_to(ORIGIN + UP*1)
        robot_label = Text("Robot Joint Angles", color=WHITE, font_size=18).next_to(robot_example, DOWN)
        robot_group = VGroup(robot_example, robot_label)
        
        # Economic indicators
        econ_example = self.create_economic_chart()
        econ_example.scale(0.6).move_to(RIGHT*4 + UP*1)
        econ_label = Text("Economic State", color=WHITE, font_size=18).next_to(econ_example, DOWN)
        econ_group = VGroup(econ_example, econ_label)
        
        # Animate each example appearing
        examples = [chess_group, robot_group, econ_group]
        
        for example in examples:
            self.play(FadeIn(example), run_time=1.5)
            self.wait(0.8)
        
        # Add diversity indicator
        diversity_text = Text("Different domains, same mathematical structure", 
                            color=GRAY, font_size=20).move_to(DOWN*2)
        self.play(Write(diversity_text), run_time=2)
        self.wait(2)
    
    def create_chess_board(self):
        board = VGroup()
        for i in range(4):
            for j in range(4):
                color = WHITE if (i+j) % 2 == 0 else GRAY_D
                square = Square(side_length=0.25, color=color, fill_opacity=0.8, stroke_width=1)
                square.move_to([i*0.25 - 0.375, j*0.25 - 0.375, 0])
                board.add(square)
        
        # Add a few pieces
        king = Text("♔", color=BLACK, font_size=12).move_to(board[5].get_center())
        queen = Text("♕", color=BLACK, font_size=12).move_to(board[9].get_center())
        pawn = Text("♙", color=BLACK, font_size=10).move_to(board[1].get_center())
        
        return VGroup(board, king, queen, pawn)
    
    def create_robot(self):
        # Robot body
        body = Rectangle(width=0.6, height=0.8, color=BLUE, fill_opacity=0.7, stroke_width=2)
        
        # Robot arms (articulated)
        arm1 = Line(ORIGIN, RIGHT*0.5, color=RED, stroke_width=4)
        arm1.move_to(body.get_top() + DOWN*0.2)
        
        arm2 = Line(ORIGIN, UP*0.3 + RIGHT*0.1, color=RED, stroke_width=3)
        arm2.move_to(arm1.get_end())
        
        # Joint indicators
        joint1 = Dot(color=YELLOW, radius=0.05).move_to(arm1.get_start())
        joint2 = Dot(color=YELLOW, radius=0.05).move_to(arm1.get_end())
        
        # Angle arcs
        arc1 = Arc(radius=0.15, start_angle=0, angle=PI/3, color=GREEN, stroke_width=2)
        arc1.move_to(joint1.get_center())
        
        arc2 = Arc(radius=0.1, start_angle=0, angle=PI/4, color=GREEN, stroke_width=2)
        arc2.move_to(joint2.get_center())
        
        return VGroup(body, arm1, arm2, joint1, joint2, arc1, arc2)
    
    def create_economic_chart(self):
        # Axes
        x_axis = Line(LEFT*0.6, RIGHT*0.6, color=WHITE, stroke_width=2)
        y_axis = Line(DOWN*0.5, UP*0.5, color=WHITE, stroke_width=2)
        
        # Data lines
        gdp_points = [[-0.5, -0.2, 0], [-0.2, 0.1, 0], [0.1, 0.3, 0], [0.4, 0.2, 0]]
        inflation_points = [[-0.5, 0.1, 0], [-0.2, -0.1, 0], [0.1, 0.0, 0], [0.4, 0.15, 0]]
        
        gdp_line = self.create_line_from_points(gdp_points, GREEN)
        inflation_line = self.create_line_from_points(inflation_points, RED)
        
        # Labels
        gdp_label = Text("GDP", color=GREEN, font_size=12).move_to(RIGHT*0.7 + UP*0.2)
        inflation_label = Text("Inflation", color=RED, font_size=12).move_to(RIGHT*0.7)
        
        return VGroup(x_axis, y_axis, gdp_line, inflation_line, gdp_label, inflation_label)
    
    def create_line_from_points(self, points, color):
        lines = VGroup()
        for i in range(len(points)-1):
            line = Line(points[i], points[i+1], color=color, stroke_width=2)
            lines.add(line)
        return lines

class AbstractionToGeometry(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Start with the complex examples (simplified versions)
        chess_board = Square(side_length=1, color=WHITE, fill_opacity=0.3)
        chess_pieces = VGroup(*[Dot(color=BLACK, radius=0.05) for _ in range(6)])
        chess_pieces.arrange_in_grid(rows=2, cols=3, buff=0.15).move_to(chess_board.get_center())
        chess_complex = VGroup(chess_board, chess_pieces).move_to(LEFT*4 + UP*2)
        
        robot_body = Rectangle(width=0.8, height=1, color=BLUE, fill_opacity=0.5)
        robot_arms = VGroup(
            Line(ORIGIN, RIGHT*0.4, color=RED, stroke_width=3),
            Line(ORIGIN, UP*0.3, color=RED, stroke_width=3)
        )
        robot_arms[0].move_to(robot_body.get_top())
        robot_arms[1].move_to(robot_arms[0].get_end())
        robot_complex = VGroup(robot_body, robot_arms).move_to(ORIGIN + UP*2)
        
        econ_axes = VGroup(
            Line(LEFT*0.4, RIGHT*0.4, color=WHITE),
            Line(DOWN*0.4, UP*0.4, color=WHITE)
        )
        econ_curve = VMobject()
        econ_curve.set_points_as_corners([[-0.3, -0.2, 0], [-0.1, 0.1, 0], [0.1, 0.2, 0], [0.3, 0.0, 0]])
        econ_curve.set_color(GREEN)
        econ_complex = VGroup(econ_axes, econ_curve).move_to(RIGHT*4 + UP*2)
        
        # Show complex examples
        complex_examples = VGroup(chess_complex, robot_complex, econ_complex)
        self.play(FadeIn(complex_examples), run_time=2)
        self.wait(1)
        
        # Abstract to simple geometric shapes
        simple_shapes = VGroup(
            Circle(radius=0.3, color=BLUE, fill_opacity=0.7),
            Square(side_length=0.6, color=GREEN, fill_opacity=0.7),
            Triangle(color=ORANGE, fill_opacity=0.7).scale(0.7)
        )
        
        simple_shapes[0].move_to(LEFT*4)
        simple_shapes[1].move_to(ORIGIN)
        simple_shapes[2].move_to(RIGHT*4)
        
        # Transform complex to simple
        transforms = [
            Transform(chess_complex, simple_shapes[0]),
            Transform(robot_complex, simple_shapes[1]),
            Transform(econ_complex, simple_shapes[2])
        ]
        
        self.play(*transforms, run_time=3)
        self.wait(1)
        
        # Add state labels
        state_labels = VGroup(
            MathTex("s_1", color=WHITE, font_size=24),
            MathTex("s_2", color=WHITE, font_size=24),
            MathTex("s_3", color=WHITE, font_size=24)
        )
        
        for label, shape in zip(state_labels, simple_shapes):
            label.move_to(shape.get_center() + DOWN*0.8)
        
        self.play(Write(state_labels), run_time=2)
        
        # Unifying concept
        unity_text = Text("All are just different representations of 'states'", 
                         color=GRAY, font_size=20).move_to(DOWN*2.5)
        self.play(Write(unity_text), run_time=2)
        self.wait(2)

class ElegantMathNotation(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Start with scattered geometric shapes representing states
        shapes = VGroup(
            Circle(radius=0.2, color=BLUE, fill_opacity=0.7),
            Square(side_length=0.3, color=GREEN, fill_opacity=0.7),
            Triangle(color=ORANGE, fill_opacity=0.7).scale(0.5),
            RegularPolygon(n=6, color=RED, fill_opacity=0.7).scale(0.25),
            RegularPolygon(n=5, color=PURPLE, fill_opacity=0.7).scale(0.3)
        )
        
        # Arrange shapes randomly
        positions = [LEFT*3 + UP*1, LEFT*1 + DOWN*0.5, RIGHT*2 + UP*1.5, 
                    RIGHT*3 + DOWN*1, ORIGIN + UP*0.3]
        
        for shape, pos in zip(shapes, positions):
            shape.move_to(pos)
        
        self.play(FadeIn(shapes), run_time=2)
        self.wait(1)
        
        # Create elegant mathematical notation
        # Start with individual elements
        s_symbols = VGroup()
        for i, shape in enumerate(shapes):
            s_symbol = MathTex(f"s_{i+1}", color=WHITE, font_size=16)
            s_symbol.move_to(shape.get_center() + DOWN*0.5)
            s_symbols.add(s_symbol)
        
        self.play(Write(s_symbols), run_time=1.5)
        self.wait(1)
        
        # Show the set notation building up
        set_elements = MathTex(
            r"s_1, s_2, s_3, s_4, s_5, \ldots",
            color=BLUE,
            font_size=32
        ).move_to(DOWN*1.5)
        
        self.play(Write(set_elements), run_time=2)
        self.wait(1)
        
        # Transform to set notation
        curly_braces = MathTex(r"\{", r"\}", color=BLUE, font_size=48)
        curly_braces[0].move_to(set_elements.get_left() + LEFT*0.3)
        curly_braces[1].move_to(set_elements.get_right() + RIGHT*0.3)
        
        self.play(Write(curly_braces), run_time=1)
        
        # Add set name
        set_S = MathTex("S = ", color=BLUE, font_size=32)
        set_S.next_to(curly_braces[0], LEFT, buff=0.2)
        
        self.play(Write(set_S), run_time=1)
        self.wait(1)
        
        # Final elegant form
        self.play(
            FadeOut(shapes),
            FadeOut(s_symbols),
            run_time=1.5
        )
        
        elegant_notation = MathTex(
            r"s \in S",
            color=WHITE,
            font_size=64
        ).move_to(UP*0.5)
        
        # Animate the elegant reveal
        self.play(
            TransformFromCopy(set_elements, elegant_notation),
            run_time=3
        )
        
        # Add explanation
        explanation = Text(
            "Any particular state s belongs to the set of all possible states S",
            color=GRAY,
            font_size=18
        ).move_to(DOWN*2.5)
        
        self.play(Write(explanation), run_time=2)
        self.wait(3)

# Additional filler scenes for transitions and emphasis

class ValuePropagation(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create a network of states
        grid_size = 5
        cell_size = 1.2
        
        states = VGroup()
        for i in range(grid_size):
            for j in range(grid_size):
                x = (i - grid_size//2) * cell_size
                y = (j - grid_size//2) * cell_size
                
                state = Circle(radius=0.2, color=BLUE, fill_opacity=0.3)
                state.move_to([x, y, 0])
                states.add(state)
        
        self.play(Create(states), run_time=2)
        
        # Create reward source
        reward_state = states[12]  # Center state
        reward_state.set_color(GOLD).set_fill(opacity=0.9)
        reward_text = Text("+10", color=WHITE, font_size=16).move_to(reward_state.get_center())
        
        self.play(
            Transform(reward_state, Circle(radius=0.25, color=GOLD, fill_opacity=0.9).move_to(reward_state.get_center())),
            Write(reward_text),
            run_time=1
        )
        
        # Animate value propagation in waves
        for wave in range(3):
            wave_states = []
            
            # Select states at increasing distances from center
            center_i, center_j = 2, 2
            for i in range(grid_size):
                for j in range(grid_size):
                    distance = abs(i - center_i) + abs(j - center_j)
                    if distance == wave + 1:
                        wave_states.append(states[i * grid_size + j])
            
            # Animate this wave
            wave_animations = []
            for state in wave_states:
                intensity = 1.0 / (wave + 2)
                color = interpolate_color(BLUE, GOLD, intensity)
                new_circle = Circle(radius=0.22, color=color, fill_opacity=0.7)
                new_circle.move_to(state.get_center())
                wave_animations.append(Transform(state, new_circle))
            
            self.play(*wave_animations, run_time=1.5)
            self.wait(0.5)
        
        # Add explanation
        explanation = Text("Value propagates backward through the state space", 
                          color=WHITE, font_size=20).move_to(DOWN*3.5)
        self.play(Write(explanation), run_time=2)
        self.wait(2)

class PolicyComparison(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create two grid worlds side by side
        grid_size = 3
        cell_size = 0.8
        
        # Left grid (Random Policy)
        left_grid = self.create_grid(grid_size, cell_size, LEFT*3)
        left_title = Text("Random Policy", color=RED, font_size=20).move_to(LEFT*3 + UP*2)
        
        # Right grid (Smart Policy)
        right_grid = self.create_grid(grid_size, cell_size, RIGHT*3)
        right_title = Text("Smart Policy", color=GREEN, font_size=20).move_to(RIGHT*3 + UP*2)
        
        self.play(Create(left_grid), Create(right_grid))
        self.play(Write(left_title), Write(right_title))
        
        # Add goal states
        goal_left = Square(side_length=cell_size*0.8, color=GOLD, fill_opacity=0.7)
        goal_left.move_to(LEFT*3 + RIGHT*cell_size + UP*cell_size)
        
        goal_right = Square(side_length=cell_size*0.8, color=GOLD, fill_opacity=0.7)
        goal_right.move_to(RIGHT*3 + RIGHT*cell_size + UP*cell_size)
        
        self.play(FadeIn(goal_left), FadeIn(goal_right))
        
        # Show different behaviors
        # Random policy arrows (scattered)
        random_arrows = VGroup()
        for i in range(3):
            for j in range(3):
                center = LEFT*3 + (i-1)*cell_size*RIGHT + (j-1)*cell_size*UP
                for direction in [UP, DOWN, LEFT, RIGHT]:
                    arrow = Arrow(
                        start=center,
                        end=center + direction * 0.2,
                        color=RED,
                        stroke_width=1,
                        max_tip_length_to_length_ratio=0.3
                    )
                    random_arrows.add(arrow)
        
        # Smart policy arrows (directed toward goal)
        smart_arrows = VGroup()
        for i in range(3):
            for j in range(3):
                center = RIGHT*3 + (i-1)*cell_size*RIGHT + (j-1)*cell_size*UP
                # Direction toward goal (top-right)
                if i < 2:  # Move right
                    arrow = Arrow(
                        start=center,
                        end=center + RIGHT * 0.3,
                        color=GREEN,
                        stroke_width=3,
                        max_tip_length_to_length_ratio=0.3
                    )
                    smart_arrows.add(arrow)
                if j < 2:  # Move up
                    arrow = Arrow(
                        start=center,
                        end=center + UP * 0.3,
                        color=GREEN,
                        stroke_width=3,
                        max_tip_length_to_length_ratio=0.3
                    )
                    smart_arrows.add(arrow)
        
        self.play(Create(random_arrows), Create(smart_arrows), run_time=2)
        self.wait(2)
    
    def create_grid(self, size, cell_size, center):
        grid = VGroup()
        for i in range(size + 1):
            # Vertical lines
            line = Line(
                start=[i*cell_size - size*cell_size/2, -size*cell_size/2, 0],
                end=[i*cell_size - size*cell_size/2, size*cell_size/2, 0],
                color=BLUE_E,
                stroke_width=2
            )
            grid.add(line)
            
            # Horizontal lines
            line = Line(
                start=[-size*cell_size/2, i*cell_size - size*cell_size/2, 0],
                end=[size*cell_size/2, i*cell_size - size*cell_size/2, 0],
                color=BLUE_E,
                stroke_width=2
            )
            grid.add(line)
        
        grid.move_to(center)
        return grid

class DecisionTreeVisualization(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Root state
        root = Circle(radius=0.3, color=BLUE, fill_opacity=0.7)
        root_label = MathTex("s", color=WHITE, font_size=20).move_to(root.get_center())
        root_group = VGroup(root, root_label).move_to(UP*2)
        
        self.play(FadeIn(root_group))
        
        # Actions from root
        actions = VGroup()
        action_positions = [LEFT*2 + UP*0.5, ORIGIN + UP*0.5, RIGHT*2 + UP*0.5]
        action_labels = ["a_1", "a_2", "a_3"]
        
        for pos, label in zip(action_positions, action_labels):
            action_square = Square(side_length=0.4, color=GREEN, fill_opacity=0.7)
            action_text = MathTex(label, color=WHITE, font_size=16)
            action_group = VGroup(action_square, action_text).move_to(pos)
            actions.add(action_group)
            
            # Arrow from root to action
            arrow = Arrow(
                start=root_group.get_bottom(),
                end=action_group.get_top(),
                color=WHITE,
                stroke_width=2
            )
            actions.add(arrow)
        
        self.play(Create(actions), run_time=2)
        
        # Outcomes from each action
        outcomes = VGroup()
        for i, action_pos in enumerate(action_positions):
            # Multiple possible outcomes
            outcome_positions = [action_pos + DOWN*1.5 + LEFT*0.8, action_pos + DOWN*1.5 + RIGHT*0.8]
            
            for j, outcome_pos in enumerate(outcome_positions):
                # Next state
                next_state = Circle(radius=0.2, color=BLUE, fill_opacity=0.5)
                next_state.move_to(outcome_pos)
                
                # Probability
                prob = 0.6 if j == 0 else 0.4
                prob_text = Text(f"{prob}", color=YELLOW, font_size=12)
                prob_text.move_to(outcome_pos + UP*0.5)
                
                # Reward
                reward = ["+1", "-1"][j]
                reward_text = Text(reward, color=WHITE, font_size=12)
                reward_text.move_to(outcome_pos + DOWN*0.4)
                
                # Arrow
                arrow = Arrow(
                    start=action_positions[i] + DOWN*0.2,
                    end=outcome_pos + UP*0.2,
                    color=GRAY,
                    stroke_width=1
                )
                
                outcome_group = VGroup(next_state, prob_text, reward_text, arrow)
                outcomes.add(outcome_group)
        
        self.play(Create(outcomes), run_time=3)
        
        # Add mathematical notation
        expectation = MathTex(
            r"\mathbb{E}[R + \gamma V(S')]",
            color=WHITE,
            font_size=32
        ).move_to(DOWN*3)
        
        self.play(Write(expectation), run_time=2)
        self.wait(2)

class LearningProgressVisualization(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create learning progress chart
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 20],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_include": np.arange(0, 11, 2)},
            y_axis_config={"numbers_to_include": np.arange(0, 101, 20)}
        )
        
        # Labels
        x_label = Text("Experience", color=WHITE, font_size=16).next_to(axes.x_axis, DOWN)
        y_label = Text("Performance", color=WHITE, font_size=16).next_to(axes.y_axis, LEFT, buff=0.5)
        y_label.rotate(PI/2)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # Learning curve
        learning_curve_points = [
            [0, 10], [1, 15], [2, 25], [3, 35], [4, 50], 
            [5, 65], [6, 75], [7, 82], [8, 87], [9, 90], [10, 92]
        ]
        
        # Convert to axes coordinates
        curve_points = [axes.coords_to_point(x, y) for x, y in learning_curve_points]
        
        # Animate learning curve drawing
        learning_curve = VMobject()
        learning_curve.set_points_as_corners(curve_points)
        learning_curve.set_color(GREEN)
        
        self.play(Create(learning_curve), run_time=4)
        
        # Add annotations
        trial_error_text = Text("Trial and Error", color=RED, font_size=14)
        trial_error_text.move_to(axes.coords_to_point(2, 40))
        
        improvement_text = Text("Improvement", color=GREEN, font_size=14)
        improvement_text.move_to(axes.coords_to_point(6, 80))
        
        convergence_text = Text("Convergence", color=BLUE, font_size=14)
        convergence_text.move_to(axes.coords_to_point(9, 95))
        
        self.play(Write(trial_error_text), run_time=1)
        self.play(Write(improvement_text), run_time=1)
        self.play(Write(convergence_text), run_time=1)
        
        self.wait(2)
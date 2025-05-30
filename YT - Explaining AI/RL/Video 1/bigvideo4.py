from manim import *
import numpy as np

class FloatingMathSymbols(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create floating mathematical symbols that gently move
        symbols = [
            MathTex(r"s \in S", color=BLUE, font_size=36),
            MathTex(r"a \in A(s)", color=GREEN, font_size=32),
            MathTex(r"r \in \mathbb{R}", color=YELLOW, font_size=28),
            MathTex(r"\pi(a|s)", color=RED, font_size=34),
            MathTex(r"V^{\pi}(s)", color=PURPLE, font_size=30),
            MathTex(r"\mathbb{E}[G]", color=ORANGE, font_size=32),
            MathTex(r"\gamma", color=PINK, font_size=40),
            MathTex(r"P(s'|s,a)", color=BLUE, font_size=26)
        ]
        
        # Position symbols randomly
        for symbol in symbols:
            x = np.random.uniform(-5, 5)
            y = np.random.uniform(-3, 3)
            symbol.move_to([x, y, 0])
        
        # Add all symbols with fade in
        self.play(LaggedStart(*[FadeIn(symbol) for symbol in symbols], 
                             lag_ratio=0.3), run_time=4)
        
        # Gentle floating animation
        floating_anims = []
        for symbol in symbols:
            # Random floating pattern
            path = VMobject()
            points = []
            for t in np.linspace(0, 2*PI, 50):
                offset_x = 0.5 * np.sin(t + np.random.random() * 2 * PI)
                offset_y = 0.3 * np.cos(1.5 * t + np.random.random() * 2 * PI)
                points.append(symbol.get_center() + [offset_x, offset_y, 0])
            
            path.set_points_as_corners(points)
            floating_anims.append(MoveAlongPath(symbol, path))
        
        # Run floating animation (loops perfectly)
        self.play(*floating_anims, run_time=15, rate_func=linear)

class GentleGridPulse(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create a subtle grid background
        grid = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 0.5,
                "stroke_opacity": 0.2
            }
        )
        
        self.add(grid)
        
        # Create pulsing agents at grid intersections
        agents = VGroup()
        for x in range(-6, 7, 2):
            for y in range(-4, 5, 2):
                agent = Dot(color=BLUE, radius=0.08, fill_opacity=0.6)
                agent.move_to([x, y, 0])
                agents.add(agent)
        
        self.add(agents)
        
        # Gentle pulsing animation
        for _ in range(10):  # 10 cycles of pulsing
            self.play(
                agents.animate.set_fill(opacity=0.9).scale(1.3),
                grid.animate.set_stroke(opacity=0.4),
                run_time=1.5
            )
            self.play(
                agents.animate.set_fill(opacity=0.6).scale(1/1.3),
                grid.animate.set_stroke(opacity=0.2),
                run_time=1.5
            )

class AbstractDataFlow(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create flowing data particles
        def create_particle():
            colors = [BLUE, GREEN, YELLOW, RED, PURPLE, ORANGE]
            particle = Dot(
                color=np.random.choice(colors),
                radius=np.random.uniform(0.05, 0.15),
                fill_opacity=0.7
            )
            return particle
        
        # Create multiple flow paths
        paths = [
            # Horizontal flows
            Line(LEFT*7, RIGHT*7, color=WHITE).move_to(UP*2),
            Line(LEFT*7, RIGHT*7, color=WHITE).move_to(DOWN*2),
            # Curved flows
            Arc(radius=3, start_angle=PI, angle=PI).move_to(UP*0.5),
            Arc(radius=3, start_angle=0, angle=PI).move_to(DOWN*0.5),
        ]
        
        # Make paths invisible but use for particle movement
        for path in paths:
            path.set_stroke(opacity=0)
        
        self.add(*paths)
        
        # Continuous particle flow
        particles = VGroup()
        
        for _ in range(20):  # 20 seconds of flow
            # Add new particles
            for path in paths:
                if np.random.random() < 0.3:  # 30% chance each frame
                    particle = create_particle()
                    particle.move_to(path.get_start())
                    particles.add(particle)
                    
                    # Animate particle along path
                    self.play(
                        MoveAlongPath(particle, path),
                        run_time=np.random.uniform(2, 4),
                        rate_func=smooth
                    )
                    
                    # Remove particle after animation
                    self.remove(particle)
                    particles.remove(particle)
            
            self.wait(0.1)

class ConceptualConnections(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create concept nodes
        concepts = [
            {"name": "State", "pos": LEFT*3 + UP*2, "color": BLUE},
            {"name": "Action", "pos": LEFT*1 + UP*2, "color": GREEN},
            {"name": "Reward", "pos": RIGHT*1 + UP*2, "color": YELLOW},
            {"name": "Policy", "pos": RIGHT*3 + UP*2, "color": RED},
            {"name": "Value", "pos": LEFT*2 + DOWN*1, "color": PURPLE},
            {"name": "Return", "pos": RIGHT*2 + DOWN*1, "color": ORANGE},
            {"name": "Future", "pos": ORIGIN + DOWN*2, "color": PINK}
        ]
        
        nodes = VGroup()
        for concept in concepts:
            circle = Circle(radius=0.6, color=concept["color"], fill_opacity=0.3)
            text = Text(concept["name"], color=WHITE, font_size=16)
            node = VGroup(circle, text).move_to(concept["pos"])
            nodes.add(node)
        
        self.add(nodes)
        
        # Create connections that appear and disappear
        connections = [
            (0, 1), (1, 2), (0, 4), (3, 1), (4, 5), (5, 6), (2, 5), (6, 4)
        ]
        
        # Animate connections appearing and fading
        for _ in range(15):  # 15 cycles
            # Choose random connections to highlight
            active_connections = np.random.choice(len(connections), 3, replace=False)
            
            lines = VGroup()
            for idx in active_connections:
                start_node = nodes[connections[idx][0]]
                end_node = nodes[connections[idx][1]]
                
                line = Line(
                    start_node.get_center(),
                    end_node.get_center(),
                    color=WHITE,
                    stroke_width=2
                )
                lines.add(line)
            
            self.play(Create(lines), run_time=1)
            self.play(FadeOut(lines), run_time=1)

class LearningWaves(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create wave functions representing learning
        axes = Axes(
            x_range=[0, 4*PI, PI/2],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            axis_config={"stroke_opacity": 0.3}
        )
        
        self.add(axes)
        
        # Multiple learning curves with different frequencies
        def create_wave(freq, amplitude, color, phase=0):
            return axes.plot(
                lambda x: amplitude * np.sin(freq * x + phase) * np.exp(-0.1 * x),
                color=color,
                stroke_width=3
            )
        
        # Create and animate multiple waves
        for cycle in range(10):  # 10 cycles
            waves = VGroup()
            colors = [BLUE, GREEN, RED, YELLOW, PURPLE]
            
            for i, color in enumerate(colors):
                freq = 1 + i * 0.5
                amplitude = 1.5 - i * 0.2
                phase = cycle * PI/4 + i * PI/3
                
                wave = create_wave(freq, amplitude, color, phase)
                waves.add(wave)
            
            self.play(Create(waves), run_time=1.5)
            self.play(FadeOut(waves), run_time=0.5)

class RotatingFramework(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create the RL framework as a 3D-looking structure
        center = ORIGIN
        
        # Core concepts arranged in a circle
        concepts = [
            {"symbol": MathTex(r"S", color=BLUE, font_size=32), "angle": 0},
            {"symbol": MathTex(r"A", color=GREEN, font_size=32), "angle": PI/3},
            {"symbol": MathTex(r"R", color=YELLOW, font_size=32), "angle": 2*PI/3},
            {"symbol": MathTex(r"\pi", color=RED, font_size=32), "angle": PI},
            {"symbol": MathTex(r"V", color=PURPLE, font_size=32), "angle": 4*PI/3},
            {"symbol": MathTex(r"\gamma", color=ORANGE, font_size=32), "angle": 5*PI/3}
        ]
        
        radius = 2.5
        framework = VGroup()
        
        for concept in concepts:
            x = radius * np.cos(concept["angle"])
            y = radius * np.sin(concept["angle"])
            concept["symbol"].move_to([x, y, 0])
            framework.add(concept["symbol"])
        
        # Add connecting lines
        connections = VGroup()
        for i, concept in enumerate(concepts):
            next_concept = concepts[(i + 1) % len(concepts)]
            line = Line(
                concept["symbol"].get_center(),
                next_concept["symbol"].get_center(),
                color=WHITE,
                stroke_width=1,
                stroke_opacity=0.5
            )
            connections.add(line)
        
        # Add center
        center_symbol = MathTex(r"\mathbb{E}", color=GOLD, font_size=48)
        center_symbol.move_to(center)
        
        framework.add(connections, center_symbol)
        self.add(framework)
        
        # Continuous rotation
        self.play(
            Rotate(framework, 4*PI, about_point=center),
            run_time=20,
            rate_func=linear
        )

class ParticleSystem(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create a particle system representing agents exploring
        particles = VGroup()
        n_particles = 30
        
        for i in range(n_particles):
            particle = Dot(
                color=[BLUE, GREEN, YELLOW, RED, PURPLE][i % 5],
                radius=0.08,
                fill_opacity=0.7
            )
            # Random starting position
            x = np.random.uniform(-6, 6)
            y = np.random.uniform(-3, 3)
            particle.move_to([x, y, 0])
            particles.add(particle)
        
        self.add(particles)
        
        # Simulate particle movement (random walk with attraction to center)
        for frame in range(300):  # 30 seconds at 10fps
            new_positions = []
            
            for particle in particles:
                current_pos = particle.get_center()
                
                # Random movement
                random_move = np.random.normal(0, 0.1, 2)
                
                # Slight attraction to center
                center_attraction = -0.05 * current_pos[:2]
                
                # Combine movements
                new_pos = current_pos[:2] + random_move + center_attraction
                
                # Boundary conditions
                new_pos[0] = np.clip(new_pos[0], -6, 6)
                new_pos[1] = np.clip(new_pos[1], -3, 3)
                
                new_positions.append([new_pos[0], new_pos[1], 0])
            
            # Animate to new positions
            animations = []
            for particle, new_pos in zip(particles, new_positions):
                animations.append(particle.animate.move_to(new_pos))
            
            self.play(*animations, run_time=0.1)

class GradientFlow(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create a gradient field visualization
        x_range = np.arange(-5, 6, 0.8)
        y_range = np.arange(-3, 4, 0.8)
        
        arrows = VGroup()
        
        for x in x_range:
            for y in y_range:
                # Create a potential function (like a value function)
                # Gradient points toward higher values
                grad_x = -0.1 * x + 0.05 * np.sin(y)
                grad_y = -0.1 * y + 0.05 * np.cos(x)
                
                # Normalize
                magnitude = np.sqrt(grad_x**2 + grad_y**2)
                if magnitude > 0:
                    grad_x /= magnitude
                    grad_y /= magnitude
                
                arrow = Arrow(
                    start=[x, y, 0],
                    end=[x + 0.3*grad_x, y + 0.3*grad_y, 0],
                    color=interpolate_color(BLUE, RED, magnitude),
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.3
                )
                arrows.add(arrow)
        
        self.add(arrows)
        
        # Animate the gradient field changing over time
        for phase in range(20):
            new_arrows = VGroup()
            
            for i, (x, y) in enumerate([(x, y) for x in x_range for y in y_range]):
                # Time-varying gradient
                t = phase * 0.5
                grad_x = -0.1 * x + 0.05 * np.sin(y + t)
                grad_y = -0.1 * y + 0.05 * np.cos(x + t)
                
                magnitude = np.sqrt(grad_x**2 + grad_y**2)
                if magnitude > 0:
                    grad_x /= magnitude
                    grad_y /= magnitude
                
                new_arrow = Arrow(
                    start=[x, y, 0],
                    end=[x + 0.3*grad_x, y + 0.3*grad_y, 0],
                    color=interpolate_color(BLUE, RED, magnitude),
                    stroke_width=2,
                    max_tip_length_to_length_ratio=0.3
                )
                new_arrows.add(new_arrow)
            
            self.play(Transform(arrows, new_arrows), run_time=1)

class PulsatingNetwork(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create a network of interconnected nodes
        n_nodes = 12
        nodes = VGroup()
        
        # Arrange nodes in a circle
        for i in range(n_nodes):
            angle = i * 2 * PI / n_nodes
            x = 3 * np.cos(angle)
            y = 3 * np.sin(angle)
            
            node = Circle(
                radius=0.2,
                color=BLUE,
                fill_opacity=0.7
            ).move_to([x, y, 0])
            nodes.add(node)
        
        # Create connections
        connections = VGroup()
        for i in range(n_nodes):
            for j in range(i + 1, n_nodes):
                if np.random.random() < 0.3:  # 30% connection probability
                    line = Line(
                        nodes[i].get_center(),
                        nodes[j].get_center(),
                        color=WHITE,
                        stroke_width=1,
                        stroke_opacity=0.3
                    )
                    connections.add(line)
        
        network = VGroup(nodes, connections)
        self.add(network)
        
        # Pulsating animation
        for _ in range(15):
            # Random activation pattern
            active_nodes = np.random.choice(n_nodes, n_nodes//3, replace=False)
            
            # Highlight active nodes
            highlight_anims = []
            for i in active_nodes:
                highlight_anims.append(
                    nodes[i].animate.set_color(YELLOW).scale(1.5)
                )
            
            self.play(*highlight_anims, run_time=0.5)
            
            # Return to normal
            reset_anims = []
            for i in active_nodes:
                reset_anims.append(
                    nodes[i].animate.set_color(BLUE).scale(1/1.5)
                )
            
            self.play(*reset_anims, run_time=0.5)

class AbstractMathematicalSpace(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Create an abstract mathematical space with floating equations
        equations = [
            MathTex(r"\sum_{t=0}^{\infty} \gamma^t r_t", color=BLUE, font_size=24),
            MathTex(r"\max_{\pi} \mathbb{E}[G]", color=GREEN, font_size=28),
            MathTex(r"P(s'|s,a)", color=YELLOW, font_size=22),
            MathTex(r"\pi^*(s) = \arg\max_a Q^*(s,a)", color=RED, font_size=20),
            MathTex(r"V^{\pi}(s) = \mathbb{E}_{\pi}[G|S_0=s]", color=PURPLE, font_size=26),
            MathTex(r"\nabla_{\theta} J(\theta)", color=ORANGE, font_size=24)
        ]
        
        # Position equations in 3D-like space
        positions = [
            [-4, 2, 0], [2, 3, 0], [-3, -1, 0],
            [4, 1, 0], [-1, -2, 0], [3, -2, 0]
        ]
        
        for eq, pos in zip(equations, positions):
            eq.move_to(pos)
        
        # Add equations with staggered timing
        self.play(
            LaggedStart(*[FadeIn(eq) for eq in equations], lag_ratio=0.5),
            run_time=3
        )
        
        # Gentle floating and rotation
        floating_anims = []
        for eq in equations:
            # Create orbital motion
            center = eq.get_center()
            orbit_radius = 0.5
            
            path = Circle(radius=orbit_radius).move_to(center)
            floating_anims.append(
                AnimationGroup(
                    MoveAlongPath(eq, path),
                    Rotate(eq, 2*PI),
                )
            )
        
        self.play(*floating_anims, run_time=12, rate_func=linear)

class MinimalistStateTransition(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        
        # Very clean, minimal state transition
        state1 = Circle(radius=0.5, color=BLUE, fill_opacity=0.3, stroke_width=2)
        state2 = Circle(radius=0.5, color=BLUE, fill_opacity=0.3, stroke_width=2)
        
        state1.move_to(LEFT*3)
        state2.move_to(RIGHT*3)
        
        # Labels
        s1_label = MathTex("s", color=WHITE, font_size=32).move_to(state1.get_center())
        s2_label = MathTex("s'", color=WHITE, font_size=32).move_to(state2.get_center())
        
        # Action
        action = Square(side_length=0.6, color=GREEN, fill_opacity=0.3, stroke_width=2)
        action_label = MathTex("a", color=WHITE, font_size=24).move_to(action.get_center())
        action_group = VGroup(action, action_label)
        
        # Reward
        reward = Circle(radius=0.3, color=YELLOW, fill_opacity=0.5)
        reward_label = MathTex("r", color=WHITE, font_size=20).move_to(reward.get_center())
        reward_group = VGroup(reward, reward_label).move_to(UP*2)
        
        # Arrows
        arrow1 = Arrow(state1.get_right(), action.get_left(), color=WHITE, stroke_width=3)
        arrow2 = Arrow(action.get_top(), reward.get_bottom(), color=WHITE, stroke_width=2)
        arrow3 = Arrow(action.get_right(), state2.get_left(), color=WHITE, stroke_width=3)
        
        # Build the scene step by step
        elements = [
            VGroup(state1, s1_label),
            arrow1,
            action_group,
            arrow2,
            reward_group,
            arrow3,
            VGroup(state2, s2_label)
        ]
        
        # Animate building and then loop
        for element in elements:
            self.play(FadeIn(element), run_time=0.8)
        
        # Gentle pulsing of the whole system
        all_elements = VGroup(*elements)
        for _ in range(10):
            self.play(all_elements.animate.scale(1.05), run_time=1)
            self.play(all_elements.animate.scale(1/1.05), run_time=1)
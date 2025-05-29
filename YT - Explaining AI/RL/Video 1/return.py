from manim import *

class returnn(Scene):
    def construct(self):
        # Create main state
        main_state = Circle(radius=0.5, color=BLUE, fill_opacity=0.5).shift(UP*2.5)
        main_text = Text("S0", font_size=24).move_to(main_state.get_center())
        main_label = Text("Start", font_size=24).next_to(main_state, UP, buff=0.1)

        # First level of actions (4 actions from main state)
        actions = []
        action_texts = ["Attack", "Block", "Hide", "Run"]
        action_probs = ["P(0.3)", "P(0.3)", "P(0.2)", "P(0.2)"]
        action_positions = [LEFT*3, LEFT*1, RIGHT*1, RIGHT*3]
        arrows_to_actions = []

        for i in range(4):
            action = Rectangle(width=1.5, height=0.8, color=GREEN, fill_opacity=0.4).shift(UP*0.5 + action_positions[i])
            action_text = Text(action_texts[i], font_size=20).move_to(action.get_center())
            prob_text = Text(action_probs[i], font_size=18).next_to(action, UP, buff=0.1)
            arrow = Arrow(start=main_state.get_bottom(), end=action.get_top(), buff=0.1, color=WHITE)
            
            actions.append((action, action_text, prob_text, arrow))

        # Second level of states (12 outcome states)
        states = []
        state_positions = [
            LEFT*4.5 + DOWN*1.5, LEFT*3 + DOWN*1.5, LEFT*1.5 + DOWN*1.5, 
            DOWN*1.5, RIGHT*1.5 + DOWN*1.5, RIGHT*3 + DOWN*1.5, RIGHT*4.5 + DOWN*1.5,
            LEFT*3.5 + DOWN*3, LEFT*1.5 + DOWN*3, RIGHT*1.5 + DOWN*3, RIGHT*3.5 + DOWN*3
        ]
        state_texts = [
            "S1", "S2", "S3", "S4", "S5", "S6", 
            "S7", "S8", "S9", "S10", "S11"
        ]
        state_labels = [
            "Victory", "Damaged", "Blocked", "Counter", "Hidden", "Found",
            "Escaped", "Safe", "Ambushed", "Lost", "Treasure"
        ]
        state_rewards = [
            "+100", "-20", "+10", "+50", "+5", "-30",
            "+20", "+15", "-10", "-5", "+200"
        ]
        arrows_to_states = []

        # Create states and connect them to actions
        for i, pos in enumerate(state_positions):
            if i >= len(state_texts):
                break
            
            state = Circle(radius=0.4, color=RED, fill_opacity=0.4).shift(pos)
            state_text = Text(state_texts[i], font_size=18).move_to(state.get_center())
            state_label = Text(state_labels[i], font_size=18).next_to(state, DOWN, buff=0.1)
            reward = Text(state_rewards[i], font_size=18, color=YELLOW).next_to(state, RIGHT, buff=0.1)
            
            # Determine which action connects to this state
            action_idx = min(i // 3, 3)
            arrow = Arrow(start=actions[action_idx][0].get_bottom(), end=state.get_top(), buff=0.1, color=WHITE)
            arrows_to_states.append(arrow)
            
            states.append((state, state_text, state_label, reward))

        # Third level (terminal states or next states)
        term_states = []
        term_positions = [LEFT*4 + DOWN*4.5, LEFT*1.5 + DOWN*4.5, RIGHT*1.5 + DOWN*4.5, RIGHT*4 + DOWN*4.5]
        term_texts = ["T1", "T2", "T3", "T4"]
        term_labels = ["Game Over", "Continue", "New Level", "Boss Fight"]
        arrows_to_term = []

        for i, pos in enumerate(term_positions):
            term = Circle(radius=0.4, color=PURPLE, fill_opacity=0.4).shift(pos)
            term_text = Text(term_texts[i], font_size=18).move_to(term.get_center())
            term_label = Text(term_labels[i], font_size=18).next_to(term, DOWN, buff=0.1)
            
            # Connect some states to terminal states
            if i < len(states):
                source_idx = i * 2 if i * 2 < len(states) else len(states) - 1
                arrow = Arrow(start=states[source_idx][0].get_bottom(), end=term.get_top(), buff=0.1, color=WHITE)
                arrows_to_term.append(arrow)
            
            term_states.append((term, term_text, term_label))

        # Animation sequence
        self.play(Create(main_state), Write(main_text), Write(main_label))

        # Create actions
        for action, action_text, prob_text, arrow in actions:
            self.play(Create(action), Write(action_text))
            self.play(Create(arrow), Write(prob_text))
            self.play(Flash(prob_text, flash_radius=0.4), run_time=0.5)

        # Create states
        for i, (state, state_text, state_label, reward) in enumerate(states):
            if i < len(arrows_to_states):
                self.play(Create(arrows_to_states[i]))
            self.play(Create(state), Write(state_text))
            self.play(Write(state_label), Write(reward))
            self.play(Flash(reward, flash_radius=0.4), run_time=0.5)

        # Create terminal states
        for i, (term, term_text, term_label) in enumerate(term_states):
            if i < len(arrows_to_term):
                self.play(Create(arrows_to_term[i]))
            self.play(Create(term), Write(term_text), Write(term_label))

        # Title and formula
        title = Text("Reinforcement Learning State Transitions", font_size=36).to_edge(UP)
        formula = MathTex(r"R = \sum_{t=0}^{\infty} \gamma^t r_t").to_edge(DOWN)

        self.play(Write(title))
        self.play(Write(formula))

        # Hold final state
        self.wait(2)

        # Optional: fade out some elements to focus on the structure
        arrows = arrows_to_actions + arrows_to_states + arrows_to_term
        self.play(FadeOut(*arrows))
        self.wait(1)
from manim import *

class AgentEnvironment(Scene):
    def construct(self):
        # Define colors and positions
        agent_color = BLUE
        env_color = GREEN

        # Create the agent and environment rectangles
        agent = Rectangle(width=2, height=2, color=agent_color, fill_opacity=0.3)
        agent.shift(3*LEFT)
        agent_text = Text("Agent", font_size=24).move_to(agent)

        environment = Rectangle(width=4, height=2, color=env_color, fill_opacity=0.3)
        environment.shift(3*RIGHT)
        env_text = Text("Environment", font_size=24).move_to(environment)

        # Create the arrows and labels
        action_arrow = Arrow(agent.get_right(), environment.get_left(), buff=0.3, color=YELLOW, stroke_width=3)
        action_text = Text("Action", font_size=20).next_to(action_arrow, UP, buff=0.1)

        reward_arrow = Arrow(environment.get_left(), agent.get_right(), buff=0.3, color=GRAY, stroke_width=3).shift(0.65*DOWN)
        reward_text = Text("Reward", font_size=20).next_to(reward_arrow, DOWN, buff=0.1)
        
        next_state_arrow = Arrow(environment.get_left(), agent.get_right(), buff=0.3, color=GRAY, stroke_width=3).shift(0.75*UP)
        next_state_text = Text("Next State", font_size=20).next_to(next_state_arrow, UP, buff=0.1)
       
        # Create a title
        title = Text("Reinforcement Learning Loop", font_size=36)
        title.to_edge(UP)

        # Animation sequence
        self.play(Write(title))
        self.play(Create(agent), Write(agent_text))
        self.play(Create(environment), Write(env_text))
        self.play(GrowArrow(action_arrow), Write(action_text))
        self.play(GrowArrow(reward_arrow), Write(reward_text))
        self.play(GrowArrow(next_state_arrow), Write(next_state_text))
        self.wait(2)
from manim import *

class MDP(Scene):
    def construct(self):
        # Title
        title = Text("Understanding Markov Chains", font_size=42)
        subtitle = Text("Using Video Game Analogy", font_size=32).next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Game state representation - moved left
        dungeon = RoundedRectangle(height=3.5, width=4, corner_radius=0.5).shift(LEFT*2.5)
        dungeon_label = Text("Dungeon (State s)", font_size=22).next_to(dungeon, UP)
        
        # Player character
        player = Text("🎮", font_size=50).move_to(dungeon.get_center())
        
        # Action representation
        sword_swing = Text("Swing Sword (Action a)", font_size=22).next_to(dungeon, DOWN, buff=0.5)
        
        self.play(Create(dungeon), Write(dungeon_label), FadeIn(player))
        self.play(Write(sword_swing))
        self.wait(1)
        
        # Animation for action
        self.play(player.animate.shift(RIGHT/4), run_time=0.2)
        self.play(player.animate.shift(LEFT/2), run_time=0.2)
        self.play(player.animate.shift(RIGHT/4), run_time=0.2)
        
        # Possible outcomes - moved right
        new_room = RoundedRectangle(height=3.5, width=4, corner_radius=0.5).shift(RIGHT*2.5)
        new_room_label = Text("New Room (State s')", font_size=22).next_to(new_room, UP)
        
        # Probability arrow - shortened
        probability = Text("P(s',r|s,a)", font_size=24)
        arrow = Arrow(start=dungeon.get_right(), end=new_room.get_left(), buff=0.2)
        probability.next_to(arrow, UP, buff=0.1)
        
        # Reward
        reward = Text("Reward: 50 points", color=YELLOW, font_size=22).next_to(new_room, DOWN, buff=0.5)
        
        self.play(
            Create(new_room),
            Write(new_room_label),
            GrowArrow(arrow),
            Write(probability),
        )
        self.wait(1)
        
        # Player moves to new state with probability
        self.play(player.animate.move_to(new_room.get_center()))
        self.play(Write(reward))

        self.wait(2)
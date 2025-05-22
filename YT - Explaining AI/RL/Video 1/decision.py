from manim import *

class decision(Scene):
    def construct(self):
        circle = Circle(radius=0.5, color=BLUE, fill_opacity=0.5).shift(UP*2.25)
        text_inside = Text("S", font_size=24).move_to(circle.get_center())
        text_label = Text("Dungeon", font_size=24).next_to(circle, UP, buff=0.1).shift(UP * 0.2)
        
        rectangle1 = Rectangle(width=2.5, height=1, color=BLUE, fill_opacity=0.5).shift(DOWN*0.25).shift(LEFT*1.5)
        text_label2 = Text("P(0.7)", font_size=24).next_to(rectangle1, LEFT, buff=0.1).shift(LEFT * 0.2)
        arrow1_1 = Arrow(start=circle.get_bottom(), end=rectangle1.get_top(), buff=0.1, color=WHITE)
        text_inside2 = Text("Swing Sword", font_size=24).move_to(rectangle1.get_center())
        
        rectangle2 = Rectangle(width=2.5, height=1, color=BLUE, fill_opacity=0.5).shift(DOWN*0.25).shift(RIGHT*1.5)
        text_label3 = Text("P(0.3)", font_size=24).next_to(rectangle2, RIGHT, buff=0.1).shift(RIGHT * 0.2)
        arrow1_2 = Arrow(start=circle.get_bottom(), end=rectangle2.get_top(), buff=0.1, color=WHITE)
        text_inside3 = Text("Run away", font_size=24).move_to(rectangle2.get_center())

        # NEXT STATES
        circle2 = Circle(radius=0.5, color=BLUE, fill_opacity=0.5).shift(DOWN*3).shift(LEFT*1.5)
        text_inside4 = Text("S2'", font_size=24).move_to(circle2.get_center())
        text_label4 = Text("New Room", font_size=24).next_to(circle2, UP, buff=0.1)
        arrow2_1 = Arrow(start=rectangle1.get_bottom(), end=text_label4.get_top(), buff=0.1, color=WHITE)
        text_label6 = Text("+50 HP", font_size=24).next_to(circle2, LEFT, buff=0.1).shift(LEFT * 0.2)
        
        circle3 = Circle(radius=0.5, color=BLUE, fill_opacity=0.5).shift(DOWN*3).shift(RIGHT*1.5)
        text_inside5 = Text("S3'", font_size=24).move_to(circle3.get_center())
        text_label5 = Text("Trap Room", font_size=24).next_to(circle3, UP, buff=0.1)
        arrow2_2 = Arrow(start=rectangle2.get_bottom(), end=text_label5.get_top(), buff=0.1, color=WHITE)
        text_label7 = Text("-10 HP", font_size=24).next_to(circle3, RIGHT, buff=0.1).shift(RIGHT * 0.2)

        self.play(Create(circle), Write(text_inside), Write(text_label))
        
        self.play(Create(rectangle1), Write(text_inside2), Create(arrow1_1))
        self.play(Write(text_label2))
        self.play(Flash(text_label2, flash_radius=0.6))
        self.play(Create(arrow2_1))
        self.play(Create(circle2), Write(text_inside4), Write(text_label4))
        self.play(Write(text_label6))
        self.play(Flash(text_label6, flash_radius=0.6))
        
        self.play(Create(rectangle2), Write(text_inside3), Create(arrow1_2))
        self.play(Write(text_label3))
        self.play(Flash(text_label3, flash_radius=0.6))
        self.play(Create(arrow2_2))
        self.play(Create(circle3), Write(text_inside5), Write(text_label5))
        self.play(Write(text_label7))
        self.play(Flash(text_label7, flash_radius=0.6))
        
        self.play(FadeOut(arrow1_1, arrow1_2, arrow2_1, arrow2_2))
        self.play(FadeOut(text_label, text_label4, text_label5, text_label6, text_label7, text_inside4, text_inside5))
        
        policy_elements = VGroup(text_inside, text_inside2, text_inside3, text_label2, text_label3)
        
        policy_text = Text("π(S) = { Swing Sword: P(0.7), Run Away: P(0.3) }", font_size=32)
        
        self.play(
            ReplacementTransform(policy_elements, policy_text),
            FadeOut(circle, circle2, circle3, rectangle1, rectangle2), run_time=3
        )
        
       
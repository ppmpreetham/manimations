from manim import *

class ProbabilityExpression(Scene):
    def construct(self):
        # Step 1: Probability expression
        p = Text("P(", font_size=48)
        s_prime = Text("S'", font_size=48)
        comma1 = Text(", ", font_size=48)
        r = Text("R", font_size=48)
        bar = Text("|", font_size=48)
        s = Text("S", font_size=48)
        comma2 = Text(", ", font_size=48)
        a = Text("A", font_size=48)
        end = Text(")", font_size=48)

        probability_expression = VGroup(
            p, s_prime, comma1, r, bar, s, comma2, a, end
        ).arrange(RIGHT)
        
        comma1.shift(DOWN*0.25)
        comma2.shift(DOWN*0.25)
        
        self.play(Write(probability_expression))
        self.play(probability_expression.animate.shift(UP * 2))

        # Step 2: Explanation lines
        lines = [
            "The probability that after",
            "taking action A in state S,",
            "you will land in state S'",
            "and receive reward R"
        ]
        explanation = VGroup(*[Text(line, font_size=36) for line in lines])
        explanation.arrange(DOWN, aligned_edge=LEFT)
        explanation.next_to(probability_expression, DOWN, buff=1.5).shift(UP * 1)
        self.play(FadeIn(explanation))

        # Step 3: Character-to-expression map
        keyword_to_expression = {
            ("S'", 2): s_prime,
            ("R", 3): r,
            ("S", 1): s,
            ("A", 1): a
        }

        # Step 4: Animate character sweep
        for line_idx, line_mobj in enumerate(explanation):
            original_text = line_mobj.text
            new_line = VGroup()

            for i, char in enumerate(original_text):
                letter = Text(char, font_size=36)
                letter.move_to(line_mobj[i].get_center())
                new_line.add(letter)

            self.remove(line_mobj)
            self.add(new_line)

            i = 0
            while i < len(new_line):
                char = new_line[i].text

                # Check for S' as a unit
                if (char == "S" and
                    i + 1 < len(new_line) and new_line[i + 1].text == "'" and
                    line_idx == 2):

                    self.wait(0.5)
                    new_line[i].set_color(BLUE)
                    new_line[i + 1].set_color(BLUE)
                    keyword_to_expression[("S'", 2)].set_color(BLUE)
                    i += 2
                    continue
                
                if (char, line_idx) in keyword_to_expression:
                    new_line[i].set_color(BLUE)
                    keyword_to_expression[(char, line_idx)].set_color(BLUE)
                    self.wait(0.5)
                else:
                    new_line[i].set_color(YELLOW)

                self.wait(0.07)
                i += 1


        self.wait(2)
        self.play(FadeOut(new_line))
        self.play(probability_expression.animate.scale(0.5).to_corner(UL), explanation.animate.scale(0.5).to_corner(UL).shift(DOWN * 0.2))
        
        circle1 = Circle(radius=0.5, color=BLUE, fill_opacity=0.5).shift(LEFT*1.5)
        circle2 = Circle(radius=0.5, color=BLUE, fill_opacity=0.5).shift(RIGHT*1.5)
        text_inside1 = Text("S'", font_size=24).move_to(circle1.get_center())
        text_inside2 = Text("S'", font_size=24).move_to(circle2.get_center())
        arrow = Arrow(start=circle1.get_right(), end=circle2.get_left(), buff=0.1, color=WHITE)
        self.play(Create(circle1), Create(circle2), Create(text_inside1), Create(text_inside2), Create(arrow))
        
        
        self.wait(2)
from manim import *

class ZeroInitialization(Scene):
    def construct(self):
        
        title = Text("Zero Initialization", font_size=40)
        subtitle = Text("All weights = 0", font_size=30, color=YELLOW)
        title_group = VGroup(title, subtitle).arrange(DOWN)
        
        self.play(Write(title_group))
        self.wait()
        self.play(
            title_group.animate.scale(0.8).to_edge(UP)
        )
        
        layer1 = VGroup(*[Circle(radius=0.3) for _ in range(3)]).arrange(DOWN, buff=0.5)
        layer2 = VGroup(*[Circle(radius=0.3) for _ in range(4)]).arrange(DOWN, buff=0.5)
        layer3 = VGroup(*[Circle(radius=0.3) for _ in range(2)]).arrange(DOWN, buff=0.5)
        
        layers = VGroup(layer1, layer2, layer3).arrange(RIGHT, buff=2)
        
        connections = VGroup()
        
        for n1 in layer1:
            for n2 in layer2:
                conn = Line(n1.get_right(), n2.get_left(), stroke_opacity=0.5)
                connections.add(conn)
        
        for n2 in layer2:
            for n3 in layer3:
                conn = Line(n2.get_right(), n3.get_left(), stroke_opacity=0.5)
                connections.add(conn)

        network = VGroup(layers, connections)
        
        self.play(Create(network))
        self.wait()
        
        weight_label = MathTex("W = 0").next_to(connections[0].get_center(), UP)
        self.play(Write(weight_label))
        
        problem_text = Text(
            "Problem: All neurons will learn\nthe same features!",
            font_size=25,
            color=RED
        ).to_edge(DOWN)
        
        self.play(Write(problem_text))
        self.wait()
        
        identical_updates = Text(
            "Identical Updates",
            font_size=25,
            color=YELLOW
        ).next_to(problem_text, UP)
        
        arrows = VGroup()
        for conn in connections[:6]:  
            arrow = Arrow(
                start=conn.get_center(),
                end=conn.get_center() + UP * 0.2,
                color=YELLOW,
                buff=0
            )
            arrows.add(arrow)
        
        self.play(Write(identical_updates))
        self.play(Create(arrows))
        self.wait(2)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
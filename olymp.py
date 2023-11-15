class AlignTo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        c1, c2, c3 = [Circle(radius=1, color=BLACK, stroke_width=15) for _ in range(3)]
        arc1 = Arc(angle=3*PI/2, color=BLACK, stroke_width=15)
        arc2 = Arc(angle=PI/2, color=BLACK, stroke_width=15)
        arc4 = Arc(angle=3*PI/2, color=BLACK, stroke_width=15)
        arc5 = Arc(angle=PI/2, color=BLACK, stroke_width=15)
        arc6 = Arc(angle=PI/2, color=BLACK, stroke_width=15)
        self.play(*[Write(o) for o in [c1, c2,c3]])
        arc3 = Arc(angle=3*PI/2, color=BLACK, stroke_width=15)
        self.play(*[Write(o) for o in [arc1, arc2, arc3, arc4, arc5, arc6]])
        self.play(
            arc3.animate.rotate(PI/2),
        )
        self.play(
            arc3.animate.shift(LEFT * 1.125 + DOWN),
        )
        self.play(
            arc2.animate.shift(LEFT * 1.125 + DOWN),
        )
        self.play(
            arc1.animate.rotate(PI/2),
        )
        self.play(
            arc1.animate.shift(RIGHT * 1.125 + DOWN),
        )
        self.play(
            arc5.animate.shift(RIGHT * 1.125 + DOWN),
        )
        self.play(
            c1.animate.next_to(c3, LEFT),
            c2.animate.next_to(c3, RIGHT),
        )
        self.play(FadeOut(c3)) 
        self.play(
            arc4.animate.rotate(-PI/2),
        )
        self.play(
            arc6.animate.rotate(PI),
        )
        self.play(
            arc6.animate.shift(LEFT + DOWN),
        )
        
        self.play(
            c1.animate.set_color(BLUE),
            c2.animate.set_color(RED), 
        )

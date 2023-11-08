%%manim -v WARNING -qm AlignTo


class AlignTo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
    
        c1, c2, c3, c4, c5 = [Circle(radius=1, color=BLACK, stroke_width=15) for _ in range(5)]

        self.play(*[Write(o) for o in [c1, c2, c3, c4, c5]])
        

       
        self.play(
            c2.animate.next_to(c3, LEFT),
            c4.animate.next_to(c3, RIGHT),
            c5.animate.shift(RIGHT * 1.125 + DOWN ),
            c1.animate.shift(LEFT * 1.125 + DOWN ),
        )
        
        self.play(
            c1.animate.set_color(YELLOW),
            c2.animate.set_color(BLUE), 
            c4.animate.set_color(RED),
            c5.animate.set_color(GREEN),
        )

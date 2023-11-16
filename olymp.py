%%manim -v WARNING -qm AlignTo

class AlignTo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        c2, c3 = [Circle(radius=1, color=BLACK, stroke_width=15) for _ in range(2)]
        arc1 = Arc(angle=3*PI/2, color=BLACK, stroke_width=15)
        arc2 = Arc(angle=PI * 11/20, color=BLACK, stroke_width=15)
        arc4 = Arc(angle=3*PI/2, color=BLACK, stroke_width=15)
        arc6 = Arc(angle=PI/2, color=BLACK, stroke_width=15)
        self.play(*[Write(o) for o in [c3]])
        arc5 = Arc(angle=PI/2, color=BLACK, stroke_width=15)
        arc3 = Arc(angle=3*PI/2, color=BLACK, stroke_width=15)
        
        arc7 = Arc(angle=PI/2, color=BLACK, stroke_width=15)
        arc8 = Arc(angle=3*PI/2, color=BLACK, stroke_width=15)
        
        self.play(*[Write(o) for o in [arc8]])           
        self.play(*[Write(o) for o in [arc3]])
        self.play(*[Write(o) for o in [arc6]])
        self.play(*[Write(o) for o in [arc1]]) 
        self.play(*[Write(o) for o in [c2]])        
        self.play(*[Write(o) for o in [arc5]])    
        self.play(*[Write(o) for o in [arc4]])   
        self.play(*[Write(o) for o in [arc2]])  
        self.play(*[Write(o) for o in [arc7]])  
        self.play(
            arc3.animate.rotate(PI * 9/16),
        )
        self.play(
            arc3.animate.shift(LEFT * 1.125 + DOWN),
        )
        self.play(
            arc2.animate.shift(LEFT * 1.234 + DOWN * 0.96),
        )
        self.play(
            arc2.animate.rotate(PI * 1/16),
        )
        self.play(
            arc1.animate.rotate(PI * 10/16),
        )
        self.play(
            arc1.animate.shift(RIGHT * 1.232 + DOWN * 0.932),
        )
        self.play(
            arc5.animate.shift(RIGHT * 1.005 + DOWN * 0.805),
        )
        self.play(
            arc5.animate.rotate(PI * 2/16),
        )
        self.play(
            c2.animate.next_to(c3, RIGHT),
        )
        self.play(
            arc4.animate.rotate(-PI * 6/16),
        )
        self.play(
            arc6.animate.rotate(PI * -14/16),
        )
        self.play(
            arc6.animate.shift(LEFT * 0.755 + DOWN* 1.146),
        )
        
        self.play(
            arc7.animate.rotate(-PI * 4/16),
        )
        self.play(
            arc7.animate.next_to(c3, LEFT),
        )
        self.play(
            arc8.animate.rotate(PI * 4/16),
        )
        self.play(
            arc8.animate.next_to(c3, LEFT),
        )
        self.play(
            arc8.animate.shift(LEFT * 0.286 ),
        )
        self.play(FadeOut(c3)) 
        self.play(

            c2.animate.set_color(RED), 
            arc1.animate.set_color(GREEN),
            arc2.animate.set_color(YELLOW), 
            arc3.animate.set_color(YELLOW),
            arc5.animate.set_color(GREEN), 
            arc7.animate.set_color(BLUE),
            arc8.animate.set_color(BLUE), 
        )
         

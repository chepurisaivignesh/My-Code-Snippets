from subprocess import run
from typing_extensions import runtime
from manim import *

class hello1(Scene):
    def construct(self):
        
        c1=Circle(radius=1,fill_color=RED)
        c2=Circle(radius=2,fill_color=RED)
        c3=Circle(radius=3,fill_color=RED)
        c4=Circle(radius=4,fill_color=RED)
        c5=Circle(radius=5,fill_color=RED)
        
        self.play(DrawBorderThenFill(c5),run_time=0.5)
        
        self.play(DrawBorderThenFill(c4),run_time=0.5)
        
        self.play(DrawBorderThenFill(c3),run_time=0.5)
        
        self.play(DrawBorderThenFill(c2),run_time=0.5)
        
        self.play(DrawBorderThenFill(c1),run_time=0.5)
        
        self.play(c1.animate.to_edge(UP),c2.animate.to_edge(UP),
        c3.animate.to_edge(UP),c4.animate.to_edge(UP),c5.animate.to_edge(UP),run_time=1)
        
        self.wait()

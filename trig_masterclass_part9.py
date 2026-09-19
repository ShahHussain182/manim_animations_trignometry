"""
Trigonometry Masterclass - Part 9: Large Angles & Exact Values
==============================================================
A beginner-friendly visualization of how to break down angles 
larger than 360 degrees and calculate exact trigonometric values.

Run this file using:
manim -pql trig_masterclass_part9.py ExactValueProofs
"""

from dataclasses import dataclass, field
import numpy as np
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

# ==============================================================================
# 1. Configuration & Color Palette
# ==============================================================================
@dataclass(frozen=True)
class TrigConfig:
    radius: float = 2.4
    origin: np.ndarray = field(
        default_factory=lambda: np.array([-3.5, 0.0, 0.0])
    )
    C_BG: str = "#0b1017"
    C_AXES: str = "#4A5568"
    C_CIRCLE: str = "#FFFFFF"
    
    C_HL1: str = "#F1C40F"  # Yellow highlight
    C_HL2: str = "#00D2D3"  # Cyan highlight
    C_HL3: str = "#FF4444"  # Red highlight
    C_HL4: str = "#E056FD"  # Purple highlight

CONFIG = TrigConfig()
CYAN = CONFIG.C_HL2
YELLOW = CONFIG.C_HL1
RED = CONFIG.C_HL3
PURPLE = CONFIG.C_HL4
# ==============================================================================
# 2. Main Scene - Part 9
# ==============================================================================
class ExactValueProofs(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en"))
        self.camera.background_color = CONFIG.C_BG

        O = CONFIG.origin
        R = CONFIG.radius

        # ----------------------------------------------------------------------
        # ACT 1: Scene Layout & Introduction
        # ----------------------------------------------------------------------
        title = Title(
            r"Part 9: Calculating Large Angles \& Exact Values",
            font_size=32, color=WHITE
        )
        self.play(Write(title))

        # Geometric Plane (Left)
        axes = Axes(
            x_range=[-1.5, 1.5, 1], y_range=[-1.5, 1.5, 1],
            x_length=R * 2.3, y_length=R * 2.3,
            tips=True, axis_config={"color": CONFIG.C_AXES, "stroke_width": 1.5}
        ).move_to(O).shift(DOWN * 0.2)
        unit_circle = Circle(radius=R, color=CONFIG.C_CIRCLE, stroke_width=2).move_to(O).shift(DOWN * 0.2)

        # Derivation Board (Right)
        board_bg = RoundedRectangle(
            corner_radius=0.2, height=6.2, width=6.8,
            color=GRAY_D, fill_color="#121a24", fill_opacity=0.95
        ).to_edge(RIGHT, buff=0.2).shift(DOWN * 0.2)
        
        board_title = Text("Numerical Proofs", font_size=20, color=YELLOW).next_to(board_bg.get_top(), DOWN, buff=0.2)
        board_line = Line(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(board_title, DOWN, buff=0.15)

        with self.voiceover(
            text="Welcome to Part 9. Today, we will solve two complex numerical proofs. "
            "To do this, we must learn how to handle angles larger than 360 degrees, and calculate their exact fractional values."
        ) as tracker:
            self.play(
                Create(axes), Create(unit_circle),
                FadeIn(board_bg), Write(board_title), Create(board_line),
                run_time=tracker.duration
            )

        # ----------------------------------------------------------------------
        # ACT 2: Question (ii) - Handling Multiples of 360
        # ----------------------------------------------------------------------
        q2_task = MathTex(
            r"\sin(810^\circ)\sin(630^\circ) + \cos(135^\circ)\sin(225^\circ) = -\frac{1}{2}", 
            font_size=26
        ).next_to(board_line, DOWN, buff=0.3)
        self.play(Write(q2_task))

        with self.voiceover(
            text="Let's start with Question 2. Sine of 810 degrees looks intimidating. "
            "But remember, a circle simply repeats every 360 degrees."
        ) as tracker:
            self.wait(tracker.duration)

        # Tracing 810 degrees
        angle_tracker = ValueTracker(0)
        
        dot = always_redraw(lambda: Dot(
            axes.c2p(np.cos(angle_tracker.get_value()), np.sin(angle_tracker.get_value())),
            color=CONFIG.C_HL1, radius=0.08
        ))
        
        trace = TracedPath(dot.get_center, stroke_color=CONFIG.C_HL1, stroke_width=3)
        
        with self.voiceover(
            text="If we subtract 360 degrees twice... that is 720 degrees. 810 minus 720 leaves us with exactly 90 degrees! "
            "It lands perfectly at the top of the y-axis, where sine is exactly positive one."
        ) as tracker:
            self.add(trace, dot)
            self.play(angle_tracker.animate.set_value(np.radians(810)), run_time=3, rate_func=smooth)
            
            calc_810 = MathTex(r"\sin(810^\circ) = \sin(90^\circ) = 1", font_size=24, color=CONFIG.C_HL1).next_to(q2_task, DOWN, buff=0.4).align_to(q2_task, LEFT)
            self.play(Write(calc_810))
            self.wait(tracker.duration - 3.5)

        # Tracing 630 degrees
        self.play(FadeOut(trace), FadeOut(dot))
        angle_tracker.set_value(0)
        
        dot2 = always_redraw(lambda: Dot(
            axes.c2p(np.cos(angle_tracker.get_value()), np.sin(angle_tracker.get_value())),
            color=CONFIG.C_HL2, radius=0.08
        ))
        trace2 = TracedPath(dot2.get_center, stroke_color=CONFIG.C_HL2, stroke_width=3)
        
        with self.voiceover(
            text="Next is 630 degrees. Subtracting one full rotation of 360 leaves us with 270 degrees. "
            "This lands at the very bottom of the unit circle, where sine is negative one."
        ) as tracker:
            self.add(trace2, dot2)
            self.play(angle_tracker.animate.set_value(np.radians(630)), run_time=2.5, rate_func=smooth)
            
            calc_630 = MathTex(r"\sin(630^\circ) = \sin(270^\circ) = -1", font_size=24, color=CONFIG.C_HL2).next_to(calc_810, DOWN, buff=0.15).align_to(calc_810, LEFT)
            self.play(Write(calc_630))
            self.wait(tracker.duration - 3)
            
        self.play(FadeOut(trace2), FadeOut(dot2))

        # 135 and 225 degrees
        with self.voiceover(
            text="For the second half, we need the exact values of 135 and 225 degrees. "
            "Both of these are separated from the horizontal x-axis by a reference angle of exactly 45 degrees."
        ) as tracker:
            pt_135 = axes.c2p(np.cos(np.radians(135)), np.sin(np.radians(135)))
            pt_225 = axes.c2p(np.cos(np.radians(225)), np.sin(np.radians(225)))
            
            l_135 = Line(axes.c2p(0,0), pt_135, color=CONFIG.C_HL3, stroke_width=3)
            l_225 = Line(axes.c2p(0,0), pt_225, color=CONFIG.C_HL4, stroke_width=3)
            
            self.play(Create(l_135), Create(l_225))
            
            calc_135 = MathTex(r"\cos(135^\circ) = -\frac{1}{\sqrt{2}}", font_size=24, color=CONFIG.C_HL3).next_to(calc_630, DOWN, buff=0.15).align_to(calc_810, LEFT)
            calc_225 = MathTex(r"\sin(225^\circ) = -\frac{1}{\sqrt{2}}", font_size=24, color=CONFIG.C_HL4).next_to(calc_135, DOWN, buff=0.15).align_to(calc_810, LEFT)
            
            self.play(Write(calc_135), Write(calc_225), run_time=tracker.duration - 2)

        # Calculate final
        with self.voiceover(
            text="Because they are in the second and third quadrants, both values are negative one over root two. "
            "Now, we simply substitute these values back into the main equation and multiply."
        ) as tracker:
            eq_sub = MathTex(r"(1)(-1) + \left(-\frac{1}{\sqrt{2}}\right)\left(-\frac{1}{\sqrt{2}}\right)", font_size=28).next_to(calc_225, DOWN, buff=0.4).align_to(calc_810, LEFT)
            self.play(Write(eq_sub), run_time=2)
            
            eq_final = MathTex(r"= -1 + \frac{1}{2} = -\frac{1}{2}", font_size=28).next_to(eq_sub, RIGHT, buff=0.2)
            self.play(Write(eq_final), run_time=2)
            self.wait(tracker.duration - 4)

        box_q2 = SurroundingRectangle(VGroup(eq_sub, eq_final), color=WHITE, buff=0.1)
        self.play(Create(box_q2))
        self.wait(1)

        # ----------------------------------------------------------------------
        # ACT 3: Question (iv) - The Third Quadrant Sum
        # ----------------------------------------------------------------------
        # Clean up screen
        self.play(
            FadeOut(q2_task, calc_810, calc_630, calc_135, calc_225, eq_sub, eq_final, box_q2, l_135, l_225)
        )

        q4_task = MathTex(
            r"\sin(210^\circ) + \cos(240^\circ) + \tan(225^\circ) + \cot(225^\circ) = 1", 
            font_size=24
        ).next_to(board_line, DOWN, buff=0.3)
        self.play(Write(q4_task))

        with self.voiceover(
            text="Let's move to Question 4. Look closely at the angles: 210, 240, and 225 degrees. "
            "Every single one of these angles lives in the third quadrant!"
        ) as tracker:
            self.wait(1)

            # Draw the 3 lines in Q3
            pt_210 = axes.c2p(np.cos(np.radians(210)), np.sin(np.radians(210)))
            pt_240 = axes.c2p(np.cos(np.radians(240)), np.sin(np.radians(240)))
            
            l_210 = Line(axes.c2p(0,0), pt_210, color=YELLOW, stroke_width=3)
            l_240 = Line(axes.c2p(0,0), pt_240, color=CYAN, stroke_width=3)
            l_225_2 = Line(axes.c2p(0,0), pt_225, color=RED, stroke_width=3)
            
            arc_180 = ArcBetweenPoints(axes.c2p(1,0), axes.c2p(-1,0), radius=R*1.1, color=GRAY_B).shift(axes.c2p(0,0))
            lbl_180 = MathTex("180^\circ", font_size=20, color=GRAY_B).next_to(axes.c2p(-1,0), LEFT, buff=0.1)

            self.play(
                Create(arc_180), Write(lbl_180),
                Create(l_210), Create(l_240), Create(l_225_2),
                run_time=tracker.duration - 1
            )

        with self.voiceover(
            text="To find their exact values, we subtract 180 degrees to find their distance to the horizontal axis. "
            "For 210 degrees, the reference angle is 30. Since sine is negative in quadrant three, we get negative one-half."
        ) as tracker:
            q4_s1 = MathTex(r"\sin(210^\circ) = -\sin(30^\circ) = -\frac{1}{2}", font_size=22, color=YELLOW).next_to(q4_task, DOWN, buff=0.3).align_to(q4_task, LEFT)
            self.play(Write(q4_s1), Indicate(l_210, color=YELLOW), run_time=tracker.duration)

        with self.voiceover(
            text="For 240 degrees, the reference angle is 60. Cosine is also negative here, so we also get negative one-half."
        ) as tracker:
            q4_s2 = MathTex(r"\cos(240^\circ) = -\cos(60^\circ) = -\frac{1}{2}", font_size=22, color=CYAN).next_to(q4_s1, DOWN, buff=0.15).align_to(q4_task, LEFT)
            self.play(Write(q4_s2), Indicate(l_240, color=CYAN), run_time=tracker.duration)

        with self.voiceover(
            text="For 225 degrees, the reference angle is 45. Remember, Tangent and Cotangent are positive in the third quadrant! "
            "The tangent of 45 is one. And the cotangent of 45 is also one."
        ) as tracker:
            q4_s3 = MathTex(r"\tan(225^\circ) = +\tan(45^\circ) = 1", font_size=22, color=RED).next_to(q4_s2, DOWN, buff=0.15).align_to(q4_task, LEFT)
            q4_s4 = MathTex(r"\cot(225^\circ) = +\cot(45^\circ) = 1", font_size=22, color=RED).next_to(q4_s3, DOWN, buff=0.15).align_to(q4_task, LEFT)
            self.play(
                Write(q4_s3), Write(q4_s4), 
                Indicate(l_225_2, color=RED, scale_factor=1.2), 
                run_time=tracker.duration
            )

        with self.voiceover(
            text="We substitute these exact fractions back into our expression. Negative one-half minus one-half gives negative one. "
            "Negative one plus one plus one equals exactly one! The identity is proven."
        ) as tracker:
            q4_sub = MathTex(r"-\frac{1}{2} - \frac{1}{2} + 1 + 1", font_size=28).next_to(q4_s4, DOWN, buff=0.4).align_to(q4_task, LEFT)
            self.play(Write(q4_sub), run_time=2)
            
            q4_final = MathTex(r"= -1 + 2 = 1", font_size=28).next_to(q4_sub, RIGHT, buff=0.2)
            self.play(Write(q4_final), run_time=2)
            
            box_q4 = SurroundingRectangle(VGroup(q4_sub, q4_final), color=WHITE, buff=0.1)
            self.play(Create(box_q4))
            self.wait(tracker.duration - 4)

        self.wait(3)
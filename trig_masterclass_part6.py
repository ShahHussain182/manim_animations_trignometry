"""
Trigonometry Masterclass - Part 6: The Triple Angle Identities
==============================================================
A detailed step-by-step algebraic derivation of the Triple Angle formulas,
visualized alongside geometric angle stacking on the unit circle.

Run this file using:
manim -pql trig_masterclass_part6.py TripleAngleIdentities
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
    # Use a smaller angle so multiplying by 3 keeps it in the first/second quadrant comfortably
    alpha_deg: float = 22.0 
    radius: float = 2.5

    # Left-shifted origin to leave half the screen for the derivation board
    origin: np.ndarray = field(
        default_factory=lambda: np.array([-3.5, -0.5, 0.0])
    )

    C_BG: str = "#0b1017"
    C_AXES: str = "#4A5568"
    C_CIRCLE: str = "#FFFFFF"
    
    C_A1: str = "#00D2D3"         # Cyan (1x Alpha)
    C_A2: str = "#E056FD"         # Purple (2x Alpha)
    C_A3: str = "#F1C40F"         # Yellow (3x Alpha)
    C_SIN: str = "#FF4444"        # Red
    C_COS: str = "#3498DB"        # Blue

    @property
    def alpha(self) -> float:
        return np.radians(self.alpha_deg)

CONFIG = TrigConfig()

# ==============================================================================
# 2. Main Scene - Part 6
# ==============================================================================
class TripleAngleIdentities(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en"))
        self.camera.background_color = CONFIG.C_BG

        O = CONFIG.origin
        R = CONFIG.radius
        a = CONFIG.alpha

        # ----------------------------------------------------------------------
        # ACT 1: Scene Layout & Geometric Stacking
        # ----------------------------------------------------------------------
        title = Title(
            r"Part 6: Deriving the Triple Angle Identities",
            font_size=32,
            color=WHITE
        )
        self.play(Write(title))

        # Geometric Plane (Left)
        axes = Axes(
            x_range=[-1.5, 1.5, 1], y_range=[-1.5, 1.5, 1],
            x_length=R * 2.3, y_length=R * 2.3,
            tips=True, axis_config={"color": CONFIG.C_AXES, "stroke_width": 1.5}
        ).move_to(O)
        unit_circle = Circle(radius=R, color=CONFIG.C_CIRCLE, stroke_width=2).move_to(O)

        # Derivation Board (Right)
        board_bg = RoundedRectangle(
            corner_radius=0.2, height=6.2, width=6.8,
            color=GRAY_D, fill_color="#121a24", fill_opacity=0.95
        ).to_edge(RIGHT, buff=0.2).shift(DOWN * 0.2)
        
        board_title = Text("Triple Angle Expansion", font_size=20, color=YELLOW).next_to(board_bg.get_top(), DOWN, buff=0.2)
        board_line = Line(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(board_title, DOWN, buff=0.15)

        with self.voiceover(
            text="Welcome to Part 6. We have conquered double angles and half angles. "
            "Now, we face the ultimate algebraic challenge: the Triple Angle identities."
        ) as tracker:
            self.play(
                Create(axes), Create(unit_circle),
                FadeIn(board_bg), Write(board_title), Create(board_line),
                run_time=tracker.duration
            )

        # Visualize 1x, 2x, 3x angles
        pt_1 = O + R * np.array([np.cos(a), np.sin(a), 0])
        pt_2 = O + R * np.array([np.cos(2*a), np.sin(2*a), 0])
        pt_3 = O + R * np.array([np.cos(3*a), np.sin(3*a), 0])

        line_1 = Line(O, pt_1, color=CONFIG.C_A1, stroke_width=3)
        arc_1 = Arc(radius=0.5, start_angle=0, angle=a, arc_center=O, color=CONFIG.C_A1)
        lbl_1 = MathTex(r"\alpha", color=CONFIG.C_A1, font_size=20).next_to(arc_1, RIGHT, buff=0.05).shift(UP*0.05)

        line_2 = Line(O, pt_2, color=CONFIG.C_A2, stroke_width=3)
        arc_2 = Arc(radius=0.7, start_angle=a, angle=a, arc_center=O, color=CONFIG.C_A2)
        lbl_2 = MathTex(r"2\alpha", color=CONFIG.C_A2, font_size=20).next_to(arc_2, UR, buff=0.05)

        line_3 = Line(O, pt_3, color=CONFIG.C_A3, stroke_width=4)
        arc_3 = Arc(radius=0.9, start_angle=2*a, angle=a, arc_center=O, color=CONFIG.C_A3)
        lbl_3 = MathTex(r"3\alpha", color=CONFIG.C_A3, font_size=24).next_to(arc_3, UP, buff=0.05)

        with self.voiceover(
            text="Geometrically, a triple angle is simply stacking our base angle alpha three consecutive times."
        ) as tracker:
            self.play(Create(line_1), Create(arc_1), Write(lbl_1), run_time=1)
            self.play(Create(line_2), Create(arc_2), Write(lbl_2), run_time=1)
            self.play(Create(line_3), Create(arc_3), Write(lbl_3), run_time=tracker.duration - 2)

        # ----------------------------------------------------------------------
        # ACT 2: Deriving Sine Triple Angle
        # ----------------------------------------------------------------------
        eq_sin_base = MathTex(r"\sin(3\alpha)", font_size=24, color=WHITE).next_to(board_line, DOWN, buff=0.25).align_to(board_line, LEFT).shift(RIGHT*0.3)
        
        with self.voiceover(
            text="To find the formula for sine of three alpha, we split it apart. Three alpha is exactly two alpha plus one alpha."
        ) as tracker:
            self.play(Write(eq_sin_base))
            
            eq_step1 = MathTex(r"= \sin(2\alpha + \alpha)", font_size=24).next_to(eq_sin_base, RIGHT, buff=0.2)
            self.play(Write(eq_step1), run_time=tracker.duration - 1)

        with self.voiceover(
            text="Now, we use the Sine Sum Formula we derived in Part 4 to expand this expression."
        ) as tracker:
            eq_step2 = MathTex(
                r"= \sin(2\alpha)\cos(\alpha) + \cos(2\alpha)\sin(\alpha)", 
                font_size=22
            ).next_to(eq_step1, DOWN, buff=0.2).align_to(eq_step1, LEFT)
            self.play(Write(eq_step2), run_time=tracker.duration)

        with self.voiceover(
            text="Next, we substitute our double angle formulas. For sine two alpha, we plug in two sine alpha cosine alpha. "
            "For cosine two alpha, we will use the sine-only version: one minus two sine squared alpha."
        ) as tracker:
            eq_step3 = MathTex(
                r"= (2\sin\alpha\cos\alpha)\cos\alpha + (1 - 2\sin^2\alpha)\sin\alpha", 
                font_size=22
            ).next_to(eq_step2, DOWN, buff=0.2).align_to(eq_step1, LEFT)
            self.play(Write(eq_step3), run_time=tracker.duration)

        with self.voiceover(
            text="Let's distribute and clean this up. Cosine times cosine becomes cosine squared. "
            "On the right, distributing sine gives sine alpha minus two sine cubed alpha."
        ) as tracker:
            eq_step4 = MathTex(
                r"= 2\sin\alpha\cos^2\alpha + \sin\alpha - 2\sin^3\alpha", 
                font_size=22
            ).next_to(eq_step3, DOWN, buff=0.2).align_to(eq_step1, LEFT)
            self.play(Write(eq_step4), run_time=tracker.duration)

        with self.voiceover(
            text="We want our final identity entirely in terms of sine. So, we convert that cosine squared into one minus sine squared using the Pythagorean identity."
        ) as tracker:
            eq_step5 = MathTex(
                r"= 2\sin\alpha(1 - \sin^2\alpha) + \sin\alpha - 2\sin^3\alpha", 
                font_size=22
            ).next_to(eq_step4, DOWN, buff=0.2).align_to(eq_step1, LEFT)
            self.play(Write(eq_step5), run_time=tracker.duration)

        with self.voiceover(
            text="Distributing the two sine alpha, and combining all our like terms, we arrive at our final, elegant result."
        ) as tracker:
            self.wait(tracker.duration - 2)

        eq_sin_final = MathTex(
            r"\sin(3\alpha) = 3\sin\alpha - 4\sin^3\alpha", 
            font_size=28, color=CONFIG.C_SIN
        ).next_to(eq_step5, DOWN, buff=0.3).align_to(eq_sin_base, LEFT)
        
        box_sin_final = SurroundingRectangle(eq_sin_final, color=CONFIG.C_SIN, buff=0.1)

        self.play(Write(eq_sin_final), Create(box_sin_final))

        # Show the physical sine on the circle
        pt_3_x = O + R * np.array([np.cos(3*a), 0, 0])
        sin_3_line = Line(pt_3_x, pt_3, color=CONFIG.C_SIN, stroke_width=5)
        
        with self.voiceover(
            text="This polynomial equation perfectly calculates the vertical red height of our triple angle, using only the sine of our original alpha!"
        ) as tracker:
            self.play(Create(sin_3_line), run_time=tracker.duration)

        # ----------------------------------------------------------------------
        # ACT 3: Deriving Cosine Triple Angle
        # ----------------------------------------------------------------------
        # Clean up board for the next derivation
        board_group1 = VGroup(
            eq_sin_base, eq_step1, eq_step2, eq_step3, eq_step4, eq_step5, eq_sin_final, box_sin_final
        )
        
        self.play(board_group1.animate.scale(0.65).next_to(board_line, DOWN, buff=0.15).align_to(board_line, LEFT).shift(RIGHT*0.2))

        divider = DashedLine(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(board_group1, DOWN, buff=0.15)
        self.play(Create(divider))

        eq_cos_base = MathTex(r"\cos(3\alpha)", font_size=24, color=WHITE).next_to(divider, DOWN, buff=0.2).align_to(board_line, LEFT).shift(RIGHT*0.3)
        
        with self.voiceover(
            text="We can perform the exact same strategic expansion for cosine of three alpha."
        ) as tracker:
            self.play(Write(eq_cos_base))
            
            eq_c_step1 = MathTex(r"= \cos(2\alpha + \alpha)", font_size=24).next_to(eq_cos_base, RIGHT, buff=0.2)
            self.play(Write(eq_c_step1), run_time=tracker.duration - 1)

        with self.voiceover(
            text="Applying the Cosine sum formula gives us cosine two alpha cosine alpha minus sine two alpha sine alpha."
        ) as tracker:
            eq_c_step2 = MathTex(
                r"= \cos(2\alpha)\cos(\alpha) - \sin(2\alpha)\sin(\alpha)", 
                font_size=22
            ).next_to(eq_c_step1, DOWN, buff=0.15).align_to(eq_c_step1, LEFT)
            self.play(Write(eq_c_step2), run_time=tracker.duration)

        with self.voiceover(
            text="We substitute our double angles, this time using the cosine-only version for the first term to keep things consistent."
        ) as tracker:
            eq_c_step3 = MathTex(
                r"= (2\cos^2\alpha - 1)\cos\alpha - (2\sin\alpha\cos\alpha)\sin\alpha", 
                font_size=22
            ).next_to(eq_c_step2, DOWN, buff=0.15).align_to(eq_c_step1, LEFT)
            self.play(Write(eq_c_step3), run_time=tracker.duration)

        with self.voiceover(
            text="We expand, turning the right term into a sine squared, which we immediately replace with one minus cosine squared."
        ) as tracker:
            eq_c_step4 = MathTex(
                r"= 2\cos^3\alpha - \cos\alpha - 2(1 - \cos^2\alpha)\cos\alpha", 
                font_size=22
            ).next_to(eq_c_step3, DOWN, buff=0.15).align_to(eq_c_step1, LEFT)
            self.play(Write(eq_c_step4), run_time=tracker.duration)

        with self.voiceover(
            text="And after combining like terms, we get a beautiful mirror image of our sine formula."
        ) as tracker:
            self.wait(tracker.duration - 2)

        eq_cos_final = MathTex(
            r"\cos(3\alpha) = 4\cos^3\alpha - 3\cos\alpha", 
            font_size=28, color=CONFIG.C_COS
        ).next_to(eq_c_step4, DOWN, buff=0.25).align_to(eq_cos_base, LEFT)
        
        box_cos_final = SurroundingRectangle(eq_cos_final, color=CONFIG.C_COS, buff=0.1)

        self.play(Write(eq_cos_final), Create(box_cos_final))

        # Show the physical cosine on the circle
        cos_3_line = Line(O, pt_3_x, color=CONFIG.C_COS, stroke_width=5)
        
        with self.voiceover(
            text="This calculates the horizontal blue base of our stacked triangle."
        ) as tracker:
            self.play(Create(cos_3_line), run_time=tracker.duration)

        # ----------------------------------------------------------------------
        # ACT 4: Masterclass Conclusion
        # ----------------------------------------------------------------------
        with self.voiceover(
            text="We have reached the end of our masterclass. From a simple geometric unit circle, "
            "and a single fundamental law, we have painstakingly derived the entire classical universe of trigonometry. "
            "Math is not a list of unrelated formulas to memorize; it is a single, perfectly connected web of logic."
        ) as tracker:
            self.play(
                Indicate(box_sin_final, scale_factor=1.1, color=CONFIG.C_SIN),
                Indicate(box_cos_final, scale_factor=1.1, color=CONFIG.C_COS),
                run_time=3
            )
            
            # Pulse the stacked angles as a final visual flourish
            self.play(
                arc_1.animate.set_stroke(width=6),
                arc_2.animate.set_stroke(width=6),
                arc_3.animate.set_stroke(width=6),
                run_time=2, rate_func=there_and_back
            )
            
            self.wait(tracker.duration - 5)

        self.wait(3)
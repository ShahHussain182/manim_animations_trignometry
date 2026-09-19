"""
Trigonometry Masterclass - Part 3: Visualizing the Identities
=============================================================
This script visualizes the geometric and algebraic derivation 
of the three Pythagorean Trigonometric Identities side-by-side.

Run this file using:
manim -pql trig_masterclass_part3.py TrigIdentitiesMasterclass
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
    alpha_deg: float = 38.0 
    radius: float = 2.8

    # Left-shifted origin to leave exactly half the screen for the derivation board
    origin: np.ndarray = field(
        default_factory=lambda: np.array([-3.5, -1.0, 0.0])
    )

    C_BG: str = "#0b1017"
    C_AXES: str = "#4A5568"
    C_CIRCLE: str = "#FFFFFF"
    C_COS: str = "#F1C40F"        # Yellow
    C_SIN: str = "#FF4444"        # Red
    C_TAN: str = "#00FFFF"        # Cyan
    C_COT: str = "#3388FF"        # Blue
    C_SEC: str = "#FF00FF"        # Magenta
    C_CSC: str = "#00FF00"        # Green
    
    @property
    def alpha(self) -> float:
        return np.radians(self.alpha_deg)

CONFIG = TrigConfig()

# ==============================================================================
# 2. Main Scene - Part 3
# ==============================================================================
class TrigIdentitiesMasterclass(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en"))
        self.camera.background_color = CONFIG.C_BG

        O = CONFIG.origin
        R = CONFIG.radius
        a = CONFIG.alpha

        # ----------------------------------------------------------------------
        # ACT 1: Scene Layout (Geometry Left, Derivation Right)
        # ----------------------------------------------------------------------
        title = Title(
            r"Part 3: Deriving the Trigonometric Identities",
            font_size=36,
            color=WHITE
        )
        self.play(Write(title))

        # Setup Geometric Plane (Left)
        axes = Axes(
            x_range=[-0.5, 1.8, 1], y_range=[-0.5, 1.8, 1],
            x_length=R * 2.3, y_length=R * 2.3,
            tips=True, axis_config={"color": CONFIG.C_AXES, "stroke_width": 1.5}
        ).move_to(O, coor_mask=np.array([1, 1, 0]))

        unit_circle = Circle(radius=R, color=CONFIG.C_CIRCLE, stroke_width=2).move_to(O)

        # Setup Derivation Board (Right)
        board_bg = RoundedRectangle(
            corner_radius=0.2, height=6.0, width=6.5,
            color=GRAY_D, fill_color="#121a24", fill_opacity=0.95
        ).to_edge(RIGHT, buff=0.3).shift(DOWN * 0.2)
        
        board_title = Text("Algebraic Derivation", font_size=20, color=YELLOW).next_to(board_bg.get_top(), DOWN, buff=0.25)
        board_line = Line(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(board_title, DOWN, buff=0.15)

        with self.voiceover(
            text="Welcome to Part 3. We have seen what the trigonometric functions look like. "
            "Now, let's prove the famous mathematical identities that bind them together, "
            "combining step-by-step algebra on the right with physical geometry on the left."
        ) as tracker:
            self.play(Create(axes), Create(unit_circle), FadeIn(board_bg), Write(board_title), Create(board_line), run_time=tracker.duration)

        # ----------------------------------------------------------------------
        # ACT 2: The First Pythagorean Identity
        # ----------------------------------------------------------------------
        pt_P = O + R * np.array([np.cos(a), np.sin(a), 0])
        pt_x = O + R * np.array([np.cos(a), 0, 0])

        base_cos = Line(O, pt_x, color=CONFIG.C_COS, stroke_width=5)
        base_sin = Line(pt_x, pt_P, color=CONFIG.C_SIN, stroke_width=5)
        base_hyp = Line(O, pt_P, color=WHITE, stroke_width=5)

        lbl_cos = MathTex(r"\cos\alpha", font_size=22, color=CONFIG.C_COS).next_to(base_cos, DOWN, buff=0.1)
        lbl_sin = MathTex(r"\sin\alpha", font_size=22, color=CONFIG.C_SIN).next_to(base_sin, RIGHT, buff=0.1)
        lbl_one = MathTex("1", font_size=22, color=WHITE).next_to(base_hyp.get_center(), UL, buff=0.05)

        base_triangle = VGroup(base_cos, base_sin, base_hyp)

        with self.voiceover(
            text="We begin with our foundational right triangle inscribed in the unit circle. "
            "Its horizontal base is cosine, its vertical height is sine, and its hypotenuse is exactly 1."
        ) as tracker:
            self.play(Create(base_cos), Write(lbl_cos), Create(base_sin), Write(lbl_sin), Create(base_hyp), Write(lbl_one), run_time=tracker.duration)

        # Derivation steps
        eq1_step1 = MathTex(r"a^2 + b^2 = c^2", font_size=26).next_to(board_line, DOWN, buff=0.4)
        eq1_step2 = MathTex(r"(\cos\alpha)^2 + (\sin\alpha)^2 = (1)^2", font_size=28).next_to(eq1_step1, DOWN, buff=0.3)
        eq1_final = MathTex(r"\cos^2\alpha + \sin^2\alpha = 1", font_size=32, color=YELLOW).next_to(eq1_step2, DOWN, buff=0.3)
        box_eq1 = SurroundingRectangle(eq1_final, color=YELLOW, buff=0.15)

        with self.voiceover(
            text="By the Pythagorean theorem, the base squared plus the height squared equals the hypotenuse squared. "
            "Substituting our lengths gives us the first and most famous trigonometric identity."
        ) as tracker:
            self.play(Write(eq1_step1), run_time=1.5)
            self.play(TransformFromCopy(VGroup(lbl_cos, lbl_sin, lbl_one), eq1_step2), run_time=2)
            self.play(Write(eq1_final), Create(box_eq1), run_time=1.5)
            self.wait(1)

        # ----------------------------------------------------------------------
        # ACT 3: The Tangent-Secant Identity (Algebra + Geometry)
        # ----------------------------------------------------------------------
        # Shift eq1 up to make room
        eq1_group = VGroup(eq1_step1, eq1_step2, eq1_final, box_eq1)
        self.play(eq1_group.animate.scale(0.7).to_corner(UR, buff=0.5).shift(LEFT*0.3 + DOWN*1.5))

        divider1 = DashedLine(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(eq1_group, DOWN, buff=0.3)
        self.play(Create(divider1))

        # Algebra
        eq2_step1 = MathTex(r"\frac{\cos^2\alpha}{\cos^2\alpha} + \frac{\sin^2\alpha}{\cos^2\alpha} = \frac{1}{\cos^2\alpha}", font_size=28).next_to(divider1, DOWN, buff=0.4)
        eq2_final = MathTex(r"1 + \tan^2\alpha = \sec^2\alpha", font_size=32, color=CONFIG.C_TAN).next_to(eq2_step1, DOWN, buff=0.3)
        box_eq2 = SurroundingRectangle(eq2_final, color=CONFIG.C_TAN, buff=0.15)

        with self.voiceover(
            text="What happens if we divide every term in this equation by cosine squared alpha? "
            "Cosine over cosine becomes 1. Sine over cosine is Tangent. And one over cosine is Secant."
        ) as tracker:
            self.play(Write(eq2_step1), run_time=2.5)
            self.play(Write(eq2_final), Create(box_eq2), run_time=2)

        # Geometry scaling!
        pt_T_base = O + R * np.array([1, 0, 0])
        pt_T_top = O + R * np.array([1, np.tan(a), 0])
        
        scaled_cos = Line(O, pt_T_base, color=WHITE, stroke_width=5)
        scaled_sin = Line(pt_T_base, pt_T_top, color=CONFIG.C_TAN, stroke_width=5)
        scaled_hyp = Line(O, pt_T_top, color=CONFIG.C_SEC, stroke_width=5)
        
        lbl_s_one = MathTex("1", font_size=22, color=WHITE).next_to(scaled_cos, DOWN, buff=0.1)
        lbl_s_tan = MathTex(r"\tan\alpha", font_size=22, color=CONFIG.C_TAN).next_to(scaled_sin, RIGHT, buff=0.1)
        lbl_s_sec = MathTex(r"\sec\alpha", font_size=22, color=CONFIG.C_SEC).next_to(scaled_hyp.get_center(), UL, buff=0.05)

        tangent_line_ref = Line(pt_T_base + DOWN*0.5, pt_T_base + UP*R*1.5, color=GRAY, stroke_width=1.5)

        with self.voiceover(
            text="But what does this division mean geometrically? Dividing by cosine scales our entire triangle up by a factor of one over cosine. "
            "Our base stretches to a length of exactly one, touching the tangent line."
        ) as tracker:
            self.play(Create(tangent_line_ref))
            self.play(
                TransformFromCopy(base_cos, scaled_cos), 
                TransformFromCopy(lbl_cos, lbl_s_one),
                run_time=2
            )
        
        with self.voiceover(
            text="The height scales up to become the literal tangent of alpha. And the hypotenuse extends to become the secant."
        ) as tracker:
            self.play(
                TransformFromCopy(base_sin, scaled_sin), 
                TransformFromCopy(lbl_sin, lbl_s_tan),
                TransformFromCopy(base_hyp, scaled_hyp),
                TransformFromCopy(lbl_one, lbl_s_sec),
                run_time=3
            )
            self.play(Indicate(box_eq2, color=CONFIG.C_TAN))

        # ----------------------------------------------------------------------
        # ACT 4: The Cotangent-Cosecant Identity
        # ----------------------------------------------------------------------
        # Fade out tangent triangle to make space
        tan_group = VGroup(scaled_cos, scaled_sin, scaled_hyp, lbl_s_one, lbl_s_tan, lbl_s_sec, tangent_line_ref)
        self.play(FadeOut(tan_group), run_time=1)

        # Shift eq2 up
        eq2_group = VGroup(eq2_step1, eq2_final, box_eq2)
        self.play(eq2_group.animate.scale(0.8).next_to(divider1, DOWN, buff=0.2).align_to(eq1_step1, LEFT))
        
        divider2 = DashedLine(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(eq2_group, DOWN, buff=0.2)
        self.play(Create(divider2))

        # Algebra
        eq3_step1 = MathTex(r"\frac{\cos^2\alpha}{\sin^2\alpha} + \frac{\sin^2\alpha}{\sin^2\alpha} = \frac{1}{\sin^2\alpha}", font_size=28).next_to(divider2, DOWN, buff=0.4)
        eq3_final = MathTex(r"\cot^2\alpha + 1 = \csc^2\alpha", font_size=32, color=CONFIG.C_COT).next_to(eq3_step1, DOWN, buff=0.3)
        box_eq3 = SurroundingRectangle(eq3_final, color=CONFIG.C_COT, buff=0.15)

        with self.voiceover(
            text="Finally, let's return to the original equation and divide every term by sine squared alpha instead. "
            "Cosine over sine gives Cotangent. Sine over sine is 1. And one over sine is Cosecant."
        ) as tracker:
            self.play(Write(eq3_step1), run_time=2.5)
            self.play(Write(eq3_final), Create(box_eq3), run_time=2)

        # Geometry scaling!
        pt_C_base = O + R * np.array([0, 1, 0])
        pt_C_right = O + R * np.array([1/np.tan(a), 1, 0])
        
        scaled_cot_sin = Line(O, pt_C_base, color=WHITE, stroke_width=5) # vertical leg = 1
        scaled_cot_cos = Line(pt_C_base, pt_C_right, color=CONFIG.C_COT, stroke_width=5) # horiz leg = cot
        scaled_cot_hyp = Line(O, pt_C_right, color=CONFIG.C_CSC, stroke_width=5) # hyp = csc
        
        lbl_c_one = MathTex("1", font_size=22, color=WHITE).next_to(scaled_cot_sin, LEFT, buff=0.1)
        lbl_c_cot = MathTex(r"\cot\alpha", font_size=22, color=CONFIG.C_COT).next_to(scaled_cot_cos, UP, buff=0.1)
        lbl_c_csc = MathTex(r"\csc\alpha", font_size=22, color=CONFIG.C_CSC).next_to(scaled_cot_hyp.get_center(), DR, buff=0.05)

        cotangent_line_ref = Line(pt_C_base + LEFT*0.5, pt_C_base + RIGHT*R*1.5, color=GRAY, stroke_width=1.5)

        with self.voiceover(
            text="Geometrically, dividing by sine scales our base triangle upwards by a factor of one over sine. "
            "Our vertical height stretches to exactly one, touching the upper horizontal boundary of our diagram."
        ) as tracker:
            self.play(Create(cotangent_line_ref))
            self.play(
                TransformFromCopy(base_sin, scaled_cot_sin), 
                TransformFromCopy(lbl_sin, lbl_c_one),
                run_time=2
            )
        
        with self.voiceover(
            text="The base scales up to become the cotangent. And the hypotenuse stretches completely to the y-intercept, forming the cosecant. "
            "Another perfect Pythagorean triangle."
        ) as tracker:
            self.play(
                TransformFromCopy(base_cos, scaled_cot_cos), 
                TransformFromCopy(lbl_cos, lbl_c_cot),
                TransformFromCopy(base_hyp, scaled_cot_hyp),
                TransformFromCopy(lbl_one, lbl_c_csc),
                run_time=3
            )
            self.play(Indicate(box_eq3, color=CONFIG.C_COT))

        # ----------------------------------------------------------------------
        # ACT 5: Conclusion
        # ----------------------------------------------------------------------
        with self.voiceover(
            text="And there you have it. The three Pythagorean identities are not just random algebraic formulas to memorize. "
            "They are literal descriptions of three similar right triangles, perfectly embedded in the geometry of the unit circle."
        ) as tracker:
            # Bring back Tangent triangle for a grand final shot
            self.play(FadeIn(tan_group), run_time=2)
            self.wait(tracker.duration - 2)

        self.wait(3)
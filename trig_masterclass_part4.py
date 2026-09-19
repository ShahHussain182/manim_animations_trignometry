"""
Trigonometry Masterclass - Part 4: Expanding the Fundamental Law
================================================================
Deriving the Sum and Double Angle identities from the Fundamental Law 
using dynamic algebraic substitution and geometric angle stacking.

Run this file using:
manim -pql trig_masterclass_part4.py FundamentalIdentities
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
    alpha_deg: float = 40.0
    beta_deg: float = 25.0
    radius: float = 2.5

    # Left-shifted origin to leave half the screen for the derivation board
    origin: np.ndarray = field(
        default_factory=lambda: np.array([-3.5, -0.5, 0.0])
    )

    C_BG: str = "#0b1017"
    C_AXES: str = "#4A5568"
    C_CIRCLE: str = "#FFFFFF"
    
    # Consistent color coding
    C_ALPHA: str = "#00D2D3"      # Cyan
    C_BETA: str = "#E056FD"       # Purple/Pink
    C_SUM: str = "#F1C40F"        # Yellow
    C_COS: str = "#F1C40F"        # Yellow
    C_SIN: str = "#FF4444"        # Red

    @property
    def alpha(self) -> float:
        return np.radians(self.alpha_deg)

    @property
    def beta(self) -> float:
        return np.radians(self.beta_deg)

CONFIG = TrigConfig()

# ==============================================================================
# 2. Main Scene - Part 4
# ==============================================================================
class FundamentalIdentities(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en"))
        self.camera.background_color = CONFIG.C_BG

        O = CONFIG.origin
        R = CONFIG.radius
        a = CONFIG.alpha
        b = CONFIG.beta

        # ----------------------------------------------------------------------
        # ACT 1: Scene Layout & The Fundamental Law
        # ----------------------------------------------------------------------
        title = Title(
            r"Part 4: Expanding the Fundamental Law",
            font_size=34,
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
        
        board_title = Text("Identity Derivations", font_size=20, color=YELLOW).next_to(board_bg.get_top(), DOWN, buff=0.2)
        board_line = Line(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(board_title, DOWN, buff=0.15)

        with self.voiceover(
            text="Welcome to Part 4. The equation we derived at the very beginning of this masterclass "
            "is called the Fundamental Law of Trigonometry. Let's place it at the top of our board."
        ) as tracker:
            self.play(
                Create(axes), Create(unit_circle),
                FadeIn(board_bg), Write(board_title), Create(board_line),
                run_time=tracker.duration
            )

        eq_base = MathTex(
            r"\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta",
            font_size=26, color=WHITE
        ).next_to(board_line, DOWN, buff=0.35)
        
        box_base = SurroundingRectangle(eq_base, color=WHITE, buff=0.1)

        self.play(Write(eq_base), Create(box_base))

        # ----------------------------------------------------------------------
        # ACT 2: Cosine Sum Formula (Substituting -Beta)
        # ----------------------------------------------------------------------
        with self.voiceover(
            text="Every other major sum and double angle formula springs from this single seed. "
            "For instance, what if we want to add two angles instead of subtracting them?"
        ) as tracker:
            self.wait(tracker.duration)

        # Draw Angle Alpha on circle
        pt_alpha = O + R * np.array([np.cos(a), np.sin(a), 0])
        line_alpha = Line(O, pt_alpha, color=CONFIG.C_ALPHA, stroke_width=3)
        arc_alpha = Arc(radius=0.5, start_angle=0, angle=a, arc_center=O, color=CONFIG.C_ALPHA)
        lbl_alpha = MathTex(r"\alpha", color=CONFIG.C_ALPHA, font_size=20).next_to(arc_alpha, RIGHT, buff=0.05).shift(UP*0.05)
        
        self.play(Create(line_alpha), Create(arc_alpha), Write(lbl_alpha))

        # Draw Angle Beta added to Alpha
        pt_sum = O + R * np.array([np.cos(a + b), np.sin(a + b), 0])
        line_sum = Line(O, pt_sum, color=CONFIG.C_BETA, stroke_width=3)
        arc_beta = Arc(radius=0.7, start_angle=a, angle=b, arc_center=O, color=CONFIG.C_BETA)
        lbl_beta = MathTex(r"\beta", color=CONFIG.C_BETA, font_size=20).next_to(arc_beta, UP, buff=0.05)

        with self.voiceover(
            text="On the circle, adding angle beta means rotating further counter-clockwise. "
            "Algebraically, we simply substitute negative beta into our fundamental law."
        ) as tracker:
            self.play(Create(line_sum), Create(arc_beta), Write(lbl_beta), run_time=tracker.duration)

        eq_sub1 = MathTex(
            r"\text{Let } \beta \rightarrow -\beta", 
            font_size=24, color=GRAY_B
        ).next_to(box_base, DOWN, buff=0.3).align_to(eq_base, LEFT)

        eq_sub2 = MathTex(
            r"\cos(\alpha - (-\beta)) = \cos\alpha\cos(-\beta) + \sin\alpha\sin(-\beta)", 
            font_size=24
        ).next_to(eq_sub1, DOWN, buff=0.2).align_to(eq_base, LEFT)

        self.play(Write(eq_sub1), run_time=1)
        self.play(Write(eq_sub2), run_time=2.5)

        with self.voiceover(
            text="Recall that cosine is an even function, meaning cosine of negative beta is just cosine beta. "
            "Sine is an odd function, so the negative sign factors out to the front."
        ) as tracker:
            self.wait(tracker.duration)

        eq_cos_sum = MathTex(
            r"\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta", 
            font_size=28, color=CONFIG.C_SUM
        ).next_to(eq_sub2, DOWN, buff=0.25).align_to(eq_base, LEFT)
        
        box_cos_sum = SurroundingRectangle(eq_cos_sum, color=CONFIG.C_SUM, buff=0.1)

        arc_sum = Arc(radius=0.9, start_angle=0, angle=a+b, arc_center=O, color=CONFIG.C_SUM, stroke_width=2.5)
        lbl_sum = MathTex(r"\alpha + \beta", color=CONFIG.C_SUM, font_size=20).next_to(arc_sum, UL, buff=0.05)

        self.play(Write(eq_cos_sum), Create(box_cos_sum), Create(arc_sum), Write(lbl_sum), run_time=2)

        # ----------------------------------------------------------------------
        # ACT 3: The Double Angle Cosine Formula
        # ----------------------------------------------------------------------
        with self.voiceover(
            text="Now that we have the sum formula, what happens if both angles are exactly the same?"
        ) as tracker:
            self.wait(tracker.duration)

        # Clean board partially
        group_to_fade = VGroup(eq_sub1, eq_sub2)
        self.play(
            FadeOut(group_to_fade),
            VGroup(eq_cos_sum, box_cos_sum).animate.next_to(box_base, DOWN, buff=0.3).align_to(eq_base, LEFT)
        )
        
        divider = DashedLine(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(box_cos_sum, DOWN, buff=0.25)
        self.play(Create(divider))

        # Geometry Update: Set Beta = Alpha
        pt_double = O + R * np.array([np.cos(a + a), np.sin(a + a), 0])
        line_double = Line(O, pt_double, color=CONFIG.C_ALPHA, stroke_width=3)
        arc_beta_new = Arc(radius=0.7, start_angle=a, angle=a, arc_center=O, color=CONFIG.C_ALPHA)
        lbl_beta_new = MathTex(r"\alpha", color=CONFIG.C_ALPHA, font_size=20).next_to(arc_beta_new, UP, buff=0.05)

        with self.voiceover(
            text="Let us set beta equal to alpha. On our circle, this doubles our initial angle."
        ) as tracker:
            self.play(
                Transform(line_sum, line_double),
                Transform(arc_beta, arc_beta_new),
                Transform(lbl_beta, lbl_beta_new),
                run_time=tracker.duration
            )

        eq_dbl1 = MathTex(
            r"\text{Let } \beta = \alpha", 
            font_size=24, color=GRAY_B
        ).next_to(divider, DOWN, buff=0.25).align_to(eq_base, LEFT)

        eq_dbl2 = MathTex(
            r"\cos(\alpha + \alpha) = \cos\alpha\cos\alpha - \sin\alpha\sin\alpha", 
            font_size=24
        ).next_to(eq_dbl1, DOWN, buff=0.2).align_to(eq_base, LEFT)

        self.play(Write(eq_dbl1), run_time=1)
        self.play(Write(eq_dbl2), run_time=2)

        eq_cos_dbl = MathTex(
            r"\cos(2\alpha) = \cos^2\alpha - \sin^2\alpha", 
            font_size=28, color=CONFIG.C_COS
        ).next_to(eq_dbl2, DOWN, buff=0.25).align_to(eq_base, LEFT)
        
        box_cos_dbl = SurroundingRectangle(eq_cos_dbl, color=CONFIG.C_COS, buff=0.1)

        arc_dbl = Arc(radius=0.9, start_angle=0, angle=2*a, arc_center=O, color=CONFIG.C_COS, stroke_width=3)
        lbl_dbl = MathTex(r"2\alpha", color=CONFIG.C_COS, font_size=22).next_to(arc_dbl, UL, buff=0.05)

        with self.voiceover(
            text="Algebraically, cosine times cosine becomes cosine squared, and sine times sine becomes sine squared. "
            "This gives us the Double Angle Formula for Cosine."
        ) as tracker:
            self.play(
                Transform(arc_sum, arc_dbl),
                Transform(lbl_sum, lbl_dbl),
                Write(eq_cos_dbl), 
                Create(box_cos_dbl), 
                run_time=tracker.duration
            )

        # ----------------------------------------------------------------------
        # ACT 4: Sine Double Angle Formula 
        # ----------------------------------------------------------------------
        # Shift everything up to fit the final formula
        board_contents = VGroup(
            eq_base, box_base, eq_cos_sum, box_cos_sum, divider, 
            eq_dbl1, eq_dbl2, eq_cos_dbl, box_cos_dbl
        )
        
        self.play(board_contents.animate.scale(0.85).shift(UP * 0.6))
        
        divider2 = DashedLine(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(box_cos_dbl, DOWN, buff=0.25)
        self.play(Create(divider2))

        eq_sin_sum_known = MathTex(
            r"\text{Similarly, } \sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta", 
            font_size=22, color=GRAY_A
        ).next_to(divider2, DOWN, buff=0.25).align_to(eq_base, LEFT)

        eq_sin_dbl_sub = MathTex(
            r"\sin(\alpha + \alpha) = \sin\alpha\cos\alpha + \cos\alpha\sin\alpha", 
            font_size=22
        ).next_to(eq_sin_sum_known, DOWN, buff=0.15).align_to(eq_base, LEFT)
        
        eq_sin_dbl = MathTex(
            r"\sin(2\alpha) = 2\sin\alpha\cos\alpha", 
            font_size=28, color=CONFIG.C_SIN
        ).next_to(eq_sin_dbl_sub, DOWN, buff=0.2).align_to(eq_base, LEFT).shift(RIGHT*1)

        box_sin_dbl = SurroundingRectangle(eq_sin_dbl, color=CONFIG.C_SIN, buff=0.1)

        with self.voiceover(
            text="By a similar process using co-functions, we can find the Sine sum formula. "
            "If we set beta equal to alpha in this equation, we get sine alpha cosine alpha, twice! "
            "This gives us our final identity for today: the Double Angle Formula for Sine."
        ) as tracker:
            self.play(Write(eq_sin_sum_known), run_time=2)
            self.play(Write(eq_sin_dbl_sub), run_time=2)
            self.play(Write(eq_sin_dbl), Create(box_sin_dbl), run_time=2)
            self.wait(tracker.duration - 6)

        # Grand Finale Highlight
        with self.voiceover(
            text="Notice how purely abstract algebraic manipulation matches perfectly with stacking rigid geometric shapes on a circle. "
            "One fundamental law unlocks the entire universe of trigonometry."
        ) as tracker:
            self.play(
                Indicate(box_base, color=WHITE, scale_factor=1.1),
                run_time=2
            )
            self.play(
                Indicate(box_cos_dbl, color=CONFIG.C_COS, scale_factor=1.1),
                Indicate(box_sin_dbl, color=CONFIG.C_SIN, scale_factor=1.1),
                run_time=3
            )
            self.wait(tracker.duration - 5)

        self.wait(2)
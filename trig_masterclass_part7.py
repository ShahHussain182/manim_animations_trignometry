"""
Trigonometry Masterclass - Part 7: Product-to-Sum Identities
============================================================
Deriving the product of sines and cosines as sums or differences.
Features algebraic elimination alongside dynamic wave interference visualization.

Run this file using:
manim -pql trig_masterclass_part7.py ProductToSumIdentities
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
    # Left-shifted origin to leave half the screen for the derivation board
    origin: np.ndarray = field(
        default_factory=lambda: np.array([-3.5, 0.0, 0.0])
    )

    C_BG: str = "#0b1017"
    C_AXES: str = "#4A5568"
    C_WAVE1: str = "#FF4444"      # Red (Sine)
    C_WAVE2: str = "#F1C40F"      # Yellow (Cosine)
    C_PRODUCT: str = "#00D2D3"    # Cyan (Resulting Wave)
    
    C_EQ: str = "#FFFFFF"

CONFIG = TrigConfig()

# ==============================================================================
# 2. Main Scene - Part 7
# ==============================================================================
class ProductToSumIdentities(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en"))
        self.camera.background_color = CONFIG.C_BG

        O = CONFIG.origin

        # ----------------------------------------------------------------------
        # ACT 1: Scene Layout & Introduction
        # ----------------------------------------------------------------------
        title = Title(
            r"Part 7: Product-to-Sum Identities",
            font_size=34,
            color=WHITE
        )
        self.play(Write(title))

        # Waveform Graph (Left)
        axes = Axes(
            x_range=[0, 4 * PI, PI/2], 
            y_range=[-1.5, 1.5, 1],
            x_length=6.0, 
            y_length=5.0,
            tips=False, 
            axis_config={"color": CONFIG.C_AXES, "stroke_width": 1.5}
        ).move_to(O).shift(DOWN * 0.2)

        # Derivation Board (Right)
        board_bg = RoundedRectangle(
            corner_radius=0.2, height=6.2, width=7.0,
            color=GRAY_D, fill_color="#121a24", fill_opacity=0.95
        ).to_edge(RIGHT, buff=0.15).shift(DOWN * 0.2)
        
        board_title = Text("System of Identities", font_size=20, color=YELLOW).next_to(board_bg.get_top(), DOWN, buff=0.2)
        board_line = Line(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(board_title, DOWN, buff=0.15)

        with self.voiceover(
            text="Welcome to Part 7. In physics, engineering, and signal processing, we frequently need to multiply two waves together. "
            "To do this, we treat our fundamental laws as a system of equations."
        ) as tracker:
            self.play(
                Create(axes), FadeIn(board_bg), Write(board_title), Create(board_line),
                run_time=tracker.duration
            )

        # ----------------------------------------------------------------------
        # ACT 2: Deriving Sine * Cosine
        # ----------------------------------------------------------------------
        eq_sin_add = MathTex(
            r"\sin(\alpha + \beta) &= \sin\alpha\cos\beta + \cos\alpha\sin\beta", 
            font_size=24
        ).next_to(board_line, DOWN, buff=0.3).shift(LEFT * 0.2)
        
        eq_sin_sub = MathTex(
            r"\sin(\alpha - \beta) &= \sin\alpha\cos\beta - \cos\alpha\sin\beta", 
            font_size=24
        ).next_to(eq_sin_add, DOWN, buff=0.2).align_to(eq_sin_add, LEFT)

        with self.voiceover(
            text="Let's bring back the Sine addition and subtraction formulas from Part 4, and stack them vertically."
        ) as tracker:
            self.play(Write(eq_sin_add), run_time=1.5)
            self.play(Write(eq_sin_sub), run_time=1.5)
            self.wait(tracker.duration - 3)

        add_line = Line(
            eq_sin_sub.get_left() + DOWN*0.2, 
            eq_sin_sub.get_right() + DOWN*0.2 + RIGHT*0.5, 
            color=GRAY
        )
        plus_sign = MathTex("+", font_size=24).next_to(add_line, LEFT, buff=0.1).shift(UP*0.2)

        eq_sum_result = MathTex(
            r"\sin(\alpha + \beta) + \sin(\alpha - \beta) &= 2\sin\alpha\cos\beta", 
            font_size=24
        ).next_to(add_line, DOWN, buff=0.2).align_to(eq_sin_add, LEFT)

        strike_1 = Line(eq_sin_add[0][14:22].get_left(), eq_sin_add[0][14:22].get_right(), color=RED)
        strike_2 = Line(eq_sin_sub[0][14:22].get_left(), eq_sin_sub[0][14:22].get_right(), color=RED)

        with self.voiceover(
            text="What happens if we simply add these two equations together? "
            "The mixed terms on the far right are identical but have opposite signs, so they completely cancel out!"
        ) as tracker:
            self.play(Create(add_line), Write(plus_sign), run_time=1)
            self.play(Create(strike_1), Create(strike_2), run_time=1.5)
            self.play(Write(eq_sum_result), run_time=2)

        eq_prod_1 = MathTex(
            r"\sin\alpha\cos\beta = \frac{1}{2}[\sin(\alpha + \beta) + \sin(\alpha - \beta)]", 
            font_size=26, color=CONFIG.C_PRODUCT
        ).next_to(eq_sum_result, DOWN, buff=0.3).align_to(eq_sin_add, LEFT)
        
        box_prod_1 = SurroundingRectangle(eq_prod_1, color=CONFIG.C_PRODUCT, buff=0.1)

        with self.voiceover(
            text="Dividing by two leaves us with our first Product-to-Sum identity: Sine times Cosine."
        ) as tracker:
            self.play(Write(eq_prod_1), Create(box_prod_1), run_time=tracker.duration)

        # ----------------------------------------------------------------------
        # ACT 3: Visualizing Wave Multiplication (AM Radio / Beats)
        # ----------------------------------------------------------------------
        with self.voiceover(
            text="Let's visualize exactly what this means algebraically. On the left, let's generate a high-frequency sine wave..."
        ) as tracker:
            wave1 = axes.plot(lambda x: np.sin(5 * x), color=CONFIG.C_WAVE1, stroke_width=2)
            lbl_w1 = MathTex(r"\sin(5x)", color=CONFIG.C_WAVE1, font_size=24).next_to(axes, UP).shift(LEFT*1.5)
            self.play(Create(wave1), Write(lbl_w1), run_time=tracker.duration)

        with self.voiceover(
            text="And a lower-frequency cosine wave."
        ) as tracker:
            wave2 = axes.plot(lambda x: np.cos(1 * x), color=CONFIG.C_WAVE2, stroke_width=2)
            lbl_w2 = MathTex(r"\cos(1x)", color=CONFIG.C_WAVE2, font_size=24).next_to(lbl_w1, RIGHT, buff=0.5)
            self.play(Create(wave2), Write(lbl_w2), run_time=tracker.duration)

        with self.voiceover(
            text="If we physically multiply these two waves together, we get a complex interference pattern known as an envelope. "
            "This is how AM radio transmits audio."
        ) as tracker:
            wave_prod = axes.plot(lambda x: np.sin(5 * x) * np.cos(1 * x), color=CONFIG.C_PRODUCT, stroke_width=3)
            self.play(FadeOut(wave1), FadeOut(wave2), Create(wave_prod), run_time=2)
            
            lbl_prod = MathTex(r"\sin(5x)\cos(x)", color=CONFIG.C_PRODUCT, font_size=24).move_to(lbl_w1.get_center() + RIGHT*0.8)
            self.play(FadeOut(lbl_w1), FadeOut(lbl_w2), FadeIn(lbl_prod))
            self.wait(tracker.duration - 3)

        with self.voiceover(
            text="But according to the formula we just derived, this complex product is mathematically identical to simply adding two pure sine waves: "
            "one at a frequency of six, and one at a frequency of four!"
        ) as tracker:
            eq_wave_math = MathTex(r"= \frac{1}{2}[\sin(6x) + \sin(4x)]", color=CONFIG.C_PRODUCT, font_size=24).next_to(lbl_prod, RIGHT, buff=0.2)
            self.play(Write(eq_wave_math), Indicate(box_prod_1), run_time=tracker.duration)

        # ----------------------------------------------------------------------
        # ACT 4: Deriving Cosine * Cosine & Sine * Sine
        # ----------------------------------------------------------------------
        # Clean up the board for the next set
        board_group1 = VGroup(
            eq_sin_add, eq_sin_sub, add_line, plus_sign, strike_1, strike_2, eq_sum_result
        )
        self.play(FadeOut(board_group1))
        self.play(
            VGroup(eq_prod_1, box_prod_1).animate.next_to(board_line, DOWN, buff=0.2).align_to(board_line, LEFT).shift(RIGHT*0.2)
        )
        
        divider = DashedLine(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(box_prod_1, DOWN, buff=0.2)
        self.play(Create(divider))

        with self.voiceover(
            text="Now, let's find the products of two cosines, and two sines. "
            "We do this by stacking the Cosine addition and subtraction formulas."
        ) as tracker:
            eq_cos_sub = MathTex(
                r"\cos(\alpha - \beta) &= \cos\alpha\cos\beta + \sin\alpha\sin\beta", 
                font_size=24
            ).next_to(divider, DOWN, buff=0.3).align_to(eq_prod_1, LEFT)
            
            eq_cos_add = MathTex(
                r"\cos(\alpha + \beta) &= \cos\alpha\cos\beta - \sin\alpha\sin\beta", 
                font_size=24
            ).next_to(eq_cos_sub, DOWN, buff=0.2).align_to(eq_cos_sub, LEFT)

            self.play(Write(eq_cos_sub), Write(eq_cos_add), run_time=tracker.duration)

        with self.voiceover(
            text="If we add them together, the sine terms cancel out, giving us the identity for Cosine times Cosine."
        ) as tracker:
            add_line2 = Line(
                eq_cos_add.get_left() + DOWN*0.2, 
                eq_cos_add.get_right() + DOWN*0.2 + RIGHT*0.5, 
                color=GRAY
            )
            strike_3 = Line(eq_cos_sub[0][14:22].get_left(), eq_cos_sub[0][14:22].get_right(), color=RED)
            strike_4 = Line(eq_cos_add[0][14:22].get_left(), eq_cos_add[0][14:22].get_right(), color=RED)
            
            self.play(Create(add_line2), Create(strike_3), Create(strike_4), run_time=1.5)
            
            eq_prod_2 = MathTex(
                r"\cos\alpha\cos\beta = \frac{1}{2}[\cos(\alpha - \beta) + \cos(\alpha + \beta)]", 
                font_size=26, color=CONFIG.C_WAVE2
            ).next_to(add_line2, DOWN, buff=0.2).align_to(eq_cos_sub, LEFT)
            box_prod_2 = SurroundingRectangle(eq_prod_2, color=CONFIG.C_WAVE2, buff=0.1)

            self.play(Write(eq_prod_2), Create(box_prod_2), run_time=2)
            self.wait(tracker.duration - 3.5)

        with self.voiceover(
            text="But if we subtract the bottom equation from the top, the cosine terms cancel out instead! "
            "This reveals our final identity for Sine times Sine."
        ) as tracker:
            # Animate the subtraction dynamically
            self.play(FadeOut(add_line2), FadeOut(strike_3), FadeOut(strike_4))
            
            sub_line = Line(
                eq_cos_add.get_left() + DOWN*0.2, 
                eq_cos_add.get_right() + DOWN*0.2 + RIGHT*0.5, 
                color=GRAY
            )
            minus_sign = MathTex("-", font_size=24).next_to(sub_line, LEFT, buff=0.1).shift(UP*0.2)
            
            # Strike out the cosines this time
            strike_5 = Line(eq_cos_sub[0][8:15].get_left(), eq_cos_sub[0][8:15].get_right(), color=RED)
            strike_6 = Line(eq_cos_add[0][8:15].get_left(), eq_cos_add[0][8:15].get_right(), color=RED)

            self.play(Create(sub_line), Write(minus_sign), Create(strike_5), Create(strike_6), run_time=2)

            eq_prod_3 = MathTex(
                r"\sin\alpha\sin\beta = \frac{1}{2}[\cos(\alpha - \beta) - \cos(\alpha + \beta)]", 
                font_size=26, color=CONFIG.C_WAVE1
            ).next_to(box_prod_2, DOWN, buff=0.3).align_to(eq_cos_sub, LEFT)
            box_prod_3 = SurroundingRectangle(eq_prod_3, color=CONFIG.C_WAVE1, buff=0.1)

            self.play(Write(eq_prod_3), Create(box_prod_3), run_time=2)

        # ----------------------------------------------------------------------
        # ACT 5: Conclusion
        # ----------------------------------------------------------------------
        with self.voiceover(
            text="These Product-to-Sum formulas are essential tools in higher mathematics. "
            "They allow us to convert difficult calculus integration problems, or complex wave interference, into simple addition."
        ) as tracker:
            # Emphasize the final three formulas
            self.play(
                Indicate(box_prod_1, scale_factor=1.05),
                Indicate(box_prod_2, scale_factor=1.05),
                Indicate(box_prod_3, scale_factor=1.05),
                run_time=3
            )
            self.wait(tracker.duration - 3)

        self.wait(2)
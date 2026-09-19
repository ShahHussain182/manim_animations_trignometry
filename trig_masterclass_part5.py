"""
Trigonometry Masterclass - Part 5: Alternate Double Angles & Half-Angles
========================================================================
Run this file using:
manim -pql trig_masterclass_part5.py HalfAngleIdentities
"""

from dataclasses import dataclass, field
import numpy as np
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

@dataclass(frozen=True)
class TrigConfig:
    theta_deg: float = 64.0  # The full angle
    radius: float = 2.5
    origin: np.ndarray = field(default_factory=lambda: np.array([-3.5, -0.5, 0.0]))
    C_BG: str = "#0b1017"
    C_AXES: str = "#4A5568"
    C_CIRCLE: str = "#FFFFFF"
    C_THETA: str = "#E056FD"      # Purple
    C_HALF: str = "#00D2D3"       # Cyan
    C_COS: str = "#F1C40F"        # Yellow
    C_SIN: str = "#FF4444"        # Red

    @property
    def theta(self) -> float: return np.radians(self.theta_deg)
    @property
    def half_theta(self) -> float: return self.theta / 2.0

CONFIG = TrigConfig()

class HalfAngleIdentities(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en"))
        self.camera.background_color = CONFIG.C_BG

        O, R, t, ht = CONFIG.origin, CONFIG.radius, CONFIG.theta, CONFIG.half_theta

        # BUG FIX: The ampersand is now escaped as \&
        title = Title(
            r"Part 5: Double Angle Expansions \& Half-Angle Identities",
            font_size=32, color=WHITE
        )
        self.play(Write(title))

        axes = Axes(
            x_range=[-1.2, 1.2, 1], y_range=[-1.2, 1.2, 1],
            x_length=R * 2.3, y_length=R * 2.3,
            tips=True, axis_config={"color": CONFIG.C_AXES, "stroke_width": 1.5}
        ).move_to(O)
        unit_circle = Circle(radius=R, color=CONFIG.C_CIRCLE, stroke_width=2).move_to(O)

        board_bg = RoundedRectangle(
            corner_radius=0.2, height=6.2, width=6.8,
            color=GRAY_D, fill_color="#121a24", fill_opacity=0.95
        ).to_edge(RIGHT, buff=0.2).shift(DOWN * 0.2)
        
        board_title = Text("Algebraic Derivation", font_size=20, color=YELLOW).next_to(board_bg.get_top(), DOWN, buff=0.2)
        board_line = Line(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(board_title, DOWN, buff=0.15)

        with self.voiceover(text="Welcome to Part 5. Let's begin by recalling the Double Angle formula for Cosine that we derived in the last part.") as tracker:
            self.play(Create(axes), Create(unit_circle), FadeIn(board_bg), Write(board_title), Create(board_line), run_time=tracker.duration)

        eq_base = MathTex(r"\cos(2\alpha) = \cos^2\alpha - \sin^2\alpha", font_size=26, color=WHITE).next_to(board_line, DOWN, buff=0.25)
        self.play(Write(eq_base))

        with self.voiceover(text="Using the Pythagorean identity from Part 3, we know that sine squared is one minus cosine squared. Substituting this gives us a version of the formula using entirely cosines.") as tracker:
            self.wait(tracker.duration - 4)

        eq_sub1 = MathTex(r"\text{Substitute } \sin^2\alpha = 1 - \cos^2\alpha:", font_size=22, color=GRAY_B).next_to(eq_base, DOWN, buff=0.2).align_to(eq_base, LEFT)
        eq_cos_only = MathTex(r"\cos(2\alpha) = 2\cos^2\alpha - 1", font_size=26, color=CONFIG.C_COS).next_to(eq_sub1, DOWN, buff=0.15).align_to(eq_base, LEFT)

        self.play(Write(eq_sub1), run_time=1.5)
        self.play(Write(eq_cos_only), run_time=2)

        with self.voiceover(text="Alternatively, substituting cosine squared for one minus sine squared gives us a third version, using entirely sines.") as tracker:
            self.wait(tracker.duration - 4)

        eq_sub2 = MathTex(r"\text{Substitute } \cos^2\alpha = 1 - \sin^2\alpha:", font_size=22, color=GRAY_B).next_to(eq_cos_only, DOWN, buff=0.2).align_to(eq_base, LEFT)
        eq_sin_only = MathTex(r"\cos(2\alpha) = 1 - 2\sin^2\alpha", font_size=26, color=CONFIG.C_SIN).next_to(eq_sub2, DOWN, buff=0.15).align_to(eq_base, LEFT)

        self.play(Write(eq_sub2), run_time=1.5)
        self.play(Write(eq_sin_only), run_time=2)

        box_3forms = SurroundingRectangle(VGroup(eq_base, eq_cos_only, eq_sin_only), color=GRAY_C, buff=0.1)
        self.play(Create(box_3forms))
        
        with self.voiceover(text="These three equations are all perfectly valid forms of the Cosine Double Angle identity. But their true power is unlocked when we read them in reverse, allowing us to halve an angle rather than double it.") as tracker:
            self.wait(tracker.duration)

        self.play(FadeOut(VGroup(eq_base, eq_sub1, eq_sub2, eq_sin_only, box_3forms)))
        self.play(eq_cos_only.animate.next_to(board_line, DOWN, buff=0.25).align_to(eq_base, LEFT))
        
        divider1 = DashedLine(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(eq_cos_only, DOWN, buff=0.2)
        self.play(Create(divider1))

        with self.voiceover(text="Let's take the cosine-only equation. We want to isolate cosine of alpha. First, we add one to both sides. Next, we divide by two. And finally, we take the square root.") as tracker:
            step1_cos = MathTex(r"2\cos^2\alpha = 1 + \cos(2\alpha)", font_size=24).next_to(divider1, DOWN, buff=0.2).align_to(eq_base, LEFT)
            self.play(Write(step1_cos), run_time=2)
            step2_cos = MathTex(r"\cos^2\alpha = \frac{1 + \cos(2\alpha)}{2}", font_size=24).next_to(step1_cos, DOWN, buff=0.2).align_to(eq_base, LEFT)
            self.play(Write(step2_cos), run_time=2)
            step3_cos = MathTex(r"\cos\alpha = \pm\sqrt{\frac{1 + \cos(2\alpha)}{2}}", font_size=24).next_to(step2_cos, DOWN, buff=0.2).align_to(eq_base, LEFT)
            self.play(Write(step3_cos), run_time=2)
            self.wait(tracker.duration - 6)

        sub_theta = MathTex(r"\text{Let } \theta = 2\alpha \implies \alpha = \frac{\theta}{2}", font_size=22, color=CONFIG.C_HALF).next_to(step3_cos, DOWN, buff=0.2).align_to(eq_base, LEFT)
        half_cos_final = MathTex(r"\cos\left(\frac{\theta}{2}\right) = \pm\sqrt{\frac{1 + \cos\theta}{2}}", font_size=28, color=CONFIG.C_COS).next_to(sub_theta, DOWN, buff=0.2).align_to(eq_base, LEFT)
        box_half_cos = SurroundingRectangle(half_cos_final, color=CONFIG.C_COS, buff=0.1)

        with self.voiceover(text="To make this more intuitive, let's substitute variables. Let theta equal two alpha. That means alpha is theta over two. Substituting this gives us the official Half-Angle Formula for Cosine.") as tracker:
            self.play(Write(sub_theta), run_time=2)
            self.play(Write(half_cos_final), Create(box_half_cos), run_time=2)

        pt_theta = O + R * np.array([np.cos(t), np.sin(t), 0])
        line_theta = Line(O, pt_theta, color=CONFIG.C_THETA, stroke_width=3)
        arc_theta = Arc(radius=0.5, start_angle=0, angle=t, arc_center=O, color=CONFIG.C_THETA)
        lbl_theta = MathTex(r"\theta", color=CONFIG.C_THETA, font_size=20).next_to(arc_theta, UR, buff=0.05)
        
        with self.voiceover(text="Let's view this on the circle. Here is an arbitrary angle, theta.") as tracker:
            self.play(Create(line_theta), Create(arc_theta), Write(lbl_theta), run_time=tracker.duration)

        pt_half = O + R * np.array([np.cos(ht), np.sin(ht), 0])
        line_half = Line(O, pt_half, color=CONFIG.C_HALF, stroke_width=3)
        arc_half = Arc(radius=0.8, start_angle=0, angle=ht, arc_center=O, color=CONFIG.C_HALF, stroke_width=2.5)
        lbl_half = MathTex(r"\frac{\theta}{2}", color=CONFIG.C_HALF, font_size=22).next_to(arc_half, RIGHT, buff=0.05).shift(UP*0.1)
        pt_half_x = O + R * np.array([np.cos(ht), 0, 0])
        cos_half_line = Line(O, pt_half_x, color=CONFIG.C_COS, stroke_width=4.5)
        
        with self.voiceover(text="If we mathematically bisect this angle, drawing a ray exactly through the middle, we get theta over two. The yellow base of this new triangle is exactly the value determined by our square-root equation!") as tracker:
            self.play(Create(line_half), Create(arc_half), Write(lbl_half), run_time=2)
            self.play(Create(cos_half_line), run_time=2)
            self.wait(tracker.duration - 4)

        board_group1 = VGroup(eq_cos_only, divider1, step1_cos, step2_cos, step3_cos, sub_theta, half_cos_final, box_half_cos)
        self.play(board_group1.animate.scale(0.65).shift(UP * 2.1).align_to(eq_base, LEFT))

        divider2 = DashedLine(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(board_group1, DOWN, buff=0.2)
        self.play(Create(divider2))

        eq_sin_only_remind = MathTex(r"\cos(2\alpha) = 1 - 2\sin^2\alpha", font_size=24, color=CONFIG.C_SIN).next_to(divider2, DOWN, buff=0.2).align_to(eq_base, LEFT)
        self.play(Write(eq_sin_only_remind))

        with self.voiceover(text="We can perform the exact same algebraic dance on the sine-only version of the double angle formula. Isolating sine squared, dividing by two, and taking the square root...") as tracker:
            step1_sin = MathTex(r"2\sin^2\alpha = 1 - \cos(2\alpha)", font_size=22).next_to(eq_sin_only_remind, DOWN, buff=0.15).align_to(eq_base, LEFT)
            self.play(Write(step1_sin), run_time=1.5)
            step2_sin = MathTex(r"\sin^2\alpha = \frac{1 - \cos(2\alpha)}{2}", font_size=22).next_to(step1_sin, DOWN, buff=0.15).align_to(eq_base, LEFT)
            self.play(Write(step2_sin), run_time=1.5)
            step3_sin = MathTex(r"\sin\alpha = \pm\sqrt{\frac{1 - \cos(2\alpha)}{2}}", font_size=22).next_to(step2_sin, DOWN, buff=0.15).align_to(eq_base, LEFT)
            self.play(Write(step3_sin), run_time=1.5)
            self.wait(tracker.duration - 4.5)

        half_sin_final = MathTex(r"\sin\left(\frac{\theta}{2}\right) = \pm\sqrt{\frac{1 - \cos\theta}{2}}", font_size=28, color=CONFIG.C_SIN).next_to(step3_sin, DOWN, buff=0.2).align_to(eq_base, LEFT)
        box_half_sin = SurroundingRectangle(half_sin_final, color=CONFIG.C_SIN, buff=0.1)

        with self.voiceover(text="Substituting theta for two alpha yields the Half-Angle Formula for Sine.") as tracker:
            self.play(Write(half_sin_final), Create(box_half_sin), run_time=tracker.duration)

        sin_half_line = Line(pt_half_x, pt_half, color=CONFIG.C_SIN, stroke_width=4.5)
        
        with self.voiceover(text="Geometrically, this corresponds to the red vertical height of our bisected angle's triangle.") as tracker:
            self.play(Create(sin_half_line), run_time=tracker.duration)

        divider3 = DashedLine(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(box_half_sin, DOWN, buff=0.2)
        self.play(Create(divider3))

        eq_tan_half = MathTex(r"\tan\left(\frac{\theta}{2}\right) = \frac{\sin(\theta/2)}{\cos(\theta/2)} = \pm\sqrt{\frac{1-\cos\theta}{1+\cos\theta}}", font_size=22, color=CONFIG.C_HALF).next_to(divider3, DOWN, buff=0.25).align_to(eq_base, LEFT)

        with self.voiceover(text="And since tangent is simply sine divided by cosine, dividing these two square roots gives us the tangent half-angle identity instantly! In Part 6, we will push these boundaries even further and derive the notorious Triple Angle identities.") as tracker:
            self.play(Write(eq_tan_half), run_time=4)
            self.wait(tracker.duration - 4)
        self.wait(2)
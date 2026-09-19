"""
Trigonometry Masterclass - Part 8: Proving Identities & Allied Angles
=====================================================================
A beginner-friendly breakdown of complex trigonometric proofs,
featuring quadrant analysis (CAST rule) and triangle angle properties.

Run this file using:
manim -pql trig_masterclass_part8.py AlliedAnglesProofs
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
    C_BG: str = "#0b1017"
    C_AXES: str = "#4A5568"
    
    C_NUM1: str = "#F1C40F"       # Yellow
    C_NUM2: str = "#00D2D3"       # Cyan
    C_DEN1: str = "#FF4444"       # Red
    C_DEN2: str = "#E056FD"       # Purple
    
    C_HL: str = "#3498DB"         # Blue highlight

CONFIG = TrigConfig()

# ==============================================================================
# 2. Main Scene - Part 8
# ==============================================================================
class AlliedAnglesProofs(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en"))
        self.camera.background_color = CONFIG.C_BG

        # ----------------------------------------------------------------------
        # ACT 1: Introduction & Question 4(i) Setup
        # ----------------------------------------------------------------------
        title = Title(
            r"Part 8: Proving Identities (Allied Angles)",
            font_size=34,
            color=WHITE
        )
        self.play(Write(title))

        with self.voiceover(
            text="Welcome to Part 8. It's time to put our knowledge to the test and solve some actual textbook proofs. "
            "We will start with a daunting fraction filled with massive angles, and prove that it simply equals negative secant squared."
        ) as tracker:
            self.wait(1)

        # Build the main equation visually
        q4_text = Text("Prove that:", font_size=24, color=GRAY_B).to_corner(UL).shift(DOWN*1.2)
        
        # We build the fraction manually to animate individual parts easily
        num1 = MathTex(r"\tan(180^\circ + \alpha)", color=CONFIG.C_NUM1, font_size=32)
        num2 = MathTex(r"\cot(90^\circ - \alpha)", color=CONFIG.C_NUM2, font_size=32)
        numerator = VGroup(num1, num2).arrange(RIGHT, buff=0.2)
        
        den1 = MathTex(r"\sin(360^\circ - \alpha)", color=CONFIG.C_DEN1, font_size=32)
        den2 = MathTex(r"\cos(270^\circ + \alpha)", color=CONFIG.C_DEN2, font_size=32)
        denominator = VGroup(den1, den2).arrange(RIGHT, buff=0.2)
        
        frac_line = Line(LEFT, RIGHT, color=WHITE).match_width(numerator).scale(1.1)
        
        fraction = VGroup(numerator, frac_line, denominator).arrange(DOWN, buff=0.2).shift(LEFT * 2.5 + DOWN * 0.5)
        
        equals = MathTex(r"=", font_size=36).next_to(fraction, RIGHT, buff=0.3)
        rhs = MathTex(r"-\sec^2\alpha", font_size=36, color=WHITE).next_to(equals, RIGHT, buff=0.3)

        self.play(Write(q4_text))
        self.play(
            FadeIn(numerator, shift=DOWN), 
            Create(frac_line), 
            FadeIn(denominator, shift=UP),
            Write(equals), Write(rhs),
            run_time=2
        )

        # ----------------------------------------------------------------------
        # ACT 2: The Quadrant Analysis Board (Right Side)
        # ----------------------------------------------------------------------
        board_bg = RoundedRectangle(
            corner_radius=0.2, height=5.5, width=4.5,
            color=GRAY_D, fill_color="#121a24", fill_opacity=0.95
        ).to_edge(RIGHT, buff=0.3).shift(DOWN * 0.2)
        
        board_title = Text("Quadrant Analysis", font_size=20, color=YELLOW).next_to(board_bg.get_top(), DOWN, buff=0.2)
        board_line_UI = Line(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(board_title, DOWN, buff=0.15)

        with self.voiceover(
            text="To a beginner, this looks impossible. But all we need to do is break it down piece by piece using our quadrant rules."
        ) as tracker:
            self.play(FadeIn(board_bg), Write(board_title), Create(board_line_UI), run_time=tracker.duration)

        # Function to do the mini-analysis
        def analyze_term(target_mob, original_tex, quad_text, rule_text, result_tex, result_color):
            hl_box = SurroundingRectangle(target_mob, color=YELLOW, buff=0.1)
            self.play(Create(hl_box), run_time=0.5)
            
            orig = MathTex(original_tex, font_size=28, color=result_color).next_to(board_line_UI, DOWN, buff=0.3)
            q_txt = Text(quad_text, font_size=18, color=GRAY_A).next_to(orig, DOWN, buff=0.3)
            r_txt = Text(rule_text, font_size=18, color=GRAY_A).next_to(q_txt, DOWN, buff=0.2)
            res = MathTex(r"\rightarrow " + result_tex, font_size=32, color=result_color).next_to(r_txt, DOWN, buff=0.3)
            
            self.play(TransformFromCopy(target_mob, orig))
            self.play(Write(q_txt), run_time=1.5)
            self.play(Write(r_txt), run_time=1.5)
            self.play(Write(res), run_time=1)
            self.wait(1)
            
            new_term = MathTex(result_tex, font_size=32, color=result_color).move_to(target_mob)
            self.play(Transform(target_mob, new_term), FadeOut(hl_box))
            self.play(FadeOut(VGroup(orig, q_txt, r_txt, res)))

        # Term 1: tan(180 + alpha)
        with self.voiceover(
            text="Let's isolate the first term: tangent of 180 degrees plus alpha. "
            "180 plus an angle lands us in the third quadrant, where tangent is positive. "
            "Because we are using 180, the function name stays exactly the same. It simplifies simply to tangent alpha."
        ) as tracker:
            analyze_term(
                num1, r"\tan(180^\circ + \alpha)", 
                "1. Quadrant III (Tan is +)", 
                "2. 180° Rule (Keep function)", 
                r"\tan\alpha", CONFIG.C_NUM1
            )

        # Term 2: cot(90 - alpha)
        with self.voiceover(
            text="Next, cotangent of 90 degrees minus alpha. This is the first quadrant, so everything is positive. "
            "However, because we use 90 degrees, we must switch to the co-function! Cotangent becomes tangent."
        ) as tracker:
            analyze_term(
                num2, r"\cot(90^\circ - \alpha)", 
                "1. Quadrant I (All are +)", 
                "2. 90° Rule (Switch to Co-function)", 
                r"\tan\alpha", CONFIG.C_NUM2
            )

        # Term 3: sin(360 - alpha)
        with self.voiceover(
            text="Down to the denominator. Sine of 360 minus alpha. We are in the fourth quadrant, where sine is negative. "
            "360 degrees means we keep the function. So, we get negative sine alpha."
        ) as tracker:
            analyze_term(
                den1, r"\sin(360^\circ - \alpha)", 
                "1. Quadrant IV (Sin is -)", 
                "2. 360° Rule (Keep function)", 
                r"-\sin\alpha", CONFIG.C_DEN1
            )

        # Term 4: cos(270 + alpha)
        with self.voiceover(
            text="Finally, cosine of 270 plus alpha. This is also the fourth quadrant, where cosine is positive. "
            "But the 270 degree line forces us to switch to the co-function. Cosine becomes sine."
        ) as tracker:
            analyze_term(
                den2, r"\cos(270^\circ + \alpha)", 
                "1. Quadrant IV (Cos is +)", 
                "2. 270° Rule (Switch to Co-function)", 
                r"\sin\alpha", CONFIG.C_DEN2
            )

        # ----------------------------------------------------------------------
        # ACT 3: Algebraic Cleanup
        # ----------------------------------------------------------------------
        with self.voiceover(
            text="Our terrifying fraction is now made entirely of simple alphas. Let's multiply them together."
        ) as tracker:
            self.wait(1)
            
        num_simp = MathTex(r"\tan^2\alpha", font_size=36, color=YELLOW).move_to(numerator)
        den_simp = MathTex(r"-\sin^2\alpha", font_size=36, color=RED).move_to(denominator)
        
        self.play(Transform(numerator, num_simp), Transform(denominator, den_simp), run_time=1.5)

        with self.voiceover(
            text="Tangent is sine over cosine. Let's expand the numerator."
        ) as tracker:
            num_exp = MathTex(r"\frac{\sin^2\alpha}{\cos^2\alpha}", font_size=36, color=YELLOW).move_to(numerator).shift(UP*0.2)
            self.play(Transform(numerator, num_exp), frac_line.animate.shift(DOWN*0.1), denominator.animate.shift(DOWN*0.2))
            self.wait(1)

        with self.voiceover(
            text="The sine squared in the numerator and the sine squared in the denominator cancel each other out perfectly."
        ) as tracker:
            strike1 = Line(numerator[0][0:5].get_left(), numerator[0][0:5].get_right(), color=WHITE)
            strike2 = Line(denominator[0][1:6].get_left(), denominator[0][1:6].get_right(), color=WHITE)
            self.play(Create(strike1), Create(strike2))
            self.wait(1)

        with self.voiceover(
            text="This leaves us with negative one over cosine squared. And since one over cosine is secant, our proof is complete!"
        ) as tracker:
            final_left = MathTex(r"-\frac{1}{\cos^2\alpha}", font_size=40).move_to(fraction)
            self.play(
                FadeOut(numerator, denominator, frac_line, strike1, strike2),
                FadeIn(final_left)
            )
            self.wait(1)
            
            final_left_sec = MathTex(r"-\sec^2\alpha", font_size=40, color=CONFIG.C_HL).move_to(fraction)
            self.play(Transform(final_left, final_left_sec))
            self.play(Indicate(final_left_sec, color=WHITE), Indicate(rhs, color=WHITE))
            self.wait(1)


        # ----------------------------------------------------------------------
        # ACT 4: Question 6 - Triangle Properties Setup
        # ----------------------------------------------------------------------
        self.play(
            FadeOut(q4_text, final_left, equals, rhs, board_bg, board_title, board_line_UI)
        )

        q6_text = Text(
            "If α, β, γ are angles of triangle ABC, prove:", 
            font_size=24, color=GRAY_B
        ).to_corner(UL).shift(DOWN*0.5)
        
        self.play(Write(q6_text))

        # Draw a glowing triangle
        pt_A = np.array([-4, -2, 0])
        pt_B = np.array([-1, -2, 0])
        pt_C = np.array([-2, 1, 0])
        
        triangle = Polygon(pt_A, pt_B, pt_C, color=WHITE, stroke_width=3)
        lbl_A = MathTex(r"\alpha", color=YELLOW, font_size=24).next_to(pt_A, UR, buff=0.2)
        lbl_B = MathTex(r"\beta", color=CONFIG.C_NUM2, font_size=24).next_to(pt_B, UL, buff=0.2)
        lbl_C = MathTex(r"\gamma", color=RED, font_size=24).next_to(pt_C, DOWN, buff=0.2)
        
        with self.voiceover(
            text="Let's apply these exact same logical rules to a geometric shape. "
            "If alpha, beta, and gamma are the interior angles of any triangle, we know their sum must equal 180 degrees."
        ) as tracker:
            self.play(Create(triangle), Write(lbl_A), Write(lbl_B), Write(lbl_C), run_time=tracker.duration)

        # Set up derivation board on the right again
        board_bg2 = RoundedRectangle(
            corner_radius=0.2, height=6.0, width=7.0,
            color=GRAY_D, fill_color="#121a24", fill_opacity=0.95
        ).to_edge(RIGHT, buff=0.2).shift(DOWN * 0.2)
        
        with self.voiceover(
            text="This gives us our master equation: alpha plus beta plus gamma equals 180 degrees."
        ) as tracker:
            self.play(FadeIn(board_bg2))
            master_eq = MathTex(r"\alpha + \beta + \gamma = 180^\circ", font_size=32).next_to(board_bg2.get_top(), DOWN, buff=0.4)
            self.play(Write(master_eq))

        # ----------------------------------------------------------------------
        # ACT 5: Q6(i) - Sine Proof
        # ----------------------------------------------------------------------
        q6i_task = MathTex(r"\text{(i) Prove: } \sin(\alpha + \beta) = \sin\gamma", font_size=28, color=YELLOW).next_to(master_eq, DOWN, buff=0.5).align_to(master_eq, LEFT).shift(LEFT*1.5)
        self.play(Write(q6i_task))

        with self.voiceover(
            text="For our first proof, we need to find sine of alpha plus beta. "
            "Using our master equation, we can subtract gamma to the other side, revealing that alpha plus beta is exactly 180 minus gamma."
        ) as tracker:
            step1 = MathTex(r"\alpha + \beta = 180^\circ - \gamma", font_size=28).next_to(q6i_task, DOWN, buff=0.3).align_to(q6i_task, LEFT)
            self.play(Write(step1), run_time=tracker.duration)

        with self.voiceover(
            text="We substitute this into our sine function. And look! This is an allied angle. "
            "180 minus an angle is the second quadrant, where sine is positive, and the function stays the same. The proof is instant!"
        ) as tracker:
            step2 = MathTex(r"\sin(\alpha + \beta) = \sin(180^\circ - \gamma)", font_size=28).next_to(step1, DOWN, buff=0.3).align_to(q6i_task, LEFT)
            self.play(Write(step2), run_time=3)
            
            step3 = MathTex(r"\sin(\alpha + \beta) = \sin\gamma", font_size=32, color=CONFIG.C_HL).next_to(step2, DOWN, buff=0.3).align_to(q6i_task, LEFT)
            box_step3 = SurroundingRectangle(step3, color=CONFIG.C_HL, buff=0.1)
            self.play(Write(step3), Create(box_step3), run_time=2)

        # ----------------------------------------------------------------------
        # ACT 6: Q6(ii) - Secant/Cosecant Proof
        # ----------------------------------------------------------------------
        divider3 = DashedLine(board_bg2.get_left(), board_bg2.get_right(), color=GRAY_D).next_to(box_step3, DOWN, buff=0.3)
        self.play(Create(divider3))

        q6ii_task = MathTex(r"\text{(ii) Prove: } \sec\left(\frac{\alpha + \beta}{2}\right) = \csc\left(\frac{\gamma}{2}\right)", font_size=28, color=YELLOW).next_to(divider3, DOWN, buff=0.3).align_to(q6i_task, LEFT)
        self.play(Write(q6ii_task))

        with self.voiceover(
            text="Let's try a harder one with fractions. Secant of alpha plus beta, divided by two. "
            "Again, we substitute 180 minus gamma into the numerator."
        ) as tracker:
            step4 = MathTex(r"\sec\left(\frac{180^\circ - \gamma}{2}\right)", font_size=28).next_to(q6ii_task, DOWN, buff=0.3).align_to(q6i_task, LEFT).shift(RIGHT*1.5)
            self.play(Write(step4), run_time=tracker.duration)

        with self.voiceover(
            text="Dividing both terms inside the bracket by two gives us 90 degrees minus gamma over two."
        ) as tracker:
            step5 = MathTex(r"= \sec\left(90^\circ - \frac{\gamma}{2}\right)", font_size=28).next_to(step4, DOWN, buff=0.2).align_to(step4, LEFT)
            self.play(Write(step5), run_time=tracker.duration)

        with self.voiceover(
            text="And once again, our allied rules save the day. 90 minus an angle is the first quadrant, but 90 means we switch to the co-function! "
            "Secant becomes Cosecant, and our final proof is complete."
        ) as tracker:
            step6 = MathTex(r"= \csc\left(\frac{\gamma}{2}\right)", font_size=32, color=CONFIG.C_HL).next_to(step5, DOWN, buff=0.2).align_to(step4, LEFT)
            box_step6 = SurroundingRectangle(step6, color=CONFIG.C_HL, buff=0.1)
            self.play(Write(step6), Create(box_step6), run_time=tracker.duration)

        self.wait(3)
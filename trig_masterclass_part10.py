"""
Trigonometry Masterclass - Part 10: Beautiful Triangle Identities
=================================================================
A step-by-step algebraic and geometric derivation of the Tangent 
sum-to-product and half-angle identities for triangles.

Run this file using:
manim -pql trig_masterclass_part10.py TriangleIdentities
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
    
    C_A: str = "#F1C40F"          # Yellow (Alpha)
    C_B: str = "#00D2D3"          # Cyan (Beta)
    C_C: str = "#FF4444"          # Red (Gamma)
    
    C_HL: str = "#3498DB"         # Blue highlight

CONFIG = TrigConfig()

# ==============================================================================
# 2. Main Scene - Part 10
# ==============================================================================
class TriangleIdentities(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en"))
        self.camera.background_color = CONFIG.C_BG

        # ----------------------------------------------------------------------
        # ACT 1: Scene Layout & Triangle Setup
        # ----------------------------------------------------------------------
        title = Title(
            r"Part 10: The Tangent Triangle Identities",
            font_size=34,
            color=WHITE
        )
        self.play(Write(title))

        # Geometric Triangle (Left)
        pt_A = np.array([-5.5, -2, 0])
        pt_B = np.array([-1.5, -2, 0])
        pt_C = np.array([-2.5, 1.5, 0])
        
        triangle = Polygon(pt_A, pt_B, pt_C, color=WHITE, stroke_width=3)
        
        arc_A = Angle(Line(pt_A, pt_B), Line(pt_A, pt_C), radius=0.6, color=CONFIG.C_A)
        arc_B = Angle(Line(pt_B, pt_C), Line(pt_B, pt_A), radius=0.6, color=CONFIG.C_B)
        arc_C = Angle(Line(pt_C, pt_A), Line(pt_C, pt_B), radius=0.6, color=CONFIG.C_C)
        
        lbl_A = MathTex(r"\alpha", color=CONFIG.C_A, font_size=28).next_to(arc_A, RIGHT, buff=0.1).shift(UP*0.2)
        lbl_B = MathTex(r"\beta", color=CONFIG.C_B, font_size=28).next_to(arc_B, LEFT, buff=0.1).shift(UP*0.2)
        lbl_C = MathTex(r"\gamma", color=CONFIG.C_C, font_size=28).next_to(arc_C, DOWN, buff=0.2)

        # Derivation Board (Right)
        board_bg = RoundedRectangle(
            corner_radius=0.2, height=6.2, width=7.4,
            color=GRAY_D, fill_color="#121a24", fill_opacity=0.95
        ).to_edge(RIGHT, buff=0.2).shift(DOWN * 0.2)
        
        board_title = Text("Algebraic Proofs", font_size=20, color=YELLOW).next_to(board_bg.get_top(), DOWN, buff=0.2)
        board_line = Line(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(board_title, DOWN, buff=0.15)

        with self.voiceover(
            text="Welcome to Part 10. Triangles hide some of the most beautiful algebraic secrets in mathematics. "
            "Let's look at any triangle with interior angles alpha, beta, and gamma."
        ) as tracker:
            self.play(
                Create(triangle), Create(arc_A), Create(arc_B), Create(arc_C),
                Write(lbl_A), Write(lbl_B), Write(lbl_C),
                FadeIn(board_bg), Write(board_title), Create(board_line),
                run_time=tracker.duration
            )

        master_eq = MathTex(r"\alpha + \beta + \gamma = 180^\circ", font_size=32).next_to(board_line, DOWN, buff=0.25)
        
        with self.voiceover(
            text="Because they form a triangle, we know their sum is exactly 180 degrees. Let's write that at the top of our board."
        ) as tracker:
            self.play(Write(master_eq), run_time=tracker.duration)

        # ----------------------------------------------------------------------
        # ACT 2: Proof (i) - Sum equals Product
        # ----------------------------------------------------------------------
        q1_task = MathTex(
            r"\text{(i) Prove: } \tan\alpha + \tan\beta + \tan\gamma = \tan\alpha\tan\beta\tan\gamma", 
            font_size=24, color=YELLOW
        ).next_to(master_eq, DOWN, buff=0.3).align_to(board_line, LEFT).shift(RIGHT*0.2)
        
        self.play(Write(q1_task))

        with self.voiceover(
            text="We want to prove that the sum of their tangents is miraculously equal to their product! "
            "We begin by taking our master equation and subtracting gamma to the other side."
        ) as tracker:
            p1_step1 = MathTex(r"\alpha + \beta = 180^\circ - \gamma", font_size=24).next_to(q1_task, DOWN, buff=0.2).align_to(q1_task, LEFT)
            self.play(Write(p1_step1), run_time=tracker.duration)

        with self.voiceover(
            text="Next, we take the tangent of both sides."
        ) as tracker:
            p1_step2 = MathTex(r"\tan(\alpha + \beta) = \tan(180^\circ - \gamma)", font_size=24).next_to(p1_step1, DOWN, buff=0.2).align_to(q1_task, LEFT)
            self.play(Write(p1_step2), run_time=tracker.duration)

        with self.voiceover(
            text="On the left, we expand using the Tangent Sum formula. On the right, 180 minus an angle is the second quadrant, "
            "where tangent is negative. So it simplifies to negative tangent gamma."
        ) as tracker:
            p1_step3 = MathTex(
                r"\frac{\tan\alpha + \tan\beta}{1 - \tan\alpha\tan\beta} = -\tan\gamma", 
                font_size=26
            ).next_to(p1_step2, DOWN, buff=0.2).align_to(q1_task, LEFT)
            self.play(Write(p1_step3), run_time=tracker.duration)

        with self.voiceover(
            text="Now, we simply cross-multiply, bringing the denominator up to the right side."
        ) as tracker:
            p1_step4 = MathTex(
                r"\tan\alpha + \tan\beta = -\tan\gamma(1 - \tan\alpha\tan\beta)", 
                font_size=24
            ).next_to(p1_step3, DOWN, buff=0.2).align_to(q1_task, LEFT)
            self.play(Write(p1_step4), run_time=tracker.duration)

        with self.voiceover(
            text="We distribute the negative tangent gamma..."
        ) as tracker:
            p1_step5 = MathTex(
                r"\tan\alpha + \tan\beta = -\tan\gamma + \tan\alpha\tan\beta\tan\gamma", 
                font_size=24
            ).next_to(p1_step4, DOWN, buff=0.2).align_to(q1_task, LEFT)
            self.play(Write(p1_step5), run_time=tracker.duration)

        with self.voiceover(
            text="...and add tangent gamma to both sides. The proof is complete! A beautifully simple result."
        ) as tracker:
            p1_final = MathTex(
                r"\tan\alpha + \tan\beta + \tan\gamma = \tan\alpha\tan\beta\tan\gamma", 
                font_size=26, color=CONFIG.C_HL
            ).next_to(p1_step5, DOWN, buff=0.25).align_to(q1_task, LEFT)
            box_p1 = SurroundingRectangle(p1_final, color=CONFIG.C_HL, buff=0.1)
            
            self.play(Write(p1_final), Create(box_p1), run_time=tracker.duration)
            self.wait(1)


        # ----------------------------------------------------------------------
        # ACT 3: Geometry of the Half-Angles
        # ----------------------------------------------------------------------
        # Clean up board for the next derivation
        board_group1 = VGroup(
            q1_task, p1_step1, p1_step2, p1_step3, p1_step4, p1_step5, p1_final, box_p1
        )
        self.play(FadeOut(board_group1))
        
        with self.voiceover(
            text="But what happens if we bisect these angles? On our triangle, let's draw the angle bisectors. "
            "They meet at a single point called the incenter."
        ) as tracker:
            # Draw angle bisectors (approximate visually)
            incenter = np.array([-3.2, -0.6, 0])
            bisect_A = DashedLine(pt_A, incenter, color=CONFIG.C_A)
            bisect_B = DashedLine(pt_B, incenter, color=CONFIG.C_B)
            bisect_C = DashedLine(pt_C, incenter, color=CONFIG.C_C)
            
            # Update labels to half angles
            lbl_A_half = MathTex(r"\frac{\alpha}{2}", color=CONFIG.C_A, font_size=22).next_to(arc_A, RIGHT, buff=0.1).shift(UP*0.1)
            lbl_B_half = MathTex(r"\frac{\beta}{2}", color=CONFIG.C_B, font_size=22).next_to(arc_B, LEFT, buff=0.1).shift(UP*0.1)
            lbl_C_half = MathTex(r"\frac{\gamma}{2}", color=CONFIG.C_C, font_size=22).next_to(arc_C, DOWN, buff=0.2).shift(UP*0.1)
            
            self.play(Create(bisect_A), Create(bisect_B), Create(bisect_C), run_time=2)
            self.play(
                Transform(lbl_A, lbl_A_half),
                Transform(lbl_B, lbl_B_half),
                Transform(lbl_C, lbl_C_half),
                run_time=tracker.duration - 2
            )

        with self.voiceover(
            text="Because we divided the angles by two, we must divide our master equation by two as well. "
            "Their sum is now exactly 90 degrees."
        ) as tracker:
            master_eq_half = MathTex(r"\frac{\alpha}{2} + \frac{\beta}{2} + \frac{\gamma}{2} = 90^\circ", font_size=32).move_to(master_eq)
            self.play(Transform(master_eq, master_eq_half), run_time=tracker.duration)


        # ----------------------------------------------------------------------
        # ACT 4: Proof (ii) - Pairwise Products equal 1
        # ----------------------------------------------------------------------
        q2_task = MathTex(
            r"\text{(ii) Prove: } \tan\frac{\alpha}{2}\tan\frac{\beta}{2} + \tan\frac{\beta}{2}\tan\frac{\gamma}{2} + \tan\frac{\gamma}{2}\tan\frac{\alpha}{2} = 1", 
            font_size=22, color=YELLOW
        ).next_to(master_eq, DOWN, buff=0.3).align_to(board_line, LEFT).shift(RIGHT*0.2)
        
        self.play(Write(q2_task))

        with self.voiceover(
            text="Let's prove that the sum of their pairwise products equals one. "
            "Just like before, we isolate the first two terms by subtracting gamma over two."
        ) as tracker:
            p2_step1 = MathTex(r"\frac{\alpha}{2} + \frac{\beta}{2} = 90^\circ - \frac{\gamma}{2}", font_size=24).next_to(q2_task, DOWN, buff=0.2).align_to(q2_task, LEFT)
            self.play(Write(p2_step1), run_time=tracker.duration)

        with self.voiceover(
            text="We take the tangent of both sides."
        ) as tracker:
            p2_step2 = MathTex(r"\tan\left(\frac{\alpha}{2} + \frac{\beta}{2}\right) = \tan\left(90^\circ - \frac{\gamma}{2}\right)", font_size=24).next_to(p2_step1, DOWN, buff=0.2).align_to(q2_task, LEFT)
            self.play(Write(p2_step2), run_time=tracker.duration)

        with self.voiceover(
            text="On the left, we use the Tangent sum formula again. On the right, tangent of 90 degrees minus an angle "
            "flips to its co-function! It becomes cotangent. And cotangent is simply one over tangent."
        ) as tracker:
            p2_step3 = MathTex(
                r"\frac{\tan\frac{\alpha}{2} + \tan\frac{\beta}{2}}{1 - \tan\frac{\alpha}{2}\tan\frac{\beta}{2}} = \cot\frac{\gamma}{2} = \frac{1}{\tan\frac{\gamma}{2}}", 
                font_size=26
            ).next_to(p2_step2, DOWN, buff=0.2).align_to(q2_task, LEFT)
            self.play(Write(p2_step3), run_time=tracker.duration)

        with self.voiceover(
            text="We have a fraction on both sides. Let's cross-multiply. Tangent gamma over two multiplies the left numerator, "
            "and the left denominator multiplies the one on the right."
        ) as tracker:
            p2_step4 = MathTex(
                r"\tan\frac{\gamma}{2}\left(\tan\frac{\alpha}{2} + \tan\frac{\beta}{2}\right) = 1 - \tan\frac{\alpha}{2}\tan\frac{\beta}{2}", 
                font_size=24
            ).next_to(p2_step3, DOWN, buff=0.2).align_to(q2_task, LEFT)
            self.play(Write(p2_step4), run_time=tracker.duration)

        with self.voiceover(
            text="Distribute the terms on the left side..."
        ) as tracker:
            p2_step5 = MathTex(
                r"\tan\frac{\gamma}{2}\tan\frac{\alpha}{2} + \tan\frac{\gamma}{2}\tan\frac{\beta}{2} = 1 - \tan\frac{\alpha}{2}\tan\frac{\beta}{2}", 
                font_size=22
            ).next_to(p2_step4, DOWN, buff=0.2).align_to(q2_task, LEFT)
            self.play(Write(p2_step5), run_time=tracker.duration)

        with self.voiceover(
            text="Finally, add the negative term to the other side to group all the products together. "
            "And there we have it, our beautiful symmetrical identity is proven."
        ) as tracker:
            p2_final = MathTex(
                r"\tan\frac{\alpha}{2}\tan\frac{\beta}{2} + \tan\frac{\beta}{2}\tan\frac{\gamma}{2} + \tan\frac{\gamma}{2}\tan\frac{\alpha}{2} = 1", 
                font_size=24, color=CONFIG.C_HL
            ).next_to(p2_step5, DOWN, buff=0.3).align_to(q2_task, LEFT)
            box_p2 = SurroundingRectangle(p2_final, color=CONFIG.C_HL, buff=0.1)
            
            self.play(Write(p2_final), Create(box_p2), run_time=tracker.duration)

        # ----------------------------------------------------------------------
        # ACT 5: Conclusion
        # ----------------------------------------------------------------------
        with self.voiceover(
            text="Through the power of trigonometric identities, we've shown that the geometry of a triangle "
            "is intimately bound by these elegant algebraic equations. Keep practicing these proofs, and you will master trigonometry in no time!"
        ) as tracker:
            self.play(
                Indicate(box_p2, scale_factor=1.05, color=WHITE),
                triangle.animate.set_stroke(color=CONFIG.C_HL, width=4),
                run_time=3
            )
            self.wait(tracker.duration - 3)

        self.wait(2)
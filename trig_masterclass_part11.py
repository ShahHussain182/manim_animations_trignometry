"""
Trigonometry Masterclass - Part 11: Harmonic Addition (Combining Waves)
=======================================================================
A beginner-friendly visual explanation of how to combine a sine 
and cosine term into a single phase-shifted wave, using coefficient 
matching and a geometric 'phantom triangle'.

Run this file using:
manim -pql trig_masterclass_part11.py HarmonicAddition
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
    origin: np.ndarray = field(
        default_factory=lambda: np.array([-3.5, -0.5, 0.0])
    )
    C_BG: str = "#0b1017"
    C_AXES: str = "#4A5568"
    
    C_A: str = "#F1C40F"          # Yellow (for coefficient 3 / cos)
    C_B: str = "#FF4444"          # Red (for coefficient 4 / sin)
    C_R: str = "#00D2D3"          # Cyan (for r / hypotenuse)
    C_PHI: str = "#E056FD"        # Purple (for angle phi)

CONFIG = TrigConfig()

# ==============================================================================
# 2. Main Scene - Part 11
# ==============================================================================
class HarmonicAddition(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en"))
        self.camera.background_color = CONFIG.C_BG

        O = CONFIG.origin

        # ----------------------------------------------------------------------
        # ACT 1: Scene Layout & The Core Concept
        # ----------------------------------------------------------------------
        title = Title(
            r"Part 11: Harmonic Addition (Combining Waves)",
            font_size=32,
            color=WHITE
        )
        self.play(Write(title))

        # Geometric Plane (Left)
        axes = Axes(
            x_range=[-1, 5, 1], y_range=[-1, 5, 1],
            x_length=4.5, y_length=4.5,
            tips=True, axis_config={"color": CONFIG.C_AXES, "stroke_width": 1.5}
        ).move_to(O)
        
        lbl_axes = axes.get_axis_labels(x_label="x", y_label="y")

        # Derivation Board (Right)
        board_bg = RoundedRectangle(
            corner_radius=0.2, height=6.2, width=7.0,
            color=GRAY_D, fill_color="#121a24", fill_opacity=0.95
        ).to_edge(RIGHT, buff=0.15).shift(DOWN * 0.2)
        
        board_title = Text("Algebraic Derivation", font_size=20, color=YELLOW).next_to(board_bg.get_top(), DOWN, buff=0.2)
        board_line = Line(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(board_title, DOWN, buff=0.15)

        with self.voiceover(
            text="Welcome to Part 11. What happens if you add a sine wave and a cosine wave together? "
            "In physics and engineering, we often need to combine them into a single, shifted sine wave."
        ) as tracker:
            self.play(
                Create(axes), Write(lbl_axes),
                FadeIn(board_bg), Write(board_title), Create(board_line),
                run_time=tracker.duration
            )

        # The Goal
        task_eq = MathTex(
            r"\text{Express } 3\sin\theta + 4\cos\theta \text{ as } r\sin(\theta + \phi)",
            font_size=26
        ).next_to(board_line, DOWN, buff=0.3).align_to(board_line, LEFT).shift(RIGHT*0.2)
        
        self.play(Write(task_eq))

        # ----------------------------------------------------------------------
        # ACT 2: Reverse Engineering the Concept
        # ----------------------------------------------------------------------
        with self.voiceover(
            text="Textbooks usually just tell you to make a substitution. But why? "
            "To understand the secret, let's look at our target expression and expand it using the Sine Sum identity from Part 4."
        ) as tracker:
            self.wait(tracker.duration)

        exp_1 = MathTex(
            r"r\sin(\theta + \phi) = r(\sin\theta\cos\phi + \cos\theta\sin\phi)",
            font_size=24
        ).next_to(task_eq, DOWN, buff=0.3).align_to(task_eq, LEFT)
        self.play(Write(exp_1))

        exp_2 = MathTex(
            r"= (r\cos\phi)\sin\theta + (r\sin\phi)\cos\theta",
            font_size=24
        ).next_to(exp_1, DOWN, buff=0.15).align_to(exp_1, LEFT).shift(RIGHT*2)
        
        with self.voiceover(
            text="If we distribute the r, and rearrange the terms slightly, we get r cosine phi times sine theta, "
            "plus r sine phi times cosine theta."
        ) as tracker:
            self.play(Write(exp_2), run_time=tracker.duration)

        with self.voiceover(
            text="Now, let's write our original problem directly underneath this."
        ) as tracker:
            exp_3 = MathTex(
                r"= \ \ \ \ \mathbf{3} \ \ \ \ \sin\theta + \ \ \ \ \mathbf{4} \ \ \ \ \cos\theta",
                font_size=24
            ).next_to(exp_2, DOWN, buff=0.15).align_to(exp_2, LEFT)
            
            exp_3[0][1].set_color(CONFIG.C_A) # The '3'
            exp_3[0][9].set_color(CONFIG.C_B) # The '4'
            
            self.play(Write(exp_3), run_time=tracker.duration)

        with self.voiceover(
            text="Look closely! By matching the coefficients, we can see exactly what we need to do. "
            "The number 3 must take the place of r cosine phi. And the number 4 must take the place of r sine phi."
        ) as tracker:
            # Highlight matching parts
            box_cos = SurroundingRectangle(exp_2[0][1:8], color=CONFIG.C_A, buff=0.05)
            box_3 = SurroundingRectangle(exp_3[0][1], color=CONFIG.C_A, buff=0.05)
            
            box_sin = SurroundingRectangle(exp_2[0][13:20], color=CONFIG.C_B, buff=0.05)
            box_4 = SurroundingRectangle(exp_3[0][9], color=CONFIG.C_B, buff=0.05)
            
            self.play(Create(box_cos), Create(box_3), run_time=1)
            self.play(Create(box_sin), Create(box_4), run_time=1)
            self.wait(tracker.duration - 2)

        # Write the equations clearly
        sys_1 = MathTex(r"3 = r\cos\phi", font_size=24, color=CONFIG.C_A).next_to(exp_3, DOWN, buff=0.4).align_to(task_eq, LEFT)
        sys_2 = MathTex(r"4 = r\sin\phi", font_size=24, color=CONFIG.C_B).next_to(sys_1, RIGHT, buff=0.8)
        
        self.play(
            FadeOut(box_cos, box_3, box_sin, box_4),
            TransformFromCopy(exp_3[0][1], sys_1),
            TransformFromCopy(exp_3[0][9], sys_2)
        )

        # ----------------------------------------------------------------------
        # ACT 3: The Geometric 'Phantom Triangle'
        # ----------------------------------------------------------------------
        with self.voiceover(
            text="This isn't just a random algebra trick. This perfectly describes a right triangle mapped onto polar coordinates! "
            "Since both 3 and 4 are positive, this triangle lives in the first quadrant."
        ) as tracker:
            self.wait(1)

            # Draw the point (3, 4)
            pt_34 = axes.c2p(3, 4)
            dot_34 = Dot(pt_34, color=WHITE)
            
            # Draw triangle legs
            leg_x = Line(axes.c2p(0,0), axes.c2p(3,0), color=CONFIG.C_A, stroke_width=4)
            lbl_leg_x = MathTex("3", font_size=24, color=CONFIG.C_A).next_to(leg_x, DOWN, buff=0.1)
            
            leg_y = Line(axes.c2p(3,0), pt_34, color=CONFIG.C_B, stroke_width=4)
            lbl_leg_y = MathTex("4", font_size=24, color=CONFIG.C_B).next_to(leg_y, RIGHT, buff=0.1)
            
            self.play(Create(leg_x), Write(lbl_leg_x), run_time=1)
            self.play(Create(leg_y), Write(lbl_leg_y), FadeIn(dot_34), run_time=1)
            
        with self.voiceover(
            text="The horizontal adjacent side is our cosine term, 3. The vertical opposite side is our sine term, 4. "
            "Our combined amplitude r is simply the hypotenuse, and phi is the angle."
        ) as tracker:
            hypot = Line(axes.c2p(0,0), pt_34, color=CONFIG.C_R, stroke_width=4)
            lbl_hypot = MathTex("r", font_size=24, color=CONFIG.C_R).next_to(hypot.get_center(), UL, buff=0.05)
            
            arc_phi = Angle(leg_x, hypot, radius=0.6, color=CONFIG.C_PHI)
            lbl_phi = MathTex(r"\phi", font_size=24, color=CONFIG.C_PHI).next_to(arc_phi, RIGHT, buff=0.1).shift(UP*0.1)
            
            self.play(Create(hypot), Write(lbl_hypot), Create(arc_phi), Write(lbl_phi), run_time=tracker.duration)

        # ----------------------------------------------------------------------
        # ACT 4: Solving for r (Pythagoras)
        # ----------------------------------------------------------------------
        div_line = DashedLine(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(sys_1, DOWN, buff=0.3)
        self.play(Create(div_line))

        with self.voiceover(
            text="To find r algebraically, we square both equations and add them together. This is just the Pythagorean theorem!"
        ) as tracker:
            sq_eq = MathTex(
                r"3^2 + 4^2 = r^2\cos^2\phi + r^2\sin^2\phi", 
                font_size=24
            ).next_to(div_line, DOWN, buff=0.2).align_to(task_eq, LEFT)
            self.play(Write(sq_eq), run_time=tracker.duration)

        with self.voiceover(
            text="Factoring out r squared leaves cosine squared plus sine squared, which we know equals one."
        ) as tracker:
            sq_eq2 = MathTex(
                r"9 + 16 = r^2(\cos^2\phi + \sin^2\phi)", 
                font_size=24
            ).next_to(sq_eq, DOWN, buff=0.2).align_to(task_eq, LEFT)
            self.play(Write(sq_eq2), run_time=tracker.duration)

        with self.voiceover(
            text="25 equals r squared. Therefore, r is 5. We have found the amplitude of our combined wave."
        ) as tracker:
            sq_eq3 = MathTex(
                r"25 = r^2(1) \implies r = 5", 
                font_size=24, color=CONFIG.C_R
            ).next_to(sq_eq2, DOWN, buff=0.2).align_to(task_eq, LEFT)
            self.play(Write(sq_eq3), run_time=2)
            
            # Update the triangle visually
            lbl_hypot_val = MathTex("5", font_size=24, color=CONFIG.C_R).move_to(lbl_hypot)
            self.play(Transform(lbl_hypot, lbl_hypot_val))
            self.wait(tracker.duration - 2)

        # ----------------------------------------------------------------------
        # ACT 5: Solving for Phi (Tangent)
        # ----------------------------------------------------------------------
        with self.voiceover(
            text="To find the angle phi, we divide our sine equation by our cosine equation. "
        ) as tracker:
            div_eq1 = MathTex(
                r"\frac{r\sin\phi}{r\cos\phi} = \frac{4}{3}", 
                font_size=24
            ).next_to(sq_eq3, DOWN, buff=0.3).align_to(task_eq, LEFT)
            self.play(Write(div_eq1), run_time=tracker.duration)

        with self.voiceover(
            text="The r cancels out, and sine over cosine becomes tangent. Tangent of phi equals four-thirds."
        ) as tracker:
            div_eq2 = MathTex(
                r"\tan\phi = \frac{4}{3}", 
                font_size=24, color=CONFIG.C_PHI
            ).next_to(div_eq1, DOWN, buff=0.2).align_to(task_eq, LEFT)
            self.play(Write(div_eq2), run_time=tracker.duration)

        # ----------------------------------------------------------------------
        # ACT 6: Final Answer & Conclusion
        # ----------------------------------------------------------------------
        div_line2 = DashedLine(board_bg.get_left(), board_bg.get_right(), color=GRAY_D).next_to(div_eq2, DOWN, buff=0.3)
        self.play(Create(div_line2))

        with self.voiceover(
            text="Now we simply substitute our values of r and phi back into the target form."
        ) as tracker:
            final_eq1 = MathTex(
                r"3\sin\theta + 4\cos\theta = 5\sin(\theta + \phi)", 
                font_size=26
            ).next_to(div_line2, DOWN, buff=0.2).align_to(task_eq, LEFT)
            self.play(Write(final_eq1), run_time=tracker.duration)

        with self.voiceover(
            text="Where the phase shift phi is the inverse tangent of four-thirds. And we are done! "
            "By looking at the math as a hidden right triangle, these equations make perfect intuitive sense."
        ) as tracker:
            final_eq2 = MathTex(
                r"\text{where } \phi = \tan^{-1}\left(\frac{4}{3}\right)", 
                font_size=26, color=CONFIG.C_PHI
            ).next_to(final_eq1, DOWN, buff=0.15).align_to(task_eq, LEFT).shift(RIGHT*1.5)
            
            box_final = SurroundingRectangle(VGroup(final_eq1, final_eq2), color=WHITE, buff=0.1)
            
            self.play(Write(final_eq2), Create(box_final), run_time=3)
            self.wait(tracker.duration - 3)

        self.wait(3)
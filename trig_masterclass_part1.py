"""
Trigonometry Masterclass - Part 1: The Foundations & Tangent Geometry
=====================================================================
Run this file using:
manim -pql trig_masterclass_part1.py TrigMasterclassPart1
"""

from dataclasses import dataclass, field
import numpy as np
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

# ==============================================================================
# 1. Configuration & Color Palette (Matched perfectly to the image)
# ==============================================================================
@dataclass(frozen=True)
class TrigConfig:
    # 42 degrees matches the proportions of the provided diagram very well
    alpha_deg: float = 42.0 
    radius: float = 2.4

    # Shifted left and down to allow room for the massive sec/csc/cot extensions
    origin: np.ndarray = field(
        default_factory=lambda: np.array([-1.5, -1.8, 0.0])
    )

    # Exact colors extracted from the visual reference
    C_BG: str = "#050505"
    C_AXES: str = "#4A5568"
    C_CIRCLE: str = "#FFFFFF"
    C_HYPOTENUSE: str = "#FFFFFF"
    
    C_COS: str = "#FFFF00"        # Yellow
    C_SIN: str = "#FF4444"        # Red
    C_TAN: str = "#00FFFF"        # Cyan
    C_COT: str = "#3388FF"        # Blue
    C_SEC: str = "#FF00FF"        # Magenta
    C_CSC: str = "#FF0000"        # Red (matches Coversin in diagram style)
    
    @property
    def alpha(self) -> float:
        return np.radians(self.alpha_deg)

CONFIG = TrigConfig()

# ==============================================================================
# 2. Main Scene - Part 1
# ==============================================================================
class TrigMasterclassPart1(VoiceoverScene):
    def construct(self):
        # Initialize Google Text-to-Speech service
        self.set_speech_service(GTTSService(lang="en"))
        
        # Set dark background matching the image
        self.camera.background_color = CONFIG.C_BG

        O = CONFIG.origin
        R = CONFIG.radius

        # ----------------------------------------------------------------------
        # ACT 1: The Title & Coordinate Foundation
        # ----------------------------------------------------------------------
        title = Text("Trigonometry", font_size=48, color="#3388FF", weight=BOLD)
        title.to_edge(UP, buff=0.5)

        with self.voiceover(
            text="Welcome to the ultimate geometric masterclass on Trigonometry. "
            "Today, we will reconstruct one of the most beautiful mathematical diagrams ever created, "
            "showing all trigonometric functions on a single unit circle."
        ) as tracker:
            self.play(Write(title), run_time=tracker.duration)

        # Create axes with specific bounds to fit the large external functions
        axes = Axes(
            x_range=[-1.5, 3.5, 1],
            y_range=[-1.5, 3.5, 1],
            x_length=R * 5,
            y_length=R * 5,
            tips=False,
            axis_config={"color": CONFIG.C_AXES, "stroke_width": 1.5},
        ).move_to(O, coor_mask=np.array([1, 1, 0]))

        unit_circle = Circle(
            radius=R,
            color=CONFIG.C_CIRCLE,
            stroke_width=3,
        ).move_to(O)

        with self.voiceover(
            text="We begin with a Cartesian coordinate system and a perfect circle centered at the origin, "
            "with a radius defined as exactly one unit."
        ) as tracker:
            self.play(Create(axes), run_time=1.5)
            self.play(Create(unit_circle), run_time=tracker.duration - 1.5)

        # ----------------------------------------------------------------------
        # ACT 2: Dynamic Sine and Cosine
        # ----------------------------------------------------------------------
        # ValueTracker allows us to smoothly animate the angle before locking it in
        theta = ValueTracker(np.radians(15))

        dot_P = always_redraw(lambda: Dot(
            O + R * np.array([np.cos(theta.get_value()), np.sin(theta.get_value()), 0]),
            color=WHITE, radius=0.06
        ))

        radius_line = always_redraw(lambda: Line(
            O, dot_P.get_center(), color=CONFIG.C_HYPOTENUSE, stroke_width=2.5
        ))
        
        lbl_one = always_redraw(lambda: MathTex("1", font_size=18, color=WHITE)
            .next_to(radius_line.get_center(), UL, buff=0.05)
        )

        angle_arc = always_redraw(lambda: Arc(
            radius=R * 0.25, start_angle=0, angle=theta.get_value(), arc_center=O,
            color=WHITE, stroke_width=2
        ))
        
        lbl_alpha = always_redraw(lambda: MathTex(r"\alpha", font_size=20, color=WHITE)
            .next_to(angle_arc, RIGHT, buff=0.08).shift(UP*0.05)
        )

        sin_line = always_redraw(lambda: Line(
            O + R * np.array([np.cos(theta.get_value()), 0, 0]), 
            dot_P.get_center(), 
            color=CONFIG.C_SIN, stroke_width=4
        ))
        
        cos_line = always_redraw(lambda: Line(
            O, 
            O + R * np.array([np.cos(theta.get_value()), 0, 0]), 
            color=CONFIG.C_COS, stroke_width=4
        ))

        with self.voiceover(
            text="Let us draw a radius line to form an angle, alpha. "
            "If we drop a perpendicular line to the x-axis, we form a right triangle."
        ) as tracker:
            self.play(
                Create(radius_line), Write(lbl_one), 
                Create(angle_arc), Write(lbl_alpha), FadeIn(dot_P),
                run_time=tracker.duration
            )

        with self.voiceover(
            text="The horizontal base of this triangle is exactly the cosine of alpha, shown in yellow. "
            "And the vertical height is the sine of alpha, shown in red."
        ) as tracker:
            self.play(Create(cos_line), Create(sin_line), run_time=tracker.duration)

        lbl_cos = always_redraw(lambda: MathTex(r"\cos \alpha", font_size=20, color=CONFIG.C_COS)
            .next_to(cos_line, DOWN, buff=0.1)
        )
        lbl_sin = always_redraw(lambda: MathTex(r"\sin \alpha", font_size=20, color=CONFIG.C_SIN)
            .next_to(sin_line, LEFT, buff=0.1)
        )
        self.play(Write(lbl_cos), Write(lbl_sin))

        # Dynamic Sweep
        with self.voiceover(
            text="Notice how as the angle changes, the physical lengths of sine and cosine grow and shrink seamlessly within the bounds of the unit circle. "
            "Let's lock our angle in place to discover the remaining functions."
        ) as tracker:
            self.play(theta.animate.set_value(np.radians(75)), run_time=2.5, rate_func=there_and_back)
            self.play(theta.animate.set_value(CONFIG.alpha), run_time=2, rate_func=smooth)

        # Clear always_redraws and replace with static objects for the complex buildup
        self.clear()
        self.add(title, axes, unit_circle)
        
        # Static definitions based on fixed alpha
        a = CONFIG.alpha
        pt_P = O + R * np.array([np.cos(a), np.sin(a), 0])
        pt_X_int = O + R * np.array([1/np.cos(a), 0, 0])
        pt_Y_int = O + R * np.array([0, 1/np.sin(a), 0])
        
        static_radius = Line(O, pt_P, color=WHITE, stroke_width=2.5)
        static_arc = Arc(radius=R*0.25, start_angle=0, angle=a, arc_center=O, color=WHITE)
        static_alpha = MathTex(r"\alpha", font_size=20, color=WHITE).next_to(static_arc, RIGHT, buff=0.08).shift(UP*0.05)
        static_dot = Dot(pt_P, color=WHITE, radius=0.06)
        
        static_cos = Line(O, O + R * np.array([np.cos(a), 0, 0]), color=CONFIG.C_COS, stroke_width=4)
        static_sin = Line(O + R * np.array([np.cos(a), 0, 0]), pt_P, color=CONFIG.C_SIN, stroke_width=4)
        s_lbl_cos = MathTex(r"\cos \alpha", font_size=22, color=CONFIG.C_COS).next_to(static_cos, DOWN, buff=0.1)
        s_lbl_sin = MathTex(r"\sin \alpha", font_size=22, color=CONFIG.C_SIN).next_to(static_sin, LEFT, buff=0.1)
        s_lbl_one = MathTex("1", font_size=18, color=WHITE).next_to(static_radius.get_center(), UL, buff=0.05)

        self.add(static_radius, static_arc, static_alpha, static_dot, static_cos, static_sin, s_lbl_cos, s_lbl_sin, s_lbl_one)

        # ----------------------------------------------------------------------
        # ACT 3: The Literal Tangent Line
        # ----------------------------------------------------------------------
        tangent_line = Line(
            pt_Y_int + np.array([-0.5, 0.5/np.tan(a), 0]), 
            pt_X_int + np.array([0.5, -0.5*np.tan(a), 0]), 
            color=WHITE, stroke_width=1.5, stroke_opacity=0.6
        )

        with self.voiceover(
            text="Why do we call the tangent function by that specific name? "
            "Because it is derived from a literal tangent line. Watch as we draw a straight line tangent to the circle, exactly at our point."
        ) as tracker:
            self.play(Create(tangent_line), run_time=tracker.duration)

        # Tangent Segment on the line
        tan_segment = Line(pt_P, pt_X_int, color=CONFIG.C_TAN, stroke_width=4.5)
        lbl_tan_diag = MathTex(r"\tan \alpha", font_size=22, color=CONFIG.C_TAN).next_to(tan_segment.get_center(), UR, buff=0.05)

        with self.voiceover(
            text="Through similar triangles, the distance from the point on the circle traveling down this tangent line to the x-axis, "
            "is mathematically identical to the tangent of alpha."
        ) as tracker:
            self.play(Create(tan_segment), Write(lbl_tan_diag), run_time=tracker.duration)

        # Cotangent Segment on the line
        cot_segment = Line(pt_P, pt_Y_int, color=CONFIG.C_COT, stroke_width=4.5)
        lbl_cot_diag = MathTex(r"\cot \alpha", font_size=22, color=CONFIG.C_COT).next_to(cot_segment.get_center(), DL, buff=0.1)

        with self.voiceover(
            text="Likewise, traveling up the tangent line to intersect the y-axis gives us the exact length of the cotangent of alpha."
        ) as tracker:
            self.play(Create(cot_segment), Write(lbl_cot_diag), run_time=tracker.duration)

        # ----------------------------------------------------------------------
        # ACT 4: Folding the Tangent & Dashed Arcs (The Magic of the Diagram)
        # ----------------------------------------------------------------------
        # Mathematical projection for Tangent Arc
        # Center = pt_X_int. Start = pt_P. Sweeps to vertical position.
        pt_tan_vert_top = O + R * np.array([1/np.cos(a), np.tan(a), 0])
        tan_fold_line = Line(pt_X_int, pt_tan_vert_top, color=CONFIG.C_TAN, stroke_width=4.5)
        lbl_tan_vert = MathTex(r"\tan \alpha", font_size=22, color=CONFIG.C_TAN).next_to(tan_fold_line, RIGHT, buff=0.1)

        tan_dashed_arc = DashedVMobject(Arc(
            radius=R * np.tan(a),
            arc_center=pt_X_int,
            start_angle=PI/2 + a,
            angle=-a,
            color=WHITE, stroke_width=1.5
        ), num_dashes=15)

        with self.voiceover(
            text="In classical geometry diagrams, we often fold these lengths so they sit parallel to the axes. "
            "If we pivot the tangent segment around its x-intercept, it stands perfectly vertical, creating the traditional right triangle representation of tangent."
        ) as tracker:
            self.play(Create(tan_dashed_arc), run_time=1.5)
            self.play(TransformFromCopy(tan_segment, tan_fold_line), Write(lbl_tan_vert), run_time=1.5)
            self.wait(0.5)

        # Mathematical projection for Cotangent Arc
        # Center = pt_Y_int. Start = pt_P. Sweeps to horizontal position.
        pt_cot_horiz_right = O + R * np.array([np.cos(a)/np.sin(a), 1/np.sin(a), 0])
        cot_fold_line = Line(pt_Y_int, pt_cot_horiz_right, color=CONFIG.C_COT, stroke_width=4.5)
        lbl_cot_horiz = MathTex(r"\cot \alpha", font_size=22, color=CONFIG.C_COT).next_to(cot_fold_line, UP, buff=0.1)

        cot_dashed_arc = DashedVMobject(Arc(
            radius=R / np.tan(a),
            arc_center=pt_Y_int,
            start_angle=a - PI/2,
            angle=PI/2 - a,
            color=WHITE, stroke_width=1.5
        ), num_dashes=20)

        with self.voiceover(
            text="Similarly, we can pivot the cotangent segment around the y-intercept. "
            "It swings up to form a perfectly horizontal line bordering the top of our geometric system."
        ) as tracker:
            self.play(Create(cot_dashed_arc), run_time=1.5)
            self.play(TransformFromCopy(cot_segment, cot_fold_line), Write(lbl_cot_horiz), run_time=1.5)

        # End of Part 1 Teaser
        with self.voiceover(
            text="We have now mapped Sine, Cosine, Tangent, and Cotangent onto a unified framework. "
            "But what about Secant, Cosecant, and the forgotten ancient functions like Versine and Exsecant? "
            "Join me in Part 2 as we complete this magnificent puzzle."
        ) as tracker:
            self.wait(tracker.duration)
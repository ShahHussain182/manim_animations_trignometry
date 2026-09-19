"""
Trigonometry Masterclass - Part 2: The Advanced & Historical Functions
======================================================================
Run this file using:
manim -pql trig_masterclass_part2.py TrigMasterclassPart2
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
    # Must match Part 1 perfectly
    alpha_deg: float = 42.0 
    radius: float = 2.4

    # Shifted left and down to allow room for the massive sec/csc projections
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
    
    # New colors for Part 2
    C_SEC: str = "#FF00FF"        # Magenta
    C_CSC: str = "#FF0000"        # Red (Leftmost outer)
    C_VERSIN: str = "#FF00FF"     # Magenta/Purple (Inner X-axis)
    C_COVERSIN: str = "#FF0000"   # Red (Inner Y-axis)
    C_EXSEC: str = "#00FF00"      # Green (Outer X-axis)
    C_EXCSC: str = "#FF00FF"      # Magenta/Purple (Outer Y-axis)
    C_VERCOS: str = "#00FFFF"     # Cyan (Bottom inner horizontal)
    C_COVERCOS: str = "#00FF00"   # Green (Left inner vertical)
    
    @property
    def alpha(self) -> float:
        return np.radians(self.alpha_deg)

CONFIG = TrigConfig()

# ==============================================================================
# 2. Main Scene - Part 2
# ==============================================================================
class TrigMasterclassPart2(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en"))
        self.camera.background_color = CONFIG.C_BG

        # Fast-forward Setup to match the end of Part 1
        self.setup_part1_state()

        O = CONFIG.origin
        R = CONFIG.radius
        a = CONFIG.alpha
        
        # Precompute key coordinates
        pt_X_int = O + R * np.array([1/np.cos(a), 0, 0])
        pt_Y_int = O + R * np.array([0, 1/np.sin(a), 0])
        
        # ----------------------------------------------------------------------
        # ACT 5: Secant and Cosecant Projections
        # ----------------------------------------------------------------------
        # Secant Projection (Magenta)
        y_sec_proj = O[1] - R * 0.45
        pt_sec_start = np.array([O[0], y_sec_proj, 0])
        pt_sec_end = np.array([pt_X_int[0], y_sec_proj, 0])

        dash_sec_L = DashedLine(O, pt_sec_start, color=GRAY, stroke_width=1.5)
        dash_sec_R = DashedLine(pt_X_int, pt_sec_end, color=GRAY, stroke_width=1.5)
        sec_line = Line(pt_sec_start, pt_sec_end, color=CONFIG.C_SEC, stroke_width=4.5)
        lbl_sec = MathTex(r"\sec \alpha", font_size=22, color=CONFIG.C_SEC).next_to(sec_line, DOWN, buff=0.1)

        with self.voiceover(
            text="Welcome back. We left off with Sine, Cosine, Tangent, and Cotangent. "
            "But what about the hypotenuses? The distance from the origin to the x-intercept of the tangent line is the Secant of alpha. "
            "Let's project this length downwards to view it clearly."
        ) as tracker:
            self.play(Create(dash_sec_L), Create(dash_sec_R), run_time=1)
            self.play(Create(sec_line), Write(lbl_sec), run_time=tracker.duration - 1)

        # Cosecant Projection (Red)
        x_csc_proj = O[0] - R * 0.45
        pt_csc_start = np.array([x_csc_proj, O[1], 0])
        pt_csc_end = np.array([x_csc_proj, pt_Y_int[1], 0])

        dash_csc_B = DashedLine(O, pt_csc_start, color=GRAY, stroke_width=1.5)
        dash_csc_T = DashedLine(pt_Y_int, pt_csc_end, color=GRAY, stroke_width=1.5)
        csc_line = Line(pt_csc_start, pt_csc_end, color=CONFIG.C_CSC, stroke_width=4.5)
        lbl_csc = MathTex(r"\csc \alpha", font_size=22, color=CONFIG.C_CSC).next_to(csc_line, LEFT, buff=0.1)

        with self.voiceover(
            text="Similarly, the distance from the origin up to the y-intercept is the Cosecant of alpha. "
            "Projecting this outward to the left completes our primary six trigonometric functions."
        ) as tracker:
            self.play(Create(dash_csc_B), Create(dash_csc_T), run_time=1)
            self.play(Create(csc_line), Write(lbl_csc), run_time=tracker.duration - 1)

        # ----------------------------------------------------------------------
        # ACT 6: The Versed Functions (Versine & Coversine)
        # ----------------------------------------------------------------------
        # Versine (Magenta/Purple on x-axis)
        pt_cos_end = O + R * np.array([np.cos(a), 0, 0])
        pt_circ_right = O + R * np.array([1, 0, 0])
        versin_line = Line(pt_cos_end, pt_circ_right, color=CONFIG.C_VERSIN, stroke_width=4.5)
        lbl_versin = MathTex(r"\text{versin}\,\alpha", font_size=20, color=CONFIG.C_VERSIN).next_to(versin_line, DOWN, buff=0.05).shift(DOWN*0.1)

        # Coversine (Red on y-axis)
        pt_sin_end = O + R * np.array([0, np.sin(a), 0])
        pt_circ_top = O + R * np.array([0, 1, 0])
        coversin_line = Line(pt_sin_end, pt_circ_top, color=CONFIG.C_COVERSIN, stroke_width=4.5)
        lbl_coversin = MathTex(r"\text{coversin}\,\alpha", font_size=20, color=CONFIG.C_COVERSIN).next_to(coversin_line, LEFT, buff=0.08)

        with self.voiceover(
            text="Before modern computers, sailors navigating by the stars relied on 'versed' functions. "
            "The Versine is the small gap between the cosine and the edge of the unit circle. It is exactly one minus cosine."
        ) as tracker:
            self.play(Create(versin_line), Write(lbl_versin), run_time=tracker.duration)

        with self.voiceover(
            text="The vertical equivalent, filling the gap from the sine to the top of the circle, is the Coversine."
        ) as tracker:
            self.play(Create(coversin_line), Write(lbl_coversin), run_time=tracker.duration)

        # ----------------------------------------------------------------------
        # ACT 7: The Exterior Functions (Exsecant & Excosecant)
        # ----------------------------------------------------------------------
        # Exsecant (Green on x-axis)
        exsec_line = Line(pt_circ_right, pt_X_int, color=CONFIG.C_EXSEC, stroke_width=4.5)
        lbl_exsec = MathTex(r"\text{exsec}\,\alpha", font_size=20, color=CONFIG.C_EXSEC).next_to(exsec_line, DOWN, buff=0.05).shift(DOWN*0.1)

        # Excosecant (Magenta/Purple on y-axis)
        excsc_line = Line(pt_circ_top, pt_Y_int, color=CONFIG.C_EXCSC, stroke_width=4.5)
        lbl_excsc = MathTex(r"\text{excsc}\,\alpha", font_size=20, color=CONFIG.C_EXCSC).next_to(excsc_line, LEFT, buff=0.08)

        with self.voiceover(
            text="Extending outwards from the circle to the tangent intercepts gives us the exterior functions. "
            "On the x-axis, the Exsecant is the Secant minus one."
        ) as tracker:
            self.play(Create(exsec_line), Write(lbl_exsec), run_time=tracker.duration)
            
        with self.voiceover(
            text="And on the y-axis, climbing from the circle to the very top, we find the Excosecant."
        ) as tracker:
            self.play(Create(excsc_line), Write(lbl_excsc), run_time=tracker.duration)

        # ----------------------------------------------------------------------
        # ACT 8: Vercosine and Covercosine (The Span of the Circle)
        # ----------------------------------------------------------------------
        # Vercosine (Cyan horizontal line)
        pt_circ_left = O + R * np.array([-1, 0, 0])
        y_vercos_proj = O[1] - R * 0.25
        pt_vercos_start = np.array([pt_circ_left[0], y_vercos_proj, 0])
        pt_vercos_end = np.array([pt_cos_end[0], y_vercos_proj, 0])

        dash_vercos_L = DashedLine(pt_circ_left, pt_vercos_start, color=GRAY, stroke_width=1.5)
        dash_vercos_R = DashedLine(pt_cos_end, pt_vercos_end, color=GRAY, stroke_width=1.5)
        vercos_line = Line(pt_vercos_start, pt_vercos_end, color=CONFIG.C_VERCOS, stroke_width=4.5)
        lbl_vercos = MathTex(r"\text{vercos}\,\alpha", font_size=20, color=CONFIG.C_VERCOS).next_to(vercos_line, DOWN, buff=0.08)

        with self.voiceover(
            text="To complete the set, we map the distances stretching from the opposite side of the circle. "
            "Vercosine is one plus cosine. We project it underneath the circle, nestled just above the Secant."
        ) as tracker:
            self.play(Create(dash_vercos_L), Create(dash_vercos_R), run_time=1)
            self.play(Create(vercos_line), Write(lbl_vercos), run_time=tracker.duration - 1)

        # Covercosine (Green vertical line)
        pt_circ_bot = O + R * np.array([0, -1, 0])
        x_covercos_proj = O[0] - R * 0.25
        pt_covercos_start = np.array([x_covercos_proj, pt_circ_bot[1], 0])
        pt_covercos_end = np.array([x_covercos_proj, pt_sin_end[1], 0])

        dash_covercos_B = DashedLine(pt_circ_bot, pt_covercos_start, color=GRAY, stroke_width=1.5)
        dash_covercos_T = DashedLine(pt_sin_end, pt_covercos_end, color=GRAY, stroke_width=1.5)
        covercos_line = Line(pt_covercos_start, pt_covercos_end, color=CONFIG.C_COVERCOS, stroke_width=4.5)
        lbl_covercos = MathTex(r"\text{covercos}\,\alpha", font_size=20, color=CONFIG.C_COVERCOS).next_to(covercos_line, LEFT, buff=0.08)

        with self.voiceover(
            text="Finally, Covercosine is one plus sine. We project it to the left, running beautifully parallel to our Cosecant."
        ) as tracker:
            self.play(Create(dash_covercos_B), Create(dash_covercos_T), run_time=1)
            self.play(Create(covercos_line), Write(lbl_covercos), run_time=tracker.duration - 1)

        # ----------------------------------------------------------------------
        # ACT 9: The Grand Finale
        # ----------------------------------------------------------------------
        # Add the remaining dashed construction circles to frame the masterpiece
        dashed_circle_left = DashedVMobject(Arc(
            radius=R, arc_center=O, start_angle=PI/2, angle=PI, color=GRAY, stroke_width=1.5
        ), num_dashes=30)
        
        dashed_circle_bot = DashedVMobject(Arc(
            radius=R, arc_center=O, start_angle=-PI/2, angle=PI/2, color=GRAY, stroke_width=1.5
        ), num_dashes=15)

        with self.voiceover(
            text="By tracing the remaining arcs of the unit circle, the master diagram is complete. "
            "What began as simple ratios of right triangles reveals itself as a majestic, interconnected system of geometric lengths. "
            "This is the true beauty of trigonometry."
        ) as tracker:
            self.play(Create(dashed_circle_left), Create(dashed_circle_bot), run_time=2)
            self.wait(tracker.duration - 2)

        self.wait(3)

    def setup_part1_state(self):
        """Instantly draws the end state of Part 1 without animation."""
        O = CONFIG.origin
        R = CONFIG.radius
        a = CONFIG.alpha
        
        # 1. Base UI
        title = Text("Trigonometry", font_size=48, color="#3388FF", weight=BOLD).to_edge(UP, buff=0.5)
        axes = Axes(
            x_range=[-1.5, 3.5, 1], y_range=[-1.5, 3.5, 1],
            x_length=R * 5, y_length=R * 5,
            tips=False, axis_config={"color": CONFIG.C_AXES, "stroke_width": 1.5}
        ).move_to(O, coor_mask=np.array([1, 1, 0]))
        unit_circle = Circle(radius=R, color=CONFIG.C_CIRCLE, stroke_width=3).move_to(O)

        self.add(title, axes, unit_circle)

        # 2. Angle and Inner Triangles
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

        # 3. Tangent Line & Folded Projections
        tangent_line = Line(
            pt_Y_int + np.array([-0.5, 0.5/np.tan(a), 0]), 
            pt_X_int + np.array([0.5, -0.5*np.tan(a), 0]), 
            color=WHITE, stroke_width=1.5, stroke_opacity=0.6
        )
        
        # Folded Vertical Tangent
        pt_tan_vert_top = O + R * np.array([1/np.cos(a), np.tan(a), 0])
        tan_fold_line = Line(pt_X_int, pt_tan_vert_top, color=CONFIG.C_TAN, stroke_width=4.5)
        lbl_tan_vert = MathTex(r"\tan \alpha", font_size=22, color=CONFIG.C_TAN).next_to(tan_fold_line, RIGHT, buff=0.1)
        tan_dashed_arc = DashedVMobject(Arc(
            radius=R * np.tan(a), arc_center=pt_X_int, start_angle=PI/2 + a, angle=-a,
            color=WHITE, stroke_width=1.5
        ), num_dashes=15)

        # Folded Horizontal Cotangent
        pt_cot_horiz_right = O + R * np.array([np.cos(a)/np.sin(a), 1/np.sin(a), 0])
        cot_fold_line = Line(pt_Y_int, pt_cot_horiz_right, color=CONFIG.C_COT, stroke_width=4.5)
        lbl_cot_horiz = MathTex(r"\cot \alpha", font_size=22, color=CONFIG.C_COT).next_to(cot_fold_line, UP, buff=0.1)
        cot_dashed_arc = DashedVMobject(Arc(
            radius=R / np.tan(a), arc_center=pt_Y_int, start_angle=a - PI/2, angle=PI/2 - a,
            color=WHITE, stroke_width=1.5
        ), num_dashes=20)

        self.add(
            tangent_line, tan_fold_line, lbl_tan_vert, tan_dashed_arc,
            cot_fold_line, lbl_cot_horiz, cot_dashed_arc
        )
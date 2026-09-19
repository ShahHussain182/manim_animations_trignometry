"""
Trigonometry Masterclass - Part 3: Fundamental Law & Deductions
======================================================================
Run this file using:
manim -pql trig_fundamental_law.py TrigFundamentalLaw
"""

from dataclasses import dataclass, field
import numpy as np
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# ==============================================================================
# 1. Configuration & Color Palette
# ==============================================================================
@dataclass(frozen=True)
class TrigConfig:
    # Default angles for demonstrations
    alpha_deg: float = 50.0
    beta_deg: float = 20.0
    radius: float = 2.0
    
    # Origin position - centered for dual-circle comparisons
    origin_left: np.ndarray = field(
        default_factory=lambda: np.array([-2.5, -0.5, 0.0])
    )
    origin_right: np.ndarray = field(
        default_factory=lambda: np.array([2.5, -0.5, 0.0])
    )
    
    # Colors
    C_BG: str = "#050505"
    C_AXES: str = "#4A5568"
    C_CIRCLE: str = "#FFFFFF"
    C_HYPOTENUSE: str = "#FFFFFF"
    
    C_ALPHA: str = "#FF4444"      # Red for alpha
    C_BETA: str = "#00FFFF"       # Cyan for beta
    C_ALPHA_MINUS_BETA: str = "#FFFF00"  # Yellow for α-β
    C_RESULT: str = "#00FF00"     # Green for result
    
    C_COS: str = "#FFFF00"        # Yellow
    C_SIN: str = "#FF4444"        # Red
    C_TAN: str = "#00FFFF"        # Cyan
    
    @property
    def alpha(self) -> float:
        return np.radians(self.alpha_deg)
    
    @property
    def beta(self) -> float:
        return np.radians(self.beta_deg)
    
    @property
    def alpha_minus_beta(self) -> float:
        return self.alpha - self.beta

CONFIG = TrigConfig()

# ==============================================================================
# Helper Functions
# ==============================================================================
def create_unit_circle_axes(origin, radius, color_axes="#4A5568", color_circle="#FFFFFF"):
    """Create axes and unit circle at specified origin."""
    axes = Axes(
        x_range=[-3.5, 3.5, 1], 
        y_range=[-3.5, 3.5, 1],
        x_length=radius * 6, 
        y_length=radius * 6,
        tips=False, 
        axis_config={"color": color_axes, "stroke_width": 1.2}
    ).move_to(origin, coor_mask=np.array([1, 1, 0]))
    
    circle = Circle(radius=radius, color=color_circle, stroke_width=2.5).move_to(origin)
    
    return axes, circle

def get_point_on_circle(origin, radius, angle):
    """Get coordinates of point on circle at given angle."""
    return origin + radius * np.array([np.cos(angle), np.sin(angle), 0])

def create_angle_arc(origin, radius, start_angle, end_angle, color, scale=0.3):
    """Create an arc showing an angle."""
    arc_radius = radius * scale
    if end_angle > start_angle:
        angle_size = end_angle - start_angle
    else:
        angle_size = 2*np.pi + end_angle - start_angle
    
    return Arc(
        radius=arc_radius, 
        arc_center=origin, 
        start_angle=start_angle, 
        angle=angle_size, 
        color=color, 
        stroke_width=3
    )

# ==============================================================================
# Main Scene
# ==============================================================================
class TrigFundamentalLaw(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en"))
        self.camera.background_color = CONFIG.C_BG
        
        O_L = CONFIG.origin_left
        O_R = CONFIG.origin_right
        R = CONFIG.radius
        
        alpha = CONFIG.alpha
        beta = CONFIG.beta
        alpha_minus_beta = CONFIG.alpha_minus_beta
        
        # Precompute points for left circle (α and β separately)
        pt_alpha_L = get_point_on_circle(O_L, R, alpha)
        pt_beta_L = get_point_on_circle(O_L, R, beta)
        
        # Precompute points for right circle (α-β)
        pt_diff_R = get_point_on_circle(O_R, R, alpha_minus_beta)
        pt_zero_R = get_point_on_circle(O_R, R, 0)
        
        # ======================================================================
        # ACT 1: Introduction to the Fundamental Law
        # ======================================================================
        title = Text("The Fundamental Law of Trigonometry", font_size=44, color="#3388FF", weight=BOLD).to_edge(UP, buff=0.5)
        
        fundamental_law = MathTex(
            r"\cos(\alpha - \beta) = \cos\alpha \cos\beta + \sin\alpha \sin\beta",
            font_size=36,
            color=CONFIG.C_RESULT
        ).to_edge(DOWN, buff=0.8)
        
        with self.voiceover(
            text="Welcome to our exploration of the Fundamental Law of Trigonometry. "
            "This elegant identity relates the cosine of a difference of two angles to the products of their sines and cosines. "
            "Let's discover why this is true through geometric reasoning."
        ) as tracker:
            self.play(Write(title), run_time=1)
            self.play(Write(fundamental_law), run_time=tracker.duration - 1)
        
        self.wait(1)
        
        # ======================================================================
        # ACT 2: Setting Up Two Unit Circles
        # ======================================================================
        axes_L, circle_L = create_unit_circle_axes(O_L, R)
        axes_R, circle_R = create_unit_circle_axes(O_R, R)
        
        label_L = MathTex(r"\text{Circle 1}", font_size=24, color=CONFIG.C_AXES).next_to(axes_L, DOWN, buff=0.3)
        label_R = MathTex(r"\text{Circle 2}", font_size=24, color=CONFIG.C_AXES).next_to(axes_R, DOWN, buff=0.3)
        
        with self.voiceover(
            text="We begin with two unit circles. On the left, we'll place angles alpha and beta separately. "
            "On the right, we'll place their difference, alpha minus beta."
        ) as tracker:
            self.play(Create(axes_L), Create(circle_L), Write(label_L), run_time=1)
            self.play(Create(axes_R), Create(circle_R), Write(label_R), run_time=tracker.duration - 1)
        
        # ======================================================================
        # ACT 3: Drawing Angles Alpha and Beta on Left Circle
        # ======================================================================
        # Draw angle beta first (smaller)
        radius_beta_L = Line(O_L, pt_beta_L, color=CONFIG.C_BETA, stroke_width=2.5)
        arc_beta_L = create_angle_arc(O_L, R, 0, beta, CONFIG.C_BETA)
        label_beta_L = MathTex(r"\beta", font_size=24, color=CONFIG.C_BETA)
        label_beta_L.move_to(O_L + (R * 0.45) * np.array([np.cos(beta/2), np.sin(beta/2), 0]))
        
        # Draw angle alpha
        radius_alpha_L = Line(O_L, pt_alpha_L, color=CONFIG.C_ALPHA, stroke_width=2.5)
        arc_alpha_L = create_angle_arc(O_L, R, 0, alpha, CONFIG.C_ALPHA)
        label_alpha_L = MathTex(r"\alpha", font_size=24, color=CONFIG.C_ALPHA)
        label_alpha_L.move_to(O_L + (R * 0.65) * np.array([np.cos(alpha/2), np.sin(alpha/2), 0]))
        
        # Dots at endpoints
        dot_alpha_L = Dot(pt_alpha_L, color=CONFIG.C_ALPHA, radius=0.08)
        dot_beta_L = Dot(pt_beta_L, color=CONFIG.C_BETA, radius=0.08)
        
        with self.voiceover(
            text="On the left circle, we draw angle beta in cyan, and angle alpha in red. "
            "Both angles are measured from the positive x-axis in the counterclockwise direction."
        ) as tracker:
            self.play(Create(radius_beta_L), Create(arc_beta_L), Write(label_beta_L), Create(dot_beta_L), run_time=1)
            self.play(Create(radius_alpha_L), Create(arc_alpha_L), Write(label_alpha_L), Create(dot_alpha_L), run_time=tracker.duration - 1)
        
        # ======================================================================
        # ACT 4: Projections on Left Circle - Cosine and Sine
        # ======================================================================
        # Projections for alpha
        proj_cos_alpha_L = Line(O_L, O_L + R * np.array([np.cos(alpha), 0, 0]), color=CONFIG.C_COS, stroke_width=4)
        proj_sin_alpha_L = Line(O_L + R * np.array([np.cos(alpha), 0, 0]), pt_alpha_L, color=CONFIG.C_SIN, stroke_width=4)
        
        lbl_cos_alpha_L = MathTex(r"\cos\alpha", font_size=22, color=CONFIG.C_COS).next_to(proj_cos_alpha_L, DOWN, buff=0.1)
        lbl_sin_alpha_L = MathTex(r"\sin\alpha", font_size=22, color=CONFIG.C_SIN).next_to(proj_sin_alpha_L, LEFT, buff=0.1)
        
        # Projections for beta
        proj_cos_beta_L = Line(O_L, O_L + R * np.array([np.cos(beta), 0, 0]), color=CONFIG.C_COS, stroke_width=4, stroke_opacity=0.7)
        proj_sin_beta_L = Line(O_L + R * np.array([np.cos(beta), 0, 0]), pt_beta_L, color=CONFIG.C_SIN, stroke_width=4, stroke_opacity=0.7)
        
        lbl_cos_beta_L = MathTex(r"\cos\beta", font_size=22, color=CONFIG.C_COS).next_to(proj_cos_beta_L, DOWN, buff=0.1).shift(DOWN*0.15)
        lbl_sin_beta_L = MathTex(r"\sin\beta", font_size=22, color=CONFIG.C_SIN).next_to(proj_sin_beta_L, LEFT, buff=0.1).shift(LEFT*0.15)
        
        with self.voiceover(
            text="Now we project these points onto the axes. For angle alpha, the horizontal projection is cosine alpha in yellow, "
            "and the vertical projection is sine alpha in red. Similarly for beta, though we show these with lower opacity."
        ) as tracker:
            self.play(Create(proj_cos_alpha_L), Write(lbl_cos_alpha_L), Create(proj_sin_alpha_L), Write(lbl_sin_alpha_L), run_time=1.5)
            self.play(Create(proj_cos_beta_L), Write(lbl_cos_beta_L), Create(proj_sin_beta_L), Write(lbl_sin_beta_L), run_time=tracker.duration - 1.5)
        
        # ======================================================================
        # ACT 5: Right Circle - Angle (α - β)
        # ======================================================================
        # Draw angle (α - β) on right circle
        radius_diff_R = Line(O_R, pt_diff_R, color=CONFIG.C_ALPHA_MINUS_BETA, stroke_width=2.5)
        arc_diff_R = create_angle_arc(O_R, R, 0, alpha_minus_beta, CONFIG.C_ALPHA_MINUS_BETA)
        label_diff_R = MathTex(r"\alpha - \beta", font_size=24, color=CONFIG.C_ALPHA_MINUS_BETA)
        label_diff_R.move_to(O_R + (R * 0.55) * np.array([np.cos(alpha_minus_beta/2), np.sin(alpha_minus_beta/2), 0]))
        
        dot_diff_R = Dot(pt_diff_R, color=CONFIG.C_ALPHA_MINUS_BETA, radius=0.08)
        
        # Reference point at angle 0
        dot_zero_R = Dot(pt_zero_R, color=WHITE, radius=0.08)
        radius_zero_R = Line(O_R, pt_zero_R, color=WHITE, stroke_width=2, stroke_opacity=0.5)
        
        with self.voiceover(
            text="Now look at the right circle. Here we draw the angle alpha minus beta in yellow. "
            "This is the difference between our two original angles. We also mark the point at angle zero for reference."
        ) as tracker:
            self.play(Create(radius_diff_R), Create(arc_diff_R), Write(label_diff_R), Create(dot_diff_R), run_time=1)
            self.play(Create(radius_zero_R), Create(dot_zero_R), run_time=tracker.duration - 1)
        
        # ======================================================================
        # ACT 6: Distance Formula - Key Insight
        # ======================================================================
        # Show chord lengths on both circles
        chord_L = Line(pt_alpha_L, pt_beta_L, color=CONFIG.C_RESULT, stroke_width=3, stroke_dashpattern=(5, 3))
        chord_R = Line(pt_diff_R, pt_zero_R, color=CONFIG.C_RESULT, stroke_width=3, stroke_dashpattern=(5, 3))
        
        label_chord_L = MathTex(r"d_1", font_size=24, color=CONFIG.C_RESULT).next_to(chord_L.get_center(), UR, buff=0.1)
        label_chord_R = MathTex(r"d_2", font_size=24, color=CONFIG.C_RESULT).next_to(chord_R.get_center(), UR, buff=0.1)
        
        distance_formula_intro = MathTex(
            r"\text{Key Insight: } d_1 = d_2",
            font_size=32,
            color=CONFIG.C_RESULT
        ).to_edge(UP, buff=0.8)
        
        with self.voiceover(
            text="Here's the key insight: the chord length between the two points on the left circle equals the chord length "
            "on the right circle. Why? Because rotating both points by the same angle preserves distances. "
            "If we rotate the left circle clockwise by beta degrees, alpha becomes alpha minus beta, and beta becomes zero."
        ) as tracker:
            self.play(Create(chord_L), Write(label_chord_L), Create(chord_R), Write(label_chord_R), run_time=1)
            self.play(Write(distance_formula_intro), run_time=tracker.duration - 1)
        
        self.wait(1)
        
        # ======================================================================
        # ACT 7: Algebraic Derivation - Distance on Left Circle
        # ======================================================================
        # Clear previous title and show derivation steps
        self.play(FadeOut(distance_formula_intro), FadeOut(label_chord_L), FadeOut(label_chord_R))
        
        derivation_title = MathTex(
            r"\text{Derivation: Distance Formula}",
            font_size=36,
            color=CONFIG.C_RESULT
        ).to_edge(UP, buff=0.8)
        
        # Coordinates of points
        coords_alpha = MathTex(
            r"P_\alpha = (\cos\alpha, \sin\alpha)",
            font_size=28,
            color=CONFIG.C_ALPHA
        ).shift(UP*2.5 + LEFT*3)
        
        coords_beta = MathTex(
            r"P_\beta = (\cos\beta, \sin\beta)",
            font_size=28,
            color=CONFIG.C_BETA
        ).shift(UP*2.0 + LEFT*3)
        
        # Distance formula for left circle
        dist_L_step1 = MathTex(
            r"d_1^2 = (\cos\alpha - \cos\beta)^2 + (\sin\alpha - \sin\beta)^2",
            font_size=28,
            color=WHITE
        ).shift(UP*1.2 + LEFT*3)
        
        dist_L_step2 = MathTex(
            r"d_1^2 = \cos^2\alpha - 2\cos\alpha\cos\beta + \cos^2\beta",
            font_size=26,
            color=WHITE
        ).shift(UP*0.7 + LEFT*3)
        
        dist_L_step3 = MathTex(
            r"+ \sin^2\alpha - 2\sin\alpha\sin\beta + \sin^2\beta",
            font_size=26,
            color=WHITE
        ).shift(UP*0.3 + LEFT*3)
        
        dist_L_step4 = MathTex(
            r"d_1^2 = (\cos^2\alpha + \sin^2\alpha) + (\cos^2\beta + \sin^2\beta)",
            font_size=26,
            color=WHITE
        ).shift(UP*(-0.2) + LEFT*3)
        
        dist_L_step5 = MathTex(
            r"- 2(\cos\alpha\cos\beta + \sin\alpha\sin\beta)",
            font_size=26,
            color=WHITE
        ).shift(UP*(-0.6) + LEFT*3)
        
        dist_L_final = MathTex(
            r"d_1^2 = 2 - 2(\cos\alpha\cos\beta + \sin\alpha\sin\beta)",
            font_size=28,
            color=CONFIG.C_RESULT
        ).shift(UP*(-1.1) + LEFT*3)
        
        with self.voiceover(
            text="Let's compute the squared distance on the left circle using the distance formula. "
            "The coordinates are cosine alpha comma sine alpha, and cosine beta comma sine beta."
        ) as tracker:
            self.play(Write(derivation_title), Write(coords_alpha), Write(coords_beta), run_time=1)
            self.play(Write(dist_L_step1), run_time=tracker.duration - 1)
        
        with self.voiceover(
            text="Expanding the squares: we get cosine squared alpha minus two cosine alpha cosine beta plus cosine squared beta, "
            "plus sine squared alpha minus two sine alpha sine beta plus sine squared beta."
        ) as tracker:
            self.play(Write(dist_L_step2), Write(dist_L_step3), run_time=tracker.duration)
        
        with self.voiceover(
            text="Grouping terms and using the Pythagorean identity: cosine squared plus sine squared equals one for both angles."
        ) as tracker:
            self.play(Write(dist_L_step4), Write(dist_L_step5), run_time=tracker.duration)
        
        with self.voiceover(
            text="This simplifies to: two minus two times the quantity cosine alpha cosine beta plus sine alpha sine beta."
        ) as tracker:
            self.play(Write(dist_L_final), run_time=tracker.duration)
        
        self.wait(1)
        
        # ======================================================================
        # ACT 8: Algebraic Derivation - Distance on Right Circle
        # ======================================================================
        # Distance formula for right circle
        coords_diff = MathTex(
            r"P_{\alpha-\beta} = (\cos(\alpha-\beta), \sin(\alpha-\beta))",
            font_size=26,
            color=CONFIG.C_ALPHA_MINUS_BETA
        ).shift(UP*2.5 + RIGHT*3)
        
        coords_zero = MathTex(
            r"P_0 = (1, 0)",
            font_size=26,
            color=WHITE
        ).shift(UP*2.0 + RIGHT*3)
        
        dist_R_step1 = MathTex(
            r"d_2^2 = (\cos(\alpha-\beta) - 1)^2 + (\sin(\alpha-\beta) - 0)^2",
            font_size=26,
            color=WHITE
        ).shift(UP*1.3 + RIGHT*3)
        
        dist_R_step2 = MathTex(
            r"d_2^2 = \cos^2(\alpha-\beta) - 2\cos(\alpha-\beta) + 1",
            font_size=26,
            color=WHITE
        ).shift(UP*0.8 + RIGHT*3)
        
        dist_R_step3 = MathTex(
            r"+ \sin^2(\alpha-\beta)",
            font_size=26,
            color=WHITE
        ).shift(UP*0.4 + RIGHT*3)
        
        dist_R_step4 = MathTex(
            r"d_2^2 = [\cos^2(\alpha-\beta) + \sin^2(\alpha-\beta)] + 1",
            font_size=26,
            color=WHITE
        ).shift(UP*(-0.1) + RIGHT*3)
        
        dist_R_step5 = MathTex(
            r"- 2\cos(\alpha-\beta)",
            font_size=26,
            color=WHITE
        ).shift(UP*(-0.5) + RIGHT*3)
        
        dist_R_final = MathTex(
            r"d_2^2 = 2 - 2\cos(\alpha-\beta)",
            font_size=28,
            color=CONFIG.C_RESULT
        ).shift(UP*(-1.0) + RIGHT*3)
        
        with self.voiceover(
            text="Now for the right circle. The point at angle alpha minus beta has coordinates "
            "cosine of alpha minus beta comma sine of alpha minus beta. The reference point is one comma zero."
        ) as tracker:
            self.play(Write(coords_diff), Write(coords_zero), run_time=1)
            self.play(Write(dist_R_step1), run_time=tracker.duration - 1)
        
        with self.voiceover(
            text="Expanding: cosine squared of alpha minus beta minus two cosine of alpha minus beta plus one, "
            "plus sine squared of alpha minus beta."
        ) as tracker:
            self.play(Write(dist_R_step2), Write(dist_R_step3), run_time=tracker.duration)
        
        with self.voiceover(
            text="Using the Pythagorean identity again: this becomes two minus two cosine of alpha minus beta."
        ) as tracker:
            self.play(Write(dist_R_step4), Write(dist_R_step5), Write(dist_R_final), run_time=tracker.duration)
        
        self.wait(1)
        
        # ======================================================================
        # ACT 9: Equating Distances and Final Result
        # ======================================================================
        equation_setup = MathTex(
            r"\text{Since } d_1 = d_2, \text{ we have } d_1^2 = d_2^2",
            font_size=30,
            color=CONFIG.C_RESULT
        ).to_edge(DOWN, buff=1.2)
        
        equation_full = MathTex(
            r"2 - 2(\cos\alpha\cos\beta + \sin\alpha\sin\beta) = 2 - 2\cos(\alpha-\beta)",
            font_size=26,
            color=WHITE
        ).shift(DOWN*1.8)
        
        equation_simplified = MathTex(
            r"\cos\alpha\cos\beta + \sin\alpha\sin\beta = \cos(\alpha-\beta)",
            font_size=32,
            color=CONFIG.C_RESULT
        ).shift(DOWN*2.4)
        
        final_law_box = SurroundingRectangle(equation_simplified, color=CONFIG.C_RESULT, buff=0.15, corner_radius=0.1)
        
        with self.voiceover(
            text="Since the distances are equal, their squares are equal. Setting our two expressions equal to each other..."
        ) as tracker:
            self.play(Write(equation_setup), run_time=tracker.duration)
        
        with self.voiceover(
            text="Two minus two times our expression equals two minus two cosine of alpha minus beta. "
            "Subtracting two from both sides and dividing by negative two..."
        ) as tracker:
            self.play(Write(equation_full), run_time=tracker.duration)
        
        with self.voiceover(
            text="We arrive at the Fundamental Law of Trigonometry: cosine of alpha minus beta equals "
            "cosine alpha cosine beta plus sine alpha sine beta!"
        ) as tracker:
            self.play(Write(equation_simplified), Create(final_law_box), run_time=tracker.duration)
        
        self.wait(2)
        
        # ======================================================================
        # ACT 10: Numerical Verification
        # ======================================================================
        self.play(FadeOut(derivation_title), FadeOut(coords_alpha), FadeOut(coords_beta),
                  FadeOut(dist_L_step1), FadeOut(dist_L_step2), FadeOut(dist_L_step3),
                  FadeOut(dist_L_step4), FadeOut(dist_L_step5), FadeOut(dist_L_final),
                  FadeOut(coords_diff), FadeOut(coords_zero),
                  FadeOut(dist_R_step1), FadeOut(dist_R_step2), FadeOut(dist_R_step3),
                  FadeOut(dist_R_step4), FadeOut(dist_R_step5), FadeOut(dist_R_final),
                  FadeOut(equation_setup), FadeOut(equation_full), FadeOut(equation_simplified),
                  FadeOut(final_law_box))
        
        # Create numerical verification display
        verification_title = MathTex(
            r"\text{Numerical Verification}",
            font_size=36,
            color=CONFIG.C_RESULT
        ).to_edge(UP, buff=0.8)
        
        # Calculate actual values
        alpha_val = CONFIG.alpha_deg
        beta_val = CONFIG.beta_deg
        diff_val = alpha_val - beta_val
        
        lhs_val = np.cos(np.radians(diff_val))
        rhs_val = np.cos(np.radians(alpha_val)) * np.cos(np.radians(beta_val)) + \
                  np.sin(np.radians(alpha_val)) * np.sin(np.radians(beta_val))
        
        numerical_lhs = MathTex(
            rf"\text{{LHS: }} \cos({alpha_val}^\circ - {beta_val}^\circ) = \cos({diff_val}^\circ) = {lhs_val:.6f}",
            font_size=28,
            color=CONFIG.C_ALPHA
        ).shift(UP*1.5)
        
        numerical_rhs = MathTex(
            rf"\text{{RHS: }} \cos({alpha_val}^\circ)\cos({beta_val}^\circ) + \sin({alpha_val}^\circ)\sin({beta_val}^\circ)",
            font_size=24,
            color=CONFIG.C_BETA
        ).shift(UP*0.8)
        
        numerical_rhs_result = MathTex(
            rf"= {np.cos(np.radians(alpha_val)):.6f} \cdot {np.cos(np.radians(beta_val)):.6f} + {np.sin(np.radians(alpha_val)):.6f} \cdot {np.sin(np.radians(beta_val)):.6f}",
            font_size=24,
            color=CONFIG.C_BETA
        ).shift(UP*0.3)
        
        numerical_rhs_final = MathTex(
            rf"= {rhs_val:.6f}",
            font_size=28,
            color=CONFIG.C_RESULT
        ).shift(UP*(-0.3))
        
        match_statement = MathTex(
            r"\therefore \text{LHS} = \text{RHS} \quad \checkmark",
            font_size=36,
            color=CONFIG.C_RESULT
        ).shift(UP*(-1.0))
        
        match_box = SurroundingRectangle(match_statement, color=CONFIG.C_RESULT, buff=0.15, corner_radius=0.1)
        
        with self.voiceover(
            text="Let's verify this numerically with our chosen angles: alpha equals fifty degrees, beta equals twenty degrees."
        ) as tracker:
            self.play(Write(verification_title), run_time=1)
            self.play(Write(numerical_lhs), run_time=tracker.duration - 1)
        
        with self.voiceover(
            text="The left hand side: cosine of thirty degrees equals point nine three nine six nine three."
        ) as tracker:
            self.wait(0.5)
        
        with self.voiceover(
            text="The right hand side: cosine of fifty degrees times cosine of twenty degrees, "
            "plus sine of fifty degrees times sine of twenty degrees."
        ) as tracker:
            self.play(Write(numerical_rhs), Write(numerical_rhs_result), run_time=tracker.duration)
        
        with self.voiceover(
            text="This also equals point nine three nine six nine three. LHS equals RHS. The identity is verified!"
        ) as tracker:
            self.play(Write(numerical_rhs_final), Write(match_statement), Create(match_box), run_time=tracker.duration)
        
        self.wait(2)
        
        # ======================================================================
        # ACT 11: Transition to Deductions Preview
        # ======================================================================
        deductions_preview = Text(
            "Next: 10 Powerful Deductions from this Law!",
            font_size=32,
            color="#00FF00"
        ).to_edge(DOWN, buff=0.8)
        
        with self.voiceover(
            text="From this single fundamental law, we can derive ten powerful identities including sum and difference formulas "
            "for sine, cosine, and tangent, as well as cofunction identities. Continue to the next video to see all deductions!"
        ) as tracker:
            self.play(Write(deductions_preview), run_time=tracker.duration)
        
        self.wait(3)
        
        # Fade out everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)

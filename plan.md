# The Fundamental Law of Trigonometry & Its Deductions

## Overview
- **Topic**: The Fundamental Law of Trigonometry and its core deductions (co-function and shift identities).
- **Hook**: Why does subtracting angles in a cosine function magically turn into a multiplication of their individual sines and cosines? 
- **Target Audience**: High school mathematics students (knows basic unit circle, sine, cosine, and right-triangle trigonometry).
- **Estimated Length**: 12-15 minutes.
- **Key Insight**: The Fundamental Law isn't just an algebraic formula; it is the geometric manifestation of rotating vectors and projecting them onto axes. The deductions are simply specific 90-degree rotations of this general principle.

## Narrative Arc
We begin by questioning the algebraic expansion of $\cos(\alpha - \beta)$, grounding it in the geometric reality of the unit circle and vector projections. Once the general law is established visually, we treat the deductions not as arbitrary algebra tricks, but as specific 90-degree rotations. We prove them algebraically to satisfy the syllabus, but constantly refer back to the geometric reality to maintain intuition.

---

## Scene 1: The Mystery of the Difference
**Duration**: ~60 seconds
**Purpose**: Hook the viewer and state the Fundamental Law.

### Visual Elements
- A clean, dark 3b1b-style background (`#1C1C1C`).
- The Fundamental Law equation written elegantly in the center.
- Two angle arcs, $\alpha$ and $\beta$, on a unit circle.

### Content
Introduce the equation $\cos(\alpha - \beta) = \cos\alpha \cos\beta + \sin\alpha \sin\beta$. Point out the disconnect: the left side is a single trigonometric function of a difference, while the right side is a sum of products. Ask why this relationship exists.

### Narration Notes
**gTTS Text**: "Let alpha and beta be any two angles. The Fundamental Law of Trigonometry states that the cosine of their difference equals cosine alpha times cosine beta, plus sine alpha times sine beta. But look closely at this equation. On the left, we have a single function of a combined angle. On the right, we have a sum of products. Why does subtracting angles magically translate into multiplying their components?"

### Technical Notes
- Use `MathTex` for the equation.
- Use `Write` and `Indicate` to highlight the left vs. right sides.
- Keep the unit circle in the background, slightly dimmed, to establish context.

---

## Scene 2: The Geometric Proof (The "Why")
**Duration**: ~180 seconds
**Purpose**: Provide the geometric intuition for the Fundamental Law before doing the algebra.

### Visual Elements
- Unit circle centered at origin.
- Vector 1 at angle $\beta$ (Blue).
- Vector 2 at angle $\alpha$ (Yellow).
- The angle between them is $\alpha - \beta$ (Green).
- Projections of Vector 2 onto Vector 1, and onto the axes.

### Content
Instead of the standard textbook coordinate geometry proof (which is algebraically heavy), use the dot product / projection intuition. Show that the length of the projection of Vector 2 onto Vector 1 is $\cos(\alpha - \beta)$. Then, decompose Vector 2 into its x and y components ($\cos\alpha, \sin\alpha$) and project *those* onto Vector 1. Show that the sum of these projections equals $\cos\alpha \cos\beta + \sin\alpha \sin\beta$.

### Narration Notes
**gTTS Text**: "Before we prove this algebraically, let us see it geometrically. Imagine two vectors on the unit circle, one at angle beta, and one at angle alpha. The angle between them is alpha minus beta. The cosine of this difference is simply the projection of the alpha vector onto the beta vector. Now, let us break the alpha vector into its horizontal and vertical components. If we project the horizontal component onto the beta vector, we get cosine alpha times cosine beta. If we project the vertical component, we get sine alpha times sine beta. Add them together, and the geometry perfectly matches the algebra."

### Technical Notes
- Use `Vector` and `Line` for projections.
- Use `DashedLine` for the perpendicular drops.
- Use `TransformMatchingShapes` to show the components adding up.
- *Crucial*: Use `always_redraw` for the projection lines if animating the angles changing, but for the proof, static, well-timed `Create` animations are cleaner.

---

## Scene 3: Deduction 1 - The Complementary Angle
**Duration**: ~120 seconds
**Purpose**: Prove $\cos(\pi/2 - \beta) = \sin\beta$ algebraically and geometrically.

### Visual Elements
- The Fundamental Law equation at the top.
- A substitution animation: $\alpha$ morphs into $\pi/2$.
- Unit circle showing angle $\beta$ and its complement $\pi/2 - \beta$.

### Content
1. **Algebraic**: Substitute $\alpha = \pi/2$ into the Fundamental Law. Show $\cos(\pi/2) = 0$ and $\sin(\pi/2) = 1$. The equation collapses to $\cos(\pi/2 - \beta) = \sin\beta$.
2. **Geometric**: Show on the unit circle that the angle $\pi/2 - \beta$ is the complement. The x-coordinate (cosine) of the complement is exactly the y-coordinate (sine) of the original angle $\beta$.

### Narration Notes
**gTTS Text**: "Now we apply this master key to unlock specific deductions. First, let alpha be exactly 90 degrees, or pi over 2. We substitute this into our Fundamental Law. Cosine of pi over 2 is zero, and sine of pi over 2 is one. The equation beautifully collapses, leaving us with cosine of pi over 2 minus beta equals sine of beta. Geometrically, this makes perfect sense. The horizontal distance of the complementary angle is exactly the vertical distance of the original angle."

### Technical Notes
- Use `TransformMatchingTex` to animate the substitution. Highlight the $\pi/2$ in yellow as it moves into the equation.
- Use `MathTex` for the step-by-step algebraic simplification.
- For the geometric part, use a `ValueTracker` to animate $\beta$ changing, showing that the x-projection of $(\pi/2 - \beta)$ always perfectly matches the y-projection of $\beta$.

---

## Scene 4: Deduction 2 - The 90-Degree Shift
**Duration**: ~120 seconds
**Purpose**: Prove $\cos(\pi/2 + \alpha) = -\sin\alpha$.

### Visual Elements
- Unit circle.
- Vector at angle $\alpha$ in Q1.
- Vector rotated by $+\pi/2$ into Q2.
- Algebraic substitution: $\beta = -\pi/2$.

### Content
1. **Geometric**: Rotate the vector $\alpha$ by 90 degrees counterclockwise. It enters the second quadrant. Its x-coordinate (cosine) becomes negative, and its magnitude matches the y-coordinate (sine) of the original angle. Hence, $-\sin\alpha$.
2. **Algebraic**: Substitute $\beta = -\pi/2$ into the Fundamental Law. Show the sign changes due to odd/even properties of sine and cosine.

### Narration Notes
**gTTS Text**: "Next, let us shift our angle by 90 degrees. What is the cosine of alpha plus pi over 2? Geometrically, if we rotate our vector by 90 degrees into the second quadrant, its horizontal projection becomes negative, matching the negative of its original vertical projection. Algebraically, we substitute beta as negative pi over 2 into the Fundamental Law. Remembering that sine is an odd function and cosine is even, the terms simplify precisely to negative sine alpha."

### Technical Notes
- Use `Rotate` animation for the vector.
- Highlight the negative sign in red during the algebraic simplification to emphasize the sign change.
- Use `Brace` or `Arrow` to point out the negative x-coordinate in Q2.

---

## Scene 5: Deduction 3 - Completing the Set
**Duration**: ~90 seconds
**Purpose**: Prove $\sin(\pi/2 + \alpha) = \cos\alpha$ (resolving the cut-off text from the prompt).

### Visual Elements
- The result from Deduction 1: $\cos(\pi/2 - \beta) = \sin\beta$.
- Substitution animation: $\beta = \pi/2 + \alpha$.
- Unit circle showing the y-coordinate (sine) of the shifted angle matching the x-coordinate (cosine) of the original.

### Content
Take the result from Deduction 1. Substitute $\beta = \pi/2 + \alpha$. 
$\cos(\pi/2 - (\pi/2 + \alpha)) = \sin(\pi/2 + \alpha)$
$\cos(-\alpha) = \sin(\pi/2 + \alpha)$
Since $\cos(-\alpha) = \cos\alpha$, we get $\sin(\pi/2 + \alpha) = \cos\alpha$.
Briefly show the geometric intuition: the y-coordinate of the 90-degree shifted vector is the x-coordinate of the original.

### Narration Notes
**gTTS Text**: "Finally, we complete the set. Using our first deduction, we substitute beta with alpha plus pi over 2. The pi over 2 terms cancel out inside the cosine, leaving us with cosine of negative alpha. Since cosine is an even function, this is just cosine alpha. Thus, the sine of alpha plus pi over 2 equals cosine alpha. Once again, the algebra perfectly mirrors the geometry: the vertical height of the shifted vector is the horizontal width of the original."

### Technical Notes
- Use `TransformMatchingTex` for the cancellation of $\pi/2$.
- Use `Circumscribe` around the final result: `\sin(\pi/2 + \alpha) = \cos\alpha`.

---

## Scene 6: Synthesis and The Big Picture
**Duration**: ~60 seconds
**Purpose**: Summarize and connect back to the core insight.

### Visual Elements
- All four equations displayed side-by-side or in a grid.
- The unit circle with all the vectors and projections fading in together.

### Content
Review the Fundamental Law and the three deductions. Emphasize that these are not random formulas to memorize, but consequences of a single geometric truth: rotation and projection on the unit circle.

### Narration Notes
**gTTS Text**: "We began with a mysterious algebraic expansion, and we grounded it in the geometry of the unit circle. From that single Fundamental Law, we derived the core shift identities. Do not just memorize these substitutions. Visualize the rotations. See the projections. When you understand the geometry, the algebra writes itself."

### Technical Notes
- Use `FadeIn` for the summary grid.
- End with a slow zoom out or a clean fade to black.

---

## Transitions & Flow
- **Algebra to Geometry**: Every time an algebraic substitution is made, immediately cut to or fade in the geometric unit circle to verify the result visually. This creates a rhythmic "claim and proof" flow.
- **Color Continuity**: 
  - $\alpha$ is always Yellow.
  - $\beta$ is always Blue.
  - $\pi/2$ shifts are always highlighted in Green.
  - Negative signs/results are always Red.

## Color Palette
- Primary (Background): `#1C1C1C` (Dark Grey)
- Angle $\alpha$: `#FFFF00` (Yellow)
- Angle $\beta$: `#58C4DD` (Blue)
- Projections/Cosine: `#83C167` (Green)
- Sine/Vertical: `#FF6666` (Red)
- $\pi/2$ Substitutions: `#FFD700` (Gold)

## Mathematical Content
- $\cos(\alpha - \beta) = \cos\alpha \cos\beta + \sin\alpha \sin\beta$
- $\cos(\pi/2 - \beta) = \sin\beta$
- $\cos(\pi/2 + \alpha) = -\sin\alpha$
- $\sin(\pi/2 + \alpha) = \cos\alpha$
- Even/Odd properties: $\cos(-\alpha) = \cos\alpha$, $\sin(-\alpha) = -\sin\alpha$.

## Implementation Order
1. **Scene 1 & 2**: Build the unit circle, vector logic, and the geometric proof of the Fundamental Law. This is the hardest part to animate smoothly.
2. **Scene 3**: Implement the `TransformMatchingTex` logic for algebraic substitution. Once the template for substitution is built here, reuse it for Scenes 4 and 5.
3. **Scene 4 & 5**: Reuse the substitution template and geometric rotation logic.
4. **Scene 6**: Assemble the final summary.

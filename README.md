# Trigonometry Masterclass with Manim 📐 ⭕

[![Manim](https://img.shields.io/badge/Made_with-Manim-E24268.svg)](https://www.manim.community/)
[![Python](https://img.shields.io/badge/Python-3.11.6-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A complete, 11-part animated video series designed to teach trigonometry from the ground up. Instead of relying on rote memorization, this masterclass uses the power of **Manim (Mathematical Animation Engine)** to bridge the gap between geometric intuition and algebraic rigor. 

Every derivation features a **Split-Screen Design**: physical geometry and waveforms are dynamically animated on the left side, while the step-by-step algebraic proofs are derived on a blackboard on the right.

## ✨ Features
* **100% Programmatic Animation:** Generated entirely in Python using Manim Community.
* **Automated Voiceover:** Integrated with `manim-voiceover` and `gTTS` to provide professional, timed narration synced perfectly to the math.
* **Dynamic Geometry:** Uses `ValueTracker` and continuous updates to show *why* functions behave the way they do (e.g., angle wrapping, triangle scaling, wave interference).
* **Comprehensive Syllabus:** Covers foundational basics, historical functions (versine/exsecant), identity derivations, and textbook problem-solving.

---

## 📚 The Syllabus (File Overview)

To render any of these lessons, run the corresponding command in your terminal.

| Part | File Name | Class Name | Topic Covered | Run Command |
| :--- | :--- | :--- | :--- | :--- |
| **1** | `trig_masterclass_part1.py` | `TrigMasterclassPart1` | The Unit Circle, Sine, Cosine, Tangent, and Cotangent geometry. | `manim -pql trig_masterclass_part1.py TrigMasterclassPart1` |
| **2** | `trig_masterclass_part2.py` | `TrigMasterclassPart2` | Advanced & Historical Functions (Sec, Csc, Versin, Coversin, Exsec). | `manim -pql trig_masterclass_part2.py TrigMasterclassPart2` |
| **3** | `trig_masterclass_part3.py` | `TrigIdentitiesMasterclass` | Pythagorean Identities (Visualizing triangle scaling). | `manim -pql trig_masterclass_part3.py TrigIdentitiesMasterclass` |
| **4** | `trig_masterclass_part4.py` | `FundamentalIdentities` | Sum and Double Angle formulas derived from the Fundamental Law. | `manim -pql trig_masterclass_part4.py FundamentalIdentities` |
| **5** | `trig_masterclass_part5.py` | `HalfAngleIdentities` | The 3 forms of $\cos(2\alpha)$ and isolating the Half-Angle identities. | `manim -pql trig_masterclass_part5.py HalfAngleIdentities` |
| **6** | `trig_masterclass_part6.py` | `TripleAngleIdentities` | Complex algebraic expansion of $\sin(3\alpha)$ and $\cos(3\alpha)$. | `manim -pql trig_masterclass_part6.py TripleAngleIdentities` |
| **7** | `trig_masterclass_part7.py` | `ProductToSumIdentities` | Combining waves, AM Radio envelopes, and algebraic elimination. | `manim -pql trig_masterclass_part7.py ProductToSumIdentities` |
| **8** | `trig_masterclass_part8.py` | `AlliedAnglesProofs` | The CAST Rule, $90^\circ/180^\circ$ shifts, and Triangle interior angle proofs. | `manim -pql trig_masterclass_part8.py AlliedAnglesProofs` |
| **9** | `trig_masterclass_part9.py` | `ExactValueProofs` | Calculating angles $> 360^\circ$ (angle wrapping) and Exact Reference Values. | `manim -pql trig_masterclass_part9.py ExactValueProofs` |
| **10** | `trig_masterclass_part10.py`| `TriangleIdentities` | Beautiful Triangle Identities ($\sum \tan = \prod \tan$) and Incenters. | `manim -pql trig_masterclass_part10.py TriangleIdentities` |
| **11** | `trig_masterclass_part11.py`| `HarmonicAddition` | Combining $a\sin\theta + b\cos\theta$ into $r\sin(\theta+\phi)$ using a "Phantom Triangle". | `manim -pql trig_masterclass_part11.py HarmonicAddition` |

---

## ⚙️ Installation & Setup

### 1. Prerequisites
You will need **Python 3.8+**, **FFmpeg** (for rendering video), and a **LaTeX distribution** (for rendering `MathTex` equations). 
* Follow the [Official Manim Installation Guide](https://docs.manim.community/en/stable/installation.html) for your specific operating system (Windows / Mac / Linux).

### 2. Install Python Dependencies
Clone this repository and install the required packages:

```bash
git clone https://github.com/YOUR-USERNAME/trigonometry-masterclass-manim.git
cd trigonometry-masterclass-manim
pip install manim
pip install "manim-voiceover[gtts]"
pip install numpy

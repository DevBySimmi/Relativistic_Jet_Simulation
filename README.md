# 🚀 Relativistic Jet Simulation

An interactive astrophysics simulation written in Python that demonstrates the effects of relativistic motion in astrophysical jets.

The project visualizes how the Doppler factor, jet intensity, and apparent velocity change with observation angle while the Lorentz factor evolves dynamically through animation.

---

## 🌌 Features

- Real-time Lorentz factor (γ) animation
- Doppler Factor vs Angle visualization
- Jet Intensity vs Angle visualization
- Apparent Velocity vs Angle visualization
- Automatic peak intensity detection
- Dark-space scientific theme
- Educational and research-oriented visualization

---

## 📊 Physics Concepts

This simulation explores several important concepts in relativistic astrophysics:

### Lorentz Factor

γ = 1 / √(1 - β²)

where:

- γ = Lorentz factor
- β = v/c
- v = object velocity
- c = speed of light

### Doppler Factor

D = γ(1 − cos θ)

### Jet Intensity

I = (γ² sin² θ) / [1 + γ²(1 − cos θ)²]

### Apparent Velocity

v_app = (β sin θ) / (1 − β cos θ)

---

## 🛠 Requirements

Install the required libraries:

```bash
pip install numpy matplotlib

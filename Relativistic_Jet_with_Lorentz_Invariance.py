import numpy as np
import matplotlib.pyplot as plt

# Parameters
gamma = 10  # Lorentz factor
beta = np.sqrt(1 - 1/gamma**2)

theta = np.linspace(0.001, np.pi/2, 500)

# Doppler Factor
def doppler_factor(gamma, theta):
    return gamma * (1 - np.cos(theta))

# Jet Intensity
def jet_intensity(gamma, theta):
    return (gamma**2 * np.sin(theta)**2) / (
        1 + gamma**2 * (1 - np.cos(theta))**2
    )

# Apparent Velocity
def apparent_velocity(beta, theta):
    return (beta * np.sin(theta)) / (
        1 - beta * np.cos(theta)
    )

# Calculations
doppler = doppler_factor(gamma, theta)
intensity = jet_intensity(gamma, theta)
v_app = apparent_velocity(beta, theta)

# Peak intensity
peak_idx = np.argmax(intensity)
peak_theta = theta[peak_idx]
peak_intensity = intensity[peak_idx]

# Plotting
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# -------------------------
# Doppler Factor
# -------------------------
axes[0].plot(theta, doppler,
             color='blue',
             linewidth=2)

axes[0].set_title('Doppler Factor vs Angle')
axes[0].set_xlabel('Angle (radians)')
axes[0].set_ylabel('Doppler Factor')
axes[0].grid(True)

axes[0].text(
    0.05, 0.90,
    f'γ = {gamma}',
    transform=axes[0].transAxes,
    bbox=dict(facecolor='white', alpha=0.8)
)

# -------------------------
# Jet Intensity
# -------------------------
axes[1].plot(theta, intensity,
             color='red',
             linewidth=2)

axes[1].scatter(
    peak_theta,
    peak_intensity,
    s=80,
    label='Peak'
)

axes[1].annotate(
    'Peak Intensity',
    (peak_theta, peak_intensity),
    xytext=(peak_theta+0.15,
            peak_intensity-1),
    arrowprops=dict(arrowstyle='->')
)

axes[1].axvspan(
    peak_theta-0.1,
    peak_theta+0.1,
    alpha=0.2,
    label='Strong Beaming'
)

axes[1].set_title('Jet Intensity vs Angle')
axes[1].set_xlabel('Angle (radians)')
axes[1].set_ylabel('Jet Intensity')
axes[1].grid(True)
axes[1].legend()

# -------------------------
# Apparent Velocity
# -------------------------
axes[2].plot(theta,
             v_app,
             color='green',
             linewidth=2)

axes[2].set_title('Apparent Velocity vs Angle')
axes[2].set_xlabel('Angle (radians)')
axes[2].set_ylabel('v_app / c')
axes[2].grid(True)

# Main Title
fig.suptitle(
    'Relativistic Jet Simulation',
    fontsize=16,
    fontweight='bold'
)

plt.tight_layout()
plt.show()
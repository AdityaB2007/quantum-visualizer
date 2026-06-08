import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from src.gaussian_wavepackets import gaussian_wavepacket

x0, spread = 0, 1
x = np.linspace(-10, 10, 1000)

fig, ax = plt.subplots()
real_line, = ax.plot([], [], label="Re(ψ)")
imag_line, = ax.plot([], [], label="Im(ψ)")

ax.set_xlim(-10, 10)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel("Position x")
ax.set_ylabel("Wavefunction")
ax.set_title("Changing Wave Number k")
ax.grid(True)
ax.legend()

def update(frame):
    k = frame
    psi = gaussian_wavepacket(x, x0, spread, k)
    real_line.set_data(x, np.real(psi))
    imag_line.set_data(x, np.imag(psi))
    ax.set_title(f"Gaussian Wavepacket (k = {k:.2f})")
    return real_line, imag_line

k_values = np.linspace(0, 20, 100)

animation = FuncAnimation(
    fig,
    update,
    frames=k_values,
    interval=50,
    blit=True
)

animation.save("figures/wavepacket_wavenumber.gif", writer="pillow", fps=20)
plt.show()
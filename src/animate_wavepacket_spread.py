import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from src.gaussian_wavepackets import gaussian_wavepacket
from src.utils import probability_density

x0, k = 0, 5
x = np.linspace(-10, 10, 1000)

fig, ax = plt.subplots()
line, = ax.plot([], [], label="Probability density")

ax.set_xlim(-10, 10)
ax.set_ylim(0, 1.2)
ax.set_xlabel("Position x")
ax.set_ylabel("Probability density")
ax.set_title("Changing Gaussian Wavepacket Spread")
ax.grid(True)
ax.legend()

def update(frame):
    spread = frame
    psi = gaussian_wavepacket(x, x0, spread, k)
    prob = probability_density(psi)
    line.set_data(x, prob)
    ax.set_title(f"Gaussian Wavepacket Spread = {spread:.2f}")
    return line,


spreads = np.linspace(0.2, 2.0, 100)

animation = FuncAnimation(
    fig,
    update,
    frames=spreads,
    interval=50,
    blit=True
)

animation.save("figures/wavepacket_spread.gif", writer="pillow", fps=20)
plt.show()
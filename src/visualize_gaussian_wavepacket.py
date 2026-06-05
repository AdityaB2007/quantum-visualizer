import numpy as np
import matplotlib.pyplot as plt

from src.gaussian_wavepackets import gaussian_wavepacket

x0 = float(input("Give the center of the distribution: "))
spread = float(input("Give the standard deviation of the distribution: "))
x = np.linspace(x0 - 5 * spread, x0 + 5 * spread, 1000)

psi = gaussian_wavepacket(x, x0, spread)

plt.plot(x, psi, label="Wavepacket")
plt.xlabel("Position")
plt.ylabel("Wavepacket")
plt.title(f"Gaussian Wavepacket (center={x0}, spread={spread})")
plt.grid(True)
plt.legend()
plt.show()
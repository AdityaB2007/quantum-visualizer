import numpy as np
import matplotlib.pyplot as plt

from src.gaussian_wavepackets import gaussian_wavepacket
from src.expectation_values import uncertainty_x, uncertainty_p

x0, k, hbar = 0, 5, 1

spreads = np.linspace(0.2, 3.0, 100)
products = []

for spread in spreads:
    x = np.linspace(x0 - 5 * spread, x0 + 5 * spread, 2000)
    psi = gaussian_wavepacket(x, x0, spread, k)
    delta_x = uncertainty_x(x, psi)
    delta_p = uncertainty_p(x, psi, hbar)
    products.append(delta_x * delta_p)

products = np.array(products)

plt.plot(spreads, products, label="ΔxΔp")
plt.axhline(hbar / 2, linestyle="--", label="ℏ/2")
plt.xlabel("Gaussian spread")
plt.ylabel("Uncertainty product")
plt.title("Heisenberg Uncertainty Product vs Gaussian Spread")
plt.grid(True)
plt.legend()
plt.show()
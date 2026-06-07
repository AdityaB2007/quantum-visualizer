import numpy as np
import matplotlib.pyplot as plt

from src.gaussian_wavepackets import gaussian_wavepacket
from src.expectation_values import expectation_x, uncertainty_x

x0 = float(input("Give the center of the distribution: "))
spread = float(input("Give the standard deviation of the distribution: "))
k = float(input("Give the wave number: "))
x = np.linspace(x0 - 5 * spread, x0 + 5 * spread, 1000)

psi = gaussian_wavepacket(x, x0, spread, k)
prob = np.abs(psi) ** 2

mean_x = expectation_x(x, psi)
std_dev = uncertainty_x(x, psi)

plt.plot(x, prob, label="probability density")
plt.axvline(mean_x, label="<x>")
plt.axvline(mean_x - std_dev, label="<x> - Δx")
plt.axvline(mean_x + std_dev, label="<x> + Δx")
plt.xlabel("position x")
plt.ylabel("probability density")
plt.title("Position Expectation Value and Uncertainty")
plt.grid(True)
plt.legend()
plt.show()
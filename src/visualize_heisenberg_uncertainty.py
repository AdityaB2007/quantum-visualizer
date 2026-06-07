import numpy as np
import matplotlib.pyplot as plt

from src.utils import probability_density
from src.gaussian_wavepackets import gaussian_wavepacket
from src.expectation_values import uncertainty_x, uncertainty_p

x0, hbar = 0, 1
spread = float(input("Give the standard deviation of the distribution: "))
k = float(input("Give the wave number: "))
x = np.linspace(x0 - 5 * spread, x0 + 5 * spread, 1000)
psi = gaussian_wavepacket(x, x0, spread, k)

delta_x = uncertainty_x(x, psi)
delta_p = uncertainty_p(x, psi, hbar)
product = delta_x * delta_p

print(f"Δx = {delta_x:.6f}")
print(f"Δp = {delta_p:.6f}")
print(f"ΔxΔp = {product:.6f}")
print(f"ℏ/2 = {hbar / 2:.6f}")

plt.plot(x, probability_density(psi), label="Probability density")
plt.title(f"Δx={delta_x:.3f}, Δp={delta_p:.3f}, ΔxΔp={product:.3f}")
plt.xlabel("position x")
plt.ylabel("probability density")
plt.title(f"Δx={delta_x:.3f}, Δp={delta_p:.3f}, ΔxΔp={product:.3f}")
plt.grid(True)
plt.legend()
plt.show()
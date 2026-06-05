import numpy as np
import matplotlib.pyplot as plt

from src.gaussian_wavepackets import gaussian_wavepacket

x0 = float(input("Give the center of the distribution: "))
spread = float(input("Give the standard deviation of the distribution: "))
k = float(input("Give the wave number: "))
x = np.linspace(x0 - 5 * spread, x0 + 5 * spread, 1000)

psi = gaussian_wavepacket(x, x0, spread, k)

"""
The below code plots the real component of psi as
a function of position x
"""
plt.plot(x, np.real(psi), label="real component")

"""
The below code plots the imaginary component of
psi as a function of position x
"""
plt.plot(x, np.imag(psi), label="imaginary component")

"""
The below code plots the probability density
of the wave as a function of position x
"""
plt.plot(x, np.abs(psi) ** 2, label="probability density")

# plot properties
plt.title("Various Visualization Metrics of Complex-Valued Gaussian Wavepackets")
plt.xlabel("Position (x)")
plt.ylabel("Wavefunction OR Probability Density")
plt.grid(True)
plt.legend()
plt.show()
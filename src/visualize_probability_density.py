import numpy as np
import matplotlib.pyplot as plt
from particle_in_box import particle_in_box_wavefunction

L = float(input("Enter box length L: "))
n = int(input("Enter quantum number n: "))
x = np.linspace(0, L, 1000)
psi_n = particle_in_box_wavefunction(x, n, L)
prob = abs(psi_n) ** 2

plt.plot(x, prob, label=f"n = {n}")
plt.xlabel("Position x")
plt.ylabel("|ψₙ(x)|²")
plt.title(f"Particle in a Box Probability Density (n = {n})")
plt.grid(True)
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from particle_in_box import particle_in_box_wavefunction

L = 1
n = 1
x = np.linspace(0, L, 1000)
psi_n = particle_in_box_wavefunction(x, n, L)
prob = abs(psi_n) ** 2

plt.plot(x, prob, label=f"n = {n}")
plt.xlabel("Position x")
plt.ylabel("Probability density function")
plt.title(f"probability density for n={n}")
plt.grid(True)
plt.legend()
plt.show()
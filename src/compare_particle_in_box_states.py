import numpy as np
import matplotlib.pyplot as plt
from particle_in_box import particle_in_box_wavefunction

L = float(input("Enter box length L: "))
n_max = int(input("Enter maximum quantum number: "))
x = np.linspace(0, L, 1000)

for n in range(1, n_max + 1):
    psi_n = particle_in_box_wavefunction(x, n, L)
    plt.plot(x, psi_n, label=f"n = {n}")

plt.xlabel("Position x")
plt.ylabel("ψₙ(x)")
plt.title(f"Particle in a Box Wavefunction (n = 1 to {n_max})")
plt.grid(True)
plt.legend()
plt.show()
import numpy as np

# tests normalize_wavefunction
from src.utils import normalize_wavefunction
x = np.linspace(-5,5,1000)
psi = np.exp(-1 * x**2)
psi_norm = normalize_wavefunction(x, psi)

result = np.trapezoid(np.abs(psi_norm)**2, x)
tolerance = 1E-10

assert abs(result - 1.0) < tolerance
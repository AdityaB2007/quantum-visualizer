import numpy as np

from src.utils import normalize_wavefunction

def test_normalize_wavefunction():
    x = np.linspace(-5, 5, 1000)
    psi = np.exp(-x**2)

    psi_norm = normalize_wavefunction(x, psi)
    result = np.trapezoid(np.abs(psi_norm) ** 2, x)

    assert abs(result - 1.0) < 1e-8
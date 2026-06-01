import numpy as np

from src.utils import normalize_wavefunction
from src.particle_in_box import particle_in_box_wavefunction


def test_normalize_wavefunction():
    x = np.linspace(-5, 5, 1000)
    psi = np.exp(-x**2)

    psi_norm = normalize_wavefunction(x, psi)
    result = np.trapezoid(np.abs(psi_norm) ** 2, x)

    assert abs(result - 1.0) < 1e-8


def test_particle_in_box_wavefunction_is_normalized():
    L = 1
    n = 1
    x = np.linspace(0, L, 1000)

    psi = particle_in_box_wavefunction(x, n, L)
    result = np.trapezoid(np.abs(psi) ** 2, x)

    assert abs(result - 1.0) < 1e-8
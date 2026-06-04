import numpy as np

from src.particle_in_box import particle_in_box_wavefunction
from src.expectation_values import expectation_x

def test_expectation_x():
    L = 1
    n = 1
    x = np.linspace(0, L, 1000)

    psi = particle_in_box_wavefunction(x, n, L)
    result = np.abs(expectation_x(x, psi) - L / 2)
    assert result < 1e-8
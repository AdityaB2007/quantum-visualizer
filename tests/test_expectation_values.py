import numpy as np

from src.particle_in_box import particle_in_box_wavefunction
from src.gaussian_wavepackets import gaussian_wavepacket
from src.expectation_values import expectation_x, expectation_x_squared, variance_x, uncertainty_x, expectation_p

def test_expectation_x():
    L = 1
    n = 1
    x = np.linspace(0, L, 1000)

    psi = particle_in_box_wavefunction(x, n, L)
    result = np.abs(expectation_x(x, psi) - L / 2)
    assert result < 1e-8

def test_variance_x():
    L = 1
    n = 1
    x = np.linspace(0, L, 1000)

    psi = particle_in_box_wavefunction(x, n, L)

    mean_x = expectation_x(x, psi)
    mean_x2 = expectation_x_squared(x, psi)
    var = variance_x(x, psi)

    assert mean_x2 > mean_x ** 2
    assert var > 0
    assert abs(var - (mean_x2 - mean_x ** 2)) < 1e-8

def test_uncertainty_x():
    L = 1
    n = 1
    x = np.linspace(0, L, 1000)

    psi = particle_in_box_wavefunction(x, n, L)

    var = variance_x(x, psi)
    std_dev = uncertainty_x(x, psi)
    
    assert std_dev > 0
    assert np.abs(std_dev ** 2 - var) < 1e-8

def test_expectation_p():
    x0 = 0
    spread = 1
    k = 5
    hbar = 1
    x = np.linspace(x0 - 5 * spread, x0 + 5 * spread, 1000)
    psi = gaussian_wavepacket(x, x0, spread, k)
    result = expectation_p(x, psi)
    assert abs(result - hbar * k) < 1e-2
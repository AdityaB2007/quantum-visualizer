import numpy as np

from src.gaussian_wavepackets import gaussian_wavepacket
from src.expectation_values import expectation_p, expectation_p_squared, variance_p, uncertainty_p, uncertainty_product, uncertainty_x


def test_expectation_p_for_complex_gaussian():
    x0, spread, k, hbar = 0, 1, 5, 1
    x = np.linspace(x0 - 5 * spread, x0 + 5 * spread, 1000)
    psi = gaussian_wavepacket(x, x0, spread, k)
    mean_p = expectation_p(x, psi, hbar)
    assert abs(mean_p - hbar * k) < 1e-2


def test_momentum_variance_and_uncertainty():
    x0, spread, k, hbar = 0, 1, 5, 1
    x = np.linspace(x0 - 5 * spread, x0 + 5 * spread, 1000)
    psi = gaussian_wavepacket(x, x0, spread, k)
    mean_p = expectation_p(x, psi, hbar)
    mean_p2 = expectation_p_squared(x, psi, hbar)
    var_p = variance_p(x, psi, hbar)
    uncertainty = uncertainty_p(x, psi, hbar)
    assert mean_p2 > mean_p ** 2
    assert var_p > 0
    assert uncertainty > 0
    assert abs(uncertainty ** 2 - var_p) < 1e-6

def test_uncertainty_product():
    x0, spread, k, hbar = 0, 1, 5, 1
    x = np.linspace(x0 - 5 * spread, x0 + 5 * spread, 1000)
    psi = gaussian_wavepacket(x, x0, spread, k)
    product = uncertainty_product(x, psi, hbar)
    assert uncertainty_product >= (hbar / 2 - 1e-2)
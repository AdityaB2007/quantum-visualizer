import numpy as np

from src.gaussian_wavepackets import gaussian_wavepacket

def test_gaussian_wavepackets():
    x0 = 0
    spread = 0.2
    k = 0
    x = np.linspace(x0 - 5 * spread, x0 + 5 * spread, 1000)
    psi = gaussian_wavepacket(x, x0, spread, k)
    max_idx = np.argmax(np.abs(psi))
    assert abs(x[max_idx] - x0) < 0.01
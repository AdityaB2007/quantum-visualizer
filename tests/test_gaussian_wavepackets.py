import numpy as np

from src.gaussian_wavepackets import gaussian_wavepacket

def test_gaussian_wavepackets():
    x = np.linspace(-100, 100, 1E10)
    x0 = 0
    spread = 0.2
    psi = gaussian_wavepacket(x, x0, spread)
    max_idx = np.argmax(psi)
    assert abs(x[max_idx] - x0) < 0.01
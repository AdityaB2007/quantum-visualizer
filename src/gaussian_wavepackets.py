import numpy as np

def gaussian_wavepacket(x, x0, spread, k):
    psi = np.exp(-1 * (x - x0) ** 2 / (2 * spread ** 2)) * np.exp(1j * k * x)
    return psi
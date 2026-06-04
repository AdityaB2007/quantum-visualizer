import numpy as np

def gaussian_wavepacket(x, x0, spread):
    phi = np.exp(-1 * (x - x0) ** 2 / (2 * spread ** 2))
    return phi
import numpy as np

def normalize_wavefunction(x, psi):
    """
    Objective: Normalize a wavefunction numerically
    @param x : ndarray, spatial grid
    @param psi : ndarray, wavefunction values
    @return ndarray : normalized wavefunction
    """
    norm = np.trapezoid(np.abs(psi) ** 2, x)
    return psi / np.sqrt(norm)
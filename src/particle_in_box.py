import numpy as np

def particle_in_box_wavefunction(x, n, L):
    """
    Objective: Obtain the normalized stationary-state
    wavefunction for a particle in a 1D box
    @param x : ndarray (ensure x is in [0:L])
    @param n : principal quantum number
    @param L : length of box
    @return : normalized wavefunction
    """
    psi_n = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
    return psi_n
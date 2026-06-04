import numpy as np

def expectation_x(x, psi):
    integrand = x * np.abs(psi) ** 2
    exp_x = np.trapezoid(integrand, x)
    return exp_x
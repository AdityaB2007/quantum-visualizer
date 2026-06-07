import numpy as np
from src.utils import probability_density

def expectation_x(x, psi):
    integrand = x * probability_density(psi)
    exp_x = np.trapezoid(integrand, x)
    return exp_x

def expectation_x_squared(x, psi):
    integrand = x ** 2 * probability_density(psi)
    return np.trapezoid(integrand, x)

def variance_x(x, psi):
    return expectation_x_squared(x, psi) - expectation_x(x, psi) ** 2

def uncertainty_x(x, psi):
    var = variance_x(x, psi)
    return np.sqrt(var)
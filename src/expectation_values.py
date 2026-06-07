import numpy as np

def expectation_x(x, psi):
    integrand = x * np.abs(psi) ** 2
    exp_x = np.trapezoid(integrand, x)
    return exp_x

def expectation_x_squared(x, psi):
    integrand = x ** 2 * np.abs(psi) ** 2
    return np.trapezoid(integrand, x)

def variance_x(x, psi):
    return expectation_x_squared(x, psi) - expectation_x(x, psi) ** 2

def uncertainty_x(x, psi):
    var = variance_x(x, psi)
    return np.sqrt(var)
# Quantum Visualizer

## Overview

Quantum Visualizer is a Python-based scientific computing project for exploring foundational concepts in quantum mechanics through numerical analysis and data visualization.

The project implements wavefunctions, probability densities, expectation values (means), uncertainty (standard deviation) calculations, and complex Gaussian wavepackets. It combines mathematical modeling with visualization to help build intuition for quantum systems and their particle-level behavior.

## Objectives

- Visualize quantum wavefunctions and probability densities
- Explore uncertainty and expectation values via numerical methods
- Develop intuition for fundamental concepts in quantum physics
- Practice scientific computing with hands-on Python programming
- Build a modular and well-tested technical project

## Technologies

- Python
- NumPy
- Matplotlib
- Pillow
- Pytest

## Features

- Wavefunction normalization using numerical integration
- Particle-in-a-box wavefunctions and probability densities
- Position expectation value, variance, and uncertainty calculations
- Momentum expectation value, variance, and uncertainty calculations using finite-difference methods
- Numerical verification of the Heisenberg uncertainty principle
- Complex-valued Gaussian wavepacket modeling
- Visualization of real, imaginary, and probability-density components of wavefunctions
- Animated Gaussian wavepacket spread visualizations
- Animated Gaussian wavepacket wave-number visualizations
- Automated unit tests using Pytest

## Example Visualizations

### Gaussian Wavepacket Spread Animation

![Wavepacket Spread](figures/wavepacket_spread.gif)

### Gaussian Wavenumber Animation

![Wavepacket Wave Number](figures/wavepacket_wavenumber.gif)

## Installation

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
pytest
```

## Example Commands

```bash
python -m src.visualize_gaussian_wavepacket
python -m src.visualize_probability_density
python -m src.visualize_uncertainty
python -m src.visualize_heisenberg_uncertainty

python -m src.compare_particle_in_box_states
python -m src.compare_uncertainty_vs_spread

python -m src.animate_wavepacket_spread
python -m src.animate_wavepacket_wavenumber
```

## Project Structure

```text
quantum-visualizer/
├── src/
│   ├── particle_in_box.py
│   ├── gaussian_wavepackets.py
│   ├── expectation_values.py
│   ├── utils.py
│   ├── animate_wavepacket_spread.py
│   ├── animate_wavepacket_wavenumber.py
│   ├── compare_uncertainty_vs_spread.py
│   ├── visualize_gaussian_wavepacket.py
│   ├── visualize_uncertainty.py
│   └── visualize_heisenberg_uncertainty.py
├── tests/
├── figures/
├── requirements.txt
└── README.md
```

## Future Improvements

- Time-dependent Schrödinger equation simulations
- Additional quantum systems and potentials
- Numerical eigenstate solvers
- Interactive visualizations
- Expanded computational physics modules

## Status

Version v1.0 completed.

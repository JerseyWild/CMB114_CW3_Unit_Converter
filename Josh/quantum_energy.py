# quantum_energy.py

import scipy.constants as const

def energy_from_frequency(frequency_hz):
    """Calculate energy (Joules) from frequency (Hz)."""
    return const.h * frequency_hz

def frequency_from_energy(energy_joules):
    """Calculate frequency (Hz) from energy (Joules)."""
    return energy_joules / const.h

def energy_from_wavelength(wavelength_m):
    """Calculate energy (Joules) from wavelength (meters)."""
    return const.h * const.c / wavelength_m

def wavelength_from_energy(energy_joules):
    """Calculate wavelength (meters) from energy (Joules)."""
    return const.h * const.c / energy_joules

def energy_from_wavenumber(wavenumber_per_m):
    """Calculate energy (Joules) from wavenumber (1/m)."""
    return const.h * const.c * wavenumber_per_m

def wavenumber_from_energy(energy_joules):
    """Calculate wavenumber (1/m) from energy (Joules)."""
    return energy_joules / (const.h * const.c)

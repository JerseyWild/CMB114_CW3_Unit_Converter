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

def frequency_from_wavelength(wavelength_m):
    """Calculate frequency (Hz) from wavelength (meters)."""
    return const.c / wavelength_m

def wavelength_from_frequency(frequency_hz):
    """Calculate wavelength (meters) from frequency (Hz)."""
    return const.c / frequency_hz

def wavenumber_from_wavelength(wavelength_m):
    """Calculate wavenumber (1/m) from wavelength (meters)."""
    return 1.0 / wavelength_m

def wavelength_from_wavenumber(wavenumber_per_m):
    """Calculate wavelength (meters) from wavenumber (1/m)."""
    return 1.0 / wavenumber_per_m

def energy_from_wavenumber(wavenumber_per_m):
    """Calculate energy (Joules) from wavenumber (1/m)."""
    return const.h * const.c * wavenumber_per_m

def wavenumber_from_energy(energy_joules):
    """Calculate wavenumber (1/m) from energy (Joules)."""
    return energy_joules / (const.h * const.c)

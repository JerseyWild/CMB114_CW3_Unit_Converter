# quantum_energy.py

import scipy.constants as const

'''
Unit Converter
'''

def eV_to_j(value):
    """Converts electron volts to joules"""
    return value*(1.602*(10**-19))

def j_to_eV(value):
    """Converts joules ot electron volts"""
    return value/(1.602*(10**-19))

def nm_to_m(value):
    """Converts nanometres to metres"""
    return value*(10**-9)

def m_to_nm(value):
    """Converts metres to nanometres"""
    return value/(10**-9)

def khz_to_hz(value):
    """Converts kilohertz to hertz"""
    return value/(10**-3)

def hz_to_khz(value):
    """Converts hertz to kilohertz"""
    return value*(10**-3)

def cm_to_m(value):
    """Converts per cm to per m"""
    return value/(10**-2)

def m_to_cm(value):
    """Converts per m to per cm"""
    return value*(10**-2)


'''
Variable finders
'''

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

'''
Variable Function Getters
'''

def From_Energy(energy_joules):
    """Gets all variable functions that are needed from energy input"""
    return energy_joules, wavelength_from_energy(energy_joules), frequency_from_energy(energy_joules), wavenumber_from_energy(energy_joules)

def From_Wavelength(wavelength_m):
    """Gets all variable functions that are needed from wavelength input"""
    energy_joules = energy_from_wavelength(wavelength_m)
    return energy_joules, wavelength_m, frequency_from_energy(energy_joules), wavenumber_from_energy(energy_joules)

def From_Frequency(frequency_hz):
    """Gets all variable functions that are needed from frequency input"""
    energy_joules = energy_from_frequency(frequency_hz)
    return energy_joules, wavelength_from_energy(energy_joules), frequency_hz, wavenumber_from_energy(energy_joules)

def From_Wavenumber(wavenumber_per_m):
    """Gets all variable functions that are needed from wavenumber input"""
    energy_joules = energy_from_wavenumber(wavenumber_per_m)
    return energy_joules, wavelength_from_energy(energy_joules), frequency_from_energy(energy_joules), wavenumber_per_m

def Decider(option, value, unit):
    """Decides what type of data has been given, and if it requires converting into standard units"""
    if option == "Energy":
        if unit == "eV":
            value=eV_to_j(value)
        return From_Energy(value)
    
    elif option == "Wavelength":
        if unit == "nm":
            value=nm_to_m(value)
        return From_Wavelength(value)
    
    elif option == "Frequency":
        if unit == "kHz":
            value=khz_to_hz(value)
        return From_Frequency(value)
    
    elif option == "Wavenumber":
        if unit == "cm^-1":
            value=cm_to_m(value)
        return From_Wavenumber(value)


def Output(option, value, unit):
    """grabs all variables and prints them"""
    energy_j, wavelength_m, frequency_hz, wavenumber_m = Decider(option, value, unit)
    energy_eV = j_to_eV(energy_j)
    wavelength_nm = m_to_nm(wavelength_m)
    frequency_khz = hz_to_khz(frequency_hz)
    wavenumber_cm = m_to_cm(wavenumber_m)
    
    print("####################")
    print("  Data From",option)
    print("####################")
    print("_____________________________")
    print(f"Energy(J)          | {energy_j:.2e}")
    print(f"Energy(eV)         | {energy_eV:.2e}")
    print(f"Wavelength(m)      | {wavelength_m:.2e}")
    print(f"Wavelength(nm)     | {wavelength_nm:.2e}")
    print(f"Frequency(Hz)      | {frequency_hz:.2e}")
    print(f"Frequency(kHz)     | {frequency_khz:.2e}")
    print(f"Wavenumber(m**-1)  | {wavenumber_m:.2e}")
    print(f"Wavenumber(cm**-1) | {wavenumber_cm:.2e}")
    print("")
    return energy_j, energy_eV, wavelength_m, wavelength_nm, frequency_hz, frequency_khz, wavenumber_m, wavenumber_cm

'''
#testers
print(Decider("Wavelength",700,"nm"))
print(Decider("Energy",1.77,"eV"))
Output("Energy",1.77,"eV")
Output("Wavelength",700,"nm")
Output("Wavenumber", 1430000, "m^-1")
'''









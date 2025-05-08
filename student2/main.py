#main.py

#Add ALL functions to the import section once finalised

from quantum_energy import energy_from_wavelength, frequency_from_energy

wavelength = 500e-9  # 500 nm in meters
energy = energy_from_wavelength(wavelength)
print(f"Energy for 500 nm photon: {energy:.3e} J")

frequency = frequency_from_energy(energy)
print(f"Frequency: {frequency:.3e} Hz")

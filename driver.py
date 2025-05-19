#!/usr/bin/python3


print("*** Starting the driver script ***\n")

# import Josh.quantum_energy as qe

# print("Imported modules successfully.")

import Jersey.GUI as gui
print("Imported modules successfully.")

print("Calling Output...\n")

qe.Output("Energy", 1.77, "eV")
gui.open_home_window()

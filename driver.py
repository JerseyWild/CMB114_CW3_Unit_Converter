#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Jersey'))
import quantum_energy

print("*** Starting the driver script ***\n")



import Jersey.GUI as gui
print("Imported modules successfully.")

print("Calling Output...\n")


gui.open_home_window()

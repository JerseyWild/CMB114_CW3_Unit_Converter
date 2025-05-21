
The code is divided between folders `Jersey` and `Josh`. These folders represent who is responsible for what code. The code in 'Josh' was repeated under 'Jersey' for ease of coding and calling functions - same applies to the image EM_spectrum so that the code can be ran from 2 places.
The README and the driver were also written by Josh

---
You can run the code by calling
~~~~
./driver.py
~~~~

or alternatively can be run from GUI.py within 'Jersey' folder

---
make sure scipy is installed by:

pip install scipy

Also pillow may need to be installed

---------------------------------------------------------------------------------------------------------------
Directory Tree of important files

CMB114_CW3_Unit_Converter
|
|--/Jersey
|  |-->GUI.py
|
|--/Josh
|  |-->quantum_energy.py
|
|-->driver.py

--------------------------------------------------------------------------------------------------------------
Explanation of the functionality of the program

The program aims to take in a value of energy, wavelength, frequency or wavenumber and then output all other values that weren't calculated, and use them to determine what type of wave the user has input and display this on a scale
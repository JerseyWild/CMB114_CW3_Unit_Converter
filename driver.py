#!/usr/bin/python3

from student1.featureA import *
from student2.featureB import *

print("*** Starting the driver script ***\n")

# Call hello_world from student1.featureA
hello_world()

# Initialize the class from student2.featureB
mc = myclass(5)
# Print the number
mc.print_num()

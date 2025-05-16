#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 16:18:24 2025

@author: cmjw
"""

from tkinter import *
from tkinter import ttk

vals_submitted = 0 # records how many values from the dropbox have been submitted


def open_converter_window():
     converter_win = Toplevel(root)
     converter_win.title("Unit Converter - Conversions Page")
     converter_win.geometry(f"800x500+{center_x}+{center_y}")
     
##     output_log = ttk.PanedWindow(orient=HORIZONTAL)
##     left_list = Listbox(converter_win)
##     left_list.pack(side=LEFT)
##     output_log.add(left_list)
##     right_list = Listbox(converter_win)
##     right_list.pack(side=RIGHT)
##     output_log.add(right_list)
##     output_log.pack(fill=BOTH, expand=True)

     def thermo_val_submitted():
          global vals_submitted
          print("val count =", vals_submitted)
          log_text = "Value chosen: " + thermo_val_choice.get()
          output_log = Label(converter_win, text=log_text) # creates a label containing the current submission choice
          output_log.place(x=450,y=(95+vals_submitted*20)) # places the label a factor of 20 below the previous entry
          vals_submitted += 1 # adds 1 to the count since 1 more submission has been made

     thermo_val_choice = StringVar()
     thermo_val_dropdown = ttk.Combobox(converter_win, font=(10), textvariable=thermo_val_choice)
     thermo_val_dropdown["values"] = ("Choose a value", "Energy", "Frequency", "Wavelength", "Wavenumber","Time", "Mass", "Velocity", "Momentum", "Charge", "Voltage")
     thermo_val_dropdown.set("Choose a value")
     thermo_val_dropdown.place(x=100, y=100)   
     
     thermo_val_button = Button(converter_win, text="Submit", font=(8), padx=0, pady=0, command=thermo_val_submitted)
     thermo_val_button.place(x=350, y=95)


root = Tk()
root.title("Unit Converter - Home Page")
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
center_x = screen_w//6
center_y = screen_h//6
root.geometry(f"800x500+{center_x}+{center_y}")
root.maxsize(800, 500)

home_title = Label(root, text="UNIT CONVERTER", font=("Comic Sans MS", 20))
home_title.place(x=290, y=100)

enter_button = Button(root, text="ENTER THE PROGRAM", font=("Comic Sans MS", 12), anchor="center", padx=20, pady=10,
                      activebackground="white", activeforeground="grey", bg="green", fg="white", cursor="hand2", command=open_converter_window)
enter_button.place(x=300, y=175)

exit_button = Button(root, text="EXIT", font=("Comic Sans MS", 12), anchor="center", padx=88, pady=10,
                     activebackground="white", activeforeground="grey", bg="red", fg="white", cursor="hand2", command=root.destroy)
exit_button.place(x=300, y=250)

options_button = Button(root, text="OPTIONS", font=("Comic Sans MS", 12), anchor="center", padx=28.5, pady=1,
                        activebackground="white", activeforeground="grey", bg="blue", fg="white", cursor="hand2")
options_button.place(x=335, y=325)

root.mainloop()

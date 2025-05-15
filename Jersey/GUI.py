#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 16:18:24 2025

@author: cmjw
"""

from tkinter import *
from tkinter import ttk


def open_converter_window():
     converter_win = Toplevel(root)
     converter_win.title("Unit Converter - Conversions Page")
     converter_win.geometry(f"800x500+{center_x}+{center_y}")
     combobox_options = StringVar()
     thermo_val_dropdown = ttk.Combobox(converter_win, textvariable=combobox_options)
     thermo_val_dropdown["values"] = ("Choose a value", "Energy", "Frequency", "Wavelength", "Wavenumber","Time", "Mass", "Velocity", "Momentum", "Charge", "Voltage")
     thermo_val_dropdown.set("Choose a value")
     thermo_val_dropdown.place(x=100, y=100)
     

  
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






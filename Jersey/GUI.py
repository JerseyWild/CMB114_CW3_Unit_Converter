#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 16:18:24 2025

@author: cmjw
"""

from tkinter import *
from tkinter import ttk

thermo_submits = 0
#vals_submitted = 0 # records how many values from the dropbox have been submitted
#units_submitted = 0

def open_home_window():
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



          def thermo_submitted():
               global thermo_submits
               #print("thermo count =", thermo_submits)
               thermo_unit_str = thermo_unit_choice.get()
               first_brack_ind = thermo_unit_str.find("(")
               second_brack_ind = thermo_unit_str.find(")")
               #print(first_brack_ind)
               #print(second_brack_ind)
               unit_abbrev = thermo_unit_str[first_brack_ind+1:second_brack_ind]
               log_text = thermo_val_choice.get() + " of " + thermo_num_choice.get() + " " + unit_abbrev
               output_log = Label(converter_win, text=log_text) # creates a label containing the current submission choice
               output_log.place(x=475,y=(95+thermo_submits*20)) # places the label a factor of 20 below the previous entry
               thermo_submits += 1 # adds 1 to the count since 1 more submission has been made

     ##     def thermo_val_submitted():
     ##          global vals_submitted
     ##          print("val count =", vals_submitted)
     ##          log_text = "Value chosen: " + thermo_val_choice.get()
     ##          output_log = Label(converter_win, text=log_text) # creates a label containing the current submission choice
     ##          output_log.place(x=475,y=(95+vals_submitted*20)) # places the label a factor of 20 below the previous entry
     ##          vals_submitted += 1 # adds 1 to the count since 1 more submission has been made
     ##
     ##     def thermo_unit_submitted():
     ##          global units_submitted
     ##          print("unit count =", units_submitted)
     ##          log_text = "Value chosen: " + thermo_unit_choice.get()
     ##          output_log = Label(converter_win, text=log_text) # creates a label containing the current submission choice
     ##          output_log.place(x=475,y=(95+units_submitted*20)) # places the label a factor of 20 below the previous entry
     ##          units_submitted += 1 # adds 1 to the count since 1 more submission has been made
          
          thermo_num_choice = StringVar()
          thermo_num_entry = Entry(converter_win, font=(10), textvariable=thermo_num_choice)
          thermo_num_entry.insert(2, "Enter a number")
          thermo_num_entry.place(x=100, y=50)   
          
          thermo_submit_button = Button(converter_win, text="Submit", font=(8), padx=0, pady=0, command=thermo_submitted)
          thermo_submit_button.place(x=175, y=200)


          thermo_val_choice = StringVar()
          thermo_val_dropdown = ttk.Combobox(converter_win, font=(10), textvariable=thermo_val_choice)
          thermo_val_dropdown["values"] = ("Energy", "Frequency", "Wavelength", "Wavenumber")
          thermo_val_dropdown.set("Choose a value")
          thermo_val_dropdown.place(x=100, y=100)   
          
          #thermo_val_button = Button(converter_win, text="Submit", font=(8), padx=0, pady=0, command=thermo_val_submitted)
          #thermo_val_button.place(x=375, y=95)

          thermo_unit_choice = StringVar()
          thermo_unit_dropdown = ttk.Combobox(converter_win, font=(10), textvariable=thermo_unit_choice)
          thermo_unit_dropdown["values"] = ("Joules (J)", "Electron volts (eV)", "Nanometers (nm)", "Meters (m)", "Hertz (Hz)", "Kilohertz (KHz)")
          thermo_unit_dropdown.set("Choose a unit")
          thermo_unit_dropdown.place(x=100, y=150)   
          
          #thermo_unit_button = Button(converter_win, text="Submit", font=(8), padx=0, pady=0, command=thermo_unit_submitted)
          #thermo_unit_button.place(x=375, y=145)

          converter_goback_button = Button(converter_win, text="GO BACK", font=("Comic Sans MS", 12), anchor="center", padx=88, pady=10,
                          activebackground="white", activeforeground="grey", bg="red", fg="white", cursor="hand2", command=converter_win.destroy)
          converter_goback_button.place(x=275, y=350)



     enter_button = Button(root, text="ENTER THE PROGRAM", font=("Comic Sans MS", 12), anchor="center", padx=20, pady=10,
                           activebackground="white", activeforeground="grey", bg="green", fg="white", cursor="hand2", command=open_converter_window)
     enter_button.place(x=300, y=175)

     exit_button = Button(root, text="EXIT", font=("Comic Sans MS", 12), anchor="center", padx=88, pady=10,
                          activebackground="white", activeforeground="grey", bg="red", fg="white", cursor="hand2", command=root.destroy)
     exit_button.place(x=300, y=250)



     def open_options_window():
          options_win = Toplevel(root)
          options_win.title("Unit Converter - Options Page")
          options_win.geometry(f"800x500+{center_x}+{center_y}")
          about_text = Label(options_win,
                             text="This Python program was created by Josh Hutchings and Jersey Wilden:\n\nJosh - formula calculations and unit conversions\nJersey - graphical user interface (GUI)",
                             font=(15), justify="left") # creates a label containing the current submission choice
          about_text.place(x=50,y=100) # places the label a factor of 20 below the previous entry

          options_goback_button = Button(options_win, text="GO BACK", font=("Comic Sans MS", 12), anchor="center", padx=88, pady=10,
                          activebackground="white", activeforeground="grey", bg="red", fg="white", cursor="hand2", command=options_win.destroy)
          options_goback_button.place(x=275, y=350)




     options_button = Button(root, text="OPTIONS", font=("Comic Sans MS", 12), anchor="center", padx=28.5, pady=1,
                             activebackground="white", activeforeground="grey", bg="blue", fg="white", cursor="hand2", command=open_options_window)
     options_button.place(x=335, y=325)

     root.mainloop()



# open_home_window() test if running GUI.py on its own (without driver)




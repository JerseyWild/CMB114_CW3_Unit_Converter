#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 16:18:24 2025

@author: cmjw
"""

import quantum_energy as qe
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


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
               thermo_submits += 1
               #int_num = int(thermo_num_choice.get())
               float_num = float(thermo_num_choice.get())

               thermo_unit_str = thermo_unit_choice.get()
               first_brack_ind = thermo_unit_str.find("(")
               second_brack_ind = thermo_unit_str.find(")")
               unit_abbrev = thermo_unit_str[first_brack_ind+1:second_brack_ind]
               
               #print(thermo_unit_choice.get())
               #int_val = int(thermo_val_choice.get())
               thermo_outs = qe.Output(thermo_val_choice.get(), float_num, unit_abbrev)
##               global wavelength
##               wavelength = thermo_outs[2]
##               print("WAVELENGTH =", wavelength)
               #print(thermo_outs)
               print("----------------------------------")
               #current_out_text =
               current_out_label = Label(converter_win, text=(f"Energy (J) = {thermo_outs[0]:.2e}\
                                                       \nEnergy (eV) = {thermo_outs[1]:.2e}\
                                                       \nWavelength (m) = {thermo_outs[2]:.2e}\
                                                       \nWavelength (nm) = {thermo_outs[3]:.2e}\
                                                       \nFrequency (Hz) = {thermo_outs[4]:.2e}\
                                                       \nFrequency (kHz) = {thermo_outs[5]:.2e}\
                                                       \nWavenumber (m^-1) = {thermo_outs[6]:.2e}\
                                                       \nWavenumber (cm^-1) = {thermo_outs[7]:.2e}"), justify="left", font=5)
               current_out_label.place(x=425,y=25)

               wavelength = thermo_outs[2]

               
               if wavelength < 10**-11:
                    EM_dot = Label(converter_win, text="    ", font=1, bg="red")
                    EM_dot.place(x=595,y=368)
               elif 10**-8 > wavelength >= 10**-11:
                    EM_dot = Label(converter_win, text="    ", font=1, bg="red")
                    EM_dot.place(x=490, y=368)
               elif 4*10**-7 > wavelength >= 10**-8:
                    EM_dot = Label(converter_win, text="    ", font=1, bg="red")
                    EM_dot.place(x=395, y=368)
               elif 7*10**-7 > wavelength >= 4*10**-7:
                    EM_dot = Label(converter_win, text="", font=1, bg="red")
                    EM_dot.place(x=347, y=368)
               elif 1*10**-3 > wavelength >= 7*10**-7:
                    EM_dot = Label(converter_win, text="    ", font=1, bg="red")
                    EM_dot.place(x=275, y=368)
               elif 10**-1 > wavelength >= 10**-3:
                    EM_dot = Label(converter_win, text="    ", font=1, bg="red")
                    EM_dot.place(x=160, y=368)


               #return 
               
##               global thermo_submits
##               #print("thermo count =", thermo_submits)

               #print(first_brack_ind)
               #print(second_brack_ind)
     
##               log_text = thermo_val_choice.get() + " of " + thermo_num_choice.get() + " " + unit_abbrev
##               output_log = Label(converter_win, text=log_text) # creates a label containing the current submission choice
##               output_log.place(x=475,y=(95+thermo_submits*20)) # places the label a factor of 20 below the previous entry
##               thermo_submits += 1 # adds 1 to the count since 1 more submission has been made

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
          
          thermo_num_title = Label(converter_win, text="Number to be converted", font=10)
          thermo_num_title.place(x=50, y=20)
          
          thermo_num_choice = StringVar()
          thermo_num_entry = Entry(converter_win, font=(10), textvariable=thermo_num_choice)
          
          #thermo_num_entry.insert(1, "Enter a number")
          thermo_num_entry.place(x=50, y=50)   
          
          thermo_submit_button = Button(converter_win, text="Submit", font=(8), padx=30, pady=0, command=thermo_submitted)
          thermo_submit_button.place(x=100, y=175)


          thermo_val_choice = StringVar()
          thermo_val_dropdown = ttk.Combobox(converter_win, font=(10), textvariable=thermo_val_choice)
          thermo_val_dropdown["values"] = ("Energy", "Frequency", "Wavelength", "Wavenumber")
          thermo_val_dropdown.set("Choose a value")
          thermo_val_dropdown.place(x=50, y=90)   
          
          #thermo_val_button = Button(converter_win, text="Submit", font=(8), padx=0, pady=0, command=thermo_val_submitted)
          #thermo_val_button.place(x=375, y=95)

          thermo_unit_choice = StringVar()
          thermo_unit_dropdown = ttk.Combobox(converter_win, font=(10), textvariable=thermo_unit_choice)
          thermo_unit_dropdown["values"] = ("Joules (J)", "Electron volts (eV)",
                                            "Meters (m)", "Nanometers (nm)",
                                            "Hertz (Hz)", "Kilohertz (kHz)",
                                            "Meters^-1 (m^-1)", "Centimeters^-1 (cm^-1)")
          thermo_unit_dropdown.set("Choose a unit")
          thermo_unit_dropdown.place(x=50, y=130)   
          
          #thermo_unit_button = Button(converter_win, text="Submit", font=(8), padx=0, pady=0, command=thermo_unit_submitted)
          #thermo_unit_button.place(x=375, y=145)

          converter_goback_button = Button(converter_win, text="GO BACK", font=("Comic Sans MS", 12), anchor="center", padx=20, pady=10,
                          activebackground="white", activeforeground="grey", bg="red", fg="white", cursor="hand2", command=converter_win.destroy)
          converter_goback_button.place(x=665, y=425)

          

          EM_spec_title = Label(converter_win, text="Electromagnetic spectrum", font=10)
          EM_spec_title.place(x=50, y=250)

          

          EM_spec_image = Image.open("EM_spectrum.png")
          resize_img = EM_spec_image.resize((600, 200))
          
          EM_spec_img = ImageTk.PhotoImage(resize_img)
          EM_spec_lab = Label(converter_win, image=EM_spec_img)
          
          EM_spec_lab.place(x=50, y=280)
          EM_spec_img.show()

          

          
          
          





     enter_button = Button(root, text="ENTER THE PROGRAM", font=("Comic Sans MS", 12), anchor="center", padx=20, pady=10,
                           activebackground="white", activeforeground="grey", bg="green", fg="white", cursor="hand2", command=open_converter_window)
     enter_button.place(x=300, y=175)

     exit_button = Button(root, text="EXIT", font=("Comic Sans MS", 12), anchor="center", padx=88, pady=10,
                          activebackground="white", activeforeground="grey", bg="red", fg="white", cursor="hand2", command=root.destroy)
     exit_button.place(x=300, y=250)



     def open_about_window():
          about_win = Toplevel(root)
          about_win.title("Unit Converter - About Page")
          about_win.geometry(f"800x500+{center_x}+{center_y}")
          about_text1 = Label(about_win,
                             text="This Python program was created by Josh Hutchings and Jersey Wilden:\n\nJosh - quantum_energy.py, driver.py, README.md\nJersey - GUI.py"
                              , font=15, justify="left") # creates a label containing the current submission choice
          about_text1.place(x=50,y=35) # places the label a factor of 20 below the previous entry

          about_text2 = Label(about_win, text="The user inputs a value of energy, frequency, wavelength or wavenumber\nthen the program outputs all other values that weren't calculated.\nThe electromagnetic wave associated to the outputted wavelength is shown\non the electromagnetic spectrum by a red square.",
                              font=(15), justify="left")
          about_text2.place(x=50, y=150)

          about_text3 = Label(about_win, text="Electromagnetic spectrum image taken from:\n\
24CMB105_FP-3_units_handout.pdf\nvia https://learn.lboro.ac.uk/course/view.php?id=15171&section=5",
                              font=(5), justify="left")
          about_text3.place(x=50, y=300) 

          about_goback_button = Button(about_win, text="GO BACK", font=("Comic Sans MS", 12), anchor="center", padx=88, pady=10,
                          activebackground="white", activeforeground="grey", bg="red", fg="white", cursor="hand2", command=about_win.destroy)
          about_goback_button.place(x=275, y=400)




     options_button = Button(root, text="ABOUT", font=("Comic Sans MS", 12), anchor="center", padx=28.5, pady=1,
                             activebackground="white", activeforeground="grey", bg="blue", fg="white", cursor="hand2", command=open_about_window)
     options_button.place(x=350, y=325)

     root.mainloop()



open_home_window() # test if running GUI.py on its own (without driver)




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 16:18:24 2025

@author: cmjw
"""

import quantum_energy as qe # import Josh's quantum_energy.py file
from tkinter import * # imports everything from tkinter
from tkinter import ttk # imports themed tkinter from tkinter
from PIL import Image, ImageTk # imports pillow to enable the display of images


thermo_submits = 0


def open_home_window(): # function that controls the home page. this is the master/root window of the program
     
     root = Tk() # create the master tkinter window that all other windows built upon
     root.title("Unit Converter - Home Page")
     screen_w = root.winfo_screenwidth() # gets the width of the current user's screen
     screen_h = root.winfo_screenheight() # gets the height of the current user's screen
     center_x = screen_w//6
     center_y = screen_h//6
     root.geometry(f"800x500+{center_x}+{center_y}") # sets the dimensions of the window and opens it in the screen's center
     root.maxsize(800, 500)

     home_title = Label(root, text="UNIT CONVERTER", font=("Comic Sans MS", 20)) # creates a title for the home page
     home_title.place(x=290, y=100)


     def open_converter_window(): # function that controls the converter page. this is a level below the home page

          converter_win = Toplevel(root) # creates a new window for the converter on top of the master window
          converter_win.title("Unit Converter - Conversions Page")
          converter_win.geometry(f"800x500+{center_x}+{center_y}") # sets the dimensions of the window and opens it in the screen's center

          def thermo_submitted(): # function that takes the 3 inputted values and uses Josh's quantum_energy.py to determine the outputs
               
               invalid_input = False
               try: # this try-except is to stop any errors due to invalid inputs made by the user (e.g. entering characters, not letters)
                    float_num = float(thermo_num_choice.get())
               except ValueError:
                    print("Please enter a number.")
                    invalid_input = True

               if invalid_input == False: # if there are no errors (i.e. the input is valid/a number) the rest of the function can run
               
                    global thermo_submits
                    thermo_submits += 1

                    thermo_unit_str = thermo_unit_choice.get()
                    first_brack_ind = thermo_unit_str.find("(")
                    second_brack_ind = thermo_unit_str.find(")")
                    unit_abbrev = thermo_unit_str[first_brack_ind+1:second_brack_ind]
                    
                    thermo_outs = qe.Output(thermo_val_choice.get(), float_num, unit_abbrev) # gets the quantum energy outputs from Josh's file using my inputs

                    # creates a label with all of the quantum energy values associated to the current user input                         
                    current_out_label = Label(converter_win, text=(f"Energy (J) = {thermo_outs[0]:.2e}\
                                                            \nEnergy (eV) = {thermo_outs[1]:.2e}\
                                                            \nWavelength (m) = {thermo_outs[2]:.2e}\
                                                            \nWavelength (nm) = {thermo_outs[3]:.2e}\
                                                            \nFrequency (Hz) = {thermo_outs[4]:.2e}\
                                                            \nFrequency (kHz) = {thermo_outs[5]:.2e}\
                                                            \nWavenumber (m^-1) = {thermo_outs[6]:.2e}\
                                                            \nWavenumber (cm^-1) = {thermo_outs[7]:.2e}"), justify="left", font=5)
                    current_out_label.place(x=425,y=25)

                    wavelength = thermo_outs[2] # finds the wavelength number within Josh's output

                    # THIS BLOCK OF CODE DETERMINES WHICH WAVELENGTH RANGE THE OUTPUT FALLS INTO AND PLACES A RED SQUARE AT THE APPROPRIATE WAVE TYPE
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

               
          thermo_num_title = Label(converter_win, text="Number to be converted", font=10) # creates a text label above the entry box
          thermo_num_title.place(x=50, y=20)
          
          thermo_num_choice = StringVar()
          thermo_num_entry = Entry(converter_win, font=(10), textvariable=thermo_num_choice) # creates an entry box for the quantum energy number to be entered
          
          thermo_num_entry.place(x=50, y=50)   
          
          thermo_submit_button = Button(converter_win, text="Submit", font=(8), padx=30, pady=0, command=thermo_submitted) # submit button, when clicked calls thermo_submitted
          thermo_submit_button.place(x=100, y=175)

          thermo_val_choice = StringVar()
          thermo_val_dropdown = ttk.Combobox(converter_win, font=(10), textvariable=thermo_val_choice) # dropdown box to pick the type of quantum value
          thermo_val_dropdown["values"] = ("Energy", "Frequency", "Wavelength", "Wavenumber")
          thermo_val_dropdown.set("Choose a value") # sets the default value of the dropdown box
          thermo_val_dropdown.place(x=50, y=90)   

          thermo_unit_choice = StringVar()
          thermo_unit_dropdown = ttk.Combobox(converter_win, font=(10), textvariable=thermo_unit_choice) # dropdown box to pick the units of the chose quantum value
          thermo_unit_dropdown["values"] = ("Joules (J)", "Electron volts (eV)",
                                            "Meters (m)", "Nanometers (nm)",
                                            "Hertz (Hz)", "Kilohertz (kHz)",
                                            "Meters^-1 (m^-1)", "Centimeters^-1 (cm^-1)")
          thermo_unit_dropdown.set("Choose a unit") # sets the default value of the dropdown box
          thermo_unit_dropdown.place(x=50, y=130)   

          converter_goback_button = Button(converter_win, text="GO BACK", font=("Comic Sans MS", 12), anchor="center", padx=20, pady=10,
                          activebackground="white", activeforeground="grey", bg="red", fg="white", cursor="hand2", command=converter_win.destroy)
          converter_goback_button.place(x=665, y=425)

          EM_spec_title = Label(converter_win, text="Electromagnetic spectrum", font=10)
          EM_spec_title.place(x=50, y=250)

          EM_spec_image = Image.open("EM_spectrum.png") # opens the EM_spectrum.png file
          resize_img = EM_spec_image.resize((600, 200)) # changes the dimensions of the EM file to fit the window as needed
          
          EM_spec_img = ImageTk.PhotoImage(resize_img)
          EM_spec_lab = Label(converter_win, image=EM_spec_img)
          
          EM_spec_lab.place(x=50, y=280)
          EM_spec_img.show() # makes the image visible on the window


     enter_button = Button(root, text="ENTER THE PROGRAM", font=("Comic Sans MS", 12), anchor="center", padx=20, pady=10, # creates an enter button, when clicked sends the user to the converter page
                           activebackground="white", activeforeground="grey", bg="green", fg="white", cursor="hand2", command=open_converter_window)
     enter_button.place(x=300, y=175)

     exit_button = Button(root, text="EXIT", font=("Comic Sans MS", 12), anchor="center", padx=88, pady=10, # creates an exit button, when clicked closes the whole program and all associated windows
                          activebackground="white", activeforeground="grey", bg="red", fg="white", cursor="hand2", command=root.destroy)
     exit_button.place(x=300, y=250)



     def open_about_window(): # function that controls the about page. this page is a level below the home page
          about_win = Toplevel(root) # creates the about page window
          about_win.title("Unit Converter - About Page")
          about_win.geometry(f"800x500+{center_x}+{center_y}") # sets the dimensions of the window and places it in the current screen's center

          # THIS BLOCK OF CODE IS TEXT CONCERNING WHO MADE THE PROGRAM, WHAT THE PROGRAM DOES AND ANY REFERENCES
          about_text1 = Label(about_win,
                             text="This Python program was created by Josh Hutchings and Jersey Wilden:\n\nJosh - quantum_energy.py, driver.py, README.md\nJersey - GUI.py"
                              , font=15, justify="left")
          about_text1.place(x=50,y=35)

          about_text2 = Label(about_win, text="The user inputs a value of energy, frequency, wavelength or wavenumber\nthen the program outputs all other values that weren't calculated.\nThe electromagnetic wave associated to the outputted wavelength is shown\non the electromagnetic spectrum by a red square.",
                              font=(15), justify="left")
          about_text2.place(x=50, y=150)

          about_text3 = Label(about_win, text="Electromagnetic spectrum image taken from:\n\
24CMB105_FP-3_units_handout.pdf\nvia https://learn.lboro.ac.uk/course/view.php?id=15171&section=5",
                              font=(5), justify="left")
          about_text3.place(x=50, y=300) 

          about_goback_button = Button(about_win, text="GO BACK", font=("Comic Sans MS", 12), anchor="center", padx=88, pady=10, # creates a go back button, when clicked deletes the current window
                          activebackground="white", activeforeground="grey", bg="red", fg="white", cursor="hand2", command=about_win.destroy)
          about_goback_button.place(x=275, y=400)



     about_button = Button(root, text="ABOUT", font=("Comic Sans MS", 12), anchor="center", padx=28.5, pady=1, # creates an about button, when clicked calls the open_about_window function
                             activebackground="white", activeforeground="grey", bg="blue", fg="white", cursor="hand2", command=open_about_window)
     about_button.place(x=350, y=325)

     root.mainloop() # keeps the tkinter running



# open_home_window() # uncomment if wanting to test GUI.py on its own (without driver)





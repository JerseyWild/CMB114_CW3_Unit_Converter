#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 16:18:24 2025

@author: cmjw
"""

from tkinter import *




def open_converter_window():
     converter_window = Toplevel(root)
     converter_window.title("Unit Converter - Conversions Page")
     converter_window.geometry("800x500+1000+500")

    
root = Tk()
root.title("Unit Converter - Home Page")
root.geometry("800x500+1000+500")
root.maxsize(800, 500)
title_label = Label(root, text="Unit Converter")




enter_button = Button(root, text="ENTER THE PROGRAM", padx=20, pady=10, activebackground="white", activeforeground="grey", anchor="center", bg="green", fg="white", font=("Comic Sans MS", 12), command=open_converter_window)
enter_button.place(x=300, y=175)



enter_button = Button(root, text="EXIT", padx=28.5, pady=10, activebackground="white", activeforeground="grey", anchor="center", bg="red", fg="white", font=("Comfortaa", 12), command=root.destroy)
enter_button.place(x=300, y=250)




root.mainloop()




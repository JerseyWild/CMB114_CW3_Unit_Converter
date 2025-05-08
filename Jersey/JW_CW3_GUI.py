#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 16:18:24 2025

@author: cmjw
"""


import tkinter as tk


root = tk.Tk()
root.title("Unit Converter")
root.geometry("800x500")
root.maxsize(800, 500)
title_label = tk.Label(root, text="Unit Converter")

enter_button = tk.Button(root, text="ENTER THE PROGRAM", padx=20, pady=10, activebackground="white", activeforeground="grey", anchor="center", bg="green", fg="white", font=("Century Gothic", 12), command=)
enter_button.place(x=300, y=175)

enter_button = tk.Button(root, text="EXIT", padx=28.5, pady=10, activebackground="white", activeforeground="grey", anchor="center", bg="red", fg="white", font=("Century Gothic", 12))
enter_button.place(x=300, y=250)

converter = tk.Frame(root)

root.mainloop()




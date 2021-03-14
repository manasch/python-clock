import tkinter as tk
from tkinter import colorchooser

colors={
    "bg_col":"black",
    "o_circle":"white",
    "i_circle":"white",
    "gear":"white",
    "line":"white",
    "num":"white",
    "hour":"white",
    "min":"white",
    "sec":"red"
}

def menu(): 
    def choose_color():
        color_code = colorchooser.askcolor(title="Choose color")
        colors["bg_col"]=color_code[1]
    root = tk.Toplevel()
    root.geometry("300x300")
    root.title("Menu")
    button=tk.Button(root, text="Choose Color",command=choose_color).pack()
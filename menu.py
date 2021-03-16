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
    def h_col():
        color_code = colorchooser.askcolor(title="Choose color")
        colors["hour"]= color_code[1] if color_code[1] else colors["hour"]
    def m_col():
        color_code = colorchooser.askcolor(title="Choose color")
        colors["min"]= color_code[1] if color_code[1] else colors["min"]
    def s_col():
        color_code = colorchooser.askcolor(title="Choose color")
        colors["sec"]= color_code[1] if color_code[1] else colors["sec"]

    def bg_col():
        color_code = colorchooser.askcolor(title="Choose color")
        colors["bg_col"]= color_code[1] if color_code[1] else colors["bg_col"]

    def close():
        root.destroy()

    root = tk.Toplevel()
    root.geometry("450x230+200+100")
    root.title("Color Menu")
    button=tk.Button(root, text="Hour Hand Color",command=h_col).pack(pady=10)#(column=1,row=1,padx=5,pady=5)
    button1=tk.Button(root, text="Min Hand Color",command=m_col).pack(pady=10)#(column=2,row=1,padx=5,pady=5)
    button2=tk.Button(root, text="Sec Hand Color",command=s_col).pack(pady=10)#(column=3,row=1,padx=5,pady=5)
    button3=tk.Button(root, text="Background Color",command=bg_col).pack(pady=10)#(column=1,row=2,padx=5,pady=5)
    button4=tk.Button(root, text="Close",command=close).pack(pady=10)
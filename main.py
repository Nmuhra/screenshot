import pyautogui
import tkinter as tk
from tkinter import filedialog

root=tk.TK()

canvas1=tk.canvas(root,width=300,height=300)
canvas1.pack()

def takescreenshot():
  myScreenshot=pyautogui.screenshot()
  file_path=fieldialog.asksaveasfilename(defaultextension=".png")
  myScreemshot.save(file_path)
  
myButton=tk.Button(text="takescreenshot",command=takeScreenshot,bg="black",fg=canvas1.create_window(150,150,window=myButton)

root.mainloop()
  

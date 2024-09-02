import tkinter as tk
from tkinter import PhotoImage
import json

window = tk.Tk()
window.geometry('1300x700')
window.title('"Who Wants to be a Millionaire" project Created By Kanan Shukurlu')
window.configure(bg='#000044')

logo_photo = PhotoImage(file = 'lessonp1/project1.png')

top_frame = tk.Frame(window, bg='#000044')
top_frame.pack(side=tk.TOP)

logo_label = tk.Label(top_frame, image=logo_photo, bg='#000044')
logo_label.pack()

#baraj

window.mainloop()
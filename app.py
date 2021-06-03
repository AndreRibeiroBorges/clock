from tkinter import *
from datetime import datetime
from time import strftime
from PIL import ImageTk, Image

window = Tk()
window.geometry('1280x720')
window.minsize(750, 200)
window.title('Clock Python')

# Background
background = Image.open('background.jpg')
image = ImageTk.PhotoImage(background)
Label(window, image=image).place(x=0, y=0)

frame = Frame(window, width=820, height=200, bg="#0e1013")
frame.pack(expand=True)
weekday = datetime.today().strftime("%A").upper()
weekday = weekday[:2]


def time():
    a = strftime('%H : %M : %S')
    label1.config(text=a)
    label1.after(1000, time)


label1 = Label(frame, font=('Century Gothic', 60), bg='black', foreground="#d3d3d3")
label1.place(x=280, y=35)
time()

label2 = Label(frame, font=('Century Gothic', 60), bg='gray', foreground="#d3d3d3")
label2.config(text=weekday + " |")
label2.place(x=90, y=35)


def labels():
    label3 = Label(frame, font=('Century Gothic', 8), bg="#0e1013", fg="#7f7f7f", text="DAY")
    label3.place(x=122, y=130)

    label3 = Label(frame, font=('Century Gothic', 8), bg="#0e1013", fg="#7f7f7f", text="HOURS")
    label3.place(x=300, y=130)

    label3 = Label(frame, font=('Century Gothic', 8), bg="#0e1013", fg="#7f7f7f", text="MINUTES")
    label3.place(x=435, y=130)

    label3 = Label(frame, font=('Century Gothic', 8), bg="#0e1013", fg="#7f7f7f", text="SECONDS")
    label3.place(x=580, y=130)


labels()
window.mainloop()

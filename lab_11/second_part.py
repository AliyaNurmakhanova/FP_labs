# Canvas модулін (оның ішінде Tkinter) қолданып, әр студент өз атын өрнектеп  логотип жасап келсін.
from tkinter import *

root = Tk()
root.title("Aliya's logo")
root.resizable(width=False, height=False)

canvas = Canvas(width=1000, height=800, bg='white')
canvas.pack()

canvas.create_text(450, 350, fill="silver", font="Times 80", text="Aliya")

canvas.create_oval(700, 500, 200, 200, outline="gold", width=6)
root.mainloop()
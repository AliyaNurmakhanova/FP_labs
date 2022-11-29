# Canvas модулін (оның ішінде Tkinter) қолданып, әр студент өз атын өрнектеп  логотип жасап келсін.
from tkinter import *

root = Tk()
root.title('Aliya')
root.geometry('800x600')
root.resizable(width=False, height=False)

canvas = Canvas(root, bg='white', width=800, height=600)
canvas.create_line(98, 100, 150, 200, width=3, fill='blue')
canvas.create_line(101, 90, 50, 200, width=3, fill='blue')

canvas.pack()

root.mainloop()
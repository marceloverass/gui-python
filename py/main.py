from tkinter import *

window=Tk()
window.title("Próteses")
window.geometry("600x600")

numeroid=StringVar()
supinf=StringVar()
cliente=StringVar()
dataentrega=StringVar()

frame = LabelFrame(window, text="Gestão de Protéses")
frame.place(x=50, y=50, width=500, height=500)

lblNumeroid = Label(frame, text="Identificação").grid(column=0, row=0)
txtNumeroid = Entry(frame, textvariable=numeroid)
txtNumeroid.grid(column=1, row=0)

lblsupinf = Label(frame, text="Superior/Inferior").grid(column=0, row=1)
txtsupinf = Entry(frame, textvariable=supinf)
txtsupinf.grid(column=1, row=1)

lblCliente = Label(frame, text="Cliente/Dentista").grid(column=2, row=0)
txtCliente = Entry(frame, textvariable=cliente)
txtCliente.grid(column=3, row=0)

lblDataentrega = Label(frame, text="Data de Entrega").grid(column=2, row=1)
txtDataentrega = Entry(frame, textvariable=dataentrega)
txtDataentrega.grid(column=3, row=1)

window.mainloop()
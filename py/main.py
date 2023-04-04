from tkinter import *
from tkinter import ttk

window=Tk()
window.title("Próteses")
window.geometry("700x700")

numeroProtese=StringVar()
supinf=StringVar()
cliente=StringVar()
dataentrega=StringVar()

frame = LabelFrame(window, text="Gestão de Protéses")
frame.place(x=50, y=50, width=600, height=600)

lblNumeroProtese = Label(frame, text="Numº Protése").grid(column=0, row=0, padx=5, pady=5)
txtNumeroProtese = Entry(frame, textvariable=numeroProtese)
txtNumeroProtese.grid(column=1, row=0)

lblsupinf = Label(frame, text="Superior ou Inferior").grid(column=0, row=1, padx=5, pady=5)
txtsupinf = Entry(frame, textvariable=supinf)
txtsupinf.grid(column=1, row=1)

lblCliente = Label(frame, text="Cliente/Dentista").grid(column=2, row=0, padx=5, pady=5)
txtCliente = Entry(frame, textvariable=cliente)
txtCliente.grid(column=3, row=0)

lblDataentrega = Label(frame, text="Data de Entrega").grid(column=2, row=1, padx=5, pady=5)
txtDataentrega = Entry(frame, textvariable=dataentrega)
txtDataentrega.grid(column=3, row=1)

txtMensagens=Label(frame, text="MENSAGENS", fg="green").grid(column=0, row=2, columnspan=4, pady=15,)

tvProteses=ttk.Treeview(frame)
tvProteses.grid(column=0, row=3, columnspan=4, padx=40)
tvProteses["columns"]=("1", "2", "3", "4", "5",)
tvProteses.column("#0", width=0, stretch=NO)
tvProteses.column("#1", width=100, anchor=CENTER)
tvProteses.column("#2", width=100, anchor=CENTER)
tvProteses.column("#3", width=100, anchor=CENTER)
tvProteses.column("#4", width=100, anchor=CENTER)
tvProteses.column("#5", width=100, anchor=CENTER)

tvProteses.heading("#0", text="")
tvProteses.heading("#1", text="ID", anchor=CENTER)
tvProteses.heading("#2", text="Número Prótese", anchor=CENTER)
tvProteses.heading("#3", text="Superior/Inferior", anchor=CENTER)
tvProteses.heading("#4", text="Cliente/Dentista", anchor=CENTER)
tvProteses.heading("#5", text="Data de Entrega", anchor=CENTER)

window.mainloop()
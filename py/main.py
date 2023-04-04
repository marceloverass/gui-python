from tkinter import *
from tkinter import ttk
from conexao import *

window=Tk()
window.title("Próteses")
window.geometry("700x700")

db=DataBase()
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
txtsupinf = ttk.Combobox(frame, values=["S", "I"],textvariable=supinf)
txtsupinf.grid(column=1, row=1)
txtsupinf.current(0)

lblCliente = Label(frame, text="Cliente/Dentista").grid(column=2, row=0, padx=5, pady=5)
txtCliente = Entry(frame, textvariable=cliente)
txtCliente.grid(column=3, row=0)

lblDataentrega = Label(frame, text="Data de Entrega").grid(column=2, row=1, padx=5, pady=5)
txtDataentrega = Entry(frame, textvariable=dataentrega)
txtDataentrega.grid(column=3, row=1)

lblMensagem=Label(frame, text="", fg="green")
lblMensagem.grid(column=0, row=2, columnspan=4, pady=15,)

tvProteses=ttk.Treeview(frame)
tvProteses.grid(column=0, row=3, columnspan=4, padx=40)
tvProteses["columns"]=("1", "2", "3", "4", "5")
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

btnDeletar=Button(frame, text="Deletar", command=lambda:deletar())
btnDeletar.grid(column=0, row=4, columnspan=4, pady=20)
btnCriar=Button(frame, text="Criar", command=lambda:criar())
btnCriar.grid(column=1, row=4)
btnAtualizar=Button(frame, text="Atualizar", command=lambda:atualizar())
btnAtualizar.grid(column=2, row=4)

def validar():
    return len(numeroProtese.get()) and len(supinf.get()) and len(cliente.get()) and len(dataentrega.get())

def limpar():
    numeroProtese.set("")
    supinf.set("")
    cliente.set("")
    dataentrega.set("")

def esvaziar_tabela():
    linhas= tvProteses.get_children()
    for linha in linhas:
        tvProteses.delete(linha)

def preencher_tabela():
    esvaziar_tabela()
    sql="select * from proteses"
    db.cursor.execute(sql)
    linhas= db.cursor.fetchall()
    for linha in linhas:
        id= linha[0]
        tvProteses.insert("", END, id, text= id, values= linha)

def deletar():
    id= tvProteses.selection()[0]
    if int(id)>0:
        sql="delete from proteses where id="+id
        db.cursor.execute(sql)
        db.connection.commit()
        tvProteses.delete(id)
        lblMensagem.config(text="A prótese foi deletada com sucesso", fg="green")
    else:
        lblMensagem.config(text="Selecione uma prótese para eliminar", fg="red")

def criar():
    if atualizar==False:
        if validar():
            val=(numeroProtese.get(), supinf.get(), cliente.get(), dataentrega.get())
            sql="insert into proteses (numeroid, supinf, cliente, dataentrega) values(%s, %s, %s, %s)"
            db.cursor.execute(sql, val)
            db.connection.commit()
            lblMensagem.config(text="A prótese foi criada com sucesso", fg="green")
            preencher_tabela()
            limpar()
        else:
            lblMensagem.config(text="Preencha os campos corretamente", fg="red")
    else: 
        atualizar=False  

def atualizar():
    pass

preencher_tabela()
window.mainloop()
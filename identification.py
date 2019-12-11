import tkinter
import tkinter.messagebox
from tkinter import Entry, Label, LabelFrame

app = tkinter.Tk()
app.title("Identification")
app.minsize(340, 280)
app.maxsize(340,280)
app.resizable(width=True, height=True)
app.geometry('800x600')

#Frame et Labels
l = LabelFrame(app, text="Identification",padx=40,pady=40 ,bg="grey")
l.pack(fill="both",expand="yes")

Label(l,text="Parametres d'authentification")
label1 = Label(l, text="Nom d'utilisateur")
label2 = Label(l, text="Mot de passe")

label1.grid(row=0)
label2.grid(row=1)

Entry(l).grid(row=0, column=1)
Entry(l).grid(row=1, column=1)


app.mainloop()
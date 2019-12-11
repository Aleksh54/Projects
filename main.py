import tkinter
import tkinter.messagebox
from tkinter import Label
#from tkinter import *

# Appel de l'application et paramètres généraux

app = tkinter.Tk()
app.title("Outil de calculs financiers et fonctions avancées")
app.minsize(640, 480)
app.maxsize(1280,720)
app.resizable(width=False, height=False)
app.geometry('800x600')

# Création du menu et Paramètrage de fenêtres
mainmenu = tkinter.Menu(app)

first_menu = tkinter.Menu(mainmenu)
first_menu.add_command(label="Enregistrer")
first_menu.add_command(label="Ouvrir")
first_menu.add_command(label="Imprimer")
first_menu.add_command(label="Quitter", command=app.quit)

second_menu = tkinter.Menu(app)
second_menu.add_command(label="Capitalisation")
second_menu.add_command(label="Actualisation")
second_menu.add_command(label="Séquence de flux")

third_menu = tkinter.Menu(app)
third_menu.add_command(label="A propos")
third_menu.add_command(label="Documentation")
third_menu.add_command(label="Rappels Mathématiques")

mainmenu.add_cascade(label="Fichier", menu=first_menu)
mainmenu.add_cascade(label="Outils", menu=second_menu)
mainmenu.add_cascade(label="Autres", menu=third_menu)

# Boucle
app.config(menu=mainmenu)
app.mainloop()



#1-Importer les biblioteques
import tkinter as tk
from tkinter import messagebox

#2-Une fenetre avec le titre
window = tk.Tk()

window.title("TIC-TAC-TOE")

window.geometry("500x500")

window.mainloop()

#3-Définir la liste
chiffres = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#4- Initialiser la variable
mark = ''

#5- la variable de comptage
count = 0

#6- Liste appelée panneau avec 10 elements
panneaux = ['panneau', 1, 2, 3, 4, 5, 6, 7, 8, 9]



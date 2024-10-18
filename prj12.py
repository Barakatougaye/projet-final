#1-Importer les biblioteques
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")


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

#7- Vérification de l'état de la case du plateau
def win(mark):
    # Exemple de conditions de victoire pour un jeu Tic-Tac-Toe
    winning_combinations = [
        [1, 2, 3],  # Ligne 1
        [4, 5, 6],  # Ligne 2
        [7, 8, 9],  # Ligne 3
        [1, 4, 7],  # Colonne 1
        [2, 5, 8],  # Colonne 2
        [3, 6, 9],  # Colonne 3
        [1, 5, 9],  # Diagonale
        [3, 5, 7]   # Diagonale
    ]
    return any(all(panneaux[pos] == mark for pos in combo) for combo in winning_combinations)


#8-
def verifier(chiffre, bouton):
    # Déclarer les variables globales
    global count, mark, chiffres, panneaux
    
    # Vérification de l'état de la case du plateau
    if chiffre in chiffres:
        # Mettre à jour le plateau de jeu
        panneaux[chiffre] = mark  
        
        # Supprimer le chiffre de la liste des chiffres disponibles
        chiffres.remove(chiffre)

        # Mettre à jour le bouton avec la marque actuelle
        bouton.config(text=mark)  

        # Incrémenter le compteur des mouvements
        count += 1

        # Déterminer la note du joueur actuel
        if count % 2 == 0:
            mark = 'O' 
            print("C'est au tour de O.")
        else:
            mark = 'X' 
            print("C'est au tour de X.")
        
        
        # Vérification du gagnant
        if win(mark):
            print(f"Le joueur {1 if mark == 'X' else 2} gagne !")
            # Afficher un message d'information
            tk.messagebox.showinfo("Fin du jeu", f"Le joueur {1 if mark == 'X' else 2} gagne !")
            root.destroy()  # Détruire la fenêtre de jeu
        
        # Vérification de l'égalité
        if count > 8:  
            print("Match à égalité.")
            # Afficher un message d'information
            tk.messagebox.showinfo("Fin du jeu", "Match à égalité.")
            root.destroy()  # Détruire la fenêtre de jeu
    else:
        print("Sélection invalide.")



import tkinter

compteur = 0

def onClickBouton(event):
    global compteur, monLabel
    compteur = compteur + 1
    monLabel.config(text='Compteur : ' + str(compteur))

maFenetre = tkinter.Tk()

monBouton = tkinter.Button(maFenetre, text='Clique ici !', width=50)
monBouton.pack()
monBouton.bind('<ButtonRelease-1>', onClickBouton)

monLabel = tkinter.Label(maFenetre, text='Compteur : 0')
monLabel.pack()

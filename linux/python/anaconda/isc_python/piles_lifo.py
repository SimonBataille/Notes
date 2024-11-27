'''
on utilise des listes pour les piles
'''

class Pile:
    def __init__(self):
        self.taille = 0
        self.valeurs = []

    def empile(self, val):
        self.taille += 1
        self.valeurs.append(val)

    def depile(self):
        if self.taille > 0:
            self.taille -= 1
            return self.valeurs.pop()

    def isVide(self):
         return self.taille == 0

    def __str__(self):
        return str(self.valeurs)

maPile = Pile()

maPile.empile(1)
maPile.empile(2)
maPile.empile(3)
maPile.empile(4)
maPile.empile(5)

print(maPile)
print('Vide ? : ' + str(maPile.isVide()))
print('Depile : ' + str(maPile.depile()))
print(maPile)

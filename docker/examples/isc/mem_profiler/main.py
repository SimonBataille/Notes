from memory_profiler import profile

@profile
def somme_liste(n):
    liste = [i for i in range(n)]
    return sum(liste)

@profile
def somme_generateur(n):
    generateur = (i for i in range(n))
    return sum(generateur)

n = 1000000
print('Calcul liste : ')#memory increases continuously because the list is stored in memory
somme_liste(n)
print('Calcul generateur : ')#more memory at start and then no increase
somme_generateur(n)
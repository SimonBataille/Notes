x = 5  # Variable globale

def modifier_x():
    global x  # Nécessaire pour modifier la valeur globale
    x += 1

def pas_besoin_global():
    print(x)  # Pas besoin de 'global' si on lit seulement la valeur globale

obj = [1, 2, 3]  # Objet global (une liste)

def modifier_obj():
    obj.append(4)  # Pas besoin de 'global', car on modifie l'objet et non la variable

def changer_obj():
    global obj  # Nécessaire pour réassigner la variable globale
    obj = [5, 6, 7]

modifier_x()
print(x)  # 6

modifier_obj()
print(obj)  # [1, 2, 3, 4]

changer_obj()
print(obj)  # [5, 6, 7]

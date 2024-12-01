import random

def get_recompense(numero_porte):
    if numero_porte == 1:
        return 1 if random.random() < 0.3 else 0
    if numero_porte == 2:
        return 1 if random.random() < 0.7 else 0


recompense_1 = 0
recompense_2 = 0

for _ in range(100):
    
    choix = random.choice([1, 2])

    if choix == 1:
      recompense_1 += get_recompense(1)
    if choix == 2:
      recompense_2 += get_recompense(2)

print(str('Recompense 1 : ' + str(recompense_1)))
print(str('Recompense 2 : ' + str(recompense_2)))

if recompense_1 > recompense_2:
    print('Il faut choisir la porte 1')
else:
    print('Il faut choisir la porte 2')

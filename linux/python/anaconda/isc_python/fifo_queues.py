'''
on utilise les listes chaînées pour les files
'''

from queue import *

file = Queue(5)
print(type(file))
print(dir(file))

file.put(1)
file.put(2)
file.put(3)
file.put(4)
file.put(5)

print('Vide ? : ' + str(file.empty()))

print(file.get())
print(file.get())
print(file.get())
print(file.get())
print(file.get())

print('Vide ? : ' + str(file.empty()))

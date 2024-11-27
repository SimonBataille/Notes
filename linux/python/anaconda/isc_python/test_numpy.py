import numpy as np
import timeit as tm

''' TESTS
a=np.array([1,2,3])
print(a)

a=np.zeros(10)
print(a)

a=np.zeros(10, int)
print(a)

a=np.ones(10)
print(a)

a=np.ones(10, int)
print(a)

a=np.random.randint(0, 100, (3,3))
print(a)
print(a[0])
print(a[0,0])
a[0,2] = 100
print(a)
print(a.ndim)
print(a.size)
print(a.shape)
print(a.dtype)
'''

TAILLE=2000

z=np.random.randint(0, 100, (TAILLE,TAILLE))

# Without np
starttime=tm.default_timer()
somme = 0
for x in range(0, TAILLE-1):
    for y in range(0, TAILLE-1):
        somme += z[x,y]
        
print('Somme1 : ' + str(somme))
print('TPS1 = ', tm.default_timer()-starttime)

# With np
starttime=tm.default_timer()

print('Somme2 : ', z.sum())
print('TPS2 = ', tm.default_timer()-starttime)













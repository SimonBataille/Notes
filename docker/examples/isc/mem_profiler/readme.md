# Python

`pip install memory-profiler`
`mprof run main.py` : watch how memory is used

`pip install matplotlib`
`pip install PyQt5`
`mprof plot`

# output
'''
mprof run main.py 
mprof: Sampling memory every 0.1s
running new process
running as a Python program...
Calcul liste : 
Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     3     22.9 MiB     22.9 MiB           1   @profile
     4                                         def somme_liste(n):
     5     61.1 MiB     38.2 MiB     1000001       liste = [i for i in range(n)]
     6     61.1 MiB      0.0 MiB           1       return sum(liste)


Calcul generateur : 
Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     8     23.9 MiB     23.9 MiB           1   @profile
     9                                         def somme_generateur(n):
    10     23.9 MiB      0.0 MiB     2000003       generateur = (i for i in range(n))
    11     23.9 MiB      0.0 MiB           1       return sum(generateur)
'''
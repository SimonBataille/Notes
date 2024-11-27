def factorielle(n):
    facto = n
    while n > 1:
        n = n - 1
        facto = facto * n
    return facto

def fact_rec(n):
    if (n>1):
        return n * fact_rec(n-1)
    else:
        return 1

nombre = 30

print(str(nombre) + '!=' + str(factorielle(nombre)))
print(str(nombre) + '!=' + str(fact_rec(nombre)))

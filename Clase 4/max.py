lista = [1,3,6,1,87,123,1,32]

aux = lista[0]
for x in lista:
    if x > aux:
        aux = x

print(aux)



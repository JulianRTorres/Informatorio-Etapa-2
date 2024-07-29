from functools import reduce

# inmutable
tupla = [1, 2, 3, 4, 5]

suma = sum(tupla)
longitud = len(tupla)
maximo = max(tupla)
minimo = min(tupla)
ordenar = sorted(tupla)
reversa = list(reversed(tupla)) #tupla[::-1]
enumerar = list(enumerate(tupla))
mapear = list(map(lambda x: x + 1, tupla))
mapRed = reduce(lambda x, y: x + y, tupla)
filtrado = list(filter(lambda x: x % 2 == 0, tupla))

print("suma: ", suma)
print("longitud: ", longitud)
print("maximo: ", maximo)
print("minimo: ", minimo)
print("ordenado: ", ordenar)
print("reversa: ", reversa)
print("enumerar: ", enumerar)
print("mapear: ", mapear)
print("mapRed: ", mapRed)
print("filtrado: ", filtrado)


# any() all()
tupla = (True, True, True, True)

any_list = any(tupla) # Verifica que aunque sea 1 elemento está en True
print("Any: ", any_list)

all_list = all(tupla) # Verifica que todos los elementos esten en True
print("All: ", all_list) # >=, <=, !=, >, <, or, xor, and, not

# zip()
tupla_1 = [1,2,3]
tupla_2 = ['a','b','c']

tupla_cpx = tuple(zip(tupla_1, tupla_2))
print(tupla_cpx)

# insert() remove() append() pop() count()
tupla = (1,2,3,4,5)
lista = list(tupla)
lista.insert(0, 38)
tupla = tuple(tupla)
print(tupla)

tupla.remove(3)
print(tupla)

tupla.append(333)
print(tupla)

tupla.pop()
print(tupla)

ocurrencias = tupla.count(4)
print(ocurrencias)
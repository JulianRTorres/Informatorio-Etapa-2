# enteros
entero = 543
print(entero)

# float - decimal
decimal = 0.43
print(decimal)


# string
cadena = "info 2024-07-11"
cadena1 = 'info 2024-07-11'
cadena2 = """DOCSTRING"""
cadena3 = '''DOCSTRING'''
print(cadena)

# boolean
verdadero = True
falso = False
print(verdadero)
print(falso)

# vacio, null, nulo, none, nill
vacio = None
print(vacio)

# funcion type(), que tipo de dato tiene dentro
print(type(vacio))

## Tipos de datos estructurados/complejos
# list --> Mutables
lista = [1,2,3,4,5,6,7,8, "algo"] # 9 elementos. Indice empieza en 0(0=1).
print(lista)
print(lista[3])
lista_lista = [[3,2,1], [7,6,5], [10,11,13]]
lista_lista.append(2)
print(lista_lista)
lista_lista[3] = 365
print(lista_lista)

# tuplas --> Inmutable
tuplas = (1,2,3,4,5,6)
print(tuplas[2])

# set-conjunto 1,2,3, --> No puede tener datos repetidos --> Mutables
conjuntos = {1,2,3,4,5,6,7,8,9,'123','123','123'}
print(conjuntos)

# diccionarios, map, clave valor, key-value --> Mutables
capitales = {'Chaco':['Resistencia', 'Fontana', 'Barranqueras'], 'Corrientes':'Corrientes', 'Misiones':'Posadas'} 
print(capitales['Chaco'])

# definidos por el progamador, librerias, dataframe(df)
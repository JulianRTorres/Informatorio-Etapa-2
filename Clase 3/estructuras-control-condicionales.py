# condicionales
# >, <, ==, <=, >=, !=
maximo = 10
minimo = 1
## condicional simple
if (maximo < minimo): # operador de comparacion
    print("cumplio la condición")

## condicional alternativo
if (maximo < minimo): # operador de comparacion
    print("Condicional alternativo: Cumplio la condición")
else:
    print("Condicional alternativo: No cumplio la condición")

## condicional multiple
opcion = 5
if (opcion == 1): # operador de comparacion
    print("opcion: 1")
elif (opcion == 2):
    print("opcion: 2")
elif (opcion == 3):
    print("opcion: 3")
else:
    print("No se cumplio ninguna de las opciones")
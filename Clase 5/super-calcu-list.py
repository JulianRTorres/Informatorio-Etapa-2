# Calculadora
# opciones
# 1 - Sumar todos los elementos de una lista
# 2 - Encontrar el máximo
# 3 - Encontrar el mínimo
# 4 - Filtrar por pares
# 5 - Filtrar por impares
## Ingrese los valores de la lista por pantalla, y además, lista puede tener cualquier tamaño.
# input() para ingresar valores por pantalla

lista = []
condicion = 'si'
while condicion == 'si':
    numero = (input("Ingresar valor para la lista: "))
    numero = int(numero)
    lista.append(numero)
    condicion = input("Desea seguir cargando valores? (si/no)")

print("Su lista cargada es la siguiente:", lista)

opcion = None
while opcion != 0:
    # Seleccion de operación de realizar.
    print(f'''
    0 - Si desea salir del programa      
    1 - Sumar todos los elementos de una lista
    2 - Encontrar el maximo
    3 - Encontrar el minimo
    4 - Filtrar por pares
    5 - Filtrar por impares
    ''')
    opcion = int(input("Por favor ingrese una opción: "))

    if opcion == 1:
        suma = sum(lista)
        print(suma)
    elif opcion == 2:
        maximo = max(lista)
        print(maximo)
    elif opcion == 3:
        minimo = min(lista)
        print(minimo)
    elif opcion == 4:
        filtradPar = list(filter(lambda x: x % 2 == 0, lista))
        print(filtradPar)
    elif opcion == 5:
        filtradoImpar = list(filter(lambda x: x % 2 != 0, lista))
    else:
        print('Su opcion ingresada no está definida dentro de los limites de las opciones')
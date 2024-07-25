# Input("") permite al usuario ingresar un valor por consola
# Consigna
# A partir de un string ingresado por consola
# determinar si dicho string es palindromo
# Palindromo: alreves y normal se escriben igual, neuquen, jojo
cadena = input("Ingrese una cadena de texto:")
print("Esta es una cadena", cadena)

cadena_invertida = cadena[::-1]

if (cadena_invertida == cadena):
    print("es palindromo")

else:
    print("no es palindromo)")

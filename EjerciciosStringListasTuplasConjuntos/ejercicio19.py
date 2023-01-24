'''
Crea un programa en el que el usuario introduzca una frase y una tabla de cifrado, es decir, una serie de
caracteres y los correspondientes sustitutos, que se guardarán en un diccionario. El programa deberá cifrar
la frase utilizando la tabla de cifrado, es decir, para cada carácter de la frase, buscará dicho carácter en el
diccionario para reemplazarlo en la frase por su sustituto.
'''

# Generamos el diccionario para cifrar

tabla = {}
caracteres = input('Introduce el carácter a cifrar y el carácter asociado separados por espacio (o nada para acabar): ')
while caracteres != '':
    a,b = caracteres.split(' ')
    tabla[a] = b
    caracteres = input('Introduce el carácter a cifrar y el carácter asociado separados por espacio (o nada para acabar): ')



# Vamos pidiendo frases y las vamos cifrando

frase = input('Introduce una frase (o nada para acabar): ')
while frase != '':
    frase2 = ''
    for c in frase:
        if c in tabla:
            frase2 = frase2 + tabla[c]
        else:
            frase2 = frase2 + c
    print('La frase cifrada es:', frase2)

    frase = input('Introduce una frase (o nada para acabar): ')

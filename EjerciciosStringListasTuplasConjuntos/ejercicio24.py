'''
En el juego del tres en raya (gato) dos jugadores se turnan para colocar sus piezas, de una en una, sobre
un tablero o matriz 3×3: Escribe un programa que pida dónde introducir la siguiente ficha, una X,
comprobando que las coordenadas sean de una casilla vacía y que compruebe si dicha pieza introducida
genera un tres en raya, bien sea horizontal, vertical, o diagonal.
'''

# a) Inicializar el tablero

M = [ [' ', 'O', ' '],
      [' ', ' ', 'O'],
      ['X', 'X', ' '] ]



# b) imprimir el tablero

print(M[0][0], M[0][1], M[0][2], sep=' | ')
print('--+---+--')
print(M[1][0], M[1][1], M[1][2], sep=' | ')
print('--+---+--')
print(M[2][0], M[2][1], M[2][2], sep=' | ')
print()



# c) Pedir la posición de la nueva X

while True:
    f = int( input('¿En qué fila quieres la nueva ficha? ') )
    c = int( input('¿En qué columna quieres la nueva ficha? ') )
    if (0 <= f <= 2) and (0 <= c <= 2):
        if M[f][c] == ' ':
            M[f][c] = 'X'
            break
        else:
            print('Casilla ocupada')
    else:
        print('Coordenadas incorrectas')
    print('Prueba de nuevo')



# d) Buscar tres en raya a partir de la posición f y c

if M[f][0] == M[f][1] == M[f][2]:
    print('¡¡¡Tres en raya horizontal!!!')

elif M[0][c] == M[1][c] == M[2][c]:
    print('¡¡¡Tres en raya vertical!!!')

elif f==c and (M[0][0] == M[1][1] == M[2][2]):
    print('¡¡¡Tres en raya diagonal!!!')

elif f+c==2 and (M[0][2] == M[1][1] == M[2][0]):
    print('¡¡¡Tres en raya diagonal inversa!!!')

else:
    print('¡¡¡Todavía no hay tres en raya!!!')

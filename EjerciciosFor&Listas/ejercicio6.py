#Análisis
#Entrada: Una cantidad indeterminada de valores enteros que representan número de celulares
#Salida: Una cantidad indeterminada de mensajes, uno por cada celular ingresado que indica
#el nombre del propietario ocontacto desconocido
#Constantes: fin dato (0), 5 números celulares, 5 nombres, celular mínimo, celular máximo.
#Diseño
#Crear Listas
#Solicitar un número de celular y validarlo
#Mientras número celular sea distinto de fin de dato
#flag = 0
#Para elemneto en la listas
#Si elemento lista celular es igual número celular ingresado
#mostrar elemento lista nombres
#flag = 1
#Si flag es igual a cero
#Mostar Contacto Desconocido
#Solicitar otro número de celular y validarlo

FINDATO = 0
MINCELU = 10000000
MAXCELU = 99999999
lista_celulares = [98989898, 67676767, 54545454, 32323232]
lista_nombres = ["PEDRO", "MARÍA", "JUAN", "SARA"]
celular = int(input("Ingrese número de celular entre {0:d} y {1:d} ({2:d} Finalizar): ".format(MINCELU,MAXCELU,FINDATO)))
while (celular < MINCELU or celular > MAXCELU) and (celular != FINDATO):
    celular = int(input("Error, debe estar entre {0:d} y {1:d} ({2:d} Finalizar): ".format(MINCELU,MAXCELU,FINDATO)))
while celular != FINDATO:
    flag = 0
    for i in range(4):
        if celular == lista_celulares[i]:
            print("Este número pertenece a: ", lista_nombres[i])
            flag = 1
    if flag == 0:
        print("Contacto Desconocido!!")
    celular = int(input("Ingrese otro número de celular entre {0:d} y {1:d} ({2:d} Finalizar):".format(MINCELU,MAXCELU,FINDATO)))
    while (celular < MINCELU or celular > MAXCELU) and (celular != FINDATO):
        celular = int(input("Error, debe estar entre {0:d} y {1:d} ({2:d} Finalizar): ".format(MINCELU,MAXCELU,FINDATO)))
import random

from random import choice
while Eleccion1!="FIN":
    print ("Juego piedra, papel o tijera.")

    
    #puntuaciones = 0
    
    Opciones = ['Piedra', 'Papel', 'Tijera'] 

    #Maquina = (choice((Opciones)))

    Eleccion1 = input("Jugador1 Seleccione Piedra, Papel o Tijera: ")
    Eleccion2 = input("Jugador2 Seleccione Piedra, Papel o Tijera: ")
    if Eleccion not in Opciones:
        print ("Seleccione una opción válida")
    
    if Eleccion1 == Eleccion2:
        #puntuaciones = 0
        print("Empate")

    if (Eleccion1 == 'Piedra'):
        if (Eleccion2 == 'Papel'):
            
            print("Jugador 1:PIEDRA v/s Jugador 2:PAPEL -> el papel cubre la piedra, gana el jugador 2")
        elif (Eleccion2 == 'Tijera'):
            
            print("Jugador 1:PIEDRA v/s Jugador 2:TIJERA -> piedra rompe tijera, gana el jugador 1")

    if (Eleccion1 == 'Papel'):
        if (Eleccion2 == 'Tijera'):
            
            print("P")
        elif (Eleccion2 == 'Piedra'):
            
            print("Ganaste")

    if (Eleccion1 == 'Tijera'):
        if (Eleccion2 == 'Piedra'):
            
            print("p1")
        elif (Eleccion2 == 'Papel'):
            puntuaciones = 1
            print("p2")

    return puntuaciones

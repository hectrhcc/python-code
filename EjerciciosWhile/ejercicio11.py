Eleccion1=""
while Eleccion1!="FIN" and Eleccion1!="fin" and Eleccion1!="Fin": 
    print ("JUEGO PIEDRA, PAPEL Y TIJERA")
    Opciones = ('Piedra', 'Papel', 'Tijera')
    Eleccion1 = input("Jugador1> Seleccione Piedra, Papel o Tijera: ")
    if Eleccion1=="FIN" or Eleccion1=="fin" or Eleccion1=="Fin":
        break
    Eleccion2 = input("Jugador2> Seleccione Piedra, Papel o Tijera: ")
    
    if Eleccion1 and Eleccion2 not in Opciones:
        print ("Seleccione una opción válida")
    
    if Eleccion1 == Eleccion2:
        print("Empate")

    if (Eleccion1 == 'Piedra'):
        if (Eleccion2 == 'Papel'):
            
            print("Jugador 1:PIEDRA v/s Jugador 2:PAPEL -> el papel cubre la piedra, gana el jugador 2")
        elif (Eleccion2 == 'Tijera'):
            
            print("Jugador 1:PIEDRA v/s Jugador 2:TIJERA -> piedra rompe tijera, gana el jugador 1")

    if (Eleccion1 == 'Papel'):
        if (Eleccion2 == 'Tijera'):
            
            print("Jugador 1:PAPEL v/s Jugador 2:TIJERA -> la tijera corta el papel, gana el jugador 2")
        elif (Eleccion2 == 'Piedra'):
            
            print("Jugador 1:PAPEL v/s Jugador 2:PIEDRA -> el papel cubre la piedra, gana el jugador 1")

    if (Eleccion1 == 'Tijera'):
        if (Eleccion2 == 'Piedra'):
            
            print("Jugador 1:TIJERA v/s Jugador 2:PIEDRA ->  piedra rompe tijera, gana el jugador 2")
        elif (Eleccion2 == 'Papel'):
        
            print("Jugador 1:TIJERA v/s Jugador 2:PAPEL -> la tijera corta el papel, gana el jugador 1")
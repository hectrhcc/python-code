import random
#ingreso de resultados
#partido de ida
print("Ingrese resultado partido de ida entre equipo A y equipo B:")
equipo_a_cant_gol_i = int(input("Ingrese la cantidad de goles de equipo A:"))
equipo_b_cant_gol_i = int(input("Ingrese la cantidad de goles de equipo B:"))
puntos_equipo_a=0
puntos_equipo_b=0
if equipo_a_cant_gol_i == equipo_b_cant_gol_i: #empate 
    puntos_equipo_a+=1 #
    puntos_equipo_b+=1
elif equipo_a_cant_gol_i> equipo_b_cant_gol_i: #gano a
    puntos_equipo_a+=3 
    puntos_equipo_b+=0
else: #gano b
    puntos_equipo_a+=0 
    puntos_equipo_b+=3     
#goles_a_favor = int(input(Ingrese goles a favor equipo A:)) No es necesario
goles_favor_a_i = equipo_a_cant_gol_i
goles_contra_a_i = equipo_b_cant_gol_i
goles_favor_b_i = equipo_b_cant_gol_i
goles_contra_b_i = equipo_a_cant_gol_i
dif_goles_a_i = goles_favor_a_i - goles_contra_a_i
dif_goles_b_i = goles_favor_b_i - goles_contra_b_i
goles_visita_a = equipo_a_cant_gol_i
#partido de vuelta
print("Ingrese resultado partido de vuelta entre equipo A y equipo B:")
equipo_a_cant_gol_v = int(input("Ingrese la cantidad de goles de equipo A:"))
equipo_b_cant_gol_v = int(input("Ingrese la cantidad de goles de equipo B:"))
if equipo_a_cant_gol_v == equipo_b_cant_gol_v: #empate 
    puntos_equipo_a+=1 
    puntos_equipo_b+=1
elif equipo_a_cant_gol_v> equipo_b_cant_gol_v: #gano a
    puntos_equipo_a+=3 
    puntos_equipo_b+=0
else: #gano b
    puntos_equipo_a+=0 
    puntos_equipo_b+=3
goles_favor_a_v = equipo_a_cant_gol_v
goles_contra_a_v = equipo_b_cant_gol_v
goles_favor_b_v = equipo_b_cant_gol_v
goles_contra_b_v = equipo_a_cant_gol_v
dif_goles_a_v = goles_favor_a_v - goles_contra_a_v
dif_goles_b_v = goles_favor_b_v - goles_contra_b_v
goles_visita_b = equipo_b_cant_gol_v
if puntos_equipo_a > puntos_equipo_b:
    RAZON = "Puntos"
    equipo_de_futbol = "equipo A"
elif puntos_equipo_a == puntos_equipo_b:
     dif_goles_a = dif_goles_a_i + dif_goles_a_v 
     dif_goles_b = dif_goles_b_i + dif_goles_b_v
     if dif_goles_a > dif_goles_b:
        RAZON= "Diferencia de goles"
        equipo_de_futbol = "equipo A"
     elif dif_goles_a == dif_goles_b:
          if goles_visita_a > goles_visita_b:
                RAZON= "Goles visita"
                equipo_de_futbol = "equipo A"
          elif goles_visita_a == goles_visita_b:
                RAZON= "Sorteo"
                sorteo = random.randrange(0,2)
                if sorteo == 0:
                    equipo_de_futbol = "equipo A"
                else:
                    equipo_de_futbol = "equipo B"
          else:
                RAZON= "Goles visita"
                equipo_de_futbol = "equipo B"
     else:
        RAZON= "Diferencia de goles"
        equipo_de_futbol = "equipo B"
else:
    RAZON = "Puntos"
    equipo_de_futbol = "equipo B"

print("El equipo de futbol que pasa a la siguiente ronda es: ",equipo_de_futbol)
print("La razón por la cual paso es:",RAZON)
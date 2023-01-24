print("Este programa mezcla dos colores.")
print("  r. Rojo      a. Azul")
primera = input("  Elija un color (r o a): ")
if primera == "r":
    print("  a. Azul      v. Verde")
    segunda = input("  Elija otro color (a o v): ")
    if segunda == "a":
        print("La mezcla de Rojo y Azul produce Magenta.")
    else:
        print("La mezcla Rojo y Verde produce Amarillo.")
else:
    print("  v. Verde    r. Rojo")
    segunda = input("  Elija otro color (v o r): ")
    if segunda == "v":
        print("La mezcla de Azul y Verde produce Cian.")
    else:
        print("La mezcla Azul y Rojo produce Magenta.")
print("¡Hasta la próxima!")
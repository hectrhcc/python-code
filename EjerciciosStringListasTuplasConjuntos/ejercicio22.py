'''
Crea un programa que dado un número introducido en una base cualquiera b1 sea capaz de convertirlo a
otra base cualquiera b2. Como nos vemos limitados a la hora de trabajar con bases por la cantidad de
símbolos de que disponemos, utilizaremos los símbolos 0,1, ..., 9, A, B, ..., Z pudiendo trabajar así con
bases hasta la base 36. El procedimiento puede ser el siguiente:
a. Pedimos las dos bases b1 y b2.
b. Leemos el número en base b1 y lo convertimos a base 10 mediante el método de las potencias
sucesivas.
c. Convertimos el número de base 10 a base b2 mediante el método de las divisiones sucesivas.

Las variables:


  MAX_DECIMALES        # Máximo número de decimales en el resultado
  cifras               # Símbolos de todas las bases
  num1                 # Cadena con el número a cambiar de base
  num2                 # Cadena con el número cambiado de base
  pos_punto            # Posición del punto decimal en num1
  correcto             # Booleano que indica si num1 es correcto
  num10int             # Número num1 en base 10, parte entera
  num10frc             # Número num1 en base 10, parte decimal
'''



MAX_DECIMALES = 6

cifras = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Leemos la base inicial

base1 = 0;
while (base1 < 2) or (base1 > len(cifras)):
    base1 = int( input('Introduce la primera base : ') )

# Leemos la base final

base2 = 0;
while (base2 < 2) or (base2 > len(cifras)):
    base2 = int( input('Introduce la segunda base : ') )

# Leemos el número y comprobamos que pertenezca a la primera base:
#  - Los símbolos han de ser de la primera base
#  - Puede aparecer 0 ó 1 puntos decimales, pero no más
# Al mismo tiempo calculamos la parte entera y decimal del número en base 10 

correcto = False
while not correcto:

    num1 = input('Introduzca el número a cambiar de base : ')

    # Variable que indica si num1 tiene los dígitos dentro de su base y no más de un punto decimal 
    correcto = True

    # Variable que indica si hemos encontrado el punto decimal en num1
    punto = False

    # Variables que contendrán la parte entera y decimal de num1, en base 10
    num10int = 0
    num10frc = 0.0
    pot_frac = base1

    for c in num1:
        if c == '.':
            # Comprobamos que no tenga dos puntos decimales
            if punto:
                correcto = False
                break
            else:
                punto = True
        else:
            # Buscamos la cifra actual en el vector de cifras
            j = cifras.find(c.upper())
            if (j < 0) or (j >= base1):
                correcto = False
                break
            else:
                if punto:
                    num10frc = num10frc + j/pot_frac
                    pot_frac = pot_frac * base1
                else:
                    num10int = num10int*base1 + j

print('El número en base 10 es', num10int + num10frc)



# Pasamos la parte entera de base 10 a la segunda base mediante divisiones sucesivas

num2 = ''

while num10int > 0:
    num2 = cifras[ num10int % base2 ] + num2
    num10int = num10int // base2

# Pasamos la parte fraccionaria de base 10 a la segunda base mediante multiplicaciones sucesivas

if num10frc != 0.0:
    num2 = num2 + '.'
    while (num10frc != 0.0) and (MAX_DECIMALES > 0):
        num10frc = num10frc * base2
        num2 = num2 + cifras[ int(num10frc) ]            # parte entera
        num10frc = num10frc - int(num10frc)              # parte fracc.
        MAX_DECIMALES = MAX_DECIMALES - 1

# Imprimimos el resultado

print('El número en base', base2, 'es', num2)

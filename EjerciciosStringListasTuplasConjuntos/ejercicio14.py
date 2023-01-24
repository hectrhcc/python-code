'''
Crea un programa que almacene en una lista la nota de los alumnos de Taller de Programación I, y
posteriormente calcule y visualice el número de notas que aparecen dentro de los siguientes intervalos:
[1 , 3]: Muy Mal, [3.1, 3.9]: Mal , [4, 5]: Suficiente, [5.1, 5.9]: Bien , [6, 7]: Muy Bien.
'''

MAX_GRUPO = 30

# Pedimos cuantos alumnos tiene el grupo

num = int( input('¿Cuántos alumnos tiene el grupo? ') )
while num < 1 or num > MAX_GRUPO:
    print('Valor incorrecto. Debe estar entre 1 y', MAX_GRUPO)
    num = int( input('¿Cuántos alumnos tiene el grupo? ') )

# Leemos las notas de todos los alumnos

notas = []

for i in range(num):
    x = int( input(f'¿Qué valor para la nota del alumno {i+1}? ') )
    while x < 1 or x > 7:
        print('Valor incorrecto. Debe estar entre 1 y 7.')
        x = int( input(f'¿Qué valor para la nota del alumno {i+1}? ') )
    notas.append( x )

# Contamos el número de muy mal, mal, suficiente, bien  y muy bien

muymal = 0
mal = 0
suficiente = 0
bien = 0
muybien = 0

for e in notas:
    if e>=1 and e<= 3:
        muymal = muymal +1
    elif e>=3.1 and e<=3.9 :
        mal = mal + 1
    elif e>=4 and e<=5:
        suficiente =suficiente + 1
    elif e>=5.1 and e<=5.9:
        bien = bien +1
    else:
        muybien = muybien +1

    
print(f'Hay {muymal} muy mal, {mal} mal, {suficiente} suficientes, {bien} bien y {muybien} muy bien')


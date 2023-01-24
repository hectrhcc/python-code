'''
Aparte de haber creado infinidad de superhéroes, Stan Lee es recordado por los cameos cinematográficos
que hizo en multitud de películas y series. Quizá por estar más escondidos, son menos conocidos sus
cameos en los comics de los que era autor. Por ejemplo, en una determinada viñeta podía leerse “¡Que me
diga dónde están, le exijo!”. Algunas veces se camuflaba más, partiendo su nombre con letras arbitrarias,
como en “Salta, no le temas”. Crea un programa que dado un texto y un “cameo” a buscar, sea capaz de
encontrar el número de veces que dicho cameo aparece en el texto, sin tener en cuenta las mayúsculas, y
con la posibilidad de que las letras originales estén separadas. Antes de empezar a buscar el cameo una
segunda vez, tiene que haber terminado de aparecer la primera. Por ejemplo, el cameo “Stan Lee”
aparecería dos veces en “Eres tanlento que te ganaria una oruga. ¿Esto es canela, verdad que si?”, pero
cero veces en “¿Dónde estarían los coches?”.

'''
cameo = input('Cameo a buscar: ')
texto = input('Texto donde buscar: ')

apariciones = 0
subrayado = ''

# Vamos a recorrer el texto donde buscar.
# Cada vez que aparece un carácter del cameo, avanzo el índice del cameo.
# Cuando llego al final del cameo, incremento las apariciones, y vuelvo 
# a la primera letra del cameo. 

i = 0
for c in texto:
    if c.upper() == cameo[i].upper():
        subrayado = subrayado + '^'
        i = i + 1
        if i == len(cameo):
            apariciones = apariciones + 1
            i = 0
    else:
        subrayado = subrayado + ' '

print(texto, ':', apariciones)
print(subrayado)

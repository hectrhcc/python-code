#Crea un programa en el que el usuario introduzca una palabra o frase y el programa diga si es palíndromo,
#es decir, si se lee igual hacia delante que hacia atrás. Por ejemplo “amor a roma” y “ojo” son palíndromos.


frase = input('Introduce una frase: ')

i = 0
j = len(frase) - 1
palin = True

while (i < j) and palin:    
    palin = palin and (frase[i] == frase[j])
    i += 1
    j -= 1

if palin:
    print('La frase es palindroma')
else:
    print('La frase no es palindroma')



# Otra manera de resolver el problema es invertir la frase
# y comparar si el original es igual a la invertida

frase2 = ''
for c in frase:
    frase2 = c + frase2

if frase == frase2:
    print('La frase es palindroma')
else:
    print('La frase no es palindroma')

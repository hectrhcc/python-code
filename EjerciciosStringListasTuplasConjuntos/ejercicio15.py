#Crea un programa en el que el usuario introduzca un número y el programa genere una frase con las
#palabras correspondientes a cada cifra. Por ejemplo, 547 devolvería “cinco cuatro siete”.

p = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']


# Primera manera: tenemos el número en un string y lo recorremos carácter a carácter 

n = input('dame número: ')
s = ''

for e in n:
    s = s + p[ int(e) ] + ' '
		
print(s)

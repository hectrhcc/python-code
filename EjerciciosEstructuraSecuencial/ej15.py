#Solicitar el valor temperatura grados Fahrenheit
#Restar 32 a los grados F
#dividir por 9 a lo anterior
#Multiplicar por 5 a lo anterior
#Mostrar la Temperatura en grados Celsius


Temp_F =float(input("Ingrese temperatura en grados Fahrenheit: "))

Temp_C = 5*((Temp_F-32)/9)

print("La temperatura en grados Celsius es: %.2f" %Temp_C)
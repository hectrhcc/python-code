#Escriba un algoritmo que solicite una temperatura en grados Fahrenheit
#y calcule el valor correspondiente
#a grados Celsius, utilizando la fórmula: C/5 = (F – 32)/9.


temp_f=float(input("Ingrese la temperatura en grados Fahrenheit: "))
temp_c = ((temp_f - 32)/9)*5
print("La temperatura en grados celsius es: %.2f"  %temp_c)
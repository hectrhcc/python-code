print("Ingrese un valor positivo:")
num1 = int (input())
print("Ingrese un valor positivo:")
num2 = int (input())
print("Ingrese un valor positivo:")
num3 = int (input())
print("Ingrese un valor positivo:")
num4 = int (input())
print("Ingrese un valor positivo:")
num5 = int (input())
prom_pares=0
prom_impar=0
contador_par =0
contador_impar =0
if num1<0  or num2<0 or num3<0 or num4<0 or num5 <0:
    print("Le dji que ingresara un numero positivo")
else:
    if num1 % 2 ==0:
        contador_par+=1
        prom_pares+= num1   
    else:
        contador_impar+=1
        prom_impar+=num1
        
    if num2 % 2 ==0:
        contador_par+=1
        prom_pares+= num2
    else:
        contador_impar+=1
        prom_impar+=num2
        
    if num3 % 2 ==0:
        contador_par+=1
        prom_pares+= num3   
    else:
        contador_impar+=1
        prom_impar+=num3
        
    if num4 % 2 ==0:
        contador_par+=1
        prom_pares+= num4   
    else:
        contador_impar+=1
        prom_impar+=num4
        
    if num5 % 2 ==0:
        contador_par+=1
        prom_pares+= num5
    else:
        contador_impar+=1
        prom_impar+=num5
        
    if contador_par ==0:
        promedio_impar = prom_impar/contador_impar  
        print("Promedio impares:", promedio_impar)
        print("No hay numeros pares")
    elif contador_impar ==0:
        promedio_par = prom_pares/contador_par
        print("Promedio pares:", promedio_par)
        print("No hay numeros impares")
    else:
        promedio_par = prom_pares/contador_par
        promedio_impar = prom_impar/contador_impar  
        print("Promedio pares:", promedio_par)
        print("Promedio impares:", promedio_impar)
    
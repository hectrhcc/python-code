num ="nada"
while num!=0:
    num = int(input("Ingrese un numero del 1 al 10:"))
    x = num
    if num>=1 and num<=10:
    #la tabla
        print(" x   x²   x³   x⁴    x⁵")
        while x:
            #print(x,x**2, x**3, x**4, x**5)
            print ('{0:2d} {1:3d} {2:4d} {3:5d} {4:6d} '.format(x, x*x, x*x*x, x*x*x*x,x*x*x*x*x))
            x-=1
    
    else:
        print("Solo ingrese un número del 1 al 10")
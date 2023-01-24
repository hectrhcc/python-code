a = float(input('Valor de a: '))

b = float(input('Valor de b: '))

c = float(input('Valor de c: '))

if a != 0:

    discriminante= b**2 - 4*a*c

    if discriminante >=0:

        x1 = (-b + (discriminante)**(1/2)) / (2 * a)

        x2 = (-b - (discriminante)**(1/2)) / (2 * a)

        if x1==x2:  #soluciones iguales

            print('La Solucion de la ecuacion es: x1=%4.3f'% x1)

        else:   #soluciones diferentes

            print('Soluciones de la ecuacion: x1=%4.3f y x2=%4.3f ' % (x1, x2))

    else:

        print('No Hay soluciones Reales. ')

else:

    if b != 0:

       x = -c / b

       print('Solucion de la ecuacion: x=%4.3f ' % x)

    else:

       if c != 0:

          print('La ecuacion no tiene solucion. ')

       else:

          print('La ecuacion tiene infinitas soluciones. ')
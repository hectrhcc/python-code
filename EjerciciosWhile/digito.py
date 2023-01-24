print("ingrese un numero")
number=int(input())
while number:
    digit = number % 10

    # do whatever with digit

    # remove last digit from number (as integer)
    number //= 10
    #print("number", number)
    print("digito", digit)
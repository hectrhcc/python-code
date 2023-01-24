# Python3 program to demonstrate 
# octal type conversion 
  
# Function returns the octal representation 
# of the value passed as parameters. 'number' 
# is floating point decimal number and 'places' 
# is the number of decimal places 
def float_octal(number, places = 3): 
  
    # split() separates whole number and decimal  
    # part and stores it in two separate variables 
    whole, dec = str(number).split(".") 
  
    # Convert both whole number and decimal   
    # part from string type to integer type 
    whole = int(whole) 
    dec = int (dec) 
  
    # Convert the whole number part to it's 
    # respective octal form and remove the 
    # "0o" from it. 
    res = oct(whole).lstrip("0o") + "."
  
    # Iterate the number of times we want 
    # the number of decimal places to be 
    for x in range(places): 
  
        # Multiply the decimal value by 8 and separate  
        # the whole number part and decimal part 
        whole, dec = str((decimal_converter(dec)) * 8).split(".") 
  
        # Convert the decimal part 
        # to integer again 
        dec = int(dec) 
  
        # keep adding the integer parts  
        # received to the result variable 
        res += whole 
  
    return res 
  
# Function converts the value passed as 
# parameter to it's respective decimal 
# representation 
def decimal_converter(num): 
    while num > 1: 
        num /= 10
    return num 
  
# Driver Code 
  
# Take the user input for  
# the floating point number 
n = input("Enter your floating point value : \n") 
  
# Take user input for the number of decimal  
# places user would like the result as 
p = int(input("Enter the number of decimal places of the result : \n")) 
  
print(float_octal(n, places = p)) 

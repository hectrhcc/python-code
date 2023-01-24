import string
import re

tecla=input("Introduce un carácter ")
if len(tecla)==1:
    if tecla in string.ascii_uppercase:
        print ("\tEs una letra mayúscula")
    elif tecla in string.ascii_lowercase:
        print ("\tEs una letra minúscula")
    elif re.match("[0-9]", tecla):
            print ("\tEs un numero")
    else:
            print ("\tNo es una letra ni un numero")
else:
    print ("\tIntroduce un solo carácter")
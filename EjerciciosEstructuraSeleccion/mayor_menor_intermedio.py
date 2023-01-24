# Este codigo ha sido generado por el modulo psexport 20180802-l64 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).
n1 = int(input("Ingresa primer numero:"))
n2 = int(input("Ingresa segundo numero:"))
n3 = int(input("Ingresa tercer numero:"))
may = n1
men = n1
inter = n1
if n2>may:
    may = n2
if n3>may:
    may = n3
if n2<men:
    men = n2
if n3<men:
    men = n3
if (n1>men) and (n1<may):
    inter = n1
if (n2>men) and (n2<may):
    inter = n2
if (n3>men) and (n3<may):
    inter = n3
print("Menor: ",men)
print("Intermedio: ",inter)
print("Mayor: ",may)
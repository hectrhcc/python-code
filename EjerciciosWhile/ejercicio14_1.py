mes=""
while mes!=0:
    signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
    fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)
    dia=int(input("dia :"))
    mes=int(input("mes :"))
    #if mes==0:break
    mes=mes-1
    if dia>fechas[mes]:
        mes=mes+1
    if mes==12:
        mes=0
    print ("Tu signo es: " + signo[mes])
    #if mes==0:
        #mes=1
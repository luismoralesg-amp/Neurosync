""" 
Trabajado por:
Luisito
Javi
Sofi

"""


flagsita = True
notas_guardadas = []
def prom():
    suma = sum(notas_guardadas)
    prome =suma /len(notas_guardadas)
    print(prome)




while flagsita == True:
    nota= int(input("Ingresa tus notas: "))
    if nota >= 0 and nota <=100:
        print("nota registrada")
        notas_guardadas.append(nota)
    elif nota == -1 and len(notas_guardadas)!= 0:
        print(notas_guardadas)
        prom()
        flagsita = False
    else:
        print("notas fuera del rango")

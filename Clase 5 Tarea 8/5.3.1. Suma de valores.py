'''
Clase:        Clase 8
Tema:         For y while
Ejercicio:    5.3.1
Descripción:  Suma de valores

Autor:        Lilly Patricia Flores Vasquez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''
sum=0
numeros = input("Dame numeros, solo numeros y yo los sumaré ").split(" ")
numnuv= []
for i in numeros:
    numnuv.append(int(i))
for i in numnuv:
    sum+=i
print(sum)
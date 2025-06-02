'''
Clase:        Clase 8
Tema:         For y while
Ejercicio:    5.3.2
Descripción:  Sumador de valores posicionales

Autor:        Lilly Patricia Flores Vasquez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

numero = input("Dame un número: ")

numero = numero.replace(" ", "")

suma = 0
for i in numero:
    if i.isdigit():
        suma = suma + int(i)

while suma >= 10:
    suma2 = 0
    
    for i in str(suma):
        suma2 = suma2 + int(i)
    suma = suma2

print("El número reducido es:", suma)
'''
Clase:        Clase 10
Tema:         Manejo de matrices
Ejercicio:    10.3.1. Matriz simétrica
Descripción:  Dada una matriz cuadrada ingresada por el
              usuario, comprueba si la matriz cuadrada es
              simétrica respecto a su diagonal principal.

Autor:        Lilly Patricia Flores Vasquez
Fecha:        2025-06-10
Estado:       [ Terminado ]
'''

cant = int(input("Dime la dimensión de la matriz cuadrada: "))
matriz = []

print("Ingresa la matriz:")
for i in range(cant):
    fila = list(map(int, input().split()))
    matriz.append(fila)

sim = True
for i in range(cant):
    for j in range(cant):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break

if sim:
    print("La matriz es simétrica.")
else:
    print("La matriz no es simétrica:(")

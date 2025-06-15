'''
Clase:        Clase 10
Tema:         Manejo de matrices
Ejercicio:    10.2.1. Diagonal principal y secundaria
Descripción:  Dada una matriz cuadrada ingresada por el
              usuario, crea dos listas, una con los
              elementos de la diagonal principal y la otra
              con los elementos de la diagonal
              secundaria.

Autor:        Lilly Patricia Flores Vasquez
Fecha:        2025-06-10
Estado:       [ Terminado ]
'''

cant = int(input("Dime la dimensión de la matriz "))
matriz =[]
y=1
e=1
for i in range(cant):
  temp = list(map(int, input().split()))
  matriz.append(temp)
nums=["a","primer","segundo","tercero"]
for i in range(len(matriz)):
  for j in range(len(matriz[i])):
    if i ==j:

      print(f"El {nums[y]} número de la diagonal primaria es {matriz[i][j]}")
      y=y+1
    if i+j == len(matriz)-1:

      print(f"El {nums[e]} número de la diagonal secundaria es {matriz[i][j]}")
      e=e+1

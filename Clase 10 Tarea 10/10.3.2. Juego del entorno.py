'''
Clase:        Clase 10
Tema:         Manejo de matrices
Ejercicio:    10.3.2. Juego del entorno
Descripción:  Dada una matriz binaria ingresada por el
              usuario, verifica para cada celda de una
              matriz binaria cuántos elementos con valor
              de 1 hay en las celdas vecinas (arriba, abajo,
              izquierda, derecha, diagonales).


Autor:        Lilly Patricia Flores Vasquez
Fecha:        2025-06-10
Estado:       [ Terminado ]
'''

filas = int(input("Número de filas de la matriz: "))
columnas = int(input("Número de columnas de la matriz: "))
matriz = []

print("Ingresa la matriz: ")
for i in range(filas):
    fila = list(map(int, input().split()))
    matriz.append(fila)



for i in range(filas):
    for j in range(columnas):
        contador = 0
        
        if i > 0:
            if matriz[i-1][j] == 1:
                contador += 1

        if i < filas - 1:
            if matriz[i+1][j] == 1:
                contador += 1

        if j > 0:
            if matriz[i][j-1] == 1:
                contador += 1

        if j < columnas - 1:
            if matriz[i][j+1] == 1:
                contador += 1

        if i > 0 and j > 0:
            if matriz[i-1][j-1] == 1:
                contador += 1

        if i > 0 and j < columnas - 1:
            if matriz[i-1][j+1] == 1:
                contador += 1

        if i < filas - 1 and j > 0:
            if matriz[i+1][j-1] == 1:
                contador += 1

        if i < filas - 1 and j < columnas - 1:
            if matriz[i+1][j+1] == 1:
                contador += 1

        print(f"La celda ({i},{j}) tiene {contador} vecinos que valen 1")
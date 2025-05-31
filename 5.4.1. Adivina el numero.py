'''
Clase:        Clase 2
Tema:         For y while
Ejercicio:    5.4.1
Descripción:  Adivina el número

Autor:        Lilly Patricia Flores Vasquez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''
import random

adivinado = random.randint(1, 100)
print("Adivina el numero")

while True:
  intento = int(input(f"Ingresa un número entre {1} y {100}: "))
  if intento > adivinado and 0<intento<101:
    print("El número secreto es menor")

  elif intento < adivinado and 0<intento<101:
    print("El número secreto es mayor")

  elif intento == adivinado and 0<intento<101:
    print(f"¡Felicidades! Has adivinado el número: {adivinado}")
    print("Fin del juego")
    break
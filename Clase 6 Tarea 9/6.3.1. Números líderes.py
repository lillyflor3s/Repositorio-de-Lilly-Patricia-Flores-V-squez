'''
Clase:        Clase 6
Tema:         Listas, sets, tuplas
Ejercicio:    6.3.1.
Descripción:  Números líderes

Autor:        Lilly Patricia Flores Vasquez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''
lista = input('Dame numeros separados por espacios SOLAMENTE ').split(" ")
lista = list(lista)
dom = []

lista = [int(x) for x in lista]

n = len(lista)
i = 0

while i < n:
  es_lider = True
  j = i + 1
  while j < n:
    if lista[i] <= lista[j]:
      es_lider = False
      break
    j = j + 1
  if es_lider:
    dom.append(lista[i])
  i = i + 1
for lider in dom:
  print(lider, end=" ")


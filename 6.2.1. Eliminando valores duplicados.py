'''
Clase:        Clase 3
Tema:         Listas, sets, tuplas
Ejercicio:    6.2.1.
Descripción:  Eliminando valores duplicados

Autor:        Lilly Patricia Flores Vasquez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''
lista = input('Dame numeros separados por espacios SOLAMENTE').split(" ")
lista = list(lista)
n_list = []

for i in lista:
  if i not in n_list:
    n_list.append(i)
    print(i, end=" ")
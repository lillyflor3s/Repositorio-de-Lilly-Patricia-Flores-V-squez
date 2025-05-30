lista = input('Dame numeros separados por espacios SOLAMENTE').split(" ")
lista = list(lista)
n_list = []

for i in lista:
  if i not in n_list:
    n_list.append(i)
    print(i, end=" ")
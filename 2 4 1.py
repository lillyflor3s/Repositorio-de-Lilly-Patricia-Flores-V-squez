numero = input("Dame un número y te diré si es mágico ")
numero = int(numero)
siete = numero%7==0
cinco = numero%5==0
if siete==True and cinco==False:
    print("Tu número es mágico:D")
else:
    print("Tu número es normal:(")
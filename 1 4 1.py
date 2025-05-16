print("Dividamos un número")
n1 = input("Dame tu primer número ")
n1=int(n1)
n2= input("Ahora dame por que número lo quieres dividir ")
n2=int(n2)
k=input("Dime el número de decimales que quieres ")
k=int(k)

div = n1/n2
div=str(div)
pos = div.find(".")
print(pos)

for i in range(k+pos+1):
    print(div[i],end="")
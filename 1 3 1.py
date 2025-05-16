princ_cuenta = input("Dime el total de tu cuenta ")
por_cuenta = input("Dime el porcentaje de cuenta SIN EL % ")

cuenta = int(princ_cuenta)
propina = int(float(por_cuenta))

total = cuenta + (cuenta/propina)

print(f"La cuenta sin propina son {cuenta} dólares.")
print(f"El porcentaje de propina es {propina} %." )
print(f"Tu total a pagar serian {total} dólares.")
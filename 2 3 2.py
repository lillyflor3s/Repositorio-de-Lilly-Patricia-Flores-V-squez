energi = input("Escriba sus unidades de energia consumidas ")
energia = int(energi)
if energia>0 and energia<101:
    print("No pagas impuestos!")
elif energia>100 and energia<201:
    impuesto = energia*0.5
    print(f"Debes pagar {impuesto} $ de impuesto")
elif energia>201:
    impuesto = energia*0.7
    print(f"Debes pagar {impuesto} $ de impuesto")
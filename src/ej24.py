
precio = float(input("Dame el precio de un producto: "))

redondeado = round(precio, 2)

euros = int(redondeado)
centimos = int((redondeado - euros) * 100)

redondeado = (redondeado - (centimos/100))

print(f"Son {redondeado} euros y {centimos} centimos")
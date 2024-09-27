final = int(input("Dame el precio de un articulo con IVA "))

noiva = (final * 1.10) / 10

impiva = final - noiva

print("El importe sin IVA del articulo es: ",noiva,"y el IVA pagado es: ",impiva)
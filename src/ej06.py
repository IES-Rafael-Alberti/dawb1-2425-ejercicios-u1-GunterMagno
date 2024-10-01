precio = float(input("Dame el precio de un articulo con IVA: "))

siniva = precio / 1.1
iva = precio - siniva

print("El importe sin IVA del articulo es: ",round(siniva,2) ,"y el IVA pagado es: ",round(iva,2))
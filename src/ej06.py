precio = int(input("Dame el precio de un articulo con IVA: "))

siniva = precio / 1.1
iva = precio - siniva

print("El importe sin IVA del articulo es: ",siniva ,"y el IVA pagado es: ",iva)

noiva = int(input("Dame el importe del articulo sin IVA "))
iva = int(input("Indicame cual es el IVA a aplicar "))
importefinal = noiva * ((iva / 100)+1)

print("El importe con IVA del producto sera: ",importefinal )
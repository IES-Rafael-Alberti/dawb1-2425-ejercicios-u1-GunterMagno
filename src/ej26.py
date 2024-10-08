
lista = input("Dame los productos de una cesta de la compra separados por comas: ")

productos = lista.split(",")

print("\nProductos en la cesta de la compra: \n")
for producto in productos:
    print(producto.strip())
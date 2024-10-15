
nombre_producto = input("Dame el nombre de un producto: ")
precio_unidad = float(input("Dame el precio por unidad del producto: "))
cantidad_producto = int(input("Dame las unidades de producto compradas: "))

precio_total = (precio_unidad * cantidad_producto)

print(f"Nombre del producto: {nombre_producto},precio por unidad; {precio_unidad:06.2f}, cantidad del producto; {cantidad_producto:03d}, precio total; {precio_total:08.2f}")
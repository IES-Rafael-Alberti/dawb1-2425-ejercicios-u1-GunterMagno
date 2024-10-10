
precio_unidad = 000000.00
cantidad_producto = 000

nombre_producto = input("Dame el nombre de un producto: ")
precio_unidad = precio_unidad + float(input("Dame el precio por unidad del producto: "))
cantidad_producto = cantidad_producto + int(input("Dame las unidades de producto compradas: "))


precio_total = 00000000.00
precio_total = precio_total + (precio_unidad * cantidad_producto)

print(f"{nombre_producto} {cantidad_producto} {precio_total}")
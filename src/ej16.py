
pandehoy = 3.49

pannohoy = pandehoy - (pandehoy*0.6)

vendidas = int(input("Dime el numero de barras de pan que no es de hoy vendidas: "))

descuento = vendidas * pannohoy

vendidashoy = (vendidas*pandehoy) - descuento

print("El coste habitual de las barras seria: ", round(pandehoy*vendidas,2))
print("El coste de todas las barras es: ", round(vendidashoy,2))
print("Y el descuento por no ser de hoy es: ", round(descuento,2))
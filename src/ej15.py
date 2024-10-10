
ingreso = float(input("Dime tu ingreso: "))

interes = 4/100

capital1 = ingreso * (1 + interes)
capital2 = capital1 * (1 + interes)
capital3 = capital2 * (1 + interes)

print("Ahorros primer año: ", round(capital1,2))
print("Ahorros segundo año: ", round(capital2,2))
print("Ahorros tercer año: ", round(capital3,2))

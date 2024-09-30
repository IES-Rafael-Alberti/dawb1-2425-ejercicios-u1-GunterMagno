
peso = int(input("Dame tu peso en kg: "))

estatura = float(input("Dame tu altura en m: "))

imc = peso / (estatura ** 2)

print("Tu indice de masa corporal es: ", round(imc,2))
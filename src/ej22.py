frase = input("Dame una frase: ")
vocal = input("Dame una vocal: ")


frasemodificada = frase.replace(vocal.lower(), vocal.upper())

print("La frase sera: ",frasemodificada)
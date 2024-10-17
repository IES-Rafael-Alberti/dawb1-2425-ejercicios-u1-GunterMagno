
numero = int(input("Dame un numero: "))

print("Los divisores son: ")
for i in range(1 , numero + 1 ):
    if numero % i == 0 :
        divisores = i
        if divisores == numero:
            print(f"{divisores}", end=".")
        else:
            print(f"{divisores}", end=", ")
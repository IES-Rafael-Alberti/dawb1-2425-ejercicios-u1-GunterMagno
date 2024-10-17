import random

def numero_aleatorio(min_valor, max_valor):
    return random.randint(min_valor, max_valor)

def main():
    min_valor = int(input("Introduce un numero para poner el minimo: "))
    max_valor = int(input("Ingrese un numero para poner el maximo: "))
    resultado = numero_aleatorio(min_valor,max_valor)
    print(f"El numero aleatorio entre {min_valor} y {max_valor} es: {resultado}")

if __name__ == "__main__":
    main()

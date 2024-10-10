
def convertir_a_binario(valor,base):
    cociente = valor
    resultado = ""

    while cociente >= base:
        resto = cociente % base
        resultado += str(resto)
        cociente = cociente // base 
    resultado += str(cociente)
    resultado = resultado[::-1]
    return resultado

def main():
    valor = int(input("Introduzca un numero: "))
    base = int(input("Dame la base a la que lo quieres pasar: "))
    

if __name__=="__main__":
    main()
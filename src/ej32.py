
def sucesion(maximo: int) -> str:
    primero = 0
    segundo = 1

    serie = str(primero) + " " + str(segundo)

    fin = primero + segundo

    while fin <= maximo:
        serie += " " + str(fin)
        
        primero = segundo
        segundo = fin
        fin = primero + segundo

    return serie
    

def convertir_num(entrada: str) -> bool:
    numero = None
    try:
        numero = int(entrada)
    except ValueError:
        print("*ERROR*")

    return numero


def __main__():
    entrada = input("Dame un numero: ")
    numero = convertir_num(entrada)

    if numero is not None:
        print(sucesion(int(entrada)))



if __name__ == "__main__":
    __main__()

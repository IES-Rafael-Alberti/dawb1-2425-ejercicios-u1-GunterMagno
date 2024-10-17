
def comprobar_entero(cadena):
    return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].itsdigit())

def dame_entero():
    cadena = input("Introduce un numero entero: ").strip()
    while not comprobar_entero(cadena):
        cadena = input("**Error** No es un numero entero, intentalo de nuevo \n\nIntroduce un numero entero: ").strip()
    return int(cadena)

def main():
    num = dame_entero()
    print(f"Has introducido el numero {num}")

if __name__=="__main__":
    main()

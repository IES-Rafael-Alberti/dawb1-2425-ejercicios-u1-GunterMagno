import math
def calcular_area(a: float,b: float,c: float) -> float:
    s = (a + b + c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def comprobrar_float(valor: str) -> bool:
    if valor.startswith("-"):
        valor = valor[1:]

    pos_punto = valor.find(".")
    if pos_punto >= 0:
        valor = valor[:pos_punto] + valor[:pos_punto + 1:]

    return valor.isdigit()

def comprobar_triangulo(a, b, c,):
    return(a + b > c) and (a + c > b) and (b + c > a)

def introduce_numero(msj: str) -> float:
    valor = input(msj).strip().replace(",",".")
    
    while not comprobrar_float(valor): 
        print("\n**ERROR**, invalido!")
        valor = input(msj).strip().replace(",",".")
    return float(valor)

def main():
    print("Dame los tres lados del triangulo...")
    lado_a = introduce_numero("Lado 1: ")
    lado_b = introduce_numero("Lado 2: ")
    lado_c = introduce_numero("Lado 3: ")

    if comprobar_triangulo(lado_a, lado_b, lado_c) == True:
        area = calcular_area(lado_a, lado_b, lado_c)
        print("El area del triangulo con lados ({:.2f}, {:.2f}, {:.2f}) es {:.2f}.".format(lado_a,lado_b,lado_c,area))
    else:
        print("El triangulo con lados ({:.2f}, {:.2f}, {:.2f}) no es valido.".format(lado_a,lado_b,lado_c))

if __name__=="__main__":
    main()
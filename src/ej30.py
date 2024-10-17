import math

def primo(numero):
  if numero < 2:
       return False
  else:
      raiz = int(math.sqrt(numero))
      for i in range(2,raiz):
          if numero % i == 0:
              return False
          return True

def main():
    numero = int(input("Introduce un numero: "))
    if primo(numero):
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")

if __name__ == "__main__":
    main()
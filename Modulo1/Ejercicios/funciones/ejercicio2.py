
 
def suma_numeros():
    suma = 0
    #numero = int(input())
    while True:
        numero = int(input())
        suma = suma + numero
        if numero == 0:
            break
    print(suma)
        

# segunda forma 
def suma_numeros2():
    suma = 0
    numero = -1
    while numero != 0:
        numero = int(input(""))
        suma += numero
                   
    print(suma)
        
        
def main():
    
    suma_numeros2()


if __name__ == "__main__":
    main()
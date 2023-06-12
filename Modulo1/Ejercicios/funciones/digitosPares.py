def digitos_pares():
    numero = str(input('Dame un número: '))
    # preguntamos si cada dígito es par (divisible entre dos)
    n1 = (int(numero[0]) % 2) == 0  
    n2 = (int(numero[1]) % 2) == 0
    n3 = (int(numero[2]) % 2) == 0
    n4 = (int(numero[3]) % 2) == 0
    # sumamos True - False (binario)
    numero_pares = n1 + n2 + n3 + n4
    
    print('El número de dígitos pares es: ', numero_pares)
    
def main():
    #escribe tu código abajo de esta línea
    digitos_pares()

if __name__ == '__main__':
    main()
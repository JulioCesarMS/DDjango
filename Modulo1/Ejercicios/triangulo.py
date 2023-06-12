import math

def main():
    
    # pedimos la altura de la casa
    x = input('Ingresa la medida del lado 1: ') 
    y = input('Ingresa la medida del lado 2: ')
    z = input('Ingresa la medida del lado 3: ')  

    if (x +y > z) and (x + z > y) and (y + z > x):
        if x == y == z:
            print('ES UN TRIANGULO EQUILATERO')
        elif (x != y) and (y!=z) and (x!=z):
            print('ES UN TRIANGULO ESCALENO')
        else:
            print('ES UN TRIANGULO ISOCELES')
    else:
        print("NO ES UN TRIANGULO")

    
if __name__ == "__main__":
    main()
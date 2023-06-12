def main():
    print('Dame la edad:')
    edad = float(input())  
    print('Dame el año:')
    anio = float(input())

    
    resultado = anio + (100-edad)
    
    print('El año en que cumpliras 100 años es: ', int(resultado))
    
if __name__ == "__main__":
    main()
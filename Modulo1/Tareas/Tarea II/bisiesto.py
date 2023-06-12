# cuenta bancaria
def anio_bisiesto():
    anio = int(input("Año: "))
    
    bisiesto = False
    # condición
    if anio <= 0:
        print("Dato incorrecto")
    else:
        #calcula bisiesto
        if anio % 4 == 0:
            if anio % 100 == 0:
                if anio % 400 == 0:
                    bisiesto = True
                else:
                    bisiesto = False
            else:
                bisiesto = True
        else:
            bisiesto = False
        
        print(bisiesto)
            
    
def main():
    #escribe tu código abajo de esta línea
    anio_bisiesto()

if __name__ == '__main__':
    main()
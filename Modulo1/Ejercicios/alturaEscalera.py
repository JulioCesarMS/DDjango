import math

def main():
    
    # pedimos la altura de la casa
    altura = float(input('Altura de la casa: '))  
    # pedimos el angulo en grddos
    angulo_grados = int(input('Angulo en grados: '))
    # convertimos grados a radianes
    angulo_radianes = math.radians(angulo_grados)
    # calculamos la longitud de la escalera : x = altura/sin(theta)
    resultado = f'{round((altura/math.sin(angulo_radianes)),0):.0f}'
    
    print('Largo de la escalera:', resultado)

    
if __name__ == "__main__":
    main()
    
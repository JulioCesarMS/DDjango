import matplotlib.pyplot as plt
import os

def regresa_suma(matriz):
    res = []
    estados = []
    for i in range(1, len(matriz)):
        fila = matriz[i]
        estados.append(fila[2])
        suma = 0
        for j in range(3, len(fila)):
            cantidad = fila[j]
            suma += int(cantidad)
        res.append(suma)
    return res, estados

def grafica_linea(x,y):
    fig, ax = plt.subplots(figsize=(16,8))
    
    ax.plot(x,y)
    plt.xticks(x, rotation=90)
    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.25)
    plt.grid(True)
    plt.title("Gráfica de línea")
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    plt.show()
    
    
def main():
    path = os.path.dirname(__file__)
    datos = []
    with open('datos.csv', 'r') as f:
        linea = True
        while linea:
            linea = f.readline()
            if len(linea) > 0:  # Limpieza de datos.. 
                linea = linea[:-1]  # Se elimina el ultimo enter
                fila = linea.split(',')
                datos.append(fila)
    resultado, estados= regresa_suma(datos)
    print(resultado, estados)

    grafica_linea(estados, resultado)


    
if __name__ == "__main__":
    main()
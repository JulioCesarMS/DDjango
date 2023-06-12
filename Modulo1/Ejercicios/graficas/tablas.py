
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

def matriz(x, y):
    mat = [[x,y] for x, y in zip(x, y)]
    return mat

def muestra_tabla(datos):
    column_labels = ['Estado', 'Calificación']
    fig, ax = plt.subplots(figsize=(16,8))
    ax.table(cellText=datos, colLabels=column_labels,loc="center")
    ax.axis('tight')
    ax.axis('off')
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
    #print(resultado, estados)
    mat = matriz(estados, resultado)
    tabla = muestra_tabla(mat)
    print(tabla)
    
if __name__ == "__main__":
    main()
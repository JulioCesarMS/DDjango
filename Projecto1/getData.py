import os

def getData(file):
    path = os.path.dirname(__file__)
    datos = []
    with open(file, 'r') as f:
        linea = True
        while linea:
            linea = f.readline()
            if len(linea) > 0:  # Limpieza de datos.. 
                linea = linea[:-1]  # Se elimina el ultimo enter
                fila = linea.split(',')
                datos.append(fila)
    return datos
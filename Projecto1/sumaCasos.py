# obtiene la suma 
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
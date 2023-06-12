from maximoCasos import maximoCasosidx
from totalCasosPoblacion import totalCasosPoblacion

def arregloCasosEstados(datos):
    maxEstado = []
    for i in range(1,34):
        maxEstado.append(maximoCasosidx(datos, idestado=i))
    return maxEstado


def arregloCasosEstados2(datos):
    listEstado = []
    for i in range(1,34):
        listEstado.append(totalCasosPoblacion(datos, idestado=i))
    return listEstado
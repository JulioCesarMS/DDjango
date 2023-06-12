
# convierte el arreglo en listas:
def listaEstados(datos):
    list_estados = []
    list_fechas = []
    list_maximos = []
    for estado, fecha, maximo in datos:
                list_estados.append(estado)
                list_fechas.append(fecha)
                list_maximos.append(maximo)
                
    return list_estados, list_fechas, list_maximos



def listaEstados2(datos):
    list_estados = []
    list_poblacion = []
    list_contagios = []
    list_porcentaje = []
    for estado,poblacion,contagios,porcentaje in datos:
                list_estados.append(estado)
                list_poblacion.append(poblacion)
                list_contagios.append(contagios)
                list_porcentaje.append(porcentaje)
                
    return list_estados, list_poblacion, list_contagios, list_porcentaje
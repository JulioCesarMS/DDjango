
# Función retorna una lista
#  - [estado, fecha_maximo, valor_maximo]
def maximoCasosidx(datos, idestado=33):
    
    dias = datos[0][3:]
    casos_por_estado = datos[idestado][3:]
    maximo = 0
    # busca el máximo
    for i in range(0,len(casos_por_estado)):
        
        if int(casos_por_estado[i]) > maximo:
            maximo = int(casos_por_estado[i])
        else:
            maximo = maximo
    # busca id del máximo
    idx = []
    for i in range(len(casos_por_estado)):
        if int(casos_por_estado[i]) == maximo:
            idx.append(dias[i])  
        else:
            continue
    
    return  [datos[idestado][2] , idx[0], maximo]

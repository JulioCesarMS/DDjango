

def totalCasosPoblacion(datos, idestado=33):
    estado = datos[idestado][2]
    poblacion = int(datos[idestado][1])
    casos_por_estado = datos[idestado][3:]
    total_contagios = 0
    
    for casos in casos_por_estado:    
        total_contagios = total_contagios + int(casos)
 
    porcen_casos_por_pob   = round((total_contagios/poblacion),2)*100
    return  [ estado, poblacion, total_contagios, porcen_casos_por_pob]
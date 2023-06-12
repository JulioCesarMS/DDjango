
def totalCasosMes(datos, idestado=33):
    
    estado = datos[idestado][2]
    fecha = datos[idestado][3]
    poblacion = int(datos[idestado][1])
    casos_por_estado = datos[idestado][3:]
    total_contagios = 0
    
    meses = ['01','02','03','04','05','06','07','08','09','10','11','12']
    anios = ['2020', '2021', '2022', '2023']
    mesanio = []
    total = []
   
    for anio in anios:
        for mes in meses:
            mesAnio = mes+'-'+anio
            mesanio.append(mesAnio)
            #print(mesAnio)
            total_contagios = 0
            i = 0
            for i in range(len(casos_por_estado)): 
                if datos[0][3+i][3:10] == mesAnio:
                    total_contagios = total_contagios + int(casos_por_estado[i])
                else:
                    continue
                i += 1
            total.append(total_contagios)
    return  mesanio, total
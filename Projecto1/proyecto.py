
import matplotlib.pyplot as plt
import os
import math
from maximoCasos import maximoCasosidx
from totalCasosPoblacion import totalCasosPoblacion
from muestraTabla import muestra_tabla, muestra_tabla2
from arregloEstados import arregloCasosEstados, arregloCasosEstados2
from getData import getData
from listaEstados import listaEstados, listaEstados2
from graficas import grafica_linea, grafica_barra, grafica_linea2
from totalCasosMes import totalCasosMes

### Menú

def menu():
    print('**'+'*'*80 +'**') 
    print('**'+' '*80 +'**') 
    print('**'+ ' 1.- Día con más casos a nivel nacional' +' '*41 +'**') 
    print('**'+ ' 2.- % Casos confirmados de acuerdo a la población' +' '*30 +'**')
    print('**'+ ' 3.- Series de tiempo' +' '*59 +'**')
    print('**'+ ' 4.- Salir' +' '*70 +'**') 
    print('**'+' '*80 +'**') 
    print('**'+'*'*80 +'**')

def menu2():
    print('**'+'*'*80 +'**') 
    print('**'+' '*80 +'**') 
    print('**'+ ' Puede teclear el nombre de algun ESTADO o NACIONAL' +' '*29 +'**')
    print('**'+' '*80 +'**')
    print('**'+ ' Lista: AGUASCALIENTES, BAJA CALIFORNIA, BAJA CALIFORNIA SUR, CAMPECHE' +' '*10 +'**')
    print('**'+ '        CHIAPAS, CHIHUAHUA, DISTRITO FEDERAL, COAHUILA, COLIMA, DURANGO' +' '*9 +'**') 
    print('**'+ '        GUANAJUATO, GUERRERO, HIDALGO, JALISCO, MEXICO, MICHOACAN, MORELOS' +' '*6 +'**') 
    print('**'+ '        NAYARIT, NUEVO LEON, OAXACA, PUEBLA, QUERETARO, QUINTANA ROO' +' '*12 +'**') 
    print('**'+ '        SAN LUIS POTOSI, SINALOA, SONORA, TABASCO, TAMAULIPAS, TLAXCALA' +' '*9 +'**') 
    print('**'+ '        VERACRUZ, YUCATAN, ZACATECAS, NACIONAL' +' '*34 +'**') 
    print('**'+' '*80 +'**') 
    print('**'+'*'*80 +'**')
    
datos = getData('Casos_Diarios_Estado_Nacional_Confirmados_20230531.csv')

# opción 3
def casosPorMesEstado(estado):
    
    if estado == 'AGUASCALIENTES':
        fechas, casos = totalCasosMes(datos, idestado=1)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'BAJA CALIFORNIA':
        fechas, casos = totalCasosMes(datos, idestado=2)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'BAJA CALIFORNIA SUR':
        fechas, casos = totalCasosMes(datos, idestado=3)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'CAMPECHE':
        fechas, casos = totalCasosMes(datos, idestado=4)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'CHIAPAS':
        fechas, casos = totalCasosMes(datos, idestado=5)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'CHIHUAHUA':
        fechas, casos = totalCasosMes(datos, idestado=6)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'DISTRITO FEDERAL':
        fechas, casos = totalCasosMes(datos, idestado=7)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'COAHUILA':
        fechas, casos = totalCasosMes(datos, idestado=8)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'COLIMA':
        fechas, casos = totalCasosMes(datos, idestado=9)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'DURANGO':
        fechas, casos = totalCasosMes(datos, idestado=10)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'GUANAJUATO':
        fechas, casos = totalCasosMes(datos, idestado=11)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'GUERRERO':
        fechas, casos = totalCasosMes(datos, idestado=12)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'HIDALGO':
        fechas, casos = totalCasosMes(datos, idestado=13)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'JALISCO':
        fechas, casos = totalCasosMes(datos, idestado=14)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'MEXICO':
        fechas, casos = totalCasosMes(datos, idestado=15)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'MICHOACAN':
        fechas, casos = totalCasosMes(datos, idestado=16)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'MORELOS':
        fechas, casos = totalCasosMes(datos, idestado=17)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'NAYARIT':
        fechas, casos = totalCasosMes(datos, idestado=18)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'NUEVO LEON':
        fechas, casos = totalCasosMes(datos, idestado=19)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'OAXACA':
        fechas, casos = totalCasosMes(datos, idestado=20)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'PUEBLA':
        fechas, casos = totalCasosMes(datos, idestado=21)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'QUERETARO':
        fechas, casos = totalCasosMes(datos, idestado=22)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'QUINTANA ROO':
        fechas, casos = totalCasosMes(datos, idestado=23)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'SAN LUIS POTOSI':
        fechas, casos = totalCasosMes(datos, idestado=24)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'SINALOA':
        fechas, casos = totalCasosMes(datos, idestado=25)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'SONORA':
        fechas, casos = totalCasosMes(datos, idestado=26)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'TABASCO':
        fechas, casos = totalCasosMes(datos, idestado=27)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'TAMAULIPAS':
        fechas, casos = totalCasosMes(datos, idestado=28)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'TLAXCALA':
        fechas, casos = totalCasosMes(datos, idestado=29)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'VERACRUZ':
        fechas, casos = totalCasosMes(datos, idestado=30)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'YUCATAN':
        fechas, casos = totalCasosMes(datos, idestado=31)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'ZACATECAS':
        fechas, casos = totalCasosMes(datos, idestado=32)
        grafica_linea2(fechas[0:-6], casos[0:-6], estado)
        # nacional
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    elif estado == 'NACIONAL':
        fechas1, casos1 = totalCasosMes(datos, idestado=33)
        grafica_linea2(fechas1[0:-6], casos1[0:-6], 'NACIONAL')
    else:
        print('Lugar inválido')


def sel():
    menu()
    
    while True:
        
        opcion = int(input("Opción -> "))
  
        if opcion == 1:
            maxPorEstado= arregloCasosEstados(datos)
            # tabla
            tabla = muestra_tabla(maxPorEstado)
            print(tabla)
            # gráfico
            estados, fechas, maximos = listaEstados(maxPorEstado)
            grafica_linea(estados[0:-1], maximos[0:-1])
            menu()
        elif opcion == 2:
            casos_estado = arregloCasosEstados2(datos)
            # tabla
            tabla2 = muestra_tabla2(casos_estado)
            print(tabla2)
            # gráfico
            estados, poblacion, contagios, porcentaje = listaEstados2(casos_estado)
            grafica_barra(estados[0:-1], porcentaje[0:-1])
            menu()
        elif opcion == 3:
            menu2()
            estado = input('Lugar -> ')
            casosPorMesEstado(estado) 
            
        elif opcion == 4:
            break
        else:
            print('Opción no válida\n')
            menu()
            
def main():
    
    # sel
    try:
        sel()
    except:
        print('Opción Inválida \n')
        sel() 

            
    
if __name__ == "__main__":
    main()
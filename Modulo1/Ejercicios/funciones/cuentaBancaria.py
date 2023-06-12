# cuenta bancaria
def cuenta_bancaria():
    # definimos entradas
    saldo_anterior = float(input('Dame el saldo del mes anterior: '))
    ingresos = float(input('Dame los ingresos: '))
    egresos = float(input('Dame los egresos: '))
    numero_cheques = int(input('Dame el número de cheques: '))
    # import por núm cheques
    costo_cheques = numero_cheques*13.00
    # saldo fianl
    saldo_final = round((saldo_anterior + ingresos) - (egresos + costo_cheques),5) 
    
    # impresión
    print('El saldo final de la cuenta es:', saldo_final*0.925)
    
def main():
    #escribe tu código abajo de esta línea
    cuenta_bancaria()

if __name__ == '__main__':
    main()
def imprime_numero_cinco_veces(nombre):
    spam = 0
    while spam < 5:
        print(nombre)
        spam = spam + 1
        
    print(f'Se rompio el while, el valor de spam es {spam}')
        
def teclea_tu_nombre():
    nombre = ' '
    while nombre != 'tu nombre':
        print('Teclea tu nombre')
        nombre = input()
    print('Gracias!!!')
 
def prueba_break():
    contador = 1
    while True:
        print(contador)
        if contador >= 10:
            break
        contador += 1
        
def prueba_continue():
    
    while True:
        name = input("Teclea tu nombre:")
        if name != 'Joe':
            continue         # Rompe la iteración, se pasa a la siguiente
        print('Hola Joe')
        
        password = input("Teclea tu password:")   
        if password == "swordfish":
            break         
def main():
    imprime_numero_cinco_veces('Pruebas')
    #teclea_tu_nombre()
    #prueba_break()
    prueba_continue()

if __name__ == "__main__":
    main()
      
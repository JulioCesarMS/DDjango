import math


def suma(x1, x2):
    resultado = x1 + x2
    return resultado

#def main():
#    res = suma(2,3)
#    print(res)
ham = 100 
    
def spam():
    eggs = 3132  # variable local a la función eggs 
    print(eggs)
    bacon()
    print(eggs)    

def bacon():
    global ham
    eggs = 90  # variable local a la función eggs 
    ham = 88
    print(eggs)  
    
def main():
    spam()
    print(f'l valor de ham es: {ham}')
            
if __name__ == "__main__":
    main()
   
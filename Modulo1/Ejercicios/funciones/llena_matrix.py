import random

def llena_matriz(filas, columnas):
    M = []
    for k in range(filas):
        F = []
        for i in range(columnas):
            F.append(int(input(f"M[{k},{i}]: ")))
        M.append(F)
    return M

def inicializa_matriz_random(filas, columnas):
    M = []
    for k in range(filas):
        F = []
        for i in range(columnas):
            F.append(random.randint(1,100))
        M.append(F)
    return M

def inicializa_matriz_0(filas, columas):
    M = []
    for k in range(filas):
        F = []
        for i in range(columas):
            F.append(0)
        M.append(F)
    return M

def main():
    M1 = llena_matriz(3,3 )
    print(M1)

if __name__ == '__main__': 
    main()

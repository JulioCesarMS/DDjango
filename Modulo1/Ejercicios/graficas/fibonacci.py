def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

        

def main():
    print("Programa que calcula número 'n' de la serie de fibonacci")
    n = int(input('n => '))
    resultado = fibonacci(n)
    print(f'El número fibonacci de {n} = {resultado}')

if __name__ == '__main__':
    main()

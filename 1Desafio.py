def is_fibonacci(num):
    if num < 0:
        return False

    # Iniciando os primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Verificando se o número informado pertence à sequência
    while a < num:
        a, b = b, a + b
    
    return a == num

def main():
    # Solicitando ao usuário para informar um número
    number = int(input("Informe um número: "))
    
    # Verificando se o número pertence à sequência de Fibonacci
    if is_fibonacci(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} NÃO pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()

def contar_a(string):
    # Convertendo a string para minúsculas para contar todas as ocorrências de 'a' e 'A'
    string_lower = string.lower()
    
    # Contando a quantidade de 'a'
    count = string_lower.count('a')
    
    return count

def main():
    # Solicitando ao usuário que insira uma string
    texto = input("Informe uma string: ")
    
    # Contando as ocorrências da letra 'a'
    quantidade = contar_a(texto)
    
    # Verificando se a letra 'a' está presente e informando a quantidade
    if quantidade > 0:
        print(f"A letra 'a' ocorre {quantidade} vezes na string.")
    else:
        print("A letra 'a' não está presente na string.")

if __name__ == "__main__":
    main()

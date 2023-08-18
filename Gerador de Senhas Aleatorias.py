import random
import string

def gerar_senha(comprimento, caracteres):
    caracteres_disponiveis = ""
    if "maiúsculas" in caracteres:
        caracteres_disponiveis += string.ascii_uppercase
    if "minúsculas" in caracteres:
        caracteres_disponiveis += string.ascii_lowercase
    if "números" in caracteres:
        caracteres_disponiveis += string.digits
    if "símbolos" in caracteres:
        caracteres_disponiveis += string.punctuation
    
    if caracteres_disponiveis:
        senha = ''.join(random.choice(caracteres_disponiveis) for _ in range(comprimento))
        return senha
    else:
        return "Nenhum tipo de caractere selecionado."

def main():
    comprimento = int(input("Digite o comprimento da senha: "))
    caracteres = input("Quais caracteres você deseja incluir? (maiúsculas, minúsculas, números, símbolos): ").split(', ')
    
    senha = gerar_senha(comprimento, caracteres)
    
    if senha != "Nenhum tipo de caractere selecionado.":
        print("Senha gerada:", senha)
    else:
        print(senha)

if __name__ == "__main__":
    main()

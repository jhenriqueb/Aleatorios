import os

def minha_system_call(nome_arquivo):
    texto = "So alegria hahaha"
    
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(texto)
        print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar o arquivo: {e}")
        return -1

if __name__ == "__main__":
    nome_arquivo = "aula.txt"
    minha_system_call(nome_arquivo)

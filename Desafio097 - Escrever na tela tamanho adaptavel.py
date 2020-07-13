print(f"\033[;1m{'Desafio 097 - Escrever na tela frase centralizada'}\033[m")

# Função que cria uma mensagem personalizada
def frase (msg):
    # tamanho da frase para deixar centralizado
    tam = len(msg) + 4
    print('-'*tam)
    print(f"{msg:^{tam}}")
    print('-'*tam)


frase('Eric Giobini')
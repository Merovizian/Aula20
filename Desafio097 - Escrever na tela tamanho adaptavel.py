print(f"\033[;1m{'Desafio 097 - Escrever na tela frase centralizada'}\033[m")


def frase (msg):
    tam = len(msg) + 4
    print('-'*tam)
    print(f"{msg:^{tam}}")
    print('-'*tam)


frase('Eric Giobini')
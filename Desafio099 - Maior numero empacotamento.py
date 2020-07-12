print(f"\033[;1m{'Desafio 99 - Maior número em um empacotamento':*^70}\033[m")
def maior (num):
    maior = 0
    for a in num:
        if a >= maior:
            maior = a
    return maior


while True:
    lista = input('Informe uma lista de números serapados por virgula: ')
    lista = lista.split(',')
    for p,a in enumerate(lista):
        lista[p] = int(a)

    print(f"O maior valor da lista {lista} é {maior(lista)}")
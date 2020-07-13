print(f"\033[;1m{'Desafio 99 - Maior número em um empacotamento':*^70}\033[m")

# função que ira receber uma lista(obrigatoriamente) e retornar o maior numero
def maior (num):
    maior = 0
    for a in num:
        if a >= maior:
            maior = a
    return maior

# metodo de criação de lista
while True:
    lista = input('Informe uma lista de números serapados por virgula: ')
    lista = lista.split(',')
    for p,a in enumerate(lista):
        lista[p] = int(a)

    print(f"O maior valor da lista {lista} é {maior(lista)}")
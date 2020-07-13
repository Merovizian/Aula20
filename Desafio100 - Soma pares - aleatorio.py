from random import randint
import time
from clear import limpatela
print(f"\033[;1m{'Desafio 100 - Função lista aleatoria e soma par':*^70}\033[m")

# Funçao que pede uma lista e se o usuario quer somar par ou impar
def soma (lista ,modo):
    total = 0
    # verifica se o que o usuario colocou é par e já faz a soma
    if modo.upper() == 'PAR':
        for a in lista:
            if a % 2 == 0:
                total += a
    # se nao for par cai neste for e faz a soma dos impares
    else:
        for a in lista:
            if a % 2 == 1:
                total += a
    return total

# cria uma lista com a quantidade e o tamanho de cada algoritimo
def newlista (quantidade,tamanho):
    lista = list()
    # for para sortear os numeros.
    for a in range(0, quantidade):
        lista.append(randint(0,tamanho))
    return lista


lista = list()
# programa principal, menu principal
while True:
    limpatela()
    print(f"{'Menu de Listas':-^50}")
    print(f"1 - Criar nova lista" if len(lista) == 0 else f"1 - Alterar Lista {lista}")
    print(f"2 - Fazer a Soma da lista Atual" if len(lista) != 0 else '')
    menu = int(input('Escolha uma opção: '))
    # obriga o usuario a escolher o menu correto
    while menu not in range(1,3):
        menu = int(input('Escolha uma opção: '))
    # Escolha do menu 1 que pede o usuario qual o tamanho e a quantidade dos valores da lista
    if menu == 1:
        quantidade = int(input("Informe a quantidade de termos na lista: "))
        tamanho = int(input("Informe o valor maximo de cada termo: "))
        print("Criando lista...")
        time.sleep(0.5)
        # cria a lista com os parametros passados pelo usuario atraves da função criada
        lista = newlista(quantidade, tamanho).copy()
        print(f"Lista criada com sucesso: {lista}")
        input("Pressione ENTER para continuar...")
    # Menu escolha 2 que pede ao usuario se ele quer somar os pares ou os impares.
    if menu == 2:
        modo = input("Deseja Somar Par ou Impar? ")
        while modo.upper() != 'PAR' and modo.upper() != 'IMPAR':
            modo = input("Deseja Somar Par ou Impar? ")
        print(f"A soma dos {modo.upper()} numeros de {lista} é: {soma(lista,modo)}")
        input("Pressione ENTER para continuar...")




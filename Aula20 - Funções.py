# função simples, com 2 argumentos:
def soma (a, b):
    s = a + b
    print(f'A soma de {a} + {b} = {s}')


soma(5,9)


# Função empacotada, com infinitos argumentos, os argumentos são transformados em uma tupla
def contador(*num):
    total = 0
    for a in num:
        total += a
    print(total)


contador(1,2,3,4,5,6,7,8,9)

# Função aceita lista e pode manipulá-la
def dobra (lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

lista = [1,3,5,9,8,5,2,0]
dobra(lista)
print(lista)

# Outra forma:
def dobra2 (lista2):
    for p,v in enumerate(lista2):
        lista2[p] *=2


lista2 = lista.copy()
dobra2(lista2)
print(lista2)



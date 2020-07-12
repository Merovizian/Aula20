import time
print(f"\033[;1m{'Desafio 98 -Contador com 3 entradas e parametros':*^70}\033[m")


def contador (inicio , fim, passo):
    if passo == 0:
        passo = 1
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio > fim:
        tamanho = len(str(abs(inicio)))
        if passo > 0:
            passo *= -1
    else:
        tamanho = len(str(abs(fim)))

    if passo > 0:
        for a in range (inicio, fim+1, passo):
            print(f'{a:0>{tamanho}}',end=' ')
            time.sleep(0.4)
        print("FIM!")
    else:
        for a in range(inicio, fim - 1, passo):
            print(f'{a:0>{tamanho}}', end=' ')
            time.sleep(0.4)
        print("FIM!")


while True:
    total = 0
    inicio = int(input("Informe o inicio[999 sair]: "))
    if inicio == 999:
        break
    fim = int(input("Informe um fim: "))
    passo = int(input("Informe o periodo: "))
    print('-='*20)
    contador(inicio, fim, passo)
    print('-=' * 20)
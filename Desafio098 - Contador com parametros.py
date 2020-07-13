import time
print(f"\033[;1m{'Desafio 98 -Contador com 3 entradas e parametros':*^70}\033[m")

# Função contador que recebe 3 parametros
def contador (inicio , fim, passo):
    # Definição do exercicio para que se o passo fosse 0, mudaria para 1
    if passo == 0:
        passo = 1
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    # Variavel tamanho para colocar saber quantos algoritmos tem o maior parametro
    if inicio > fim:
        tamanho = len(str(abs(inicio)))
        # caso o inicio tenha o maior parametro o passo tem que ser negativo para ocorrer contagem
        if passo > 0:
            passo *= -1
    else:
        tamanho = len(str(abs(fim)))
    # Se o passo for positivo conta-se normal
    if passo > 0:
        for a in range (inicio, fim+1, passo):
            print(f'{a:0>{tamanho}}',end=' ')
            time.sleep(0.4)
        print("FIM!")
    # Se o passo for negativo conta-se inversamente
    else:
        for a in range(inicio, fim - 1, passo):
            print(f'{a:0>{tamanho}}', end=' ')
            time.sleep(0.4)
        print("FIM!")

# Loop para rodar o programa principal
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
print(f"\033[;1m{'Desafio 096 - Area':*^70}\033[m")

# funçao que IMPRIME uma are
def area(comprimento , largura):
    print(f'A area do terreno {comprimento}m x {largura}m é de {comprimento*largura:.2f}m²')
    print(f'O terreno tem {(comprimento*largura)/100} are')
    print(f'O terreno tem {(comprimento * largura) / 10000} hectare')
    print(f'O terreno tem {((comprimento * largura) / 10000)*0.4} acre')

# puxando a função e colocando parametros.
l = float(input("Informe a largura do terreno: "))
c = float(input("Informe o comprimento do terreno: "))

area(c,l)

# Estanislau deseja comprar 08 jogos para seu console favorito. 
# O preço varia de um siite para o outro, mas é sempre igual para todos os títulos. 
# O valor de frete é fixo e custa R$ 45,00.

# Escreva um programa que leia:

# O valor (unitário) do jogo em um determinado site.

# Como saída, determine o preço a ser pago por Estanislau pelo total de 8 jogos,
# acrescido do valor do frete.

def calcular_preco_total(preco_unitario, quantidade_jogos):
    preco_total_jogos = preco_unitario * quantidade_jogos
    frete = 45.00
    preco_total = preco_total_jogos + frete
    return preco_total

# Leitura do valor unitário do jogo
preco_unitario = float(input("Digite o valor unitário do jogo: "))

# Número de jogos desejados
quantidade_jogos = 8

# Calcula o preço total
preco_total = calcular_preco_total(preco_unitario, quantidade_jogos)

# Saída
print("O preço total a ser pago por Estanislau é R$ {:.2f}".format(preco_total))
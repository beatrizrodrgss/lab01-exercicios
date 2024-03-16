# Estanislau deseja comprar 08 jogos para seu console favorito. 
# O preço varia de um site para o outro, mas é sempre igual para todos os títulos. O valor do frete é fixo e custa R$45,00.

# Escreva um programa que leia:

# o valor (unitário) do jogo em um determinado site.
# Como saída, determine o preço a ser pago por Estanislau pelo total de 8 jogos, acrescido do valor do frete.
# Agora, Estanislau deseja comprar vários jogos para seu console favorito. Em um mesmo site, o preço do jogo é sempre o mesmo para todos os títulos. O valor do frete é diferente para cada site.

# Escreva um programa que leia as seguintes entradas, nesta ordem:

# 1: A quantidade de jogos a serem encomendados;
# 2: O valor unitário de cada jogo;
# 3: O valor do frete.
# Como saída, determine o preço total a ser pago por Estanislau pelos jogos que for encomendar do site, incluindo o valor do frete.

def calcular_preco_total(quantidade_jogos, preco_unitario, valor_frete):
    preco_total_jogos = quantidade_jogos * preco_unitario
    preco_total = preco_total_jogos + valor_frete
    return preco_total

# Leitura das entradas
quantidade_jogos = int(input("Digite a quantidade de jogos a serem encomendados: "))
preco_unitario = float(input("Digite o valor unitário de cada jogo: "))
valor_frete = float(input("Digite o valor do frete: "))

# Calcula o preço total
preco_total = calcular_preco_total(quantidade_jogos, preco_unitario, valor_frete)

# Saída
print("O preço total a ser pago por Estanislau é R$ {:.2f}".format(preco_total))

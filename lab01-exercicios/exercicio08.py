# Considere um triângulo de lados a, b, c. O semiperímetro (metade do perímetro) desse triângulo é definido por:
# S = a + b + c sobre 2

# A área A do triângulo pode ser calculada pela seguinte fórmula:
# A = raiz quadrada de S (s - a) (s - b) (s - c)
# Escreva um programa que leia os comprimentos dos lados de um triângulo, 
# Como saída, determine a sua área arredondada com até cinco casas decimais.

import math

# Função para calcular a área do triângulo
def calcular_area_triangulo(a, b, c):
    # Calcula o semiperímetro
    s = (a + b + c) / 2
    # Calcula a área usando a fórmula especificada
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Leitura dos comprimentos dos lados do triângulo
a = float(input("Digite o comprimento do lado a: "))
b = float(input("Digite o comprimento do lado b: "))
c = float(input("Digite o comprimento do lado c: "))

# Calcula a área do triângulo
area_triangulo = calcular_area_triangulo(a, b, c)

# Saída com a área arredondada para cinco casas decimais
print("A área do triângulo é: {:.5f}".format(area_triangulo))

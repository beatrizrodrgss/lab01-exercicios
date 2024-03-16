# Conversão de Celsius para Fahrenheit

# Você está trabalhando em uma estação meteorológica e precisa fornecer as temperaturas em diferentes escalas para os visitantes. 
# Crie um programa que receba a temperatura em graus Celsius e realize a conversão para Fahrenheit.

# Considere as fórmulas de conversão:

# Fahrenheit = (Celsius * 9/5) + 32

# A saída deve ser arredondada para duas casas decimais.


# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Leitura da temperatura em graus Celsius
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Conversão para Fahrenheit
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

# Saída com o resultado arredondado para duas casas decimais
print("A temperatura em Fahrenheit é: {:.2f}".format(temperatura_fahrenheit))

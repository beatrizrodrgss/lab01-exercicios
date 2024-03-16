# Conversão de Celsius para Kelvin

# Você está trabalhando em uma estação meteorológica e precisa fornecer as temperaturas em diferentes escalas para os visitantes. 
# Crie um programa que receba a temperatura em graus Celsius e realize a conversão para Kelvin.

# Considere a fórmula de conversão:

# Kelvin = Celsius + 273.15

# A saída deve ser arredondada para duas casas decimais.


# Função para converter Celsius para Kelvin
def celsius_para_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

# Leitura da temperatura em graus Celsius
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Conversão para Kelvin
temperatura_kelvin = celsius_para_kelvin(temperatura_celsius)

# Saída com o resultado arredondado para duas casas decimais
print("A temperatura em Kelvin é: {:.2f}".format(temperatura_kelvin))

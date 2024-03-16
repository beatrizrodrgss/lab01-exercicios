# Escreva um programa que leia dois números inteiros, nesta ordem:
# X (dividendo)
# Y (divisor)

# Como saída, imprima os quatro elementos da divisão inteira, nesta ordem:
# dividendo
# divisor 
# quociente
# resto

def divisao_inteira(x, y):
    quociente = x // y
    resto = x % y
    return quociente, resto

# Leitura dos números inteiros
x = int(input("Digite o dividendo (X): "))
y = int(input("Digite o divisor (Y): "))

# Calcula o quociente e o resto
quociente, resto = divisao_inteira(x, y)

# Saída
print("Dividendo:", x)
print("Divisor:", y)
print("Quociente:", quociente)
print("Resto:", resto)

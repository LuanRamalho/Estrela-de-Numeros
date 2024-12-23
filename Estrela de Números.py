# Programa para exibir uma estrela de números de 5 pontas

# Número de linhas da estrela
n = 5

# Função para criar a linha de números
def print_line(num):
    print(' ' * (n - num), end='')   # Espaços antes dos números
    print(' '.join(str(x) for x in range(1, num + 1)))  # Números crescentes

# Parte superior da estrela
for i in range(1, n + 1):
    print_line(i)

# Parte inferior da estrela
for i in range(n - 1, 0, -1):
    print_line(i)
input()
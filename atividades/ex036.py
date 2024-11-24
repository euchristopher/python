# Função para calcular a determinante de três retas
def calcular_determinante(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    # Fórmula da determinante 3x3
    determinante = (
        (a1 * (b2 * c3 - b3 * c2))
        - (b1 * (a2 * c3 - a3 * c2))
        + (c1 * (a2 * b3 - a3 * b2))
    )
    return determinante


# Função para verificar se as 3 retas formam um triângulo
def verificar_triangulo(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    # Calcula a determinante
    determinante = calcular_determinante(a1, b1, c1, a2, b2, c2, a3, b3, c3)

    # Verifica se a determinante é diferente de zero
    if determinante != 0:
        return True  # As retas formam um triângulo
    else:
        return False  # As retas não formam um triângulo


# Entrada dos coeficientes das 3 equações das retas
a1, b1, c1 = map(
    float, input("Digite os coeficientes da primeira reta (a1, b1, c1): ").split()
)
a2, b2, c2 = map(
    float, input("Digite os coeficientes da segunda reta (a2, b2, c2): ").split()
)
a3, b3, c3 = map(
    float, input("Digite os coeficientes da terceira reta (a3, b3, c3): ").split()
)

# Verifica se as retas formam um triângulo
if verificar_triangulo(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    print("As retas formam um triângulo.")
else:
    print("As retas NÃO formam um triângulo.")

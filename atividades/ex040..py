# Loop Principal
while True:

    # Loop de Perguntas
    while True:
        try:
            print(f"Digite o tamanho dos 3 lados de um triangulo")
            a = float(input("Digite o tamanho do Lado A: "))
            b = float(input("Digite o tamanho do Lado B: "))
            c = float(input("Digite o tamaho do Lado C: "))
            break
        except ValueError:
            print(f"Digite um numero valido!")

    # Calcular Triangulo
    def calcular(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True, "Forma um triângulo"
        else:
            return False, "Nâo forma um triângulo"

    # Verifica o triangulo
    def triangulo(a, b, c):
        if a == b == c:
            return "Equilatero"
        elif a == b != c:
            return "Isosceles"
        elif a != b != c:
            return "Escaleno"

    # Chamada para funcao
    forma_triangulo, mensagem = calcular(a, b, c)
    print(mensagem)

    # Tipo do triangulo
    if forma_triangulo:
        tipo = triangulo(a, b, c)
        print(f"O triângulo é {tipo}.")
    else:
        print("Nao e possivel verificar o tipo, pois nao forma um triangulo.")

    continuar = input("Deseja continuar? (s/n): ")
    if continuar != "s":
        print(f"Programa encerrado.")
        break

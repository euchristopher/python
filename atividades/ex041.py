# Loop Principal
while True:
    # Loop de perguntas
    while True:
        # Dados do cliente
        try:
            print(f"Calculadora IMC")
            altura = float(input("Digite a sua altura: "))
            peso = float(input("Digite o seu peso em KG: "))
            break
        except ValueError:
            print(f"[ERROR] Digite numeros validos.")

    # Calcula o IMC
    def calcularIMC(altura, peso):
        imc = peso / (altura * altura)
        if imc < 18.5:
            return imc, "Abaixo do peso"
        elif 18.5 <= imc <= 24.9:
            return imc, "Peso normal"
        elif 25 <= imc <= 29.9:
            return imc, "Sobrepeso"
        else:
            return imc, "Obesidade"

    # Chama o calculo como função
    imc, mensagem = calcularIMC(altura, peso)
    # Resultado
    print(f"O seu IMC é: {imc:.2f}")
    print(f"Categoria: {mensagem}")

    # Estrutura de repetição
    continuar = input("Deseja calcular outro IMC? (s/n): ")
    if continuar != "s":
        print(f"Programa encerrado.")
        break

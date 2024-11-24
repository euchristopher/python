# Loop principal para repetição
while True:
    # Entrada de dois números
    while True:
        try:
            n1 = int(input("Digite um numero: "))
            n2 = int(input("Digite outro numero: "))
            break  # Sai do loop interno se os números forem válidos
        except ValueError:
            print("Por favor, digite números válidos.")

    # Cálculo do maior e menor número
    maior = max(n1, n2)
    menor = min(n1, n2)

    # Exibindo o resultado
    if maior == menor:
        print(f"Não existe um número maior, pois ambos são iguais.")
    else:
        print(f"O maior número é {maior}")
        print(f"O menor número é {menor}")

    # Pergunta se o usuário quer continuar
    repetir = input("Deseja repetir? (s/n): ").lower()
    if repetir != "s":
        print("Programa encerrado.")
        break  # Sai do loop principal e encerra o programa

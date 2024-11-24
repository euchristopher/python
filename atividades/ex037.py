def calcular(n, sistema):
    resultado = ""

    if sistema == 1:  # Binário
        while n > 0:
            resto = n % 2
            resultado = str(resto) + resultado
            n = n // 2

    elif sistema == 2:  # Octal
        while n > 0:
            resto = n % 8
            resultado = str(resto) + resultado
            n = n // 8

    elif sistema == 3:  # Hexadecimal
        while n > 0:
            resto = n % 16
            if resto < 10:
                resultado = str(resto) + resultado
            else:
                resultado = chr(resto + 87) + resultado  # Para A-F (resto 10 a 15)
            n = n // 16

    return resultado if resultado else "0"


# Loop principal para repetir a ação
while True:
    # Validação para garantir que o número inserido seja válido
    while True:
        try:
            n = int(input("Digite um numero: "))
            break  # Se a entrada for válida, sai do loop de validação
        except ValueError:
            print("Número inválido! Por favor, digite um número inteiro válido.")

    # Escolha do Sistema
    print(f"Sistemas Numericos:\n1 - Binário\n2 - Octal\n3 - Hexadecimal")

    # Validação para garantir que o usuário escolha uma opção válida
    while True:
        try:
            sOP = int(
                input(
                    "Escolha qual sistema operacional para operar o numero escolhido: "
                )
            )
            if sOP in [1, 2, 3]:  # Verifica se a escolha está entre as opções válidas
                break
            else:
                print("Escolha inválida! Por favor, digite 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida! Por favor, escolha uma opção válida.")

    # Chama a função de conversão
    resultado = calcular(n, sOP)
    print(f"O número {n} no sistema escolhido é: {resultado}")

    # Pergunta se o usuário quer continuar ou sair
    repetir = input("Deseja repetir? (s/n): ").lower()
    if repetir != "s":
        print("Programa encerrado.")
        break

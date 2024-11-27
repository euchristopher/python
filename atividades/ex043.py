# Import de numeros random
import random

# Pontuação
pontuacao_maquina = 0
pontuacao_usuario = 0

# Loop Principal
while True:

    # Escolha da maquiba
    numero_maquina = random.randint(1, 3)

    # Loop De pergunta
    while True:
        try:
            # Escolha do Jogador
            print(f"JOKENPÔ")
            print(f"Escolha um número para representar um deles abaixo:")
            print(f"1 - Pedra")
            print(f"2 - Papel")
            print(f"3 - Tesoura")
            numero_usuario = int(input("Escolha entre o número 1 e 3: "))
            print("-" * 40)

            # Verificação
            if numero_usuario not in [1, 2, 3]:
                raise ValueError("Opçãoo inválida.")
            break
        except ValueError:
            print(f"Número inválido.")
            print("-" * 40)
            continue

    # Verificação do resultado
    def verificar_jokepo(numero_maquina, numero_usuario):
        if numero_maquina == numero_usuario:
            return "Empate!"
        elif (
            (numero_maquina == 1 and numero_usuario == 3)  # Pedra vence Tesoura
            or (numero_maquina == 2 and numero_usuario == 1)  # Papel vence Pedra
            or (numero_maquina == 3 and numero_usuario == 2)  # Tesoura vence Papel
        ):
            return "Eu venci!"
        else:
            return "Você venceu!"

    # Chamada da função
    resultado = verificar_jokepo(numero_maquina, numero_usuario)

    # Sistema de pontuação
    if resultado == "Eu venci!":
        pontuacao_maquina += 1
    elif resultado == "Você venceu!":
        pontuacao_usuario += 1

    # Resultado
    print(f"\nMinha escolha: {numero_maquina} | Sua escolha: {numero_usuario}")
    print(f"{resultado}")
    print("-" * 40)

    # Estrutura de repetição para continuar jogando
    while True:
        continuar = input("Deseja jogar de novo? (s/n): ").strip().lower()
        if continuar not in ["s", "n"]:
            print("[ERROR] Digite uma opção válida ('s' para sim ou 'n' para não).")
        else:
            break  # Sai do loop se for 's' ou 'n'

    if continuar == "n":
        print("Programa encerrado.")
        break

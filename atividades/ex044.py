# Import de escolha aleátoria pela máquina
from random import randint

# Base do Jokenpô
itens = ["Pedra", "Papel", "Tesoura"]
pontuacao_computador = 0
pontuacao_jogador = 0


# Verificador de jogadas
def jokenpo(computador, jogador):
    if computador == jogador:
        return "Empate!"
    elif (
        (computador == 1 and jogador == 3)
        or (computador == 3 and jogador == 2)
        or (computador == 2 and jogador == 1)
    ):
        return "Computador venceu!"
    else:
        return "Jogador venceu!"


# Loop de perguntas principal
while True:

    computador = randint(1, 3) - 1  # Escolha do computador

    # Menu de opções
    print("-" * 35)
    print("JOKENPÔ")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("-" * 30)

    # Loop de pegunta para o jogador
    while True:
        try:
            jogador = (
                int(input("Escolha a sua jogada entre 1 e 3: ")) - 1
            )  # Escolha do jogador
            print("-" * 35)
            if jogador not in [0, 1, 2]:
                raise ValueError
            break
        except ValueError:
            print("-" * 35)
            print("Número inválido. Por favor digite um número válido.")
            print("-" * 35)

    # Resultado
    resultado = jokenpo(computador, jogador)

    # Pontuação
    if resultado == "Computador venceu!":
        pontuacao_computador += 1
    elif resultado == "Jogador venceu!":
        pontuacao_jogador += 1

    # Exibição do Resultado
    print(f"JOGADOR escolheu: {itens[jogador]}.")
    print(f"COMPUTADOR escolheu: {itens[computador]}.")
    print(f"RESULTADO: {resultado}")
    print("-" * 35)
    print(f"PLACAR")
    print(f"JOGADOR: {pontuacao_jogador}")
    print(f"COMPUTADOR: {pontuacao_computador}")
    print("-" * 35)

    # Loop de pergunta de repetição
    while True:
        continuar = input("Quer jogador de novo? (s/n): ").strip().lower()
        if continuar not in ["s", "n"]:
            print("-" * 35)
            print("Escolha invalida! digite 's' para sim ou 'n' não")
            print("-" * 35)
        else:
            break

        if continuar == "n":
            print("Obrigado por jogar!")
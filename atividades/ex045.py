from random import randint
from time import sleep

# Constantes
ITENS = ["Pedra", "Papel", "Tesoura"]
DIVISOR = "-" * 35


# Função para verificar quem venceu
def jokenpo(computador, jogador):
    if computador == jogador:
        return "Empate!"
    elif (jogador - computador) % 3 == 1:
        return "Jogador venceu!"
    else:
        return "Computador venceu!"


# Função para exibir placar
def exibir_placar(jogador_pontos, computador_pontos):
    print(DIVISOR)
    print("PLACAR")
    print(f"JOGADOR: {jogador_pontos}")
    print(f"COMPUTADOR: {computador_pontos}")
    print(DIVISOR)


# Variáveis de pontuação
pontuacao_computador = 0
pontuacao_jogador = 0

# Loop principal do jogo
while True:
    print(DIVISOR)
    print("JOKENPÔ")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print(DIVISOR)

    # Escolha do jogador
    while True:
        try:
            jogador = int(input("Escolha sua jogada entre 1 e 3: ")) - 1
            print("JO")
            sleep(1)
            print("KEN")
            sleep(1)
            print("PÔ!!!")
            if jogador not in [0, 1, 2]:
                raise ValueError
            break
        except ValueError:
            print(DIVISOR)
            print("Entrada inválida. Digite um número entre 1 e 3.")
            print(DIVISOR)

    # Escolha do computador
    computador = randint(0, 2)

    # Exibir escolhas e resultado
    print(DIVISOR)
    print(f"JOGADOR escolheu: {ITENS[jogador]}.")
    print(f"COMPUTADOR escolheu: {ITENS[computador]}.")
    resultado = jokenpo(computador, jogador)
    print(f"RESULTADO: {resultado}")

    # Atualizar placar
    if resultado == "Jogador venceu!":
        pontuacao_jogador += 1
    elif resultado == "Computador venceu!":
        pontuacao_computador += 1

    exibir_placar(pontuacao_jogador, pontuacao_computador)

    # Perguntar se o jogador quer continuar
    while True:
        continuar = input("Quer jogar de novo? (s/n): ").strip().lower()
        if continuar not in ["s", "n"]:
            print(DIVISOR)
            print("Entrada inválida! Digite 's' para sim ou 'n' para não.")
            print(DIVISOR)
        else:
            break

    if continuar == "n":
        print("Obrigado por jogar! Até a próxima.")
        exibir_placar(pontuacao_jogador, pontuacao_computador)
        break

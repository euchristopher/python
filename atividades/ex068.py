import random

while True:
    # Entrada do jogador
    jogador = int(input("\nDigite um valor: "))
    pc = random.randint(1, 10)
    escolha = input("Par ou ímpar? (digite 'p' para par ou 'i' para ímpar): ").strip().lower()

    # Validação da escolha
    if escolha not in ['p', 'i']:
        print("[ERROR] Digite 'p' (par) ou 'i' (ímpar) para continuar.")
        continue

    # Soma de valores
    soma = jogador + pc
    resultado = 'p' if soma % 2 == 0 else 'i'

    # Exibição do resultado
    print(f"\nVocê escolheu {jogador} e o computador escolheu {pc}.")
    print(f"A soma é {soma}, que é {'par' if resultado == 'p' else 'ímpar'}.")

    # Determinação do vencedor
    if escolha == resultado:
        print("Parabéns! Você venceu!")
    else:
        print("O computador venceu! Jogo encerrado.")
        break  # Encerra o programa

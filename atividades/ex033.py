while True:
    while True:
        try:
            dataNascimento = int(input("Digite a sua data de nascimento: "))
            break
        except ValueError:
            print("Data de nascimento inválida! Tente novamente.")

    dataAtual = 2024
    idade = dataAtual - dataNascimento

    if idade < 14:
        print(f"Você tem {idade} anos, não pode se alistar.")
    elif 14 <= idade <= 16:
        print(f"Você tem {idade} anos, pode se alistar, mas não é obrigatório.")
    else:
        print(f"Você tem {idade} anos, alistamento obrigatório.")

    repetir = input("Deseja repetir? (s/n): ").strip().lower()
    if repetir != "s":
        print("Programa encerrado.")
    break

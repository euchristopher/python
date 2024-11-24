from datetime import datetime

# Data Atual
data_atual = datetime.now()

# Loop principal
while True:
    # Loop de pergunta
    while True:
        try:
            # Solicita a data de nascimento no formato dd/mm/yyyy
            data_nascimento_str = input(
                "Digite a sua data de nascimento (dd/mm/yyyy): "
            )

            # Converte a string para objeto datetime
            data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

            # Verifica se a data está no futuro
            if data_nascimento > data_atual:
                print(
                    f"A data inserida ultrapassa a data atual. Por favor, digite novamente."
                )
                continue

            # Sai do loop interno se a data for válida
            break
        except ValueError:
            print(f"Data inválida. Insira a data no formato: dd/mm/yyyy.")

    # Cálculo da idade
    idade = data_atual.year - data_nascimento.year

    # Ajusta a idade se o aniversário ainda não aconteceu no ano atual
    if (data_atual.month, data_atual.day) < (
        data_nascimento.month,
        data_nascimento.day,
    ):
        idade -= 1

    # Verifica a elegibilidade para alistamento
    if idade < 14:
        print(f"Você tem {idade} anos. Ainda não pode se alistar.")
    elif 14 <= idade <= 16:
        print(f"Você tem {idade} anos. Está na idade opcional de alistamento.")
    else:
        print(f"Você tem {idade} anos. Já pode se alistar!")

    # Pergunta se deseja continuar
    repetir = input("Deseja verificar outra data? (s/n): ").lower()
    if repetir != "s":
        print("Programa encerrado.")
        break
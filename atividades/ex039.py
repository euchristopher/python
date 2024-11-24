from datetime import datetime

# Data Atual
data_atual = datetime.now()

# Loop Principal
while True:
    # Loop de Pergunta
    while True:
        try:
            # Solicita a data de nascimento como string
            data_nascimento_str = input("Digite a data de nascimento (dd/mm/ano): ")

            # Converte a data string para objeto datetime
            data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

            # Verifica se está no futuro
            if data_nascimento > data_atual:
                print("A data de nascimento ultrapassa a data atual. Digite novamente.")
                continue
            break
        except ValueError:
            print("Data inválida. Digite novamente no formato dd/mm/yyyy.")

    def calcular(data_atual, data_nascimento):
        # Calcula idade
        idade = data_atual.year - data_nascimento.year

        # Ajusta a idade se o aniversário ainda não aconteceu no ano atual
        if (data_atual.month, data_atual.day) < (
            data_nascimento.month,
            data_nascimento.day,
        ):
            idade -= 1

        # Determina a categoria
        if idade <= 9:
            categoria = "Mirim"
        elif 10 <= idade <= 14:
            categoria = "Infantil"
        elif 15 <= idade <= 19:
            categoria = "Junior"
        elif idade == 20:
            categoria = "Sênior"
        else:
            categoria = "Master"

        # Retorna a idade e a categoria
        return idade, categoria

    # Chama a função para calcular idade e categoria
    idade, categoria = calcular(data_atual, data_nascimento)

    # Resultado
    print(f"Idade do atleta: {idade}\nCategoria: {categoria}")

    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja verificar outra data? (s/n): ").lower()
    if continuar != "s":
        print("Programa encerrado.")
        break

cont_maior18 = contH = contM_menor18 = 0
divisor = '-' * 35

while True:
    # Entrada da idade com validação
    while True:
        try:
            print(divisor)
            idade = int(input("Idade: "))
            if idade < 0:
                print("[ERROR] Digite uma idade válida.")
                continue
            break
        except ValueError:
            print("[ERROR] Digite um número válido para idade.")

    # Entrada do gênero com validação
    sexo = ""
    while sexo not in ["H", "M"]:
        print(divisor)
        sexo = input('Gênero - [H/M]: ').strip().upper()
        if sexo not in ["H", "M"]:
            print('[ERROR] Digite "H" para homem ou "M" para mulher.')

    # Lógica de contagem
    if idade > 18:
        cont_maior18 += 1
    if sexo == "H":
        contH += 1
    if sexo == "M" and idade < 18:
        contM_menor18 += 1

    # Pergunta de continuidade
    continuar = ""
    while continuar not in ["S", "N"]:
        continuar = input("Deseja continuar? [S/N]: ").strip().upper()
        if continuar not in ["S", "N"]:
            print('[ERROR] Responda com "S" ou "N".')

    if continuar == "N":
        break

# Resultados finais
print(divisor)
print(f"Pessoas com mais de 18 anos: {cont_maior18}")
print(f"Homens cadastrados: {contH}")
print(f"Mulheres menores de 18 anos: {contM_menor18}")
print(divisor)

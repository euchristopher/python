# Inicialização de variáveis
cont_M = 0
cont_F = 0

while True:
    genero = input("Informe o seu gênero [M/F] ou digite 'SAIR' para encerrar: ").strip().upper()[0]

    # Verifica se o usuário deseja encerrar o programa
    if genero == 'SAIR':
        print("\nPROGRAMA ENCERRADO.")
        break

    # Validação do gênero
    if genero == 'M':
        cont_M += 1
        print("Gênero 'Masculino' registrado com sucesso!")
    elif genero == 'F':
        cont_F += 1
        print("Gênero 'Feminino' registrado com sucesso!")
    else:
        print("Valor inválido! Por favor, informe 'M', 'F' ou 'SAIR'.")

# Exibe o resumo final
print("\nResumo dos registros:")
print(f"- Homens registrados: {cont_M}")
print(f"- Mulheres registradas: {cont_F}")

# Inicializando os contadores
maior = 0
menor = 0

# Loop para ler os dados de 7 pessoas
for c in range(1, 8):  # range(1, 8) já cobre de 1 a 7
    ano_nascimento = int(input(f'Digite o ano de nascimento da pessoa {c}: '))
    
    # Verifica se o ano de nascimento é válido
    if ano_nascimento > 2024 or ano_nascimento < 1900:
        print("Ano de nascimento inválido. Tente novamente.")
        continue  # Pula para a próxima iteração se a entrada for inválida
    
    # Calcula a idade
    idade = 2024 - ano_nascimento
    
    # Incrementa os contadores de acordo com a idade
    if idade >= 18:
        maior += 1
    else:
        menor += 1

# Exibindo os resultados finais
print(f'\nPessoas maiores de idade: {maior}')
print(f'Pessoas menores de idade: {menor}')

soma_idades = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for c in range(1, 5):
    print(f'----- {c}ª Pessoa -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    # Soma das idades para calcular a média
    soma_idades += idade

    # Verifica o homem mais velho
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        homem_mais_velho = nome

    # Conta mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

# Calcula a média das idades
media_idades = soma_idades / 4

print('\n----- RESULTADOS -----')
print(f'A média de idade do grupo é: {media_idades:.0f} anos.')
if homem_mais_velho:
    print(f'O homem mais velho é {homem_mais_velho}, com {idade_homem_mais_velho} anos.')
else:
    print('Não há homens no grupo.')
print(f'Há {mulheres_menos_20} mulher(es) com menos de 20 anos.')

divisor = '-' * 35
print("Progressão Aritmética (PA)")
print(divisor)

# Entrada dos valores iniciais
pa = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print(divisor)

# Variáveis de controle
termo = pa
cont = 1
total = 0
mais = 10

# Loop principal
while mais != 0:
    total += mais  # Atualiza o total de termos a serem exibidos
    while cont <= total:  # Exibe os termos da PA até o total acumulado
        print(f'{termo} ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))

print(f'Progressão finalizada com {total} termos exibidos.')

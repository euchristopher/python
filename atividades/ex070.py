total = 0
produto_1000 = 0
menor_valor = float('inf')  # Define o menor valor como infinito
produto_mais_barato = ''
while True:
    # Entrada do nome do produto
    produto = input('Nome do produto: ').strip()
    if not produto:
        print('[ERROR] Não deixe o nome do produto em branco.')
        continue

    # Entrada do valor do produto
    try:
        valor = float(input('Valor: '))
    except ValueError:
        print('[ERROR] Digite um valor válido para o preço.')
        continue

    if valor < 0:
        print('[ERROR] O valor não pode ser negativo.')
        continue
    
    # Atualiza total de gastos
    total += valor

    # Verifica se o produto custa mais de 1000
    if valor > 1000:
        produto_1000 += 1

    # Verifica se o valor do produto é o menor até o momento
    if valor < menor_valor:
        menor_valor = valor
        produto_mais_barato = produto

    # Pergunta se deseja continuar
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        print('[ERROR] Responda com "S" para continuar ou "N" para encerrar.')

# Exibição do resultado
print(f'\nTotal gasto: R$ {total:.2f}')
print(f'Quantidade de produtos que custam mais de R$ 1000: {produto_1000}')
print(f'O produto mais barato foi "{produto_mais_barato}" que custa R$ {menor_valor:.2f}')

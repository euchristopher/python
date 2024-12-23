# Entrada do valor a ser sacado
valor = int(input('Valor a ser sacado: '))

# Inicializa o total restante para o valor a ser sacado
total = valor

# Define a maior cédula disponível inicialmente
ced = 50

# Contador para acompanhar quantas cédulas de cada tipo foram usadas
total_ced = 0

# Loop principal: continua até que todo o valor seja distribuído em cédulas
while True:
    # Verifica se ainda podemos usar a cédula atual para subtrair do total
    if total >= ced:
        total -= ced  # Subtrai o valor da cédula do total restante
        total_ced += 1  # Incrementa o contador de cédulas usadas
    else:
        # Se usamos alguma cédula, mostramos o total de cédulas usadas desse tipo
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R${ced}')
        
        # Troca para a próxima menor cédula disponível
        if ced == 50:
            ced = 20  # Se a cédula era de R$50, passa para R$20
        elif ced == 20:
            ced = 10  # Se a cédula era de R$20, passa para R$10
        elif ced == 10:
            ced = 1  # Se a cédula era de R$10, passa para R$1
        
        # Reinicia o contador de cédulas para a próxima denominação
        total_ced = 0
        
        # Se o total restante é zero, encerra o loop
        if total == 0:
            break

# Mensagem final para o usuário
print('Volte sempre!')

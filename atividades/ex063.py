# Exibe o divisor e o título do programa
divisor = '-' * 35
print(divisor)
print('Sequência de Fibonacci')
print(divisor)

# Solicita o número de termos ao usuário
n = int(input('Quantos termos você quer mostrar?: '))
print(divisor)

# Inicializa os dois primeiros termos
t1 = 0
t2 = 1
cont = 3  # O contador começa no terceiro termo, já que os dois primeiros já estão definidos

# Exibe os dois primeiros termos da sequência
print(f'{t1} {t2}', end=' ')

# Gera os termos da sequência até o número solicitado
while cont <= n:
    t3 = t1 + t2
    print(f'{t3}', end=' ')
    t1 = t2
    t2 = t3
    cont += 1

# Finaliza o programa com um divisor e uma mensagem de encerramento
print('\n' + divisor)
print('FIM DO PROGRAMA')

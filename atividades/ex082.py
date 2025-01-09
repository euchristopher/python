valores = []
par = []
impar = []

while True:
    num = int(input('Digite um valor: '))
    
    if num == 99:
        break
    
    valores.append(num)  # Adiciona o número na lista de valores
    
    if num % 2 == 0:
        par.append(num)  # Adiciona em 'par' se o número for par
    else:
        impar.append(num)  # Adiciona em 'impar' se o número for ímpar

# Ordena as listas
valores.sort()
par.sort()
impar.sort()

# Exibe as listas
print(f'Todos os valores: {valores}')
print(f'Valores PAR: {par}')
print(f'Valores IMPAR: {impar}')

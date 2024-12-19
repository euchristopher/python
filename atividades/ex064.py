# Variável
n = total = soma = 0
divisor = '-' * 35
# Loop
print(divisor)
while True:
  n = int(input('Digite um numero: '))
  if n == 999:
    break
  soma += n
  total += 1
  
# Resultado
print(divisor)
print(f'- Total de números digitados: {total}')
print(f'- Soma total: {soma}')
print(f'- Fim do Programa')

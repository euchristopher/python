divisor = '-' * 35
print(divisor)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
print(f'{divisor}')
termo = primeiro
cont = 1
while cont <= 10:
  print(f'{termo} ', end='')
  termo += razao
  cont += 1
print(f'\n{divisor}')
print(f'\nFIM DO PROGRAMA')

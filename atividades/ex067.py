DIVISOR = '-' * 35
cont = 1

while True:
  print(f'\nTABUADA')
  print(f'{DIVISOR}')
  n = int(input(f'Digite um valor: '))
  if n == -1:
    break
  
  while cont <= 10:
    res = n * cont
    print(f'{n} x {cont} = {res}')
    cont += 1
print(f'{DIVISOR}')
print(f'PROGRAMA ENCERRADO')
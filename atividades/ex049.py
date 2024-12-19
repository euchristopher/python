from time import sleep
DIVISOR = '-' * 40
n = int(input('Digite um valor para gerar a tabuada: '))
print(DIVISOR)
print(f'Tabuada de {n}')
for i in range(1, 11):
  print(f'{n} x {i} = {n * i}')
  sleep(1)
print(DIVISOR)
print(f'Fim da tabuada.')
n = int(input('Digite um número e veja o fatorial: '))
c = n
f = 1
print(f'CALCULANDO O FATORIAL DE {n}')
while c > 0:
  print(f'{c}', end='')
  print(f' x ' if c > 1 else ' = ', end='')
  f *= c
  c -= 1
print(f'{f}')
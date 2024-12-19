num = int(input('DIgite um numero: '))
tot = 0
for c in range(1, num, +1):
  if num % c == 0:
    print(f'\033[33m', end='')
    tot += 1
  else:
    print('\033[31m', end='')
  print({c}, end='')
print(f'\nO numero {num} foi divisível {tot} vezes')
if tot == 2:
  print('E PRIMO')
else:
  print('E COMPOSTO')
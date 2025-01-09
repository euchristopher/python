n = (int(input('Digite o valor 1: ')), int(input('Digite o valor 2: ')), 
     int(input('Digite o valor 3: ')), int(input('Digite o valor 4: ')))

print(f'Valores digitados: {n}')
print(f'O valor 9 aparece {n.count(9)} vezes')
if 3 in n:
  print(f'O valor 3 apareceu na {n.index(3)+1} posição')
else:
  print(f'O valor 3 não foi inserido.')
for num in n:
  if num % 2 == 0:
    print(f'Valores pares: {num}')
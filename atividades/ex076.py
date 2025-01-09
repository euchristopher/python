lista = ('Caderno', 25.90, 
         'Lápis', 1.50, 
         'Borracha', 2,
         'Caneta', 1.75, 
         'Mochila', 59.90)
print('-'* 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)
for pos in range(0, len(lista)):
  if pos % 2 == 0:
    print(f'{lista[pos]:.<30}', end='')
  else:
    print(f'R${lista[pos]:>6.2f}')
print(f'-'*40)
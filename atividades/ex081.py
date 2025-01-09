valores = []
total = 0
while True:
  num = int(input(f'Digite um valor: '))
  
  if num == 99:
    break
  
  if num in valores:
    print(f'Valor existente em lista, escolha outro.')
  else:
    print(f'Valor {num} adicionado!')
    total += 1
    valores.append(num)

valores.sort(reverse=True)
  
print(f'Valores: {valores}')
print(f'Total de valores adicionados: {total}')
if 5 in valores:
  print(f'O valor 5 foi adicionado a lista e esta na posição {valores.index(5)+1}')

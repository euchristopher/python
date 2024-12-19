cont = 0
soma = 0
for c in range(1, 7):
  n = int(input(f'Digite o valor de {c}: '))
  if n % 2 == 0:
    soma += n
    cont += +1
print(f'Foram {cont} valores, e a soma dos números pares e de {soma}')
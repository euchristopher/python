maior_peso = -float('inf')
menor_peso = float('inf')
for c in range(1, 6):
  peso = float(input(f'Qual é o peso em kg da pessoa {c}?: '))
  if peso > maior_peso:
    maior_peso = peso
  if peso < menor_peso:
    menor_peso = peso
print(f'O maior peso: {maior_peso:.2f}.')
print(f'O menor peso: {menor_peso:.2f}.')
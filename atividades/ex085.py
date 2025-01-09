nome = []
peso = []
dados = list(zip(nome, peso))
contP = 1
while True:
  pessoa = input(f'Digite o nome da pessoa {contP}: ').lower()
  nome.append(pessoa)
  peso0 = float(input(f'Peso da pessoa {contP}: '))
  peso.append(peso0)
  dados.append(nome, peso)
  contP += 1
  
  if pessoa == 'n':
    break

print(dados)
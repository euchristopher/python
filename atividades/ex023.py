nome = str(input('Digite o seu nome completo: ')).strip()
nomeC = nome.split()
nome1 = nomeC[0]
nome2 = nomeC[-1]

print(f'O seu primeiro nome e {nome1}.')
print(f'O seu segundo nome e {nome2}.')
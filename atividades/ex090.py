dados = {}

while True:
    nome = input('Aluno: ')
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    
    dados[nome] = media
    
    end = input('Encerrar o programa? [S/N]: ').lower()
    if end == 's':
      break
    
for nome, media in dados.items():
  print(f'Aluno: {nome}')
  print(f'Media: {media}')
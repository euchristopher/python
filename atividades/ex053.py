frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1] #Método do fatiamento
'''for letra in range(len(junto) - 1, -1, -1):
  inverso += junto[letra]'''
print(f'O inverso de {junto} e {inverso}')
if inverso == junto:
  print('PALÍNDROMO')
else:
  print('NÃO É POLÍDROMO')
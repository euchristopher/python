n = soma = contador = 0
maior = menor = None

while True:
  
  n = int(input('Digite um numero: '))
  
  if n == 999:
    break
  
  soma += n
  contador += 1
  media = soma / contador if contador > 0 else 0
  
  if contador == 1:
    maior = menor = n
    
  else: 
    if maior is None or n > maior:
      maior = n
      
    if menor is None or n < menor:
      menor = n

print(f'\nResultados')
print(f'Total: {contador}')
print(f'Soma: {soma}')
print(f'Media: {media}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Programa Encerrado')
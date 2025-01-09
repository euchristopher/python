cont = ('Zero', 'Um', 'Dois','Três', 'Quatro', 'Cinco', 
     'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 
     'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 
     'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
  n = int(input('Digite um valor entre 0 e 20: '))
  if 0 <= n >= 20:
    print(f'Tente novamente')
    continue
  print(f'{cont[n]}')
  
  continuar = input(f'Continuar? [S/N]: ').lower()
  if continuar != 's':
    print(f'Programa Encerrado.')
    break
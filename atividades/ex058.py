from random import randint
from time import sleep

pc = randint(1, 3)
tentativa = 0
DIVISOR = '-' * 30

while True:
  print(DIVISOR)
  print(f'---Tente adivinhar o número que estou pensando!---')
  print(f'Escolha um número de 1 até 3')
  palpite = int(input('Digite um número: '))
  tentativa += 1
  
  while pc != palpite:
    sleep(1)
    print(DIVISOR)
    print(f'Errou! tente de novo!')
    palpite = int(input('Digite outro valor: '))
    tentativa += 1
    
  sleep(1)
  print(DIVISOR)
  print(f'- Eu escolhi o número {pc} e você escolheu o {palpite}.')
  print(f'- Você precisou de {tentativa} tentativas para acertar!')
  print(DIVISOR)

  while True:
    continuar = str(input('Quer jogar de novo? [S/N]: ')).strip().upper()
    if continuar not in ['S', 'N']:
      print(f'Entrada invalida! digite "S" ou "N".')
    else:
      break
    if continuar == 'N':
      print(f'Obrigado por jogar!')
      break
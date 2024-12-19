DIVISOR = '-' * 35
menu = 0
while menu != 5:
    try:
          #ESCOLHA DO USUARIO
          n1 = float(input('Digite o valor do número 1: '))
          n2 = float(input('Digite o valor do número 2: '))
        # EXIBE O MENU
          print(DIVISOR)
          print(f'\nMENU MATEMÁTICO')
          print(f'\nEscolha uma das opções:\n')
          print(f'[1] Somar')
          print(f'[2] Multiplicar')
          print(f'[3] Maior')
          print(f'[4] Novos números')
          print(f'[5] Sair do programa\n')
          print(DIVISOR)
        
          #AVISO DE ERRO
          menu = int(input('Digite a escolha: '))
          if menu not in [1, 2, 3, 4, 5]:
            raise ValueError
        
          # Lógica do menu
          if menu == 1:
              print(DIVISOR)
              print(f'SOMA\n')
              soma = n1 + n2
              print(f'O valor de: {n1:g} + {n2:g} = {soma:g}')
              print(DIVISOR)
            
          elif menu == 2:
            print(DIVISOR)
            print(f'MULTIPLICAÇÃO\n')
            multi = n1 * n2 
            print(f'O valor de: {n1:g} x {n2:g} = {multi:g}')
            print(DIVISOR)
          
          elif menu == 3:
            print(DIVISOR)
            print(f'MAIOR VALOR\n')
            maior = max(n1, n2)
            print(f'O maior valor entre {n1:g} e {n2:g} o maior valor é {maior:g}')
            print(DIVISOR)
            
          elif menu == 4:
            print(DIVISOR)
            print(f'Escolha novos números\n')
            print(DIVISOR)
            
          else:
            print(DIVISOR)
            print(f'PROGRAMA ENCERRADO')
            
    except ValueError:
        print(DIVISOR)
        print('Escolha inválida! Por favor, selecione uma opção entre 1 e 5.')
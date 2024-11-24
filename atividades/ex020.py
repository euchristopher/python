texto = input("Digite o nome da sua cidade: ")
palavra = "Santo"

if palavra == texto:
    print(f'A sua cidade tem "{palavra.upper()}" no nome.')
else:
    print(f'O nome "{palavra.upper()}" não foi encontrada.')

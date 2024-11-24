print("Vamos ver se o número é par ou ímpar. Digite um número abaixo.")

# Solicita o número ao usuário
numero = int(input("Digite um número: "))

# Verifica se o número é par
if numero % 2 == 0:
    print(f"O número {numero} é par!")
else:
    print(f"O número {numero} é ímpar!")

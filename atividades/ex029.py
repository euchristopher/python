# Solicita os três números ao usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

# Encontra o maior e o menor número
maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

# Exibe o resultado
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

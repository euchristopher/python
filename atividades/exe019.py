# Campo para solicitar um numero
numero = input('Digite um numereo de 1 ate 9999: ')

#Verifica se possui 4 caracteres
numero = numero.zfill(4)

# Faz a separação das casas
unidade = numero[0]
centena = numero[1]
dezena = numero[2]
milhar = numero[3]

# Resultado
print(f'Unidade: {milhar}')
print(f'Centena: {centena}')
print(f'Dezena: {dezena}')
print(f'Milhar: {milhar}')
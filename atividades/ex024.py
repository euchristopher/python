import random

numeroM = random.randint(1, 5)

print(f"Tente advinhar o numereo que a maquina escolheu!")
numeroU = int(input("Digite um numero: "))

if numeroU == numeroM:
    print(f"Voce acertou! :)1 eu escolhi o numero {numeroM}!")
else:
    print(f"Voce errou:(, eu pensi no numero {numeroM}")

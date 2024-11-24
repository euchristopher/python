import random

nomes = ["Marcos", "Eduarda", "Rayssa", "Pedro", "Lucas", "Felipe"]

resultado = random.shuffle(nomes)

print(f"Ordem de apresentação:")
for i, nome in enumerate(nomes, start=1):
    print(f"{i}º: {nome}")

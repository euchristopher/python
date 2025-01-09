from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)
maior = max(n)
menor = min(n)
print(f'Os valores sorteados foram:\n{n}')
print(f'O maior valor foi: {maior}')
print(f'O menor valor foi: {menor}')
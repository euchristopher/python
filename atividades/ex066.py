c = n = s = 0
while True:
  n = int(input('Digite um número: '))
  if n == 999:
    break
  c += 1
  s += n
print(f'Total de números digitados: {c}')
print(f'Soma: {s}')
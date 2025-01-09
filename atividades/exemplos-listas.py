num = [2, 4, 6, 8]
num[2] = 3
num.append(7)
num.insert(1, 0)
num.pop(3)
num.remove(0)
if 5 in num:
  num.remove(5)
else:
  print(f'Valor "5" nao encontrado')
num.sort()
print(num)
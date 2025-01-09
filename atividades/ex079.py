valores = []  # Lista para armazenar os valores

while True:
    add = int(input('Adicionar um valor (digite 99 para parar): '))
    if add == 99:  # Condição de parada
        break
    if add in valores:  # Verifica se o valor já está na lista
        print(f"O número {add} já foi adicionado. Tente outro.")
    else:
        valores.append(add)  # Adiciona o valor à lista
        valores.sort()
        print(f"Valor {add} adicionado!")

print("\nOs valores digitados foram:")
print(valores)

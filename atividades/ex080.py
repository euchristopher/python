valores = []
for c in range(5):
    num = int(input(f"Digite o {c + 1}º valor: "))
    
    pos = 0
    while pos < len(valores):
        if num <= valores[pos]:
            valores.insert(pos, num)
            print(f"Adicionado {num} na posição {pos} da lista!")
            break
        pos += 1
    
    # Se o número não foi inserido no loop, ele é adicionado ao final
    else:
        valores.append(num)
        print(f"Adicionado {num} na última posição da lista!")

print("\nOs valores digitados em ordem:")
print(valores)

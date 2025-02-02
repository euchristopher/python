from time import sleep


def maior(*num):
    cont = maior = 0
    print("Analisando os valores...")
    for valor in num:
        print(f"{valor}", end=" ", flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informado {cont} valores ao todo")
    print(f"O maior valor e {maior}")


maior(2, 9, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

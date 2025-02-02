from time import sleep


def cont(i, f, p):
    if p < 0:
        p *= -1

    if p == 0:
        p = i

    print("-" * 40)
    print(f"Contagens de {i} ate {f} de {p} em {p}")
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=", ", flush=True)
            sleep(0.5)
            cont += p
        print("FIM")

    else:
        cont = i
        while cont >= f:
            print(f"{cont}", end=", ", flush=True)
            sleep(0.5)
            cont -= p
        print("FIM")


cont(1, 10, 1)
cont(10, 0, 2)
print("-" * 40)
print("Agora e a sua vez de personalizar a contagem!")
ini = int(input(f"Inicio: "))
fim = int(input(f"Fim: "))
pas = int(input(f"Passo: "))
cont(ini, fim, pas)

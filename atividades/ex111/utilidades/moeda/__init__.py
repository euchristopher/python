def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if not formato else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if not formato else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda="R$"):
    return f"{moeda}{preco:.2f}".replace(".", ",")


def resumo(preco=0, taxaA=10, taxaR=5):
    divisor = "-" * 40
    print(divisor)
    print(f"RESUMO DO VALOR".center(30))
    print(divisor)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metade do preço: \t{metade(preco, True)}")
    print(f"Com {taxaA}% de aumento: \t{aumentar(preco, taxaA, True)}")
    print(f"Com {taxaR}% de redução: \t{diminuir(preco, taxaR, True)}")
    print(divisor)

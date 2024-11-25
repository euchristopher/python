while True:
    while True:
        try:
            print("-" * 40)
            print(f"--CALCULAR O VALOR DO PRODUTO--")
            produto = float(input("Digite o valor do produto: "))
            break
        except ValueError:
            print(f"[ERROR] Digite um valor valido.")

    # Metodo de pagamento
    print("-" * 40)
    print("--FORMAS DE PAGAMENTIO--")
    print(f"1 - A vista dinheiro/cheque(10% de desconto\n2 - A vista cartao (5% de desconto)\n3 - 2x no cartao (preco normal\n4 - 3x ou mais no cartao (20% de juros))")

    def pagamento(produto):
        1 = produto - (10/100)
        2 = produto - (5/100)
        3 = produto
        4 = produto + (20/100)

        if produto == 1:
            return 1
        elif produto == 2:
            return 2
        elif produto == 3:
            return 3
        else:
            return 4
        
    
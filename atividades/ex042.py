# Loop Principa;
while True:
    # Loop de pergunta do produto
    while True:
        try:
            print("-" * 40)
            produto = float(input("Digite o valor do produto: R$ "))
            break
        except ValueError:
            print("-" * 40)
            print(f"Digite um numero valido.")
            continue

        # Exibe as opções de pagamento
    print("-" * 40)
    print("--FORMAS DE PAGAMENTO--")
    print("1 - À vista dinheiro/cheque (10% de desconto)")
    print("2 - À vista cartão (5% de desconto)")
    print("3 - 2x no cartão (preço normal)")
    print("4 - 3x ou mais no cartão (20% de juros)")

    # Loop do metodo de pagamentio
    while True:
        try:
            opcao = int(input("Escolha a forma de pagamento (1-4): "))
            if opcao not in [1, 2, 3, 4]:
                raise ValueError("Opcao invalida.")
            break
        except ValueError:
            print("[ERROR] Digite um valor entre 1 e 4.")

    # Calcular o valor do produto
    def calcular_valor(produto, opcao):
        if opcao == 1:
            valor_final = produto - (produto * (10 / 100))
            metodo = "A vista em dinheiro/chque"
        elif opcao == 2:
            valor_final = produto - (produto * (5 / 100))
            metodo = "A vista no cartao"
        elif opcao == 3:
            valor_final = produto
            metodo = "Em 2x no cartao"
        else:
            valor_final = produto + (produto * (20 / 100))
            metodo = "3x ou mais no cartao"
        return valor_final, metodo

    valor_final, metodo = calcular_valor(produto, opcao)

    print("-" * 40)
    print(f"Valor original do produto: R$ {produto}.")
    print(f"Forma de pagamento: {metodo}.")
    print(f"Valor final a pagar: {valor_final}.")
    print(f"-" * 40)

    continuar = input("Deseja calcular outro produto? (s/n): ")
    if continuar != "s":
        print("Programa encerrado.")
        break

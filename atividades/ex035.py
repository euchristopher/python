# Entrada de dados
valorCasa = float(input("Digite o valor da casa: "))  # Valor da casa
salario = float(input("Digite o seu salario bruto: "))  # Salario bruto do client
parcela = int(input("Digite em quantos anos deseja pagar: "))  # parcelas em ANOS

# Calculos
cm = parcela * 12  # Conversor de ANOS para MESES
pm = valorCasa / cm  # Calcula a prestacao mensal
limite = salario * 30 / 100

# Verificacao
if pm > limite:
    print(f"A parcela de {pm:.2f} reais excede o limite de 30% do salario. NEGADO")
else:
    print(
        f"A parcela de {pm:.2f} reais esta dentro do limite de 30% do salario. APROVADO"
    )

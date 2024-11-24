# Solicita o salário do usuário
salario = float(input("Digite o salário: "))

# Verifica o valor do aumento com base no salário
if salario <= 1250.00:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)

# Exibe o novo salário com formatação de duas casas decimais
print(f"Novo salário: R${aumento:.2f}")

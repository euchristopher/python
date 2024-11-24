# Seletor de Dias e KM
dias = int(input("Quantos dias o carro foi alugado?: "))
km = float(input("QUantos KM foram pecorridos?: "))

# Seletor dos valores
valorD = dias * 60
valorKM = km * 0.15
somaFinal = valorD + valorKM

# Resultado
print(f"O valor a pagar é de R${somaFinal:.2f} reais.")

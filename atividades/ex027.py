# Solicita a distância percorrida
distancia = int(input("Quantos km foram percorridos?: "))

# Define o preço por km dependendo da distância
if distancia <= 200:
    preco_por_km = 0.50
else:
    preco_por_km = 0.45

# Calcula o preço da viagem
preco_total = distancia * preco_por_km

# Exibe o preço da viagem com duas casas decimais
print(f"O preço da viagem custou R${preco_total:.2f} reais.")

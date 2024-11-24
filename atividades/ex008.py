# Solicitar o preço do produto
preco = float(input("Digite o valor do produto: "))

# Calcular o desconto do produto
desconto = preco * 0.5

# Calcular o preço final do produto
preco_desconto = preco - desconto

# Resultado
print(f"O Preço do produto é {preco:.2f}.")
print(f"O valor do desconto é de {desconto:.2f}.")
print(f"O valor do produto com 10% de desconto é {preco_desconto:.2f}")

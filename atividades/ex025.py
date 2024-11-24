# Solicitar a velocidade do carro (em km/h)
velocidade = int(input("Digite a velocidade do carro (em km/h): "))

# Definir o valor da multa
valor_multa = 7

# Verificar se o limite de velocidade foi ultrapassado (80 km/h)
if velocidade > 80:
    multa = (
        velocidade - 80
    ) * valor_multa  # A multa é calculada com base nos km/h acima do limite
    print(
        f"O carro percorreu a {velocidade} km/h, limite ultrapassado. Valor da multa: R${multa:.2f}."
    )
else:
    print(f"Velocidade dentro do limite. Sem multa.")

# Import de módulos matemáticos
import math

# Solicitando ângulo
angulo = float(input("Digite o valor do angulo: "))

# Convertendo Ângulo em Radiano
radianos = math.radians(angulo)

# Calculando o Ângulo
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

# Resultado
print(f"O angulo de {angulo} tem: ")
print(f"Seno: {seno:.2f}.")
print(f"Cosseno: {cosseno:.2f}.")
print(f"Tangente: {tangente:.2f}.")

# Solicitando Altura e Largura
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

# Calculando a área
area = largura * altura

# Calculando a quantidade de tinta
tinta = area / 2

# Resultado
print(f'A Área da parede é {area:.2f} m².')
print(f'A quantidade de tinta necessária para pintar a parede é de {tinta:.2f} litros.')
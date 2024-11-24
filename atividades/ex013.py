import math

catetoO = float(input("Digite o cumprimento do cateto oposto: "))
catetoA = float(input("Digite o cumprimento do cateto adjacente: "))
hipotenusa = math.sqrt(catetoO**2 + catetoA**2)
print(f"O cumprimento da hipotenusa é {hipotenusa:.2f}.")

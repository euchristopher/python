def triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


print("Escreva 3 numeros para cada reta e veja se forma um triangulo!")
a = float(input("Digite o valor da primeira reta: "))
b = float(input("Digite o valor da primeira reta: "))
c = float(input("Digite o valor da primeira reta: "))

if triangulo(a, b, c):
    print(f"Forma um triangulo")
else:
    print("Nao forma um triangulo")

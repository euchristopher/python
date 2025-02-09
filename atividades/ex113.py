def leiaInt(num):
    while True:
        try:
            n = int(input(num).strip())
        except (ValueError, TypeError):
            print("[ERROR] Digite um valor inteiro valido.")
            continue
        except KeyboardInterrupt:
            print
            ("[ERROR] O usuario preferiu nao digitar um valor. Valor retornado: 0")
            return 0
        else:
            return n


def leiaFloat(num):
    while True:
        try:
            n = float(input(num).strip())
        except (ValueError, TypeError):
            print(f"[ERROR] Valor digitado invalido.")
            continue
        except KeyboardInterrupt:
            print
            ("[ERROR] O usuario preferiu nao digitar um valor. Valor retornado: 0")
            return 0
        else:
            return n


num1 = leiaInt("Digite um valor INTEIRO: ")
num2 = leiaFloat("Digite um valor REAL: ")
print(f"Valor INTEIRO digitado: {num1}")
print(f"Valor REAL digitado: {num2}")

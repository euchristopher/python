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


num = leiaInt("Digite um valor: ")
print(f"Valor digitado: {num}")

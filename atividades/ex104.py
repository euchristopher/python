def leiInt(msg):
    while True:
        n = input(msg)  # Recebe a entrada do usuário

        if n.isnumeric():  # Verifica se a entrada é numérica
            msg = int(n)
            return f"Voce digitou o numero {n}"
        elif n == "":
            return f"Espaco vazio"
        else:
            return f"Erro! Digite um número inteiro válido."


# Programa Principal
n = leiInt("Digite um número: ")  # Chama a função para ler um número inteiro
print(n)

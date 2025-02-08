def leiInt(msg):
    while True:
        try:
            n = int(input(msg).strip())
            return f"Valor digitado: {n}"
        except ValueError:
            print("[ERROR] Por favor, digite um número inteiro válido.")
        except KeyboardInterrupt:
            print("\n[ERROR] Entrada interrompida pelo usuário.")
            return "Nenhum valor foi digitado."
        except EOFError:
            print("\n[ERROR] Entrada inesperadamente encerrada.")
            return "Nenhum valor foi digitado."
        finally:
          print('Programa encerrado.')


# Programa Principal
print("Testando a função leiInt:")
n = leiInt("Digite um número: ")
print(n)

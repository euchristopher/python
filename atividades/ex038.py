# Loop Principal
while True:
    # Loop de perguntas
    while True:
        try:
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            break
        except ValueError:
            print(f"[ERROR] Nota invalida. Digite novamente.")

    # Função para calcular a média
    def calcular(nota1, nota2):
        media = (nota1 + nota2) / 2

        # Status Final
        if media < 5:
            resultado = "Reprovado"
        elif 5 <= media < 7:
            resultado = "Recuperação"
        else:
            resultado = "Aprovado"

        # Retorna a media e o resultado
        return media, resultado

    # Chamada da função
    media, resultado = calcular(nota1, nota2)

    # Resultado
    print(f"Média final: {media:.1f}.\nSituação: {resultado}")

    # Pergunta se deseja continuar
    continuar = input("Deseja calcular outra média? (s/n): ")
    if continuar != "s":
        print(f"Programa encerrado")
        break
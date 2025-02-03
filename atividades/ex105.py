def notas(*valores, sit=False):

    if not valores:
        return "Nenhuma nota foi informada."

    dados = {
        "Total de notas": len(valores),
        "Maior nota": max(valores),
        "Menor nota": min(valores),
        "Média da turma": round(sum(valores) / len(valores), 2),
    }

    if sit:
        if dados["Média da turma"] >= 7:
            dados["Situação"] = "Boa"
        elif dados["Média da turma"] >= 5:
            dados["Situação"] = "Razoável"
        else:
            dados["Situação"] = "Ruim"

    return dados


# Exemplo de uso:
res = notas(7.5, 8, 6, 9, 5.5, sit=True)
for k, v in res.items():
    print(f"{k}: {v}")

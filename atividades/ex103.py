def ficha(jog="<desconhecido>", gol=0):
    print(f"O jogador {jog} fez {gol} gol(s) no campeonato.")


# Programa Principal
n = str(input("Nome do jogador: ")).strip()
g = input("Gols marcados: ")

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == "":
    ficha(gol=g)
else:
    ficha(n, g)

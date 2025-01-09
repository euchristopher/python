times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
         'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama',
         'Vitória', 'Atlético Mineiro', 'Fluminense', 'Grêmio', 'Red Bull Bragantino'
         'Juventude', 'Sport', 'Ceará', 'Santos', 'América Mineiro')

print(f'5 Primeiros Colocados: {times[0:5]}')
print(f'4 Últimos Colocados: {times[-4:]}')
print(f'Tabela em ordem alfabética: \n{sorted(times)}')
print(f'O Flamengo esta na {times.index("Flamengo")+1} colocação')
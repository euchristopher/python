def voto(ano):
    from datetime import date

    atual = date.today().year
    idade = atual - ano
    
    if idade < 16:
      return f'Com {idade} anos: NAO Vota.'
    elif 16 <= idade < 18 or idade > 65:
      return f'Com {idade} anos: Voto OPCIONAL.'
    else:
      return f'Com {idade} anos: Voto OBRIGATORIO'
    
nasc = int(input('Ano de nascimento: '))
print(voto(nasc))

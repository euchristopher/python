def fatorial(n, show=False):
    """
    Calcula o fatorial de um número inteiro n.

    Parâmetros:
    -----------
    n : int
        O número inteiro para o qual o fatorial será calculado.
        Deve ser um número não negativo.

    show : bool, opcional
        Se True, exibe o processo de cálculo do fatorial no formato:
        n x (n-1) x ... x 1 = resultado.
        Se False (padrão), apenas retorna o valor do fatorial.

    Retorna:
    --------
    int
        O valor do fatorial de n.

    Exemplos:
    ---------
    >>> fatorial(5)
    120

    >>> fatorial(5, show=True)
    5 x 4 x 3 x 2 x 1 = 120
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c
    return f


print(fatorial(5, show=True))

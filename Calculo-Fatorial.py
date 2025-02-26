

def fatorial(num=1, show=False):
    """
     → Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (Opcional) mostar ou não a conta
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    if show:
        for c in range(num, 0, -1):
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
            f *= c
            c -= 1
        return f
    else:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f


print(fatorial(6, show=False))
# help(fatorial)


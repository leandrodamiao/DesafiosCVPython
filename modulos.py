def fatorial(n, show=False):
  '''
  -> Calcula o fatorial de um número inteiro (N)
  :param n: Número a ser calculado
  :param show: Mostra ou não a conta (padrão False)
  :return: Resultado do fatorial
  '''
  f=1
  for c in range (n, 0, -1):
    f *= c
    if show:
      print(c, end=' ')
      if c != 1:
        print('x', end=' ')
      else:
        print('=', end=' ')
  return f

  
    
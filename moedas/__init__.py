def metade(n, moeda=False):
  '''
  -> Calcula a metade de um valor
  :param n: valor a ser calculada
  :param moeda: transforma o retorno em moeda brasileira com duas casa decimais (R$)
  :return: valor calculado
  '''
  #return n / 2 if moeda=False else f'R${n / 2:.2f}'
  if moeda:
    return f'R${n / 2:.2f}'
  else:
    return n / 2
  


def dobro(n, moeda=False):
  '''
  -> Calcula o dobro de um valor
  :param n: valor a ser calculado
  :param moeda: transforma o retorno em moeda brasileira com duas casa decimais (R$)
  :return: valor calculado
  '''
  if moeda:
    return f'R${n * 2:.2f}'
  else:
    return n * 2
  

def aumentar(n, x=10, moeda=False):
  '''
  -> Calcula um acréscimo de x% ao valor
  :param n: valor a ser calculado
  :param moeda: transforma o retorno em moeda brasileira com duas casa decimais (R$)
  :param x: porcentagem que insidirá sobre o valor (n) padrão 10%
  :return: valor calculado
  '''
  if moeda:
    return f'R${n + (n * x / 100):.2f}'
  else:
    return n + (n * x / 100)


def diminuir(n, x=10, moeda=False):
  '''
  -> Calcula uma redução de x% sobre um valor
  :param n: valor a ser calculado
  :param moeda: transforma o retorno em moeda brasileira com duas casa decimais (R$)
  :param x: porcentaguem que insidirá sobre o valor (n) padrão 10%
  :return: valor calculado
  '''
  if moeda:
    return f'R${n - (n * x / 100):.2f}'
  else:
    return n - (n * x / 100)


def moeda(n):
  '''
  -> transforma um número floal em moeda(Real brasileiro)
  :param n: Número a ser convertido em moeda
  :retur: String com R$ e duas casas decimais
  '''
  return f'R${n:.2f}'


def resumo(n, a, d):
  '''
  -> Analisa um valor (n) e informa o dobro, metade aumento em x% e redução em x%
  :param n: Número a ser analisado
  :param a: (Aumentar) soma (A)% ao valor
  :param d: (Diminuir) subtrai (D)% do valor
  :return: 0 - printa uma tabela formatada com o resultado
  '''
  print('-'*25)
  print(f'{"Resumo do valor":^25}')
  print('-'*25)
  print(f'{"Preço analisado:":17}', end='')
  print(moeda(n))
  print(f'{"Dobro do preço:":17}', end='')
  print(dobro(n, True))
  print(f'{"Metade do Preço:":17}', end='')
  print(metade(n, True))
  print(f'{a}{"% de aumento:":15}', end='')
  print(aumentar(n, a, True))
  print(f'{d}{"% de redução:":15}', end='')
  print(diminuir(n, a, True))
  print('-'*25)



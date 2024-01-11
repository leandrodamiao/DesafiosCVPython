def metade(n):
  '''
  -> Calcula a metade de um valor
  :param n: valor a ser calculada
  :return: valor calculado
  '''
  return n / 2
  


def dobro(n):
  '''
  -> Calcula o dobro de um valor
  :param n: valor a ser calculado
  :return: valor calculado
  '''
  return n * 2
  

def aumentar(n, x=10):
  '''
  -> Calcula um acréscimo de 10% ao valor
  :param n: valor a ser calculado
  :param x: porcentagem que insidirá sobre o valor (n) padrão 10%
  :return: valor calculado
  '''
  return n + (n * x / 100)


def diminuir(n, x=10):
  '''
  -> Calcula uma redução de 13% sobre um valor
  :param n: valor a ser calculado
  :param x: porcentaguem que insidirá sobre o valor (n) padrão 10%
  :return: valor calculado
  '''
  return n - (n * x / 100)


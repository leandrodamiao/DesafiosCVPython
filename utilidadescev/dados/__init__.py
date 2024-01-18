def fcores(text='', cor='', fundo=False):
  '''
  -> Função que adiciona cores aos textos.
  :param arg: Texto que será editado
  :param cor: Cor adicionada ao texto
  :return: Texto formatado com a cor escolhida
  '''
  if fundo: 
    cores = {
      '' : f'\033[m{text}\033[m',
      'branco' : f'\033[40m{text}\033[m',
      'vermelho' : f'\033[41m{text}\033[m',
      'verde' : f'\033[42m{text}\033[m',
      'amarelo': f'\033[43m{text}\033[m',
      'azul': f'\033[44m{text}\033[m',
      'magenta': f'\043[35m{text}\033[m',
      'ciano': f'\033[46n{text}\033[m',
      'cinza' : f'\033[47m{text}\033[m'
    }
  else:
    cores = {
      '' : f'\033[m{text}\033[m',
      'branco' : f'\033[30m{text}\033[m',
      'vermelho' : f'\033[31m{text}\033[m',
      'verde' : f'\033[32m{text}\033[m',
      'amarelo': f'\033[33m{text}\033[m',
      'azul': f'\033[34m{text}\033[m',
      'magenta': f'\033[35m{text}\033[m',
      'ciano': f'\033[36n{text}\033[m',
      'cinza' : f'\033[37m{text}\033[m'
    }
  r = cores[cor]
  return r



def leiadinheiro(msg):
  '''
  => Lê um dado e aceita apenas valores monetários, mesmo que com vírgula.
  :param arg: Mensagem recebida que será printada na tela
  :return: valor monetário digitado
  '''
  
  while True:
    dado = str(input(msg)).strip().replace(',','.')
    if dado.isalpha() or dado == '':
      print('Erro! Digite apenas números!')
      dado = str(input(msg)).strip().replace(',','.')
    else:
      dado = float(dado)
      return dado


def leiainteiro(msg):
  '''
  => Lê um dado e só aceita números inteiros.
  :param msg: Mensagem na tela
  :return: Apenas números inteiros
  '''
  while True:
    dado = str(input(msg)).strip()
    if dado.isnumeric():
      dado = int(dado)
      return dado
    else:
      print(fcores('Erro: Favor digite apenas um número inteiro válido.', 'vermelho'))




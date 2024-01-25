from time import sleep

'''
Módulo criado com as funções do desafio 115
'''


def fcores(text='', cor='', fundo=False):
  '''
  -> Função que adiciona cores aos textos.
  :param arg: Texto que será editado
  :param cor: Cor adicionada ao texto
  :param fundo: Padrão False, se verdadeiro altera as cores de fundo
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

def finterface_menu():
  print('-'*25)
  print(f'{"MENU PRINCIPAL":^25}')
  print('-'*25)
  print(fcores('1', 'amarelo'), '-', fcores('Pessoas cadastradas', 'azul'))
  print(fcores('2', 'amarelo'), '-',fcores('Cadastrar nova pessoa', 'azul'))
  print(fcores('3', 'amarelo'), '-',fcores('Sair do sistema', 'azul'))
  print('-'*25)


def fmenu():
  finterface_menu()
  while True:
    try:
      match int(input(fcores('Sua opção: ', 'verde'))):
        case 1:
          return fconsulta_pessoas()
        case 2:
          return fcadatra_pessoas()
        case 3:
          print('Saindo...')
          sleep(1)
          return 
        case _:
          print(fcores('Erro! Digite uma opção válida.', 'vermelho'))
          continue
    except (TypeError, ValueError):
      print(fcores('Erro! Digite apenas números inteiros.', 'vermelho'))
      continue
  

def fconsulta_pessoas():
  print('-'*25)
  print(f'{"Opção 1":^25}')
  print('-'*25)
  sleep(1)
  fmenu()


def fcadatra_pessoas():
  print('-'*25)
  print(f'{"Opção 2":^25}')
  print('-'*25)
  sleep(1)
  fmenu()





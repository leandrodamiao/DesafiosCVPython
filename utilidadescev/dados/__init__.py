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



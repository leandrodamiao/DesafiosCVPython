print("=" * 60)
print(f"{'Desafios Curso em Vídeo Pyhton':^60}")
print("=" * 60)
print('')

while True:
  opcaodesafio = input(print('QUal desafio deseja ver agora? \nTecle s ou sair para finalizar o programa.'))
  if opcaodesafio in ('s', 'sair'):
    print('Foi um prazer tê-lo aqui, até a próxima!')
    break

  if opcaodesafio == '1':
    print("=" * 60)
    print(f"{'Desafio 1 Curso em Vídeo Pyhton':^60}")
    print("=" * 60)
    print('')
    print('Olá Mundo \n')

  else:
    print("Infálido ou ainda não existe!")

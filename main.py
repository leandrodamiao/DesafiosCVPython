print("=" * 60)
print(f"{'Desafios Curso em Vídeo Pyhton':^60}")
print("=" * 60)
print('')

while True:
  opcaodesafio = input(
    print(
      'QUal desafio deseja ver agora? \nTecle s ou sair para finalizar o programa. \n'
    ))
  if opcaodesafio in ('s', 'sair'):
    print('Foi um prazer tê-lo aqui, até a próxima!')
    break

  if opcaodesafio == '1':
    print("=" * 60)
    print(f"{'Desafio 1 Curso em Vídeo Pyhton':^60}")
    print("=" * 60)
    print('')
    print('Olá Mundo \n')

  if opcaodesafio == '2':
    print('=' * 60)
    print(f"{'Desafio 2 Curso em Vídeo Python:':^60}")
    print('=' * 60)
    nome = input('Qual o seu nome? ')
    print(f"É um prazer conhecer você {nome}! \n")

  if opcaodesafio == '3':
    print('=' * 60)
    print(f"{'Desafio 3 Curso em Vídeo Python:':^60}")
    print('=' * 60)
    n1 = int(input('Informe um número: '))
    n2 = int(input('Informe outro número: '))
    print(f"A soma entre {n1} e {n2} é igual a {n1+n2}. \n")

  if opcaodesafio == '4':
    print('=' * 60)
    print(f"{'Desafio 4 Curso em Vídeo Python:':^60}")
    print('=' * 60)
    print('')
    algo = input('Digite algo: \n')
    print(f"O tipo primitivo desse valor é {type(algo)}")
    print(f"Só tem espaços? {algo.isspace()}")
    print(f"É um número? {algo.isnumeric()}")
    print(f"É alfabético? {algo.isalpha()}")
    print(f"É alfanumérico? {algo.isalnum()}")
    print(f"Está em maiúsculas? {algo.isupper()}")
    print(f"Está em minúsculas? {algo.islower()}")
    print(f"Está capitalizada? {algo.istitle()} \n")

  else:
    print("Infálido ou ainda não existe!")

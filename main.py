print("=" * 60)
print(f"{'Desafios Curso em Vídeo Pyhton':^60}")
print("=" * 60)
print('')

while True:
  opcaodesafio = input(
    print(
      '\nQUal desafio deseja ver agora? \nTecle s ou sair para finalizar o programa. \n'
    ))
  if opcaodesafio in ('s', 'sair'):
    print('Foi um prazer tê-lo aqui, até a próxima!')
    break

  elif opcaodesafio == '1':
    print("=" * 60)
    print(f"{'Desafio 1 Curso em Vídeo Pyhton':^60}")
    print("=" * 60)
    print('')
    print('Olá Mundo')

  elif opcaodesafio == '2':
    print('=' * 60)
    print(f"{'Desafio 2 Curso em Vídeo Python:':^60}")
    print('=' * 60)
    nome = input('Qual o seu nome? ')
    print(f"É um prazer conhecer você {nome}!")

  elif opcaodesafio == '3':
    print('=' * 60)
    print(f"{'Desafio 3 Curso em Vídeo Python:':^60}")
    print('=' * 60)
    n1 = int(input('Informe um número: '))
    n2 = int(input('Informe outro número: '))
    print(f"A soma entre {n1} e {n2} é igual a {n1+n2}.")

  elif opcaodesafio == '4':
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
    print(f"Está capitalizada? {algo.istitle()}")

  elif opcaodesafio == '5':
    print('=' * 60)
    print(f"{'Desafio 5 Curso em Vídeo Python:':^60}")
    print('=' * 60)
    print('')
    n = int(input("Digite um número inteiro: "))
    print(f"Analisando o valor {n}, o antecessor é {n-1} e o sucessor é {n+1}")

  elif opcaodesafio == '6':
    print('=' * 60)
    print(f"{'Desafio 6 Curso em Vídeo Python:':^60}")
    print('=' * 60, '\n')
    n = int(input("Digite um número: "))
    print(
      f"O dobro de {n} vale {n*2}. \nO triplo de {n} vale {n*3}. \nA raiz quadrada de {n} vale {n**(1/2):.2f}."
    )

  elif opcaodesafio == '7':
    print('=' * 60)
    print(f"{'Desafio 7 Curso em Vídeo Python:':^60}")
    print('=' * 60, '\n')
    n1 = float(input("Primeira nota do aluno: "))
    n2 = float(input("Segunda nota do aluno: "))
    print(f"A média entre {n1} e {n2} é igual a {(n1+n2)/2:.1f}")

  else:
    print("Infálido ou ainda não existe!")

'''Código dedicado a revisar todo o Curso em Vídeo de Python. O programa pergunta o número do exercício a ser exibido na tela.'''

print("=" * 25)
print(f"{'Desafios Pyhton':^25}")
print("=" * 25)
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
    print("=" * 25)
    print(f"{'D1 - Primeiro Print:':^25}")
    print("=" * 25)
    print('')
    print('Olá Mundo')

  elif opcaodesafio == '2':
    print('=' * 25)
    print(f"{'D2 - Boas Vindas:':^25}")
    print('=' * 25)
    nome = input('Qual o seu nome? ')
    print(f"É um prazer conhecer você {nome}!")

  elif opcaodesafio == '3':
    print('=' * 25)
    print(f"{'D3 - Soma:':^25}")
    print('=' * 25)
    n1 = int(input('Informe um número: '))
    n2 = int(input('Informe outro número: '))
    print(f"A soma entre {n1} e {n2} é igual a {n1+n2}.")

  elif opcaodesafio == '4':
    print('=' * 25)
    print(f"{'D4 - Tipo de Dados:':^25}")
    print('=' * 25)
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
    print('=' * 25)
    print(f"{'D5 - Antes/Depois nº:':^25}")
    print('=' * 25)
    print('')
    n = int(input("Digite um número inteiro: "))
    print(f"Analisando o valor {n}, o antecessor é {n-1} e o sucessor é {n+1}")

  elif opcaodesafio == '6':
    print('=' * 25)
    print(f"{'D6 - Dobro/Triplo/Raiz:':^25}")
    print('=' * 25, '\n')
    n = int(input("Digite um número: "))
    print(
      f"O dobro de {n} vale {n*2}. \nO triplo de {n} vale {n*3}. \nA raiz quadrada de {n} vale {n**(1/2):.2f}."
    )

  elif opcaodesafio == '7':
    print('=' * 25)
    print(f"{'D7 - Média:':^25}")
    print('=' * 25, '\n')
    n1 = float(input("Primeira nota do aluno: "))
    n2 = float(input("Segunda nota do aluno: "))
    print(f"A média entre {n1} e {n2} é igual a {(n1+n2)/2:.1f}")

  elif opcaodesafio == '8':
    print('=' * 25)
    print(f"{'D8 - Conversor Medidas':^25}")
    print('=' * 25)
    distancia = float(input('Uma distância em metros: '))
    print(f"A medida de {distancia:.1f}m corresponde a: ")
    print(
      f"{distancia/1000}km \n{distancia/100}hm \n{distancia/10}dam \n{distancia*10:.0f}dm \n{distancia*100:.0f}cm \n{distancia*1000:.0f}mm"
    )

  elif opcaodesafio == '9':
    print('=' * 25)
    print(f"{'D9 - Tabuada 1.0':^25}")
    print('=' * 25)
    numtab = int(input('Digite um número para ver sua tabuada: '))
    print('_' * 15)
    print(f"{numtab} x  1 = {numtab*1:>3}")
    print(f"{numtab} x  2 = {numtab*2:>3}")
    print(f"{numtab} x  3 = {numtab*3:>3}")
    print(f"{numtab} x  4 = {numtab*4:>3}")
    print(f"{numtab} x  5 = {numtab*5:>3}")
    print(f"{numtab} x  6 = {numtab*6:>3}")
    print(f"{numtab} x  7 = {numtab*7:>3}")
    print(f"{numtab} x  8 = {numtab*8:>3}")
    print(f"{numtab} x  9 = {numtab*9:>3}")
    print(f"{numtab} x 10 = {numtab*10:>3}")
    print('_' * 15)

  elif opcaodesafio == '10':
    print('=' * 25)
    print(f"{'D10 - Conversor de Moedas':^25}")
    print('=' * 25)
    dinheiro = float(input('Quanto dinheiro você tem na carteira R$'))
    print(f"Com {dinheiro} você pode comprar US${dinheiro / 3.27:.2f}")

  else:
    print("Infálido ou ainda não existe!")

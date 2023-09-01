import math
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
    print(
      f"Com {dinheiro} (no dia 24/08/2023) você pode comprar US${dinheiro / 4.88:.2f}"
    )

  elif opcaodesafio == '11':
    print('=' * 25)
    print(f"{'D11 - Pintando Parede':^25}")
    print('=' * 25)
    largura = float(input('Largura da parede: '))
    altura = float(input('Altura da parede: '))
    print(
      f"Sua parede tem a dimensão de {largura}x{altura} e sua área é {largura*altura:.3f}m².\nPara pintar essa parede, você precisará de {(largura*altura)/2:.3f}l de tinta."
    )

  elif opcaodesafio == '12':
    print('=' * 25)
    print(f"{'D12 - Calculando Descontos':^25}")
    print('=' * 25)
    precoproduto = float(input('Qual é o preço do produto? R$'))
    print(
      f"O produto que custava R${precoproduto} com 5% de desconto vai custar R${precoproduto - (precoproduto*0.05):.2f}"
    )

  elif opcaodesafio == '13':
    print('=' * 25)
    print(f"{'D13 - Reajuste Salarial':^25}")
    print('=' * 25)
    salario = float(input('Qual é o salário do funcionário? R$'))
    print(
      f"Um funcionário que ganhava R${salario} passa a receber R${salario + (salario*15/100):.2f} com o aumento de 15%."
    )

  elif opcaodesafio == '14':
    print('=' * 25)
    print(f"{'D14 - Conversor de Temp':^25}")
    print('=' * 25)
    temperatura = float(input('Informe a temperatura em ºC: '))
    print(
      f"A temperatura de {temperatura}ºC corresponde a {1.8*temperatura+32}ºF!"
    )

  elif opcaodesafio == '15':
    print('=' * 25)
    print(f"{'D15 - Aluguel de Carros':^25}")
    print('=' * 25)
    diasalugados = int(input('Quantos dias alugados? '))
    kmrodados = float(input('Quantos Km rodados? '))
    preco_aluguel_carro = (diasalugados * 60) + (kmrodados * 0.15)
    print(f"O total a pagar é de R${preco_aluguel_carro:.2f}")

  elif opcaodesafio == '16':
    print('=' * 25)
    print(f"{'D16 - QUbrando um Número':^25}")
    print('=' * 25)
    numero = float(input('Digite um valor: '))
    valor_quebrado = math.floor(numero)
    print(
      f"O valor digitaro foi {numero} e sua porção inteira é {valor_quebrado}")
    #print(f"O valor digitado foi {numero} e a sua porção inteiro é {int(numero)}")

  elif opcaodesafio == '17':
    print('=' * 25)
    print(f"{'D17 - Catetos Hipotenusa':^25}")
    print('=' * 25)
    cateto_oposto = float(input('Comprimento do cateto oposto: '))
    cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
    hipoten = math.hypot(cateto_oposto, cateto_adjacente)
    print(f"A hipotenusa vai medir {hipoten:.2f}")
    print('OU')
    print(
      f"({cateto_oposto}² + {cateto_adjacente}²) = Hipotenusa² - sendo assim o valor é {((cateto_oposto**2)+(cateto_adjacente**2))**(1/2):.2f}"
    )

  else:
    print("Infálido ou ainda não existe!")

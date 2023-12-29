import math
from random import choice, shuffle, randint
import pygame
from time import sleep
from datetime import date
import emoji
from operator import itemgetter
'''Código dedicado a revisar todo o Curso em Vídeo de Python. O programa pergunta o número do exercício a ser exibido na tela.'''

print("")
print("=" * 25)
print(f"{'Desafios Pyhton':^25}")
print("=" * 25)
print('')

while True:
  opcaodesafio = input(
    print(
      '\nQUal desafio deseja ver agora? \nTecle s ou sair para finalizar o programa. \n'
    )).strip()

  match opcaodesafio:

    case 's' | 'sair':
      print('Foi um prazer tê-lo aqui, até a próxima!')
      break

    case '1':
      print("=" * 25)
      print(f"{'D1 - Primeiro Print:':^25}")
      print("=" * 25)
      print('')
      print('Olá Mundo')

    case '2':
      print('=' * 25)
      print(f"{'D2 - Boas Vindas:':^25}")
      print('=' * 25)
      nome = input('Qual o seu nome? ')
      print(f"É um prazer conhecer você {nome}!")

    case '3':
      print('=' * 25)
      print(f"{'D3 - Soma:':^25}")
      print('=' * 25)
      n1 = int(input('Informe um número: '))
      n2 = int(input('Informe outro número: '))
      print(f"A soma entre {n1} e {n2} é igual a {n1+n2}.")

    case '4':
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

    case '5':
      print('=' * 25)
      print(f"{'D5 - Antes/Depois nº:':^25}")
      print('=' * 25)
      print('')
      n = int(input("Digite um número inteiro: "))
      print(
        f"Analisando o valor {n}, o antecessor é {n-1} e o sucessor é {n+1}")

    case '6':
      print('=' * 25)
      print(f"{'D6 - Dobro/Triplo/Raiz:':^25}")
      print('=' * 25, '\n')
      n = int(input("Digite um número: "))
      print(
        f"O dobro de {n} vale {n*2}. \nO triplo de {n} vale {n*3}. \nA raiz quadrada de {n} vale {n**(1/2):.2f}."
      )

    case '7':
      print('=' * 25)
      print(f"{'D7 - Média:':^25}")
      print('=' * 25, '\n')
      n1 = float(input("Primeira nota do aluno: "))
      n2 = float(input("Segunda nota do aluno: "))
      print(f"A média entre {n1} e {n2} é igual a {(n1+n2)/2:.1f}")

    case '8':
      print('=' * 25)
      print(f"{'D8 - Conversor Medidas':^25}")
      print('=' * 25)
      distancia = float(input('Uma distância em metros: '))
      print(f"A medida de {distancia:.1f}m corresponde a: ")
      print(
        f"{distancia/1000}km \n{distancia/100}hm \n{distancia/10}dam \n{distancia*10:.0f}dm \n{distancia*100:.0f}cm \n{distancia*1000:.0f}mm"
      )

    case '9':
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

    case '10':
      print('=' * 25)
      print(f"{'D10 - Conversor de Moedas':^25}")
      print('=' * 25)
      dinheiro = float(input('Quanto dinheiro você tem na carteira R$'))
      print(
        f"Com {dinheiro} (no dia 24/08/2023) você pode comprar US${dinheiro / 4.88:.2f}"
      )

    case '11':
      print('=' * 25)
      print(f"{'D11 - Pintando Parede':^25}")
      print('=' * 25)
      largura = float(input('Largura da parede: '))
      altura = float(input('Altura da parede: '))
      print(
        f"Sua parede tem a dimensão de {largura}x{altura} e sua área é {largura*altura:.3f}m².\nPara pintar essa parede, você precisará de {(largura*altura)/2:.3f}l de tinta."
      )

    case '12':
      print('=' * 25)
      print(f"{'D12 - Calculando Descontos':^25}")
      print('=' * 25)
      precoproduto = float(input('Qual é o preço do produto? R$'))
      print(
        f"O produto que custava R${precoproduto} com 5% de desconto vai custar R${precoproduto - (precoproduto*0.05):.2f}"
      )

    case '13':
      print('=' * 25)
      print(f"{'D13 - Reajuste Salarial':^25}")
      print('=' * 25)
      salario = float(input('Qual é o salário do funcionário? R$'))
      print(
        f"Um funcionário que ganhava R${salario} passa a receber R${salario + (salario*15/100):.2f} com o aumento de 15%."
      )

    case '14':
      print('=' * 25)
      print(f"{'D14 - Conversor de Temp':^25}")
      print('=' * 25)
      temperatura = float(input('Informe a temperatura em ºC: '))
      print(
        f"A temperatura de {temperatura}ºC corresponde a {1.8*temperatura+32}ºF!"
      )

    case '15':
      print('=' * 25)
      print(f"{'D15 - Aluguel de Carros':^25}")
      print('=' * 25)
      diasalugados = int(input('Quantos dias alugados? '))
      kmrodados = float(input('Quantos Km rodados? '))
      preco_aluguel_carro = (diasalugados * 60) + (kmrodados * 0.15)
      print(f"O total a pagar é de R${preco_aluguel_carro:.2f}")

    case '16':
      print('=' * 25)
      print(f"{'D16 - QUbrando um Número':^25}")
      print('=' * 25)
      numero = float(input('Digite um valor: '))
      valor_quebrado = math.floor(numero)
      print(
        f"O valor digitaro foi {numero} e sua porção inteira é {valor_quebrado}"
      )
      #print(f"O valor digitado foi {numero} e a sua porção inteiro é {int(numero)}")

    case '17':
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

    case '18':
      print('=' * 25)
      print(f"{'D18 - Seno Cos. Tang.':^25}")
      print('=' * 25)
      angulo = float(input('Digite o ângulo desejado: '))
      print(
        f"O ângulo de {angulo} tem: \n \nSENO = {math.sin(math.radians(angulo)):.2f} \nCOSSENO = {math.cos(math.radians(angulo)):.2f} \nTANGENTE = {math.tan(math.radians(angulo)):.2f}"
      )

    case '19':
      print('=' * 25)
      print(f"{'D19 - Sorteio Item Lista':^25}")
      print('=' * 25)
      aluno1 = str(input('Primeiro aluno: '))
      aluno2 = str(input('Segundo Aluno: '))
      aluno3 = str(input('Terceiro aluno: '))
      aluno4 = str(input('Quarto aluno: '))
      sorteio_aluno = aluno1, aluno2, aluno3, aluno4
      print(f"O aluno escolhido foi {choice(sorteio_aluno)}")

    case '20':
      print('=' * 25)
      print(f"{'D20 - Sorteio ordem na lista':^25}")
      print('=' * 25)
      a1 = str(input('Primeiro aluno: '))
      a2 = str(input('Primeiro aluno: '))
      a3 = str(input('Primeiro aluno: '))
      a4 = str(input('Primeiro aluno: '))
      lista_alunos = [a1, a2, a3, a4]
      shuffle(lista_alunos)
      print(f"A ordem de apresentação será:\n{lista_alunos}")

    case '21':
      print('=' * 25)
      print(f"{'D21 - Tocando um mp3':^25}")
      print('=' * 25)
      pygame.init()
      pygame.mixer.music.load('kalimba.mp3')
      pygame.mixer.music.play()
      pygame.event.wait()

    case '22':
      print('=' * 25)
      print(f"{'D22 - Analisando Nomes':^25}")
      print('=' * 25)
      nome_completo = str(input('Informe seu nome completo')).strip()
      print(f"Olá {nome_completo}!")
      print(
        f"Seu nome com todas as letras maiúsculas é: \n{nome_completo.upper()}\n"
      )
      print(f"Com todas as letras minúsculas é: \n{nome_completo.lower()} \n")
      print(
        f"{nome_completo} tem {len(''.join(nome_completo.split()))} letas sem espaços. \n"
      )
      nome_dividido = nome_completo.split()
      print(f"Seu primeiro nome tem {len(nome_dividido[0])} letras.")

    case '23':
      print('=' * 25)
      print(f"{'D23 - Separando Dígitos Nº':^25}")
      print('=' * 25)
      numero = int(input('informe um número: '))
      print(f"Analisando o número {numero} temos:")
      print(f"Unidade: {numero//1%10}")
      print(f"Dezena: {numero//10%10}")
      print(f"Centena: {numero//100%10}")
      print(f"Milhar: {numero//1000%10}")

    case '24':
      print('=' * 25)
      print(f"{'D24 - Checando Letras':^25}")
      print('=' * 25)
      cidade = str(input('Em que cidade você nasceu? ')).strip().split()
      print('SANTO' in cidade[0].upper())

    case '25':
      print('=' * 25)
      print(f"{'D25 - Procurando String':^25}")
      print('=' * 25)
      nome = str(input('Qual é o seu nome completo? ')).strip()
      print(f"Seu nome tem Silva? {'SILVA' in nome.upper()}")

    case '26':
      print('=' * 25)
      print(f"{'D26 - Ocorrências strings':^25}")
      print('=' * 25)
      frase = str(input('Digite uma frase: ')).strip().upper()
      print(f"A letra A aparece {frase.count('A')} vezes na frase.")
      print(f"A primeira letra A apareceu na {frase.find('A')+1}ª posição")
      print(f"A última letra A apareceu na {frase.rfind('A')+1}ª posição ")

    case '27':
      print('=' * 25)
      print(f"{'D27 - 1º e último nomne':^25}")
      print('=' * 25)
      nome_completo = str(input('Digite seu nome completo: ')).strip()
      print(f"Seu primeiro nome é {nome_completo[:nome_completo.find(' ')]}")
      print(f"Seu último nome é {nome_completo[nome_completo.rfind(' ')+1:]}")

    case '28':
      print('=' * 25)
      print(f"{'D28 - Jogo Advinhação':^25}")
      print('=' * 25)
      print('\nPensei em um número entre 0 e 5. Tente adivinhar...\n')
      maquina = randint(0, 5)
      jogador = int(input('Em que númeo pensei? '))
      print('PROCESSANDO...')
      sleep(3)
      print("Parabéns! Você conseguiu me vencer!" if maquina == jogador else
            f"Ganhei! Eu pensei no número {maquina} e não no {jogador}!")

    case '29':
      print('=' * 25)
      print(f"{'D29 - Radar Eletrônico':^25}")
      print('=' * 25)
      velocidade_carro = int(input('Qaul é a velocidade atual do carro? '))
      if velocidade_carro >= 80:
        print("Multado! Você excedeu o limite permitido que é de 80Km/h")
        print(f"Você deve pagar uma multa de R${(velocidade_carro-80)*7:.2f}!")
      print("Tenha um bom dia! Dirija com segurança!")

    case '30':
      print('=' * 25)
      print(f"{'D30 - Par ou Ímpar':^25}")
      print('=' * 25)
      n = int(input('Me diga um número qualquer: '))
      print(f"O número {n} é PAR" if n % 2 == 0 else f"O número {n} é ÍMPAR")

    case '31':
      print('=' * 25)
      print(f"{'D31 - Custo da Viagem':^25}")
      print('=' * 25)
      distancia_viagem = float(input("Qual é a distância da sua viagem? "))
      print(
        f"Você está prestes a começar uma viagem de {distancia_viagem:.1f}Km.")
      #     if distancia_viagem <= 200:
      #       custo_viagem = distancia_viagem * 0.50
      #     else:
      #       custo_viagem = distancia_viagem * 0.45
      custo_viagem = distancia_viagem * 0.50 if distancia_viagem <= 200 else distancia_viagem * 0.45
      print(f"O preço da sua passagem será de R${custo_viagem:.2f}")

    case '32':
      print('=' * 25)
      print(f"{'D32 - Ano Bissexto':^25}")
      print('=' * 25)
      ano = int(
        input("Qual ano quer analizar? Coloque 0 para analizar o ano atual: "))
      if ano == 0:
        ano = date.today().year
      if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} é BISSEXTO")
      else:
        print(f"O ano {ano} NÂO é BISSEXTO")

    case '33':
      print('=' * 25)
      print(f"{'D33 - Maior Menor Valores':^25}")
      print('=' * 25)
      valor_a = int(input("Primeiro valor: "))
      valor_b = int(input("Segundao valor: "))
      valor_c = int(input("Terceiro valor: "))
      #Comparando dos três qual é o maior valor
      maior_valor = valor_a
      if valor_b > valor_a and valor_c:
        maior_valor = valor_b
      if valor_c > valor_a and valor_b:
        maior_valor = valor_c

        #Comparando dos três quel é o menor valor
      menor_valor = valor_a
      if valor_b < valor_a and valor_c:
        menor_valor = valor_b
      if valor_c < valor_a and valor_b:
        menor_valor = valor_c

      print(f"O menor valor digitado foi{menor_valor}")
      print(f"O maior valor digitado foi {maior_valor}")

    case '34':
      print('=' * 25)
      print(f"{'D34 - Aumentos Múltiplos':^25}")
      print('=' * 25)
      salario = float(input("Qual é o salário do funcionário? R$"))
      if salario <= 1250:
        salario_aumento = salario + (salario * 15 / 100)
      else:
        salario_aumento = salario + (salario * 10 / 100)
      print(
        f"Quem ganhava R${salario:.2f} passa a ganhar R${salario_aumento:.2f} agora."
      )

    case '35':
      print('=' * 25)
      print(f"{'D35 - Analisador de Triânculos':^25}")
      print('=' * 25)
      seg1 = float(input("Primeiro Segmento: "))
      seg2 = float(input("Segundo Segmento: "))
      seg3 = float(input("Terceiro Segmento: "))
      if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
        print("Os segmentos acima PODEM FORMAR triângulos!")
      else:
        print("Os segmentos acima NÂO PODEM FORMAR triângulos!")

    case '36':
      print('=' * 25)
      print(f"{'D36 - Aprovando Empréstimo':^25}")
      print('=' * 25)
      valor_casa = float(input("Qual o valor da casa? R$"))
      salario_comprador = float(input("Qual o salário do comprador? R$"))
      tempo_financ = int(input("Quantos anos de financiamento? "))
      prestacao_casa = valor_casa / (tempo_financ * 12)
      print(
        f"Para pagar uma casa de R${valor_casa:.2f} em {tempo_financ} anos a prestação será de R${prestacao_casa:.2f}"
      )
      if prestacao_casa > salario_comprador * 30 / 100:
        print("Empréstimo NEGADO!")
      else:
        print("Parabéns! Empréstimo CONCEDIDO!")

    case '37':
      print('=' * 25)
      print(f"{'D37 - Bases Numéricas':^25}")
      print('=' * 25)
      num = int(input("Digite um número inteiro"))
      print("Escolha uma das bases para conversão")
      print("[ 1 ] converter para BINÁRIO")
      print("[ 2 ] converter para OCTAL")
      print("[ 3 ] converter para HEXADECIMAL")
      sua_opcao = int(input("Sua Opção: "))
      if sua_opcao == 1:
        print(f"{num} convertio para BINáARIO é ifual a {bin(num)[2:]}")
      elif sua_opcao == 2:
        print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
      elif sua_opcao == 3:
        print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
      else:
        print("Opção inválida! Tente novamente!")

    case '38':
      print('=' * 25)
      print(f"{'D38 - Comparando Numeros':^25}")
      print('=' * 25)
      primeiro_num = int(input("Primeiro número: "))
      segundo_num = int(input("Segundo Número: "))
      if primeiro_num > segundo_num:
        print("O PRIMEIRO valor é maior!")
      elif segundo_num > primeiro_num:
        print("O SEGUNDO valor é maior!")
      else:
        print("Os dois valores são iguais")

    case '39':
      print('=' * 25)
      print(f"{'D39 - Alistamento Militar':^25}")
      print('=' * 25)
      ano_nascimento = int(input("Ano de Nascimento: "))
      idade = date.today().year - ano_nascimento
      print(
        f"Quem nasceu em {ano_nascimento} tem {idade} em {date.today().year}.")
      if idade < 18:
        print(f"Ainda faltam {18-idade} anos para o alistamento")
        print(f"Seu alistamento será em {ano_nascimento + 18}.")
      elif idade == 18:
        print("Você deve se alistar IMEDIATAMENTE!")
      else:
        print(
          f"Você já deveria ter se alistaro há {date.today().year - (ano_nascimento + 18)} anos"
        )
        print(f"Seu alistamento foi em {ano_nascimento + 18}.")

    case '40':
      print('=' * 25)
      print(f"{'D40 - Clássico da Média':^25}")
      print('=' * 25)
      nota1 = float(input("Primeira nota: "))
      nota2 = float(input("Segunda nota: "))
      media = (nota1 + nota2) / 2
      print(
        f"Tirando {nota1:.1f} e {nota2:.1f} a média do aluno é {media:.1f}")
      if media < 5:
        print("O aluno está REPROVADO!")
      elif media < 7:
        print("O alono está de RECUPERAÇÂO!")
      else:
        print("O aluno está APROVADO!")

    case '41':
      print('=' * 25)
      print(f"{'D41 - Confed Natação':^25}")
      print('=' * 25)
      nascimento = int(input("Qual seu ano de nascimento? "))
      #Calculando a idade com base no ano de nascimento:
      idade = date.today().year - nascimento
      #Classificação do atleta de acordo com sua idade:
      if idade <= 9:
        classificacao = "MIRIM"
      elif idade > 9 and idade <= 14:
        classificacao = "INFANTIL"
      elif idade > 14 and idade <= 19:
        classificacao = "JUNIOR"
      elif idade > 19 and idade <= 25:
        classificacao = "SÊNIOR"
      elif idade > 25:
        classificacao = "MASTER"

      print(f"O atleta tem {idade} anos.")
      print(f"Classificação: {classificacao}")

    case '42':
      print('=' * 25)
      print(f"{'D42 - Triângulos Plus':^25}")
      print('=' * 25)
      segmento1 = int(input("Primeiro Segmento: "))
      segmento2 = int(input("Segundo Segmento: "))
      segmento3 = int(input("Terceiro Segmento: "))
      if segmento1 + segmento2 < segmento3 or segmento1 + segmento3 < segmento2 or segmento2 + segmento3 < segmento1:
        print("Os segmentos acima NÂO PODEM FORMAR triângulo")
      else:
        if segmento1 == segmento2 == segmento3:
          print("Os segmentos acima FORMAM um triângulo EQUILÁTERO")
        elif segmento1 == segmento2 or segmento1 == segmento3 or segmento2 == segmento3:
          print("Os segmentos acima FORMAM um triângulo ISÓSCELES")
        else:
          print("Os segmentos acima FORMAM um triângulo ESCALENO")

    case '43':
      print('=' * 25)
      print(f"{'D43 - Massa Corporea':^25}")
      print('=' * 25)
      peso = float(input("Qual é o seu peso? (Kg) "))
      altura = float(input("Qaul é sua altura? (m) "))
      #Calculando IMC usando o peso e altula lidos:
      imc = peso / altura**2
      print(f"O IMC dessa pessoa é de {imc:.1f}")
      #Gerando Status de acordo com o IMC calculado:
      if imc <= 18.5:
        print("Você está abaixo do peso")
      elif imc <= 25:
        print("Parabéns!!! Você está no peso ideal!")
      elif imc <= 30:
        print("Cuidado! Você está sobrepeso")
      elif imc <= 40:
        print("Você está em obesidade.")
      else:
        print("Atenção! Você está em obesidade mórbida.")

    case '44':
      print('=' * 25)
      print(f"{'D44 - Pagamentos':^25}")
      print('=' * 25)
      preco = float(input("Preço das compras: R$"))
      print("FORMAS DE PAGAMENTO")
      print('''[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
      ''')
      opcao = int(input("Qual é a opão? "))
      if opcao == 0 or opcao > 4:
        print("Opcção inválida")
      elif opcao == 1:
        print(
          f"Sua compra de R${preco:.2f} vai custar {preco - (preco*10/100):.2f} no final"
        )
      elif opcao == 2:
        print(
          f"Sua compra de R${preco:.2f} vai custar {preco - (preco*5/100):.2f}"
        )
      elif opcao == 3:
        print(
          f"Sua será paga em 2 parcelas de R${preco/2:.2f} sem juros, total {preco:.2f}"
        )
      elif opcao == 4:
        parcelas = int(input("Quantas parcelas? "))
        print(
          f"Sua compra será parcelada em {parcelas}x de R${(preco + (preco * 20 / 100)) / parcelas:.2f} COM JUROS"
        )
        print(
          f"Sua compra de R${preco:.2f} vai custar R${preco + (preco * 20 / 100):.2f} no final."
        )

    case '45':
      print('=' * 25)
      print(f"{'D45 - JOKENPO':^25}")
      print('=' * 25)
      print(emoji.emojize("""Suas Opões:
[ 0 ] Pedra :raised_fist:
[ 1 ] Papel :raised_hand:
[ 2 ] Tesoura :victory_hand:
"""))
      escolha = [
        ':raised_fist:', ':raised_hand:', ':victory_hand:', ':prohibited:'
      ]
      jogador = int(input("Qual é a sua jogada? "))
      if jogador > 2:
        jogador = 3
      comp = randint(0, 2)
      print("Jo")
      sleep(1)
      print("KEN")
      sleep(1)
      print("PO!!!")
      print('')
      print(emoji.emojize(f'A máquina escolheu {escolha[comp]}'))
      print(emoji.emojize(f'O jogador escolheu {escolha[jogador]}'))
      print('')
      if jogador > 2:
        print("Jogada inválida! Você pode tentar novamente.")
      elif jogador == comp:
        print("Empate")
      elif jogador == 0 and comp == 1 or jogador == 1 and comp == 2 or jogador == 2 and comp == 0:
        print("Computador venceu!!!")
      elif comp == 0 and jogador == 1 or comp == 1 and jogador == 2 or comp == 2 and jogador == 0:
        print("Parabéns!!! Você venceu!!!")

    case '46':
      print('=' * 25)
      print(f"{'D46 - Contagem Regressiva':^25}")
      print('=' * 25)
      for c in range (10, -1, -1):
        print(c)
        sleep(1)
      print('Feliz ano novo!!!')
      print(emoji.emojize(':fireworks: :fireworks: :fireworks: :fireworks:'))

    case '47':
      print('=' * 25)
      print(f"{'D47 - Contagem de Pares':^25}")
      print('=' * 25)
      for c in range (2, 51, 2):
         print(c, end=' ')
      print("Acabou!")

    case '48':
      print('=' * 25)
      print(f"{'D47 - Soma Impares /3':^25}")
      print('=' * 25)
      #Faça um programa que calcule asoma entre todos os números impares que são múltiplos de três dentro do intervalo de 1 a 500
      n=0
      for c in range (1, 500, 2):
        if c % 3 == 0:
          n += c
      print(f"A soma dos valores ímpares e múltiplos de 3 no intervalo de 1 a 500 é {n}")

    case '49':
      print('=' * 25)
      print(f"{'D49 - Tabuada 2.0':^25}")
      print('=' * 25)
      n=int(input('Digite um número para ver sua tabuada: '))
      for _ in range (1, 11):
        print(f"{n:2}  x {_:2} = {n*_:2}")

    case '50':
      print('=' * 25)
      print(f"{'D50 - Soma dos Pares':^25}")
      print('=' * 25)
      #Desenvolva um programa que leira 6 números inteiros e mostre a soma apenas daqueles que forem pares:
      soma=0
      cont=0
      for _ in range (1, 7):
        n=int(input(f"Digite o {_}º numero: "))
        if n % 2 == 0:
          soma += n
          cont += 1
      print(f"Você informou {cont} valores pares e a soma é igual a {soma}")

    case '51':
      print('=' * 25)
      print(f"{'D51 - 10 Termos de uma PA':^25}")
      print('=' * 25)
      termo1=int(input("Primeiro termo: "))
      razao=int(input("Razão: "))
      ultimo=termo1 + 10 * razao
      for a in range (termo1, ultimo, razao):
        print(a, end=' ')

    case '52':
      print('=' * 25)
      print(f"{'D52 - Números Primos':^25}")
      print('=' * 25)
      n=int(input('Digite um número: '))
      cont=0
      for _ in range(1, n + 1):
        if n % _ == 0:
          print(f"\033[33m{_}\033[m", end=' ')
          cont += 1
        else:
          print(f"\033[31m{_}\033[m", end=' ')
      print(f"\nO número {n} foi divisível {cont} vezes")
      print("E por isso ele É PRIMO!" if cont == 2 else "E por isso ele NÃO É PRIMO!")

    case '53':
      print('=' * 25)
      print(f"{'D53 - Detec Palíndromos':^25}")
      print('=' * 25)
      #Crie um programa que inverta uma frase ou palavra e diga se é ou não palíndromo:
      frase=str(input("Digite uma frase: ")).strip().upper().split()
      frase = ''.join(frase)
      print(f"\nO inverso de \033[32m{frase}\033[m é \033[33m{frase[::-1]}\033[m")
      print("A frase digitada é um palíndromo!" if frase == frase[::-1] else "A frase digitada não é um palíndromo!")

    case '54':
      print('=' * 25)
      print(f"{'D54 - Grupo Maioridade':^25}")
      print('=' * 25)
      ano_nasc = 0
      maior_idade = 0
      menor_idade = 0
      
      for pessoa in range(1, 8):
        ano_nasc = int(input(f"Em que ano a {pessoa}ª pessoa nasceu? "))
        if date.today().year - ano_nasc < 21:
          menor_idade += 1
        else:
          maior_idade += 1
      print(f"Ao todo tivemos {maior_idade} pessoa(s) maior(es) de idade")
      print(f"E também tivemos {menor_idade} pessoa(s) menor(es) de idade")

    case '55':
      print('=' * 25)
      print(f"{'D55 - Maior/menor Peso':^25}")
      print('=' * 25)
      Maior_peso = 0
      menor_peso = 0
      for pessoa in range(1, 6):
        peso = float(input(f"Peso da {pessoa}ª pessoa: "))
        if pessoa == 1:
          maior_peso = peso
          menor_peso = peso
        else:
          if peso > maior_peso:
            maior_peso = peso
          if peso < menor_peso:
            menor_peso = peso
      print(f"O maior peso lido foi de  {maior_peso}Kg")
      print(f"O menor peso lido foi de {menor_peso}Kg")

    case '56':
      print('=' * 25)
      print(f"{'D56 - Analizador Completo':^25}")
      print('=' * 25)
      soma_idade = 0
      homem_velho = ''
      maior_idade = 0
      mulheres = 0
      for pessoa in range (1, 5):
        print(f"\n--- {pessoa}ª PESSOA ---")
        nome=str(input("Nome: ")).strip()
        idade=int(input("Idade: "))
        sexo=str(input("Sexo [M/F]: ")).strip().upper()
        soma_idade += idade
        if sexo == 'M' and idade > maior_idade:
          homem_velho = nome
          maior_idade = idade
        if sexo == 'F' and idade < 20:
          mulheres += 1
      print(f"A média de idade do grupo é de {soma_idade/4:.1f}.")
      print(f"O homem mais velhor tem {maior_idade} e se chama {homem_velho}.")
      print(f"Ao todo são {mulheres} mulheres com menos de 20 anos.")
      
    case '57':
      print('=' * 25)
      print(f"{'D57 - Validação de Dados':^25}")
      print('=' * 25)
      '''Faça um programa que leia o sexo de uma pessoa mas só aceite "M" ou "F". Caso esteja errado peça a digitação novamente até um valor correto.'''
      sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
      while sexo not in "MF":
        sexo=str(input("Opção inválida. Por favor informe seu sexo [M/F]: ")).strip().upper()[0]
      print(f"Sexo {sexo} registrado com sucesso")

    case '58':
      print('=' * 25)
      print(f"{'D58 - Adivinhação 2.0':^25}")
      print('=' * 25)
      #Melhore o jogo do desafio 28 onde o computador pensa em um número de 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
      print("Sou seu computador...")
      pc = randint(0, 10)
      print(f"Acabei de pensar em um número entre 0 e 10.")
      print("Será que você consegue adivinhar qual foi?")
      gamer = int(input("Qual é o seu palpite? "))
      tentativas = 1
      while gamer != pc:
        if gamer > 10:
          print("Escolha um número entre 0 e 10.")
        else:
          print("Mais... " if gamer < pc else "Menos... ", end='')
        print("tente novamente.")
        gamer = int(input("Qual é o seu palpite? "))
        tentativas += 1
      print(f"\n\033[32mAcertou em {tentativas} tentativas. Parabéns\033[m")
    

    case '59':
      print('=' * 25)
      print(f"{'D59 - Menu de Opções':^25}")
      print('=' * 25)
      '''Leia dois valores e mostre um menu na tela
      [1]Somar
      [2]Multiplicar
      [3]Maior
      [4]Novos Números
      [5]Sair do Programa
      Seu programa devera realizar a operação solicitada em cada caso'''
      opcao = 4
      while opcao != 5:
        if opcao == 1:
          print(f"A soma entre {n1} e {n2} é igual a {n1 + n2}")
        elif opcao == 2:
          print(f"O resultado de {n1} x {n2} é {n1 * n2}")
        elif opcao == 3:
          print(f"Entre {n1} e {n2} o maior é {max(n1, n2)}")
        elif opcao == 4:
          n1 = int(input("Primeiro valor: "))
          n2 = int(input("Segundo valor: "))
        elif opcao > 5:
          print("Opcão inválida!")  
        print("""        [1]Somar
        [2]Multiplicar
        [3]Maior
        [4]Novos Números
        [5]Sair do Programa""")
        print('=' * 25)
        opcao = int(input("Qual é a sua opcao? \n"))
      print("Finalizando...")
      sleep(2)
      print("Fim do Programa!! Volte sempre!")
            
    case '60':
      print('=' * 25)
      print(f"{'D60 - Fatorial':^25}")
      print('=' * 25)      
      #Faça um programa que leia um númeo qualquer e mostre seu fatorial.
      n = c =int(input("Digite um número para calcular seu fatorial: "))
      print(f"Calculando {n}! = {n}", end='')
      while c > 1:
        c -= 1
        print(f" x {c}", end='')
        n *= c
      print('=',n)

    case '61':
      print('=' * 25)
      print(f"{'D61 - P.A. V2.0':^25}")
      print('=' * 25)
      #Refaça o desavio 51, lendo o primeiro termo e a razão de uma PA, mostrando so 10 primeiros termos da progreção usando a estrutura While
      termo = int(input("Primeiro termo: "))
      razao = int(input("Razão da PA: "))
      ultimo = termo + razao * 10
      a = termo
      while a != ultimo:
        print(a, end=' -> ')
        a += razao
      print("Fim")

    case '62':
      print('=' * 25)
      print(f"{'D62 - Super P.A. V3.0':^25}")
      print('=' * 25)
      #Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
      primeiro = termo = int(input("Primeiro temo: "))
      razao = int(input("Razão da PA: "))
      opcao = 10
      cont = 0
      while opcao != 0:
        opcao += cont
        while cont < opcao:
          print(termo, end=' -> ')
          termo += razao
          cont += 1
        print("PAUSA")
        opcao = int(input("Quantos termos você quer mostrar a mais? "))
      print(f"Progressão finalizada com {cont} termos mostrados.")



    case '63':
      print('=' * 25)
      print(f"{'D63 - Seq. de Fibonacci':^25}")
      print('=' * 25)
      """Escreva um programa que leia um número N inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci."""
      termo = int(input("Quantos termos você quer mostrar? "))
      a = 0
      b = 1
      cont = 2
      print(f"{a} -> {b} -> ", end='')
      while cont < termo:
        c = a + b
        print(c, end=' -> ')
        a = b
        b = c
        cont += 1
      print('FIM')

    case '64':
      print('=' * 25)
      print(f"{'D64 - Vários valores V1.0':^25}")
      print('=' * 25)
      """Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)"""
      n = total = cont = 0
      while n != 999:
        n = int(input("Digite um númeo [999 para parar]: "))
        if n != 999:
          total += n
          cont += 1
      print(f"Você digitou {cont} números e a  soma entre eles foi {total}")

    case '65':
      print('=' * 25)
      print(f"{'D65 - Vários valores V1.0':^25}")
      print('=' * 25)
      """Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o meor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""
      opcao = "S"      
      maior = menor = soma = cont = 0
      while opcao != "N":
        if opcao == "S":
          n = int(input("Digite um número: "))        
          cont += 1
          soma += n
          if cont == 1:
            maior = menor = n
          else:
            if n > maior:
              maior = n
            if n < menor:
              menor = n
        else:
          print("Opcao inválida. Apenas Sim ou Não")
        opcao = str(input("Quer continuar? [S/N]")).strip().upper()[0]
      media = soma / cont
      print(f"Você digitou {cont} números e a média foi {media:.2f}")
      print(f"O maior valor foi {maior} e o menor foi {menor}")

    case '66':
      print('=' * 25)
      print(f"{'D66 - Números com flag':^25}")
      print('=' * 25)
      cont = soma = 0
      while True:
        n = int(input("Digite um valor (999 para parar): "))
        if n == 999:
          break
        cont += 1
        soma += n
      print(f"A soma dos {cont} valores foi {soma}!")

    case '67':
      print('=' * 25)
      print(f"{'D67 - Tabuadas 3.0':^25}")
      print('=' * 25)
      while True:
        tab = int(input("Quer ver a tabuada de qual valor? (Negativo para parar): "))
        print('-' *25)
        if tab > 0:
          for _ in range (1, 11):
            print(f"{tab:2} x {_:3} = {tab * _ :3}")
          print('-' *25)
        else:
          break
      print("Tabuada encerrada. Volte sempre!!!")
      
    case '68':
      print('=' * 25)
      print(f"{'D68 - Par ou Impar':^25}")
      print('=' * 25)
      vitorias = 0
      while True:
        jogador = int(input("Digite um valor: "))
        jogada =' '
        while jogada not in "PI":
          jogada = str(input("Par ou Ímpar? [P/I]")).strip().upper()[0]
        maquina = randint(0, 10)
        total = maquina + jogador
        print('-'*25)
        print(f"Você jogou {jogador} e o computador {maquina}. Total deu {total}")
        print('-'*25)
        if total % 2 == 0 and jogada == 'P' or total % 2 == 1 and jogada == 'I':
          print("Você VENCEU!!!")
          print("Vamos jogar novamente...")
          vitorias += 1
        else:
          print("Você PERDEU!!!")
          break
      print("-" *25)
      print(f"GAME OVER! Você venceu {vitorias} vezes.")

    case '69':
      print('=' * 25)
      print(f"{'D69 - Dados do Grupo':^25}")
      print('=' * 25)
      print(f"{'Cadastre uma pessoa':^25}")
      print('-'*25)
      maiores_idade = homens = mulheres_menores = 0
      while True:
        idade = int(input("Idade: "))
        sexo = ' '
        while sexo not in "MmFf":
          sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
        if idade > 18:
          maiores_idade += 1
        if sexo == 'M':
          homens += 1
        if sexo == 'F' and idade < 20:
          mulheres_menores += 1
        opcao = " "
        while opcao not in 'SN':
          print('-'*25)
          opcao = str(input("Quer continuar? ")).strip().upper()
          print('-'*25)
        if opcao == 'N':
          break
      print(f"Total de pessoas com mais de 18 anos: {maiores_idade}")
      print(f"Ao todo temos {homens} homens cadastrados")
      print(f"E temos {mulheres_menores} com menos de 20 anos")

    case '70':
      print('=' * 25)
      print(f"{'D70 - Estatistica em Prod':^25}")
      print('=' * 25)
      total_compra = preco_caro = preco_barato = 0
      prod_barato = ' '
      print(f"{'SUPER LOJA':^25}")
      print('-' *25)
      while True:
        prod = str(input("Nome do Produto: ")).strip()
        preco = float(input("Preço: R$"))
        if total_compra == 0:
          preco_barato = preco
          prod_barato = prod
        else:
          if preco < preco_barato:
            preco_barato = preco
            prod_barato = prod
        total_compra += preco
        if preco > 1000.00:
          preco_caro += 1
        opcao = ' '
        while opcao not in 'SN':
          opcao = str(input("Quer continuar? ")).strip().upper()[0]
        if opcao == 'N':
          break
      print(f"{'FIM DO PROGRAMA':-^25}")
      print(f"O total da compra foi R${total_compra:.2f}")
      print(f"Temos {preco_caro} produtos custando mais de R$1000.00")
      print(f"O produto mais barato foi {prod_barato} custando R${preco_barato:.2f}")


    case '71':
      print('=' * 25)
      print(f"{'D71 - Caixa Eletrônico':^25}")
      print('=' * 25)
      saque = int(input("Que valor você quer sacar? R$"))      
      print('=' * 25)
      saldo = saque
      cedula = 50
      while True:
        if saldo >= cedula:
          totcedula = saque // cedula
          saldo = saque % cedula
          print(f"Total de {totcedula} de R${cedula}")
          saque = saldo
        if saldo == 0:
          break
        match cedula:
          case 50:
            cedula = 20
          case 20:
            cedula = 10
          case 10:
            cedula = 1            
      print("Fim caixa eletrônico, volte sempre!")


    case '71b':
      print('=' * 25)
      print(f"{'D71 - Caixa Eletrônico':^25}")
      print('=' * 25)
      valor = int(input('Quanto dinheiro deseja sacar? '))
      print(f'==> {valor // 50} notas de R$50') if valor // 50 > 0 else False
      valor %= 50
      print(f'==> {valor // 20} notas de R$20') if valor // 20 > 0 else False
      valor %= 20
      print(f'==> {valor // 10} notas de R$10') if valor // 10 > 0 else False
      valor %= 10
      print(f'==> {valor} notas de R$1') if valor > 0 else False

    case '72':
      print('=' * 25)
      print(f"{'D72 - Números por Extenso':^25}")
      print('=' * 25)
      numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'douze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
      n = int(input('Digite um número entre 0 e 20: '))
      while n < 0 or n > 20:
        n = int(input("Tente novamente. Digite um número entre 0 e 20: "))
      print(f"Você digitou o número \33[32m{numeros[n]}\33[m")

    case '73':
      print('=' * 25)
      print(f"{'D73 - TImes Futebol 2023':^25}")
      print('=' * 25)
      times = ('Palmeiras', 'Botafogo', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Cuiabá', 'São Paulo', 'Corinthians', 'Fortaleza', 'Internacional', 'Santos', 'Vasco da Gama', 'Cruzeiro', 'Bahia', 'Goiás', 'Coritiba', 'América-MG')
      print(times)
      print('-' * 25)
      print(f"Os 5 primeiros são: \33[32m{times[:5]}\33[m")
      print('-' * 25)
      print(f"Os 4 últimos são \33[31m{times[-4:]}\33[m")
      print('-' * 25)
      print(f"Times em ordem alfabética \33[34m{sorted(times)}\33[m")
      print('-' * 25)
      print(f"O \33[35mFluminense\33[m esta na {times.index('Fluminense')+1}º posição.")

    case '74':
      print('=' * 25)
      print(f"{'D74 - Valores em Tuplas':^25}")
      print('=' * 25)
      valores = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
      print(f"O valores sorteados foram: ", end='')
      for valor in valores:
        print(valor, end=' ')
      print(f"\nO maior valor sorteado foi {max(valores)}")
      print(f"O menor valor sorteado foi {min(valores)}")

    case '75':
      print('=' * 25)
      print(f"{'D75 - Análise de dados':^25}")
      print('=' * 25)
      numeros =(
        int(input('Digite um núemro: ')), int(input('Digite outro número: ')), int(input('Digite mai um número: ')), int(input('Digite o último número: '))
      )
      print(f"Você digitou os valores {numeros}")
      print(f"O valor 9 apareceu {numeros.count(9)} vezes")
      if 3 in numeros:
        print(f"O valor 3 apareceu na {numeros.index(3)+1}ª posição")
      else:
        print('O valor 3 não foi digitado')
      print("Os valores pares digitados foram: ")
      for numero in numeros:
        if numero % 2 ==0:
          print(numero, end=' ')

    case '76':
      print('=' * 25)
      print(f"{'D76 - Listagem de Preços':^25}")
      print('=' * 25)
      produtos = 'Lápis', 1.75, 'borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Trasnferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90
      for c, produto in enumerate(produtos):
        if c % 2 ==0:
          print(f"{produto:.<13}", end=' ')
        else:
          print(f"R${produto:>7}")
          
    case '77':
      print('=' * 25)
      print(f"{'D77 - Contando Vogais':^25}")
      print('=' * 25)
      palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO', 
      for palavra in palavras:
        print(f"\nNa palavra {palavra} temos ", end='')
        for letra in palavra:
          if letra in 'AEIOU':
            print(letra.lower(), end=' ')
            
    case '78':
      print('=' * 25)
      print(f"{'D78 - Maior Menor em Lista':^25}")
      print('=' * 25)
      valores = []
      for c in range(0, 5):
       valores.append(int(input(f'Digite um valor para a posição {c}: ')))
      print(f"Você digitou os valores {valores}")
      maior = max(valores)
      menor = min(valores)
      print(f"O maior valor digitado foi {maior} na(s) posição(ções)", end=' ')
      for p, valor in enumerate(valores):
        if valor == maior:
          print(p, end='... ')
      print(f"\nO menor valor digitado foi {menor} na(s) porsição(ções)", end=' ')
      for p, valor in enumerate(valores):
        if valor == menor:
          print(p, end ='... ')

    case '79':
      print('=' * 25)
      print(f"{'D79 - Únicos em Lista':^25}")
      print('=' * 25)
      lista_numeros = []
      while True:
        n = int(input('Digite um valor: '))
        if n not in lista_numeros:
          lista_numeros.append(n)
          print('Valor adicionado com sucesso...')
        else:
          print('Valor duplicado! Não adicionado...')
        opcao = ' '
        while opcao not in 'SN':
          opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if opcao == "N":
          break
      lista_numeros.sort()
      print(f"Os valores digitados foram {lista_numeros}")
      
    case '80':
      print('=' * 25)
      print(f"{'D80 - Lista Ordenada':^25}")
      print('=' * 25)
      numeros = []
      for c in range (1, 6):
        n = int(input('Digite um valor: '))
        if c == 1 or n >= max(numeros):
          print('Adicionado na úlrima posição')
          numeros.append(n)
        else:
          for k, numero in enumerate(numeros):
            if n < numero:
              numeros.insert(k, n)
              print(f"Acidionado na {k+1}ª posição")
              break
      print(numeros)

    case '81':
      print('=' * 25)
      print(f"{'D80 - Extraindo Dados':^25}")
      print('=' * 25)
      cont = 0
      lista = []
      while True:
        lista.append(int(input('Digite um valor: ')))
        cont += 1
        op = ' '
        while op not in 'sSnN':
          op = str(input('QUer continuar? [S/N]')).strip()[0]
        if op in 'Nn':
          break
      print(f"Você digitou {cont} elementos.")
      lista.sort(reverse=True)
      print(f"Os valores em orde decrescente são {lista}")
      print('O valor 5 faz parte da lista!' if 5 in lista else 'O valor 5 não faz parte da lista')

    case '82':
      print('=' * 25)
      print(f"{'D82 - Dividindo listas':^25}")
      print('=' * 25)
      numeros = []
      pares = []
      impares = []
      while True:
        n = int(input('Digite um número: '))
        numeros.append(n)
        if n % 2 == 0:
          pares.append(n)
        else:
          impares.append(n)
        op = ' '
        while op not in "SsNn":
          op = str(input("Quer Continuar? [S/N] ")).strip()[0]
        if op in 'Nn':
          break
      print('-'*25)
      print(f"A lista completa é {numeros}")
      print(f"A lista de pares é {pares}")
      print(f"A lista de ímpares é {impares}")
      
    case '83':
      print('=' * 25)
      print(f"{'D83 - Expressões Mat.':^25}")
      print('=' * 25)
      expressao = str(input('Digite a expressão: ')).strip()
      parentesis=[]
      for letra in expressao:
        if letra == '(':
          parentesis.append(letra)
        elif letra == ')':
          if len(parentesis) == 0:
            parentesis.append(letra)
            break
          else:
            parentesis.pop()
      if len(parentesis) == 0:
        print('Sua expressão está válida.')
      else:
        print('Sua expressão está errada!')

    case '84':
      print('=' * 25)
      print(f"{'D84 - Análise Lista Comp.':^25}")
      print('=' * 25)
      pessoas = list()
      dados = list()
      lista_pesados = list()
      lista_leves = list()
      cont = pesado = leve = 0
      while True:
        dados.append(str(input('Nome: ')))
        dados.append(float(input('Peso: ')))
        if len(pessoas) == 0:
          pesado = leve = dados[1]
        else:
          if dados[1] > pesado:
            pesado = dados[1]
          if dados[1] < leve:
            leve = dados[1]
        pessoas.append(dados[:])
        dados.clear()
        cont += 1
        op = ' '
        while op not in 'SN':
          op = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if op == 'N':
          break
      for pessoa in pessoas:
        if pessoa[1] == pesado:
          lista_pesados.append(pessoa[0])
        if pessoa[1] == leve:
          lista_leves.append(pessoa[0]) 
      print('-'*25)
      print(f"Ao todo, você cadastrou {cont} pessoas.")
      print(f"O maior peso foi {pesado:.1f}Kg. peso de ", end='')
      for p in lista_pesados:
        print(p, end=' ')
      print(f"\nO menor peso foi de {leve:.1f}Kg. peso de ", end='')
      for p in lista_leves:
        print(p, end='')
      print()
      
    case '85':
      print('=' * 25)
      print(f"{'D85 - Listas Pares/Ímpares':^25}")
      print('=' * 25)
      lista=[[], []]
      for c in range (1, 8):
        n = int(input(f"Digite o {c}º valor: "))
        if n % 2 == 0:
          lista[0].append(n)
        else:
          lista[1].append(n)
      lista[0].sort()
      lista[1].sort()
      print(f"Os valores pares digitados foram: {lista[0]}")
      print(f"Os valores ímpares digitados foram: {lista[1]}")

    case '86':
      print('=' * 25)
      print(f"{'D86 - Matriz Python':^25}")
      print('=' * 25)
      matriz = [[], [], []]
      for x in range (0, 3):
        for y in range(0, 3):
          matriz[x].append(int(input(f"Digite um valor para [{x}, {y}]: ")))
      print('-'*25)
      for x in matriz:
        for y in x:
          print(f"[{y:^5}]", end=' ')
        print()
        
    case '87':
      print('=' * 25)
      print(f"{'D87 - Analise/Matriz':^25}")
      print('=' * 25)
      matriz = [[], [], []]
      pares = terceira_coluna = 0
      for l in range (0, 3):
        for c in range (0, 3):
         matriz[l].append(int(input(f"Digite um valor para [{l}, {c}]: ")))
      print("-"*25)
      for x in matriz:
        for p, y in enumerate(x):
          print(f"[{y:^5}]", end=' ')
          if y % 2 == 0:
            pares += y
          if p == 2:
            terceira_coluna += y
        print()
      print('-'*25)
      print(f"A soma dos valores pares é {pares}")
      print(f"A soma dos valores da terceira coluna é {terceira_coluna}")
      print(f"O maior valor da segunda linha é {max(matriz[1])}")
      
    case '88':
      print('=' * 25)
      print(f"{'D88 - MEGA SENA':^25}")
      print('=' * 25)
      jogada = []
      jogos = list()
      q = int(input('Quantos jogos você quer que eu sorteir? '))
      print(f"{f' Sorteando {q} jogos ':-^25}")
      for c in range (1, q+1):
        while len(jogada) != 6:
          n = randint(1, 60)
          if n not in jogada:
            jogada.append(n)
        jogada.sort()
        print(f"Jogo {c}: {jogada}")
        jogos.append(jogada[:])
        jogada.clear()
        sleep(0.8)
      print(f"{' BOA SORTE! ':*^25}")

    case '89':
      print('=' * 25)
      print(f"{'D89 - Bolerim':^25}")
      print('=' * 25)
      boletim = list()
      while True:
        nome = str(input('Nome: '))
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        media = (nota1 + nota2)/2
        boletim.append([nome, [nota1, nota2], media])
        op = ' '
        while op not in 'SsNn':
          op = str(input('Quer continuar? [S/N]'))
        if op in 'Nn':
          break
      print('-'*25)
      print(f'No', f"{'nome':<15}", 'MÉDIA')
      for n, aluno in enumerate(boletim):
        print(n, end='  ')
        print(f"{f'{aluno[0]}':<16}", end='')
        print(f"{aluno[2]:^5.1f}")
      print('-'*25)
      while True:
        escolha = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
        if escolha == 999:
          print('Programa Finalizado, volte sempre!')
          break
        elif escolha >= len(boletim):
          print('Inválido, aluno não cadastrado! Tente novamente.')
        else:
          print('Notas do ', boletim[escolha][0], 'são', boletim[escolha][1])
          print('-'*25)

    case '90':
      print('=' * 25)
      print(f"{'D89 - Dicionário Python':^25}")
      print('=' * 25)
      aluno = {}
      aluno['nome'] = str(input('Nome: '))
      aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
      if aluno['media'] >= 7:
        aluno['situação'] = 'APROVADO'
      elif aluno['media'] >= 5:
        aluno['situação'] = 'RECUPERAÇÂO'
      else:
        aluno['situação'] = 'REPROVADO'
      print('-'*25)
      for k, v in aluno.items():
        print(f'- {k} é igual a {v}')

    case '91':
      print('=' * 25)
      print(f"{'D91 - Jogando Dados':^25}")
      print('=' * 25)
      jogadores = {}
      ranking = {}
      for j in range(1, 5):
        jogadores[f'jogador{j}'] = randint(0, 6)
        print(f'O jogador{j} tirou {jogadores[f"jogador{j}"]} no dado.')
        sleep(1)
      print('-'*25)
      print(f"{'== RANKGING ==':^25}")
      ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
      for i, v in enumerate(ranking):
        print(f'{i}º lugar: {v[0]} com {v[1]}')
        sleep(1)

    case '92':
      print('=' * 25)
      print(f"{'D92 - Cadastro Trabalho':^25}")
      print('=' * 25)
      cadastro = dict()
      cadastro['nome'] = str(input('Nome: '))
      cadastro['idade'] = date.today().year - int(input('Ano de Nascimento: '))
      cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
      if cadastro['ctps'] != 0:
        cadastro['contratação'] = int(input('Ano de Contratação: '))
        cadastro['salario'] = float(input('Salário: R$'))
        cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratação'] + 35) - date.today().year)
      print('-'*25)
      for k, v in cadastro.items():
        print(f'  - {k} tem valor {v}')

    case '93':
      print('=' * 25)
      print(f"{'D93 - Cadastro Jogador':^25}")
      print('=' * 25)
      jogador = {'nome':'','gols':list(),'total': 0}
      jogador['nome'] = str(input('Nome do jogador: '))
      partida = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
      for c in range(1, partida +1):
        jogador['gols'].append(int(input(f'Quantos gols na {c}ª partida? ')))
      jogador['total'] = sum(jogador['gols'])
      print('-'*25)
      print(jogador)
      print('-'*25)
      for k, v in jogador.items():
        print(f'O campo {k} tem o valor {v}')
      print('-'*25)
      print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
      for p, gol in enumerate(jogador['gols']):
        print(f' => Na partida {p+1}, fez {gol} gols.')
      print(f'Foi um total de {jogador["total"]} gols.')
        
    case '94':
      print('=' * 25)
      print(f"{'D94 - Dicionários/Listas':^25}")
      print('=' * 25)
      pessoas = []
      soma_idade = 0
      muleres = 0
      while True:
        nome = str(input('Nome: '))
        while True:
          sexo = str(input('Sexo: [M/F]'))[0].strip().upper()
          if sexo not in 'MF':
            print('Favor apenas M ou F.')
          else:
            break
        idade = int(input('Idade: '))
        soma_idade += idade
        pessoas.append({'nome': nome, 'sexo': sexo, 'idade': idade})
        while True:
          op = str(input('Deseja continuar? [S/N]'))[0].strip().upper()
          if op not in 'SN':
            print('Erro! Favor apenas S ou N!')
          else:
            break
        if op == 'N':
          break
      print('-'*25)
      print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
      print(f'B) A média de idade é {soma_idade/len(pessoas):5.2f} anos.')
      print(f'C) As mulheres cadastradas foram ', end='')
      for p in pessoas:
        if p['sexo'] == 'F':
          print(p['nome'], end=' ')
      print()
      print(f'D) Lista das pessoas acima da média:')
      for p in pessoas:
        if p['idade'] > soma_idade/len(pessoas):
          print(f'  Nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')
          
    case '95':
      print('=' * 25)
      print(f"{'D94 - Dicionário Jogadores':^25}")
      print('=' * 25)
      jogadores = []
      gols = []
      while True:
        nome = str(input('Nome do jogador: '))
        partidas = int(input(f'Quantas partidas {nome} jogou?'))
        for g in range(1, partidas +1):
          gols.append(int(input(f'Quantos gols na {g}ª partida? ')))
        total = sum(gols)
        jogadores.append({'nome' : nome, 'gols' : gols.copy(), 'total': total})
        gols.clear()
        while True:
          op = str(input('Quer continuar? [S/N]: '))[0].strip().upper()
          if op not in 'SN':
            print('Inválido! Apenas S ou N')
          else:
            break
        if op == 'N':
          break
      print('-'*25)
      print('cod nome   gols    total')
      print('-'*25)
      for c, jogador in enumerate(jogadores):
        print(f'{c:<4}{jogador["nome"]:<7}{str(jogador["gols"]):<7}{jogador["total"]:>3}')
      print('-'*25)
      while True:
        op = int(input('Quer mostrar os dados de qual jogador? (999 para parar)'))
        if op <= len(jogadores):
          print(f'-- Levantamento do jogador {jogadores[op]["nome"]}:')
          for c, v in enumerate(jogadores[op]["gols"]):
            print(f'     No jogo {c+1} fez {v} gols.')
          print('-'*25)
        elif op == 999:
          break
        else:
          print(f'Não existe jogador com o código {op}!')
          print('-'*25)
      print('Volte Sempre!!!')

    case '96':
      print('=' * 25)
      print(f"{'D96 - Controle de Terrenos':^25}")
      print('=' * 25)
      def area(l, c):
        print(f'A área de um terreno {l:.1f}x{c:.1f} é de {l*c:.1f}m².')

  
      print('-'*25)
      largura = float(input('LARGURA (m): '))
      comprimento = float(input('COMPRIMENTO (m): '))
      area(largura, comprimento)

    case '97':
      print('=' * 25)
      print(f"{'D97 - Print Especial':^25}")
      print('=' * 25)
      def escreva(mensagem):
        espaco = len(mensagem) + 4
        print('~'*espaco)
        print(f'  {mensagem}  ')
        print('~'*espaco)


      escreva(str(input('Digite algo: ')))
        

    #case '':
      #print('=' * 25)
      #print(f"{'D9 - ':^25}")
      #print('=' * 25)
  
    case _:
      print("Infálido ou ainda não existe!")

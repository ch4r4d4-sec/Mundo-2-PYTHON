#FAÇA UM PROGRAMA QUE LEIA O NAO DE NASCIMENTO DE UM JOVEM E INFORME DE ACORDO COM SUA IDADE 
#SE ELE IANDA VAI SE ALISTAR AO SERVIÇO MILITAR SE É A HORA DE SE ALISTAR OU JA PASSOU.

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.' .format(nasc, idade, atual))

if idade == 18:
   print('Você tem que se alistar IMEDIATAMENTE1')
elif idade < 18:
   saldo  = 18 - idade
   print('Ainda faltam {} anos para o ALISTAMENTO:' .format(saldo))
   ano = atual + saldo
   print('Seu alistamento será em {}' .format(ano))
elif idade > 18:
   saldo = idade - 18
   print('Você já deveria ter se alistado há {} anos.' .format(saldo))
   ano = atual - saldo
   print('Seu alistamento foi em {}' .format(ano))

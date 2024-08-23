#A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA
# - ATÉ 9 ANOS:MIRIM - ATÉ 14 ANOS:INFANTIL - ATÉ 19 ANOS:JUNIOR - ATÉ 25 ANOS: SÊNIOR - ACIMA: MASTER

from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.' .format(idade))

if idade <= 9:
   print('Classificação: MIRIM')
elif idade <= 14:
   print('Classificação: INFANTIL')
elif idade <= 19:
   print('Classificação: JUNIOR')
elif idade <= 25:
   print('Classificação: SÊNIOR')
else:
   print('Classificação: MASTER')
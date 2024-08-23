#FAÇA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA.
#PERGUNTE O VALOR DA CASA , O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
#A PRESTAÇÃO MENSAL, NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMRESTIMO SERÁ NEGADO. 

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print('Para pagar a casa de R$ \033[32m{:.2f}\033[m em {} anos' .format(casa, anos), end='')
print('a prestação será de R$ \033[32m{:.2f}\033[m' .format(prestacao))

if prestacao <= minimo:
   print('Empréstimos pode ser \033[32mCONCEDIDO!\033[m')
else:
   print('Empréstimo \033[31mNEGADO!\033[m')

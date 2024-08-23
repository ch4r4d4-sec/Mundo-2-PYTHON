#FAÇA UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO
# A VISTA DINHEIRO/CHEQUE:10% DE DESCONTO
#A VISTA NO CARTÃO:5% DE DESCONTO
#EM ATE 2x NO CARTÃO:PREÇO NORMAL
#3X OU MAIS NO CARTÃO:20% DE JUROS

print(' \033[34m{:=^40}\033[m' .format(' Painel de pagamento '))
preco = float(input('Preço das compras: R$ '))
print('''\033[36mFORMAS DE PAGAMENTO\033[m
\033[34m[ 1 ]\033[m Á vista dinheiro/cheque
\033[34m[ 2 ]\033[m Á vista cartão
\033[34m[ 3 ]\033[m 2x no cartão
\033[34m[ 4 ]\033[m 3x ou mais no cartão''')

opcao = int(input('Qual a sua opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em \033[31m2x\033[m de R$\033[32m{:.2f}\033[m sem juros!' .format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em \033[31m{}x\033[m de R$\033[32m{:.2f}\033[m com juros!'.format(totparc, parcela))
else:
    total = preco
    print('\033[31mOPÇÃO INVÁLIDA\033[m de pagamento. Tente novamente.')
print('Sua compra de R$\033[32m{:.2f}\033[m vai custar R$\033[32m{:.2f}\033[m no final.' .format(preco, total))
#FAÇA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS MOSTRANDO NA TELA UMA MENSAGEM:
# - O PRIMEIRO VALOR É MAIOR
#- O SEGUNDO VALOR É MAIOR
#- OS DOIS SÃO IGUAIS

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
   print('O primeiro valor é maior: ')
elif n2 > n1:
   print('O segundo valor é maior: ')
else:
   print('Os dois valores são iguais')

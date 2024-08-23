#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USÚARIO ESCOLHER QUAL 
#SERÁ A BASE DE CONVERSÃO:
#[ 1 ] COVERTER PARA BINÁRIO
#[ 2 ] COVERTER PARA OCTAL
#[ 3 ] CONVERTER PARA HEXADECIMAL

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
\033[32m[ 1 ]\033[m converter para BINÁRIO
\033[32m[ 2 ]\033[m coverter para OCTAL
\033[32m[ 3 ]\033[m converter para HEXADECIMAL''')
opcao = int(input('Qual a sua opção: '))
if opcao == 1:
   print('{} convertido para BINÁRIO é igual a {}' .format(num, bin(num) [2:]))
elif opcao == 2:
   print('{} convertido para OCTAL é igual a {}' .format(num, oct(num)[2:]))
elif opcao == 3:
   print('{} convertido para HEXADECIMAL é igual a {}' .format(num, hex(num)[2:]))
else:
   print('Opção inválida. Tente novamente.')
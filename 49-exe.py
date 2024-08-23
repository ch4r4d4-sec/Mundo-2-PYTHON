#REFAÇA O DESAFIO 09 MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER SÓ QUE AGORA UTILIZANDO UM LAÇO FOR

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    print('{} x {:2} = {}' .format(num, c, num*c))
#JOGO JOKENPÔ


from random import randint
from time import sleep

items = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''\033[34mSuas opções:\033[m
\033[36m[ 0 ]\033[m PEDRA
\033[36m[ 1 ]\033[m PAPEL
\033[36m[ 2 ]\033[m TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.4)
print('KEN')
sleep(0.4)
print('PÔ!!')
print('\033[35m-=\033[m' * 11)
print('Computador jogou {}' .format(items[computador]))
print('Jogador jogou {}' .format(items[jogador]))
print('\033[35m-=\033[m' * 11)

if computador == 0:
    if jogador == 0:
        print('\033[34mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCEU!\033[m')
    else:
        print('\033[33mJOGADA INVÁLIDA!\033[m')
elif computador == 1:
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[34mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[32mJOGADOR VENCEU!\033[m')
    else:
        print('\033[33mJOGADA INVÁLIDA!\033[m')
elif computador == 2:
    if jogador == 0:
        print('\033[32mJOGADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[34mEMPATE!\033[m')
    else:
        print('\033[33mJOGADA INVÁLIDA!\033[m')
#FAÇA UM PROGRAMA QUE LEIA 6 NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES
#SE O VALOR FOR IMPAR DESCONSIDERAR-O

soma = 0
cont = 0

for c in range(1,7):
    num = int(input('Digite o {} valor: ' .format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}' .format(cont, soma))
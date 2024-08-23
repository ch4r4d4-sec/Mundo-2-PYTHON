#FAÇA UM PROGRAMA QUE LEIA 3 VALORES E DIGA SE PODE FAZER UM TRIANGULO E O TIPO QUE PODE FORMAR:
#EQUILÁTERO: TODOS OS LADOS IGUAIS
#ISÓSCELES: DOIS LADOS IGUAIS
#ESCALENO: TODOS OS LADOS DIFERENTES

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else: 
        print('ISÓSCELES!')

else:
    print('OS segmentos acima NÃO PODEM FORMAR triângulo!')
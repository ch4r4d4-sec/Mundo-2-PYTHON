#DESENVOLVA UMA LOGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA CALCULE O IMC E MOSTRE SEUS STATUS
#ABAIXO DE 18.5:ABAIXO DO PESO
#ENTRE 18.5 E 25:PESO IDEAL
#25 ATÉ 30:SOBREPESO
#30 ATÉ 40:OBSIDADE
#ACIMA DE 40:OBSIDADE MÓRBIDA

peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}' .format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBSIDADE')
elif  imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado')
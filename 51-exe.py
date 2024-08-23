#FAÇA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. NO FINAL MOSTRE AS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{} ' .format(c), end='-> ')
print('ACABOU.')
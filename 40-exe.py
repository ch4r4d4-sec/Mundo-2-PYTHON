#FAÇA UM PROGRAMA QUE LEIA A 2 NOTAS DE UM ALUNO E FAÇA A MEDIA PARA VER SE ESTÁ (REPROVADO, RECUPERAÇÃO OU APROVADO)

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print('Tirando as notas {:.1f} e {:.1f} sua média é {:.1f}' .format(nota1, nota2, media))

if 7 > media >= 5:
   print('O aluno está em RECUPERAÇÃO')
elif media < 5:
   print('O aluno está REPROVADO')
elif media >= 7:
   print('O aluno está APROVADO')
from datetime import date
atual = date.today().year
nascimento = int(input('Em que ano você nasceu? '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado a {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para seu alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamente será em {}'.format(ano))
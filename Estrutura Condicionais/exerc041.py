from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento
print('O atetla tem {}'.format(idade))
if idade <= 9:
    print('Ele está na categoria MIRIM!')
elif idade <= 14:
    print('Ele está na categoria INFATIL!')
elif idade <= 19:
    print('Ele está na categoria JUNIOR!')
elif idade <= 25:
    print('Ele está na categoria SÊNIOR!')
elif idade > 25:
    print('Ele está na categoria MASTER!')
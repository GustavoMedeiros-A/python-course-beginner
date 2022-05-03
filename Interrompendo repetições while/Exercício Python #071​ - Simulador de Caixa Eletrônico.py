# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
# o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("=" * 30)
print("{:^30}".format("Banco Dumb"))
print("=" * 30)
valor = int(input("Que valor você quer sacar? R$ "))
total = valor
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total = total - cedula
        total_cedula  = total_cedula + 1
    else:
        if total_cedula > 0:
            print(f"Total de {total_cedula} cédula de R${cedula}")
        if cedula == 50:
            cedula = 20
            total_cedula = 0
        else:
            if cedula == 20:
                cedula = 10
                total_cedula = 0
            else:
                if cedula == 10:
                    cedula = 1
                    total_cedula = 0
                else:
                    if total == 0:
                        break
print("="*10)
print("Volte sempre Dumb!")
# Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input("Você quer vê a tabuada de qual valor? "))
    if n < 0:
        break
    print('-' * 30)
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")
    print('-' * 30)
print("END")
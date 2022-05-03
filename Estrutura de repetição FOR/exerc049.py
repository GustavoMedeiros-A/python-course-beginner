# Refaça o DESAFIO 009, mostrando tauada de um número que o usuário escolher, só que agora utilizando laço for
n = int(input("Digite um número para vê sua tabuada: "))
for x in range(1, n):
    print(f"{n} x {x} = {n*x}")
    # or
    # print('{} x {} = {}'.format(n, x, n * x))
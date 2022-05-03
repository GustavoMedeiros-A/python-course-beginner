# Faça um programa que leia um número qualquer e mostre o seu fatorial
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120



n = int(input("Digite um número para calcular seu fatorial: "))
cont = n
f = 1
print(f"Calculando {n}! = ", end="")
while cont > 0:
    print(f"{cont} ", end="")
    print("x " if cont > 1 else "= ", end="")
    f *= cont
    cont -= 1
print(f"{f}")


from math import factorial
n = int(input("Digite um número para calcular seu fatorial: "))
f = factorial(n)
print(f"O fatorial de {n} é {f}")
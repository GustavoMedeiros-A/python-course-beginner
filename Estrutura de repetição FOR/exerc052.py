# Faça um programa que leia um número inteiro e diga se ele é ou não número primo

num = int(input("Digite um número: "))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[33m', end="")
        total += 1
    else:
        print("\33[31m", end="")
    print(f"{c}", end=" ")

print(f"\n\033[mO número {num} foi divisível {total}")
if total == 2:
    print("E por isso esse número é primo")
else:
    print("E por isso ele não é primo")
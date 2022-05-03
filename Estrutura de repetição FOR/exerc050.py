# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitador for ímpar desconsidere

soma = 0
cont = 0
for x in range(1, 7):
    num = int(input(f"Digite o {x} valor: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"Você informou {cont} números e a soma é {soma}")

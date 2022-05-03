# Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50

for x in range(2, 51):
    if x % 2 == 0:
        print(x, end=" ")
print("Acabou")

print("-"*85)
# OR

for n in range(2, 51, 2):
    print(n, end=" ")
print("Fim")
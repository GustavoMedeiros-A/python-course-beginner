# Faça um programa que mostre na tela uma contagem regressiva para o estouro dos fogos;
# indo de 10 até 0, com uma pausa de um segundo
from time import sleep
for x in range (10, -1, -1):
    print(x)
    sleep(0.5)
print("BOM")



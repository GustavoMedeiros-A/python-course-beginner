# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = total_1000 = menor = contador = 0
barato = ""
while True:
    produto = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$ "))
    contador = contador + 1
    total = total + preco
    if preco > 1000:
        total_1000 = total_1000 + 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = produto
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    if resposta == "N":
        break
print("{:-^40}".format(" Fim do Programa! "))
print(f"O valor total das comprar foi de R$ {total}")
print(f"Existem {total_1000} produtos que custam mais de R$ 1000,00")
print(f"O produto mais barato foi {barato} que custa R$ {menor:.2f}")
print("Acabou!")
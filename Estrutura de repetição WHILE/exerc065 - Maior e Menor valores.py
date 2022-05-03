# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = "S"
soma = quant = media = maior = menor = 0
while resp in "S":
    num = int(input("Digite um valor: "))
    quant = quant + 1
    soma = soma + num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N]: ")).upper().strip()
media = soma / quant
print(f"Você digitou {quant} e a média é {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
print("END!")



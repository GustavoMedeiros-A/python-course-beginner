# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre quantos números foram digitador e qual foi a soma entre eles
# (Desconsiderando o FLAG)


cont = n = soma = 0
while n != 999:
    n = int(input("Digite um valor [999 para parar]: "))
    if n != 999:
        soma = soma + n
        cont = cont + 1
print("END!")
print(f"Você digitou {cont} números! A soma entre eles é {soma}")



num = cont = soma = 0
num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um número [999 para parar]: "))
print(f"Você digitou {cont} números! A soma entre eles é {soma}")



n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print(f"A soma vale {s}")
# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
masculino = feminino_20 = idade_18 = 0
while True:
    idade = int(input("Digite a idade da pessoa: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Digite o sexo: [M/F] ")).strip().upper()[0]
    if idade > 18:
        idade_18 = idade_18 + 1
    if sexo == "M":
        masculino = masculino + 1
    if sexo == "F" and idade < 20:
        feminino_20 = feminino_20 + 1
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if resposta == "N":
        break


print(f"Exitem {idade_18} pessoas com idade maior que 18 anos!")
print(f"Existem {masculino} homens cadastrados!")
print(f"Existe {feminino_20} mulheres com menos de 20 anos cadrastradas!")
print("Acabou! ")

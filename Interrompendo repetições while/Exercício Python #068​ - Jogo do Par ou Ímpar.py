# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint
vitoria = 0
while True:
    print("=-"*10)
    print("VAMOS JOGAR PAR OU ÍMPAR")
    print("=-"*20)
    jogador = int(input("Digite um valor: "))
    computador = randint(0,11)
    total = jogador + computador
    escolha = " "
    while escolha not in "PI":
        escolha = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
        print("=-" * 10)
    print(f"Você jogou {jogador} e o computador {computador}! Total de {total}!", end=' ')
    print("DEU PAR!" if total % 2 == 0 else "DEU ÍMPAR!")
    if escolha == "P":
        if total % 2 == 0:
            print("Você ganhou!")
            vitoria = vitoria + 1
        else:
            print("Você perdeu! ")
            break
    else:
        if escolha == "I":
            if total % 2 == 1:
                print("Você ganhou!")
                vitoria = vitoria + 1
            else:
                print("Você perdeu!")
                break
    print("Vamos jogar novamente!")
print(f"Você venceu {vitoria} vezes! ")
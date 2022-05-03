from random import randint
print("""Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
print("--" * 11)
itens  = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input("Digite sua jogada: "))
cont = 0
print("--" * 11)
while cont <= 3:
    cont = cont + 1
    if jogador < 0 or jogador > 2:
        print("Jogada Inválida")
    else:
        print(f"Computador jogou {itens[computador]}")
        print(f"Jogador jogou {itens[jogador]}")
    if computador == 0:
        if jogador == 0:
            print("Empate")
        else:
            if jogador == 1:
                print("Jogador Ganhou!")
            else:
                if jogador == 2:
                    print("Computador Ganhou!")

    if computador == 1:
        if jogador == 0:
            print("Computador Ganhou!")
        else:
            if jogador == 1:
                print("Empate")
            else:
                if jogador == 2:
                    print("Jogador Ganhou!")
                else:
                    print("Jogada Inválida")
    if computador == 2:
        if jogador == 0:
            print("Jogador Ganhou!")
        else:
            if jogador == 1:
                print("Computador Ganhou!")
            else:
                if jogador == 2:
                    print("Empate")

# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador
# vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual o seu palpite? "))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais...Tente mais um vez!")
        else:
            if jogador > computador:
                print("Menos... Tente mais um vez!")

print(f"O número é {jogador}")
print(f"Acertou com {palpite} Tentativas! Parabéns!")
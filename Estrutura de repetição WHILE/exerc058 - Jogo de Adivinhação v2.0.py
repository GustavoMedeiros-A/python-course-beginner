# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador
# vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
print("Vou pensar em um número entre 0 e 10, tente adivinhar")
palpite = 0
jogador = int(input("Em que número eu pensei? "))
while jogador != computador:
    print("Errou, tente de novo!")
    jogador = int(input("Em que número eu pensei? "))
    palpite += 1
print(f"Acertou! Eu pensei no número {jogador}")
print(f"Foram necessários {palpite}!")
# Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
# Seu programa deverá realizar a operação solicitada em casa caso
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
opcao = 0
while opcao != 5:
    print(
    """
     [1] somar
     [2] multiplicar 
     [3] maior
     [4] novos números
     [5] sair do programa
    """)
    opcao = int(input(">>>>> Qual a sua opção: "))
    if opcao == 1:
        soma = num1 + num2
        print(f"A soma entre {num1} e {num2} é {soma}")
    else:
        if opcao == 2:
            multi = num1 * num2
            print(f"A multiplicação entre {num1} e {num2} é {multi}")
        else:
            if opcao == 3:
                if num1 > num2:
                    maior = num1
                else:
                    maior = num2
                    print(f"Entre {num1} e {num2} o maior é o {maior}")
            else:

                if opcao == 4:
                    print("Informe os números novamente!")
                    num1 = int(input("Digite o primeiro número: "))
                    num2 = int(input("Digite o segundo número: "))
                else:
                    if opcao == 5:
                        print("Finalizando! Volte sempre!")
                    else:
                        print("Opção Inválida! Tente Novamente!")
            print("=-="*10)






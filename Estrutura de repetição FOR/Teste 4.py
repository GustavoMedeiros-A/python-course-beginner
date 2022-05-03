#Perguntar 4 valores e somar ele no final
s = 0
for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s += n
print("Somatório de todos os valores foi {}".format(s))
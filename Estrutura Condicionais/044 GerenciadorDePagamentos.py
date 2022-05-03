print("{:=^40}".format(" Lojas M&M "))
preço = float(input("Preço das compras: R$ "))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input("Qual é a opção? "))

if opção == 1:
    total = preço * 0.90
elif opção == 2:
    total = preço * 0.95
elif opção == 3:
    total = preço
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R${:.2f}".format(parcela))
elif opção == 4:
    total = preço * 1.20
    totalparcelas = int(input("Quantas parcelas? "))
    parcela = total / totalparcelas
    print("Sua compra será parcelada em {}x de R${:.2f}".format(totalparcelas, parcela))
else:
    total = preço
    print("OPÇÃO INVÁLIDA de pagamento. Tente novamente!")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço, total))

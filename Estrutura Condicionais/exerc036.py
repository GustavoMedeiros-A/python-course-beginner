valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
meses = int(input('Em quantos meses pretende parcelar? '))
prestação = valor / meses
if prestação > salario * 0.30:
    print('Pagamento NEGADO!!')
else:
    print('Pagamento ACEITO!!')
print('A prestação será de {:.2f}'.format(prestação))
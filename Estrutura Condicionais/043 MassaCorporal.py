peso = float(input("Qual é o seu peso? (kg) "))
altura = float(input("Qual é a sua altura? (m) "))
imc = peso/ (altura ** 2)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.50:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Você está na faixa de peso normal")
elif 25 <= imc < 30:
    print("Você está em sobrepeso")
elif 30 <= imc < 40:
    print("Você está em obesidade, cuidado!")
elif imc >= 40:
    print("Você está em OBESIDADE MÓRBIDA!")

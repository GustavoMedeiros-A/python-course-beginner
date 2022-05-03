#Estrutura Aninhada

nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'José':
    print('Seu nome é bem usado no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Eca! Que nome feio!')

print('Tenha um bom dia {}'.format(nome))
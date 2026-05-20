

nome_dig = input('Digite seu nome: ')
peso_dig = float(input('Digite seu peso(kg): '))
altura_dig = float(input('Digite sua altura(m): '))


imc = peso_dig / (altura_dig*altura_dig)

print(f'Olá {nome_dig}, seu IMC é: {imc:.2f}')


nome_dig = input('Digite seu nome: ')
peso_dig = float(input('Digite seu peso(kg): '))
altura_dig = float(input('Digite sua altura(m): '))



imc = peso_dig / (altura_dig*altura_dig)

if imc < 18.5 :
    
    print(f'Olá {nome_dig}, seu IMC é: {imc:.2f}.')
    print('Alerta! Seu IMC está abaixo do peso. \nProcure um profissional')

if imc >= 18.5 and imc <= 24.9 :
    
    print(f'Olá {nome_dig}, seu IMC é: {imc:.2f}.')
    print('Parabéns! Seu IMC está no peso saudável. \nContinue assim!')

if imc >= 25 and imc <= 29.9 :
    
    print(f'Olá {nome_dig}, seu IMC é: {imc:.2f}.')
    print('Atenção! Seu IMC está em sobrepeso. \nProcure um profissional')
    
if imc > 29.9:
    
    print(f'Olá {nome_dig}, seu IMC é: {imc:.2f}.')
    print('Alerta! Seu IMC está em obesidade! \nProcure um profissional de urgência')

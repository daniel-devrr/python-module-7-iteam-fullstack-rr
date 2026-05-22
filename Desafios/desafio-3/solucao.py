

vel_dig = int(input('Digite a velocidade do veículo(Em número. Sem km/h): '))

if vel_dig > 80 :
    print("Multado! \nVocê excedeu o limite de 80km/h") 

elif vel_dig < 40 :
    print("Atenção! \nSua velocidade está abaixo do limite mínimo de 40km/h")

elif vel_dig < 80 :
    print("Boa viagem! \nDirija com segurança")

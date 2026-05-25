#calculos.py

def calcular_imc(peso, altura):
    imc = peso / altura
    return imc

def calassicar_imc(imc):

    msg_al = 'Alerta!'
    msg_pr = 'Seu IMC está: '

    if imc < 18.5:
        return f"{msg_al} Você está abaixo do peso!\nProcure um especialista."
    
    elif imc >= 18.5 and imc <= 24.99:
        return f'{msg_pr} Normal'
    
    elif imc >= 25 and imc <= 29.99:
        return f'{msg_pr} em Sobrepeso'
    
    elif imc >= 30 and imc <  39.99:
        return f'{msg_al} Seu IMC está em Obesidade!\nProcure um especialista.'
    
    elif imc > 40:
        return f'{msg_al} Você está em Obesidade Grave!\nProcure um especialista urgentemente!'
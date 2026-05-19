from datetime import datetime

nome = input("Digite seu nome: ")
anoDeNascimento = int(input("Digite seu ano de nascimento: "))
anoAtual = datetime.now().year

idadeHoje = anoAtual - anoDeNascimento

print(f'Sua idade é {idadeHoje}')
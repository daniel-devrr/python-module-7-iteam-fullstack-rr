# Lista 01 — Questão 03: Ficha de Cadastro
# Aluno: Daniel
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Solicite: nome completo, CPF (str), ano de nascimento (int), altura (float).
# O programa deve:
#   1. Calcular e exibir a idade em 2026.
#   2. Exibir todos os dados com f-string e tipos corretos.
#   3. Tratar com try/except o caso em que o ano não seja um número.
# Explique em comentário: por que float para altura e não int?
#   Resposta> A altura na maioria das vezes, contém números Racionais (com várias casas decimais), e
#  o tipo inteiro não é o ideal

# ── Sua solução abaixo ──────────────────────────────────────────────────────
from datetime import datetime

try:

    names = []
    cpf_db = []
    ano_db = []
    altura_db = []

    anoAtual = datetime.now().year

    name_dig = input('Digite seu nome: ')
    names.append(name_dig)

    cpf_dig = input('\nDigite seu CPF: ')
    cpf_db.append(cpf_dig)

    ano_nasc_dig = int(input('\nDigite o seu ano de nascimento: '))
    ano_db.append(ano_nasc_dig)
    idade_hoje = anoAtual - ano_db[-1]

    altura_dig = float(input('\nDigite sua altura: '))
    altura_db.append(altura_dig)


    


    print(f"\nDados salvos:\n\nNome: {names[-1]}\n",
         f"\nAno de Nascimento: {ano_db[-1]}\n",
         f"\nCPF: {cpf_db[-1]}\n",
         f"\nAltura: {altura_db[-1]}\n",
         f'\nSua idade hoje: {idade_hoje}')

except ValueError:
    print('\nErro! Digite um ano válido.')

finally:
    print('\nObrigado por utilizar nossos serviços.')

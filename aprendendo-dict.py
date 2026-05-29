lista_alunos = [] #--> aqui se cria uma lista

for i in range(2): # --> repete-se 2 vezes
    print(f'Cadastro de Alunos {i+1}\n')

    nome_dig = input('\n\nDigite seu nome: ') #
    idade_dig = int(input('\n\nDigite sua idade: '))

    novo_aluno = {
        'nome': nome_dig,
        'idade': idade_dig
    }

    lista_alunos.append(novo_aluno)

print('\n\nAlunos Cadastrados\n')
for aluno in lista_alunos:
    print(f'\nNome: {aluno['nome']}\nIdade: {aluno['idade']}')
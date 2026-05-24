# Lista 01 — Questão 10: Análise Crítica de Código
# Aluno: Daniel
# Data: 24/05/2026

# ── Sua solução abaixo ──────────────────────────────────────────────────────

def processar_alunos(alunos=None):
    # Correção do argumento mutável padrão
    if alunos is None:
        alunos = []
        
    aprovados = []
    
    # Correção do loop (iteração direta) e da construção da lista (.append)
    for aluno in alunos:
        if aluno['nota'] >= 7.0:
            aprovados.append(aluno['nome'])
            
    print(aprovados)
    return aprovados  # Boa prática: retornar o resultado além de apenas printar

# Exemplo para teste do código corrigido:
turma = [
    {'nome': 'Daniel', 'nota': 9.5},
    {'nome': 'Lucas', 'nota': 6.0},
    {'nome': 'Maria', 'nota': 8.0}
]
processar_alunos(turma)  # Saída esperada: ['Daniel', 'Maria']

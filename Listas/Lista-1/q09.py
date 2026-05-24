# Lista 01 — Questão 09: EAFP vs LBYL
# Aluno: Daniel
# Data: 24/05/2026

# ── Sua solução abaixo ──────────────────────────────────────────────────────

def dividir(a, b):
    try:
        # Tenta executar a operação diretamente
        return a / b
    except ZeroDivisionError:
        # Trata a exceção caso b seja igual a 0
        return None

# Testes para validação do comportamento:
print(dividir(10, 2))  # Saída: 5.0
print(dividir(10, 0))  # Saída: None

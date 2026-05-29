# Lista 02 — Questão 05: Funções de Alta Ordem
# Aluno: Daniel
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q05.py: escreva aplicar(lista, funcao) que retorna uma nova lista com a
# função aplicada a cada elemento. Demonstre com:
#   (a) função que eleva ao quadrado
#   (b) função que retorna True se o número for par
# 
# Em q05_resposta.txt: explique o que significa dizer que funções são
# 'cidadãs de primeira classe' em Python.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

def aplicar(lista, funcao):
    nova_lista = []
    for item in lista:
        nova_lista.append(funcao(item))
    return nova_lista

# (a) Elevando ao quadrado
numeros = [1, 2, 3, 4]
quadrados = aplicar(numeros, lambda x: x ** 2)
print(f"Quadrados: {quadrados}")

# (b) Verificando se é par
pares = aplicar(numeros, lambda x: x % 2 == 0)
print(f"É par: {pares}")
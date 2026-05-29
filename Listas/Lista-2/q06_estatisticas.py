# Lista 02 — Questão 06: Módulo de Estatísticas (módulo estatísticas)
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# q06_estatisticas.py: crie o módulo com as funções:
#   media(dados), mediana(dados), moda(dados), desvio_padrao(dados)
# Todas devem: receber lista de floats, validar que não está vazia
# (lançar ValueError se estiver), retornar resultado arredondado (2 casas).
# Use apenas stdlib (math permitido, não use statistics).
# 
# q06_main.py: importe o módulo e aplique as 4 funções sobre 10 notas
# digitadas pelo usuário.

# ── Sua solução abaixo ──────────────────────────────────────────────────────  

import math

def validar(dados):
    if not dados:
        raise ValueError("A lista não pode estar vazia.")

def media(dados):
    validar(dados)
    return round(sum(dados) / len(dados), 2)

def mediana(dados):
    validar(dados)
    ordenados = sorted(dados)
    n = len(ordenados)
    meio = n // 2
    if n % 2 == 0:
        res = (ordenados[meio - 1] + ordenados[meio]) / 2
    else:
        res = ordenados[meio]
    return round(res, 2)

def moda(dados):
    validar(dados)
    contagem = {x: dados.count(x) for x in set(dados)}
    max_freq = max(contagem.values())
    modas = [k for k, v in contagem.items() if v == max_freq]
    return modas[0] if len(modas) == 1 else modas

def desvio_padrao(dados):
    validar(dados)
    m = media(dados)
    variancia = sum((x - m) ** 2 for x in dados) / len(dados)
    return round(math.sqrt(variancia), 2)
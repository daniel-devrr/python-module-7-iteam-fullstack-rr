# Lista 02 — Questão 03: Sistema de Inventário
# Aluno: Daniel 
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente com lista de dicionários:
#   1. adicionar_produto(inventario, nome, codigo, quantidade, preco)
#   2. buscar_por_codigo(inventario, codigo)  → produto ou None
#   3. listar_abaixo_do_minimo(inventario, minimo)
#   4. valor_total(inventario)  → soma de quantidade × preço
# Use funções para cada operação. Demonstre as 4 no código principal.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

def adicionar_produto(inventario, nome, codigo, quantidade, preco):
    produto = {
        "nome": nome,
        "codigo": codigo,
        "quantidade": quantidade,
        "preco": preco
    }
    inventario.append(produto)


def buscar_por_codigo(inventario, codigo):
    for produto in inventario:
        if produto["codigo"] == codigo:
            return produto
    return None


def listar_abaixo_do_minimo(inventario, minimo):
    produtos = []

    for produto in inventario:
        if produto["quantidade"] < minimo:
            produtos.append(produto)

    return produtos


def valor_total(inventario):
    total = 0

    for produto in inventario:
        total += produto["quantidade"] * produto["preco"]

    return total


# ── Código principal ────────────────────────────────────────────────────────

inventario = []

adicionar_produto(inventario, "Teclado", "P001", 10, 120.0)
adicionar_produto(inventario, "Mouse", "P002", 3, 50.0)
adicionar_produto(inventario, "Monitor", "P003", 2, 900.0)

print("Inventário:")
print(inventario)

print("\nBusca por código:")
print(buscar_por_codigo(inventario, "P002"))

print("\nProdutos abaixo do mínimo:")
print(listar_abaixo_do_minimo(inventario, 5))

print("\nValor total do inventário:")
print(valor_total(inventario))
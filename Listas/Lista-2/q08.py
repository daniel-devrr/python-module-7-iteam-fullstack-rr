# Lista 02 — Questão 08: Herança e Polimorfismo
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente:
#   - Funcionario(nome, salario): calcular_bonus() → 10% do salário
#   - Gerente(departamento): bônus = 20%
#   - Estagiario(curso): bônus = 5%
# Crie lista com objetos dos 3 tipos, itere exibindo nome e bônus.
# Explique em comentário: por que o Python chama a versão correta de
# calcular_bonus() sem você verificar o tipo do objeto?

# ── Sua solução abaixo ──────────────────────────────────────────────────────

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20

class Estagiario(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.05

# Lista com os objetos
equipe = [
    Funcionario("Ana", 3000),
    Gerente("Carlos", 5000),
    Estagiario("Beatriz", 1500)
]

for obj in equipe:
    print(f"Nome: {obj.nome} | Bônus: R$ {obj.calcular_bonus():.2f}")

# Explicação:
# Isso acontece por causa do Polimorfismo. O Python não precisa saber 
# qual é a classe exata do objeto; ele simplesmente confia que, se o 
# método 'calcular_bonus()' existe em todos, ele pode chamar. Como cada 
# classe tem sua própria versão do método (sobrescrita), o Python usa a 
# que pertence ao objeto que está sendo processado na vez.
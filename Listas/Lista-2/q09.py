class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.__estoque = estoque

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("O preço precisa ser maior que zero.")
        self._preco = valor

    @property
    def estoque(self):
        return self.__estoque

    def repor(self, qtd):
        self.__estoque += qtd

    def vender(self, qtd):
        if qtd > self.__estoque:
            raise ValueError("Estoque insuficiente!")
        self.__estoque -= qtd

    def __str__(self):
        return f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.__estoque}"

    def __repr__(self):
        return f"Produto(nome='{self.nome}', preco={self.preco}, estoque={self.__estoque})"

# Demonstração
p = Produto("Notebook", 3000, 10)
p.repor(5)
p.vender(3)
print(p)
try:
    p.vender(50)
except ValueError as e:
    print(f"Erro: {e}")
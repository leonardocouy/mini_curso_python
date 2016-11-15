class Item:

    def __init__(self, nome, preco, quantidade=50):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def baixa(self, quantidade):
        self.quantidade -= quantidade

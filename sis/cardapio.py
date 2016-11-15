class Cardapio:

    def __init__(self, lista_items):
        self.lista_items = lista_items
        print(list(lista_items))

    def incluir_item(self, item):
        self.lista_items.append(item)

    def remover_item(self, nome_item):
        self.lista_items.remove(nome_item)

    def apresentar_cardapio(self):
        print("O nosso cardápio é: ")
        for nome, preco in self.lista_items:
            print("{} - {}".format(nome, preco))

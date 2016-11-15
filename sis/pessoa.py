class Pessoa:

    def __init__(self, nome, idade, dinheiro):
        self.nome = nome
        self.idade = idade
        self.dinheiro = dinheiro

    def gastar(self, item, quantidade=1):
        if self.dinheiro < item.preco:
            print('Vaza daqui caloteiro')
        else:
            self.dinheiro -= item.preco * quantidade
            print('''
            Você comprou {} e gastou R${:.2f}
            Ainda resta no bolso R${:.2f}
            '''.format(item.nome, item.preco * quantidade, self.dinheiro))


class Cachaceiro(Pessoa):
    e_cachaceiro = True

    def __init__(self, nome, idade, dinheiro):
        super(Cachaceiro, self).__init__(nome, idade, dinheiro)
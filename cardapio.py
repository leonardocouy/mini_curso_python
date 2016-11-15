import requests
from bs4 import BeautifulSoup as bs


CARDAPIO_URL = 'http://cardapioagil.com.br/jaboticabal/' \
               'restaurantes/senhor-boteco.php'

class Cardapio:

    cardapio = {}

    def __init__(self):
        self._extrair_cardapio()
        self.mostrar_cardapio()

    def _extrair_cardapio(self):
        r = requests.get(CARDAPIO_URL)
        html = bs(r.content)
        cardapio_html = html.select('div.div-apresentacao-cardapio')[0]
        paineis_html = cardapio_html.find_all('div', {'class': 'panel panel-default'})
        for painel in paineis_html:
            nome_categoria = painel.find('h3', {'class': 'panel-title'}).text
            itens = [item.text.strip() for item in painel.find_all('span', {'class':
                                                                            'list-group-item'})]
            self.cardapio[nome_categoria] = itens

    def mostrar_cardapio(self):
        for categoria in self.cardapio:
            print("\n====={}=====\n".format(categoria))
            for item in self.cardapio[categoria]:
                print(item)

cardapio = Cardapio()
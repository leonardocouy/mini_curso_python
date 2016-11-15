import requests
from bs4 import BeautifulSoup as bs
from bs4 import NavigableString

# CARDAPIO_URL = 'http://www.botecopinguimpoa.com.br/cardapio.php'
CARDAPIO_URL = 'http://cardapioagil.com.br/jaboticabal/restaurantes/senhor-boteco.php'

class Cardapio:
    categorias = {}

    def __init__(self, lista_items):
        self._download_cardapio()
        self.lista_items = lista_items
        print(list(lista_items))

    def incluir_item(self, item):
        self.lista_items.append(item)

    def remover_item(self, nome_item):
        self.lista_items.remove(nome_item)

    def apresentar_cardapio(self):
        print("Cardápio")
        for categoria in self.categorias:
            print('\n====== {} ====== \n'.format(categoria))
            for item in self.categorias[categoria]:
                print(item)

    def _download_cardapio(self):
        r = requests.get(CARDAPIO_URL) # Faço a requisição HTTP
        html = bs(r.content, 'html.parser')  # Leio o HTML e passo para o BeautifulSoup manipular
        conteudo_html = html.select('div.div-apresentacao-cardapio')[0] # Seleciono a div que possui o conteudo do cardapio
        paineis_html = conteudo_html.find_all('div', {'class': 'panel'}) # Pego cada painel de cada actegoria
        for painel in paineis_html:  # Iteracao
            nome_categoria = painel.find('h3', {'class':'panel-title'}).text # Pesquiso pelo titulo da categoria
            items = [item.text.strip() for item in painel.find_all('span', {'class': 'list-group-item'})] # Pego os itens desse painel
            self.categorias[nome_categoria] = items


cardapio = Cardapio(['test'])
cardapio.apresentar_cardapio()

# def _download_cardapio(self):
#     r = requests.get(CARDAPIO_URL)  # Faço a requisição HTTP
#     html = bs(r.content, 'html.parser')  # Leio o HTML e passo para o BeautifulSoup manipular
#     secoes = html.find_all('h3')  # Procuro por todas as Tags H3 (Representa as seções)
#     for secao in secoes:  # Iterar sobre cada secao
#         categoria = secao.text.strip()  # Pego o nome da secao e limpo ela
#         self.categorias[categoria] = []  # Crio uma nova categoria no cardapio
#
#         for no_irmao in secao.next_siblings:  # Itero pelas tags IRMÃS do H3
#             if no_irmao.name == 'h3':  # Se a irmã for H3 (outra seção) quebre o LOOP!
#                 break
#             elif no_irmao.name == 'h4':  # Se for H4 pule pois é
#                 pass
#             elif isinstance(no_irmao, NavigableString):
#                 if no_irmao != '':
#                     print(self.categorias[categoria])
#                     self.categorias[categoria][-1]['detalhes'] = no_irmao
#             else:
#                 for nome_item in no_irmao.stripped_strings:  # Se existir um nó irmão com nome, LIMPE (Stripped Strings)
#                     self.categorias[categoria].append(nome_item)  # Adiciona a lista e categoria.
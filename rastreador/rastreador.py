from bs4 import BeautifulSoup as bs
import requests

RASTREIO_NAO_ENCONTRADO = """
O nosso sistema não possui dados sobre o objeto informado. Se o objeto foi postado recentemente,
é natural que seus rastros não tenham ingressado no sistema, nesse caso, por favor, tente novamente mais tarde.
Adicionalmente, verifique se o código digitado está correto: {}
"""


class Rastreador:
    _url = 'http://websro.correios.com.br/sro_bin/txect01$.QueryList?P_LINGUA=001&P_TIPO=001&P_COD_UNI={}'
    status = []

    def __init__(self, codigo, descricao):
        self.codigo = codigo
        self.descricao = descricao
        self._url = self._url.format(codigo)

    def rastrear(self):
        self._extrair_status()
        for status in self.status:
            if len(status) == 4:
                print('{} - {} - {} - {}'.format(status[0], status[1], status[2], status[3]))
            else:
                print('{} - {} - {}'.format(status[0], status[1], status[2]))

    def _extrair_status(self):
        r = requests.get(self._url).content
        html = bs(r, "html.parser")
        extrair_tabela = html.find('table')
        if extrair_tabela is not None:
            extrair_linhas = extrair_tabela.find_all('tr')
            for linha_html in extrair_linhas[1:]:
                status = []
                dados = linha_html.contents
                if len(dados) == 3:
                    data = dados[0].text
                    local = dados[1].text
                    situacao = dados[2].text
                    status.extend([data, local, situacao])
                    self.status.append(status)
                elif len(dados) == 1:
                    descricao = dados[0].text
                    self.status[-1].append(descricao)
        else:
            print(RASTREIO_NAO_ENCONTRADO.format(self.codigo))


rastreia = Rastreador('RQ033493412MY', 'Teclado')
rastreia.rastrear()

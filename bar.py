# Esse script se destina ao Bar Virtual - Mini Curso Python Una Bom Despacho - Leonardo Flores

# TO-DO LIST

"""
    Bar Script

    TO-DO LIST

    - LOGIN
    - LISTA DE PESSOAS DENTRO DO BAR
    - CHECAR QUEM É VIP E PISTA
    - CRIAR LISTA DE CARDAPIO FIXO
    - SORTEAR RODADA DE CERVEJA
    - MAIS..

    FUNCTIONS
"""


lista_de_pessoas = ['Wendel', 'Jean', 'Marco', 'Bruna', 'PH']
lista_negra = ['Dionatha']
cardapio = {
    'corotinho': ['Corotinho', 2.00],
    'vodka_absolut': ['Vodka Absolut Açai', 100.00]
}

print("Você escolheu o {} e ele custa R${:.2f}".format(cardapio['corotinho'][0], cardapio['corotinho'][1]))


limite_cerveja = 5

while(limite_cerveja >= 1):
    limite_cerveja -= 1
    print("Você tem {} vezes para tomar cerveja e dar fora daqui"
          .format(limite_cerveja))


logado = True

while(logado):
    print("beba cerveja e vaza")
    logado = False

for nome in lista_de_pessoas:
    print(nome + " Cachaceiro")

for nome in lista_negra:
    print(nome)

username = input("Digite seu nome: ")

if not username in lista_negra:
    print("Seja bem vindo")
else:
    print("Vaza daqui cachaceiro, vou chamar o segurança")



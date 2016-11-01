import db
import random
# Esse script se destina ao Bar Virtual - Mini Curso Python Una Bom Despacho - Leonardo Flores

# TO-DO LIST

"""
    Bar Script

    TO-DO LIST

    - LOGIN
    - LISTA DE PESSOAS DENTRO DO BAR
    - CHECAR QUEM É VIP E PISTA
    - CRIAR LISTA DE CARDAPIO
    - SORTEAR RODADA DE CERVEJA
    - MAIS..

    FUNCTIONS
"""

# db.criar_tabela()
# db.inserir_cliente('Gyonathan', '40', True)
# db.inserir_cliente('Uhendeu', '19', False)
# db.inserir_cliente('PH Amigo do Gyonathan', '36', False)

clientes = db.obter_clientes()
lista_clientes = []

for cliente in clientes:
    lista_clientes.append(cliente[1])

def sortear_rodada():
    random.shuffle(lista_clientes)
    print(lista_clientes)
    cliente_escolhido = random.choice(lista_clientes)
    print('O GANHADOR DA RODADA DE CERVEJA FOI: {}'
          .format(cliente_escolhido))

sortear_rodada()
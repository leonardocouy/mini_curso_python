import sqlite3

conn = sqlite3.connect('bar.db')
c = conn.cursor()


def criar_tabela():
    query = '''
    CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL , nome text, idade text, cachaceiro bool)
    '''
    c.execute(query)

def inserir_cliente(nome, idade, cachaceiro=False):
    query = '''
    INSERT INTO clientes (nome, idade, cachaceiro) VALUES (?, ?, ?)
    '''
    c.execute(query, (nome, idade, cachaceiro) )
    conn.commit()

def obter_clientes():
    query = '''
    SELECT * FROM clientes
    '''
    c.execute(query)
    return c.fetchall()
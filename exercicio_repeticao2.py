lista_de_pessoas = ['Bruna', 'Neymar', 'Irmã do Neymar', 'Mãe do Neymar']

for nome in lista_de_pessoas:
    print(nome)


idade_pessoas = {
    'Dionatha': 40,
    'PH': 20,
    'Wendel': 19,
    'Bruna': 39
}

for chave, valor in idade_pessoas.items():
    print('{} - Idade: {}'.format(chave, valor))



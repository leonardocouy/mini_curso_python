def primeira_funcao():
    print('Essa é a primeira funcao')


def funcao_parametros(param1, param2):
    print('Primeiro parametro: {}, Segundo parametro: {}'.format(param1, param2))


def funcao_param_padrao(param1, param2=99):
    funcao_parametros(param1, param2)


def funcao_param_tupla(nome, *caracteristicas):
    print('Oi meu nome é: {} e minhas características são:'.format(nome))
    for caracteristica in caracteristicas:
        print('\t - {}'.format(caracteristica))


def funcao_param_dict(nome_bar, **catalogo):
    print('Seja bem vindo ao {}, nosso catalogo é: '.format(nome_bar))
    for chave, valor in catalogo.items():
        print('{} - {}'.format(chave, valor))


def funcao(nome, **kwargs):
    print('{} - {}'.format(nome, kwargs))

primeira_funcao()
funcao_parametros('leo', 21)
funcao_param_padrao('Executando funcao dentro de outra')
funcao_param_tupla('Leo', 'gente boa', 'legal', 'chato',)
funcao_param_dict('black jack', bebidas=('vodka belvedere', 'blue label',), comidas=('batata frita', 'bife',))
funcao('teste', b=4, c=5, idade=15)

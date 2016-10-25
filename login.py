lista_negra = ['leo', 'dionatha']

lista_users = {
    'rafa': 'windows123',
    'witaly': 'telazul'
}


logado = False

while logado == False:  # or not logado
    username = input("Digite seu login: ")
    password = input("Digite sua senha: ")

    if lista_users.get(username) == password:
        print('Você logou!')
        logado = True
    else:
        print('Usuário e senha inválidos')

nome = input("Qual seu nome?")
if nome in lista_negra:
    print("vaza daqui")
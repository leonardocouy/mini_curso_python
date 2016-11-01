i = 0

while(i < 10):
    print('{} é menor que 10'.format(i))
    i += 1

num_chances = 4
while(num_chances != 0):
    gente_boa = input('O Leo é gente boa? (s/n)')
    gente_boa = gente_boa.toUpperca
    if gente_boa == 's':
        print('Você fez a escolha certa')
        break
    elif gente_boa == 'n':
        print('Vou te dar mais uma chance sujeito')
        num_chances -= 1
    else:
        print('Você digitou uma opção inválida')





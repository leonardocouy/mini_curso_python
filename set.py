usuarios_cadastrados = ['leo', 'dionatha', 'bruna', 'leo']
usuarios_validados = set(usuarios_cadastrados)
usuarios_validados.add('leo')
print(usuarios_validados)


# Operacoes com Sets

a = set('CAVALO')
b = set('PONEI')

print (a)
print (b)

print("Letra em A mas não em B")
print(a-b)

print("Letra em A ou em B")
print(a | b)

print("Letra em A mas não em B")
print(a & b)

print("Letra em A ou B mas não em ambos")
print(a ^ b)
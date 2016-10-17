faculdade = "Una Bom Despacho"
num_letras = len(faculdade)

print(num_letras)
print(faculdade)

# Manipulação de Strings
print("Faculdade invertida")
print(faculdade[::-1])

print("Adjetivo da faculdade")
print(faculdade[4:7])

# Concatenação de Strings
dionatha = "coca-cola" + "jack daniels" + "jack cola"

print(dionatha)

print(dionatha * 10)

# Composição de Strings

dionatha = "cansei dessa vida"
num_vodka = 10
dinheiro = 10.57

print("Dionatha disse: %s, ainda tenho %i vodkas e tenho R$%.2f"
      % (dionatha, num_vodka, dinheiro))

print("Dionatha disse: {}, ainda tenho {} vodkas e tenho R${:0.2f}"
.format(dionatha, num_vodka, dinheiro))


# SPLIT (DIVIDIR)

nomes = 'ana, wendel, jean, dionatha'
print(nomes.split(', '))

# STRIP  (EXPLODIR)
texto = '????????? DILMA VOLTA AO SENADO ??????'
print(texto.strip("?"))

# STRIP ESPAÇO EM BRANCO
texto = '           EU VI O DIONATHA NO BAR      \n\n\n'
print(texto.strip())

# REPLACE (SUBSTITUICAO)
dionatha = "Dionatha gosta de vodka"
print(dionatha.replace('gosta', 'não gosta'))
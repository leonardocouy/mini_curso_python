precos_bebidas = {
    "vodka": 90.00,
    "51": 30.00,
    "corotinho": 2.00
}

print("vodka" in precos_bebidas)
print("rum" in precos_bebidas)


for chave, valor in precos_bebidas.items():
    print("{} - R${:.2f}".format(chave, valor))
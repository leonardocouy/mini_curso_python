nome = input("Digite seu nome:")
idade = int(input("Digite sua idade: "))
dinheiro = float(input("Digite quant dinheiro: R$"))

print("%s, você tem %i anos e R$%.2f" % (nome, idade, dinheiro))



try:
    num = int(input("Digite um numero:"))
    print(num)
except ValueError:
    print("Ops, verifique se digitou um numero valido")

try:
    num = int(input("Digite um numero:"))
    print(num)
except ValueError:
    raise ValueError("Ops, verifique se digitou um numero valido")

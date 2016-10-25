pontos = 0
questao = 1

# Simple is Better Than Complex

while questao <= 3:
    resposta = input("Resposta da questão %d: " % questao)
    if questao == 1 and resposta == "b":
        pontos += 1
    elif questao == 2 and resposta == "a":
        pontos += 1
    elif questao == 3 and resposta == "d":
        pontos += 1
    questao += 1

print("O Aluno fez %d ponto(s)" % pontos)

pontos = 0
questao = 1

while questao <= 3:
    resposta = input("Resposta da questão %d: " % questao)
    if (questao == 1 and resposta == "b") or (questao == 2 and resposta == "a") or (questao == 3 and resposta == "d"):
        pontos += 1
    questao += 1

print("O Aluno fez %d ponto(s)" % pontos)
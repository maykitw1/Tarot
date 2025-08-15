import random
# implementar um chatbot que absorvesse o significado das caras para o user
cartas_tarot = [
    {"nome": "O Louco", "normal": "Novos começos, liberdade", "invertido": "Imprudência, falta de direção"},
    {"nome": "O Mago", "normal": "Habilidade, ação, iniciativa", "invertido": "Manipulação, ilusão"},
    {"nome": "A Sacerdotisa", "normal": "Intuição, mistério", "invertido": "Segredos, bloqueio intuitivo"},
    {"nome": "A Imperatriz", "normal": "Fertilidade, amor, criatividade", "invertido": "Bloqueios criativos, insegurança"},
    {"nome": "A Justiça", "normal": "Equilíbrio, verdade, karma", "invertido": "Injustiça, desequilíbrio"},
    {"nome": "A Morte", "normal": "Transformação, renascimento", "invertido": "Resistência à mudança"},
    {"nome": "A Estrela", "normal": "Esperança, inspiração", "invertido": "Desânimo, desesperança"},
    {"nome": "A Lua", "normal": "Sonhos, intuição, mistério", "invertido": "Ilusão, confusão"},
    {"nome": "O Sol", "normal": "Alegria, sucesso, clareza", "invertido": "Excesso de confiança, negatividade"},
    {"nome": "O Julgamento", "normal": "Renascimento, chamada interior", "invertido": "Autocrítica, medo de julgamento"},
]
def sortear_tarot(qtd_cartas=1):
    sorteio = random.sample(cartas_tarot, qtd_cartas)
    print("Cartas sorteadas:")
    for carta in sorteio:
        posicao = random.choice(["normal", "invertido"])
        significado = carta[posicao]
        print(f"\n {carta['nome']} ({posicao.upper()})\n {significado}")
print("Bem-vindo ao sorteio de cartas de tarot!")
motivo = input("Qual o motivo do seu sorteio de tarot?: ")
print("Entendo...")
escolha = int(input("Quantas cartas deseja sortear? (1-3): "))
sortear_tarot(escolha)
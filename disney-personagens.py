# Lista de personagens mais conhecidos
personagens_populares = [
    "Mickey Mouse", "Donald Duck", "Goofy", "Minnie Mouse", "Pluto",
    "Simba", "Ariel", "Elsa", "Anna", "Buzz Lightyear", "Woody",
    "Aladdin", "Genie", "Belle", "Beast", "Cinderella", "Snow White",
    "Tinker Bell", "Moana", "Rapunzel", "Olaf", "Stitch", "Mulan",
    "Hercules", "Tarzan", "Pocahontas", "Peter Pan", "Nemo"
]

# Função para escolher personagem baseado em dificuldade
def personagem_aleatorio(dificuldade=0):
    personagem = None
    tentativas = 0

    while not personagem or not personagem.get("imageUrl"):
        tentativas += 1
        pagina = random.randint(1, 100)
        personagens = buscar_personagens(pagina)
        if not personagens:
            continue
        candidato = random.choice(personagens)
        nome = candidato.get("name", "")

        # Fase fácil: garantir personagens populares
        if dificuldade <= 5:
            if nome in personagens_populares:
                personagem = candidato
        # Fase média: 50% de chance de vir personagem popular
        elif dificuldade <= 10:
            if nome in personagens_populares or random.random() < 0.5:
                personagem = candidato
        # Fase difícil: qualquer personagem
        else:
            personagem = candidato

        # Evita loop infinito
        if tentativas > 10 and personagem:
            break

    return personagem

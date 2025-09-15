import streamlit as st
import requests
import random

st.set_page_config(page_title="Adivinhe o Personagem da Disney", page_icon="🎬")

st.title("🎬 Adivinhe o Personagem da Disney!")
st.write("Veja a imagem e tente adivinhar o nome do personagem. Vamos testar seu conhecimento do mundo Disney!")

# Lista de personagens mais conhecidos
personagens_populares = [
    "Mickey Mouse", "Donald Duck", "Goofy", "Minnie Mouse", "Pluto",
    "Simba", "Ariel", "Elsa", "Anna", "Buzz Lightyear", "Woody",
    "Aladdin", "Genie", "Belle", "Beast", "Cinderella", "Snow White",
    "Tinker Bell", "Moana", "Rapunzel", "Olaf", "Stitch", "Mulan",
    "Hercules", "Tarzan", "Pocahontas", "Peter Pan", "Nemo"
]

# Função para buscar personagens da API
def buscar_personagens(pagina=1):
    url = f"https://api.disneyapi.dev/character?page={pagina}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json().get("data", [])
    return []

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

# Função para gerar opções com 1 certa e 3 erradas, com personagens mais semelhantes
def gerar_opcoes(nome_correto, todos_personagens, personagem_atual):
    opcoes = [nome_correto]
    nomes_usados = set(opcoes)

    # Buscar personagens semelhantes (usando nome ou algo relacionado)
    for p in todos_personagens:
        nome = p.get("name", "")
        if nome and nome != personagem_atual["name"] and nome not in nomes_usados:
            # Verificar semelhança nos nomes
            if personagem_atual["name"].lower() in nome.lower():
                opcoes.append(nome)
                nomes_usados.add(nome)

    # Caso não tenha opções semelhantes, adicionar aleatórias
    while len(opcoes) < 4:
        p = random.choice(todos_personagens)
        nome = p.get("name", "")
        if nome and nome not in nomes_usados:
            opcoes.append(nome)
            nomes_usados.add(nome)

    random.shuffle(opcoes)
    return opcoes

# Inicializa a pontuação
if "acertos" not in st.session_state:
    st.session_state.acertos = 0
if "erros" not in st.session_state:
    st.session_state.erros = 0
if "personagem_atual" not in st.session_state:
    st.session_state.personagem_atual = personagem_aleatorio(st.session_state.acertos)
if "opcoes" not in st.session_state:
    todos = buscar_personagens()
    st.session_state.opcoes = gerar_opcoes(st.session_state.personagem_atual["name"], todos, st.session_state.personagem_atual)
if "respondido" not in st.session_state:
    st.session_state.respondido = False

# Mostrar imagem do personagem
st.image(st.session_state.personagem_atual["imageUrl"], use_container_width=True)
escolha = st.radio("Quem é esse personagem?", st.session_state.opcoes)

# Botão para responder
if not st.session_state.respondido:
    if st.button("Responder"):
        if escolha == st.session_state.personagem_atual["name"]:
            st.success("✅ Acertou!")
            st.session_state.acertos += 1
        else:
            st.error(f"❌ Errou! Era: {st.session_state.personagem_atual['name']}")
            st.session_state.erros += 1
        st.session_state.respondido = True

# Mostrar pontuação
st.markdown(f"### Pontuação: ✅ {st.session_state.acertos} | ❌ {st.session_state.erros}")

# Próxima pergunta
if st.session_state.respondido:
    if st.button("Próximo personagem 🎲"):
        st.session_state.personagem_atual = personagem_aleatorio(st.session_state.acertos)
        todos = buscar_personagens()
        st.session_state.opcoes = gerar_opcoes(st.session_state.personagem_atual["name"], todos, st.session_state.personagem_atual)
        st.session_state.respondido = False

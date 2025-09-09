import streamlit as st
import requests
import random

st.set_page_config(page_title="Adivinhe o Personagem da Disney", page_icon="🎬")

st.title("🎬 Adivinhe o Personagem da Disney!")
st.write("Veja a imagem e tente adivinhar o nome do personagem. Vamos testar seu conhecimento do mundo Disney!")

# Função para buscar personagens da API
def buscar_personagens(pagina=1):
    url = f"https://api.disneyapi.dev/character?page={pagina}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json().get("data", [])
    return []

# Função para escolher personagem aleatório com imagem
def personagem_aleatorio():
    personagem = None
    while not personagem or not personagem.get("imageUrl"):
        pagina = random.randint(1, 100)  # Número de páginas da API
        personagens = buscar_personagens(pagina)
        if personagens:
            personagem = random.choice(personagens)
    return personagem

# Função para gerar opções com 1 certa e 3 erradas
def gerar_opcoes(nome_correto, todos_personagens):
    opcoes = [nome_correto]
    nomes_usados = set(opcoes)
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
    st.session_state.personagem_atual = personagem_aleatorio()
if "opcoes" not in st.session_state:
    todos = buscar_personagens()
    st.session_state.opcoes = gerar_opcoes(st.session_state.personagem_atual["name"], todos)
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
        st.session_state.personagem_atual = personagem_aleatorio()
        todos = buscar_personagens()
        st.session_state.opcoes = gerar_opcoes(st.session_state.personagem_atual["name"], todos)
        st.session_state.respondido = False

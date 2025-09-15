import streamlit as st
import requests
import random

st.set_page_config(page_title="Quiz Disney - API", page_icon="🎯")
st.title("🎯 Quiz Disney com API: Quem é este personagem?")
st.write("Veja a imagem e escolha o nome correto do personagem.")

API_URL = "https://api.disneyapi.dev/character"

@st.cache_data(show_spinner=False)
def carregar_personagens(pagina=1, limite=50):
    """Carrega lista grande para sortear opções"""
    response = requests.get(f"{API_URL}?page={pagina}&limit={limite}")
    if response.status_code == 200:
        return response.json()["data"]
    else:
        st.error("Erro ao acessar a API da Disney.")
        return []

# Carregar uma lista maior para montar as opções
todos_personagens = carregar_personagens(pagina=1, limite=100)

# Selecionar 10 personagens aleatórios para perguntas
quiz_personagens = random.sample(todos_personagens, 10)

if "respostas" not in st.session_state:
    st.session_state.respostas = []
if "verificado" not in st.session_state:
    st.session_state.verificado = False

for i, personagem in enumerate(quiz_personagens):
    if len(st.session_state.respostas) <= i:
        st.image(personagem["imageUrl"], width=400)
        st.markdown(f"### Quem é este personagem?")

        # Nome correto
        correto = personagem["name"]

        # Sortear 3 nomes errados (sem repetir o correto)
        outros = [p["name"] for p in todos_personagens if p["name"] != correto]
        opcoes_erradas = random.sample(outros, 3)

        opcoes = opcoes_erradas + [correto]
        random.shuffle(opcoes)

        escolha = st.radio("Escolha uma opção:", opcoes, key=f"q{i}")

        if st.button(f"Confirmar resposta {i+1}"):
            st.session_state.respostas.append(escolha)
        st.stop()

# Verificar respostas
if len(st.session_state.respostas) == len(quiz_personagens) and not st.session_state.verificado:
    acertos = 0
    for idx, personagem in enumerate(quiz_personagens):
        if st.session_state.respostas[idx] == personagem["name"]:
            acertos += 1
    erros = len(quiz_personagens) - acertos
    st.session_state.acertos = acertos
    st.session_state.erros = erros
    st.session_state.verificado = True

if st.session_state.verificado:
    st.markdown("## ✅ Resultado Final:")
    st.success(f"Você acertou {st.session_state.acertos} de {len(quiz_personagens)} perguntas!")
    st.error(f"Você errou {st.session_state.erros} perguntas.")
    st.markdown(f"### 🎯 Pontuação final: **{st.session_state.acertos * 10} pontos**")

    if st.button("Responder novamente 🔁"):
        st.session_state.respostas = []
        st.session_state.verificado = False
        st.experimental_rerun()

import streamlit as st
import requests
import random

st.set_page_config(page_title="Quiz Disney - Personagens", page_icon="🎯")

st.title("🎯 Quiz Disney: Quem é esse personagem?")
st.write("Responda às perguntas e veja sua pontuação no final!")

API_URL = "https://api.disneyapi.dev/character"

def carregar_todos_personagens(max_personagens=100):
    personagens = []
    pagina = 1
    while len(personagens) < max_personagens:
        try:
            response = requests.get(f"{API_URL}?page={pagina}")
            response.raise_for_status()
            data = response.json()
            pagina_personagens = data.get("data", [])
            if not pagina_personagens:
                break  # Sem mais personagens
            personagens.extend(pagina_personagens)
            if not data.get("nextPage"):
                break  # Não tem próxima página
            pagina += 1
        except Exception as e:
            st.error(f"Erro ao acessar a API da Disney: {e}")
            break
    return personagens[:max_personagens]


todos_personagens = carregar_todos_personagens(max_personagens=100)

if len(todos_personagens) < 10:
    st.error("Não foi possível carregar personagens suficientes para o quiz.")
    st.stop()

quiz_personagens = random.sample(todos_personagens, 10)

todos_nomes = [p['name'] for p in todos_personagens]

perguntas = []

for personagem in quiz_personagens:
    correta = personagem['name']
    opcoes_erradas = random.sample([n for n in todos_nomes if n != correta], 3)
    opcoes = opcoes_erradas + [correta]
    random.shuffle(opcoes)

    perguntas.append({
        "pergunta": "Qual o nome deste personagem?",
        "imagem": personagem.get("imageUrl", ""),
        "correta": correta,
        "opcoes": opcoes
    })

if "respostas" not in st.session_state:
    st.session_state.respostas = []
if "verificado" not in st.session_state:
    st.session_state.verificado = False

for i, p in enumerate(perguntas):
    if len(st.session_state.respostas) <= i:
        if p["imagem"]:
            st.image(p["imagem"], width=300)
        escolha = st.radio(p["pergunta"], p["opcoes"], key=f"q{i}")
        if st.button(f"Confirmar resposta {i+1}"):
            st.session_state.respostas.append(escolha)
        st.stop()

if len(st.session_state.respostas) == len(perguntas) and not st.session_state.verificado:
    acertos = 0
    for idx, p in enumerate(perguntas):
        if st.session_state.respostas[idx] == p["correta"]:
            acertos += 1
    st.session_state.acertos = acertos
    st.session_state.erros = len(perguntas) - acertos
    st.session_state.verificado = True

if st.session_state.verificado:
    st.markdown("## ✅ Resultado Final:")
    st.success(f"Você acertou {st.session_state.acertos} de {len(perguntas)} perguntas!")
    st.error(f"Você errou {st.session_state.erros} perguntas.")
    st.markdown(f"### 🎯 Pontuação final: **{st.session_state.acertos * 10} pontos**")

    if st.button("Jogar novamente 🔁"):
        st.session_state.respostas = []
        st.session_state.verificado = False
        st.rerun()

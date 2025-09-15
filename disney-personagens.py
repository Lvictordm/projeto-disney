import streamlit as st
import requests
import random

st.set_page_config(page_title="Quiz Disney - Personagens", page_icon="🎯")

st.title("🎯 Quiz Disney: Quem é esse personagem?")
st.write("Responda às perguntas e veja sua pontuação no final!")

API_URL = "https://api.disneyapi.dev/character"

def carregar_personagens(pagina=1, limite=100):
    try:
        response = requests.get(f"{API_URL}?page={pagina}&limit={limite}")
        response.raise_for_status()
        data = response.json()
        personagens = data.get("data", [])
        if not personagens:
            st.error("Nenhum personagem encontrado na API.")
            return []
        return personagens
    except Exception as e:
        st.error(f"Erro ao acessar a API da Disney: {e}")
        return []

# Carrega personagens
todos_personagens = carregar_personagens()

# Verifica se tem personagens suficientes
if len(todos_personagens) < 10:
    st.error("Não foi possível carregar personagens suficientes para o quiz.")
    st.stop()

# Escolhe 10 personagens aleatórios para o quiz
quiz_personagens = random.sample(todos_personagens, 10)

# Preparar perguntas no formato:
# "Qual o nome desse personagem?"
# opções = nome correto + 3 nomes errados aleatórios

perguntas = []

# Para criar opções erradas, vamos coletar nomes de personagens diferentes
todos_nomes = [p['name'] for p in todos_personagens]

for personagem in quiz_personagens:
    correta = personagem['name']

    # Escolhe 3 nomes errados que não sejam o correto
    opcoes_erradas = random.sample([n for n in todos_nomes if n != correta], 3)
    opcoes = opcoes_erradas + [correta]
    random.shuffle(opcoes)

    perguntas.append({
        "pergunta": "Qual o nome deste personagem?",
        "imagem": personagem.get("imageUrl", ""),
        "correta": correta,
        "opcoes": opcoes
    })

# Controle de estado para respostas e verificação
if "respostas" not in st.session_state:
    st.session_state.respostas = []
if "verificado" not in st.session_state:
    st.session_state.verificado = False

# Loop para perguntas
for i, p in enumerate(perguntas):
    if len(st.session_state.respostas) <= i:
        if p["imagem"]:
            st.image(p["imagem"], width=300)
        escolha = st.radio(p["pergunta"], p["opcoes"], key=f"q{i}")
        if st.button(f"Confirmar resposta {i+1}"):
            st.session_state.respostas.append(escolha)
        st.stop()

# Avaliação das respostas
if len(st.session_state.respostas) == len(perguntas) and not st.session_state.verificado:
    acertos = 0
    for idx, p in enumerate(perguntas):
        if st.session_state.respostas[idx] == p["correta"]:
            acertos += 1
    st.session_state.acertos = acertos
    st.session_state.erros = len(perguntas) - acertos
    st.session_state.verificado = True

# Mostrar resultado final
if st.session_state.verificado:
    st.markdown("## ✅ Resultado Final:")
    st.success(f"Você acertou {st.session_state.acertos} de {len(perguntas)} perguntas!")
    st.error(f"Você errou {st.session_state.erros} perguntas.")
    st.markdown(f"### 🎯 Pontuação final: **{st.session_state.acertos * 10} pontos**")

    if st.button("Jogar novamente 🔁"):
        st.session_state.respostas = []
        st.session_state.verificado = False
        st.experimental_rerun()

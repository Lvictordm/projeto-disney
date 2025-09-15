import streamlit as st
import requests
import random

st.set_page_config(page_title="Quiz Disney - Personagens Famosos", page_icon="🎯")

st.title("🎯 Quiz Disney: Quem é esse personagem?")
st.write("Responda às perguntas e veja sua pontuação no final!")

API_URL = "https://api.disneyapi.dev/character"

# Lista de personagens conhecidos
personagens_famosos = [
    "Mickey Mouse", "Donald Duck", "Goofy", "Minnie Mouse", "Pluto", 
    "Ariel", "Simba", "Aladdin", "Jasmine", "Hercules", 
    "Buzz Lightyear", "Woody", "Elsa", "Anna", "Olaf", "Moana",
    "Rapunzel", "Cinderella", "Belle", "Beast", "Maleficent"
]

def carregar_personagens_famosos():
    personagens = []
    for nome in personagens_famosos:
        try:
            response = requests.get(f"{API_URL}?name={nome}")
            response.raise_for_status()
            data = response.json()
            personagem = data.get("data", [])
            if personagem:
                personagens.extend(personagem)
        except Exception as e:
            st.error(f"Erro ao acessar a API da Disney: {e}")
    return personagens

# Carrega personagens mais conhecidos
todos_personagens = carregar_personagens_famosos()

if len(todos_personagens) < 10:
    st.error("Não foi possível carregar personagens suficientes para o quiz.")
    st.stop()

quiz_personagens = random.sample(todos_personagens, 10)

perguntas = []

for personagem in quiz_personagens:
    correta = personagem['name']
    opcoes_erradas = random.sample([p['name'] for p in todos_personagens if p['name'] != correta], 3)
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
        st.experimental_rerun()

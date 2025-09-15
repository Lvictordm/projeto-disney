import streamlit as st
from collections import Counter

st.set_page_config(page_title="Qual Filme da Disney combina com você?", page_icon="🎥")

st.title("🎥 Qual Filme da Disney combina com você?")
st.write("Responda às perguntas sobre os filmes e descubra qual universo da Disney tem mais a ver com você!")

# Perguntas baseadas em história e características dos filmes
perguntas = [
    {
        "pergunta": "Quem é o vilão no filme Aladdin?",
        "opcoes": {
            "Jafar": "Aladdin",
            "Hades": "Hércules",
            "Gaston": "A Bela e a Fera",
            "Úrsula": "A Pequena Sereia"
        }
    },
    {
        "pergunta": "O que a Fera veste no baile com a Bela?",
        "opcoes": {
            "Terno azul": "A Bela e a Fera",
            "Capa vermelha": "Aladdin",
            "Armadura": "Mulan",
            "Vestido amarelo": "A Pequena Sereia"
        }
    },
    {
        "pergunta": "O que Ariel mais deseja?",
        "opcoes": {
            "Viver no mundo humano": "A Pequena Sereia",
            "Ser princesa do mar": "Moana",
            "Encontrar um gênio": "Aladdin",
            "Aprender a lutar": "Mulan"
        }
    },
    {
        "pergunta": "Qual objeto mágico aparece em Aladdin?",
        "opcoes": {
            "Tapete voador": "Aladdin",
            "Tridente mágico": "A Pequena Sereia",
            "Espada encantada": "Mulan",
            "Coração de Te Fiti": "Moana"
        }
    },
    {
        "pergunta": "Quem é o companheiro de Moana em sua jornada?",
        "opcoes": {
            "Maui": "Moana",
            "Sebastião": "A Pequena Sereia",
            "Fera": "A Bela e a Fera",
            "Rajah": "Aladdin"
        }
    },
    {
        "pergunta": "Qual é o disfarce de Mulan durante o treinamento?",
        "opcoes": {
            "Ela se veste como soldado": "Mulan",
            "Ela vira princesa": "A Bela e a Fera",
            "Ela usa vestido mágico": "A Pequena Sereia",
            "Ela se disfarça de pirata": "Moana"
        }
    },
    {
        "pergunta": "Qual desses itens representa melhor a Moana?",
        "opcoes": {
            "Oceano e canoa": "Moana",
            "Espelho mágico": "A Bela e a Fera",
            "Tridente do mar": "A Pequena Sereia",
            "Espada e dragão": "Mulan"
        }
    }
]

# Estados
if "respostas" not in st.session_state:
    st.session_state.respostas = []
if "filme_final" not in st.session_state:
    st.session_state.filme_final = None

# Apresenta perguntas
for i, p in enumerate(perguntas):
    if len(st.session_state.respostas) <= i:
        escolha = st.radio(p["pergunta"], list(p["opcoes"].keys()), key=f"q{i}")
        if st.button(f"Confirmar resposta {i+1}"):
            st.session_state.respostas.append(p["opcoes"][escolha])
        st.stop()

# Resultado
if len(st.session_state.respostas) == len(perguntas):
    contagem = Counter(st.session_state.respostas)
    filme = contagem.most_common(1)[0][0]
    st.session_state.filme_final = filme

# Exibir resultado
if st.session_state.filme_final:
    st.success(f"🎉 O filme da Disney que mais combina com você é **{st.session_state.filme_final}**!")

    imagens = {
        "Aladdin": "https://upload.wikimedia.org/wikipedia/en/5/58/Aladdin_disney.png",
        "A Bela e a Fera": "https://upload.wikimedia.org/wikipedia/en/7/7c/Beautybeastposter.jpg",
        "A Pequena Sereia": "https://upload.wikimedia.org/wikipedia/en/7/75/Ariel_disney.png",
        "Moana": "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_disney.png",
        "Mulan": "https://upload.wikimedia.org/wikipedia/en/4/4c/Mulan_disney.png"
    }

    url = imagens.get(st.session_state.filme_final)
    if url:
        st.image(url, caption=st.session_state.filme_final, use_container_width=True)
    else:
        st.warning("Imagem do filme não disponível.")

    if st.button("Refazer o teste 🔁"):
        st.session_state.respostas = []
        st.session_state.filme_final = None
        st.experimental_rerun()

import streamlit as st
from collections import Counter

st.set_page_config(page_title="Qual Personagem da Disney é Você?", page_icon="🎭")

st.title("🎭 Qual Personagem da Disney é Você?")
st.write("Responda às perguntas e descubra qual personagem da Disney mais combina com você!")

perguntas = [
    {
        "pergunta": "Qual dessas qualidades mais te define?",
        "opcoes": {
            "Corajoso(a)": "Mulan",
            "Sonhador(a)": "Ariel",
            "Líder nato(a)": "Simba",
            "Independente": "Elsa",
            "Aventureiro(a)": "Buzz Lightyear",
        }
    },
    {
        "pergunta": "O que você prefere fazer no tempo livre?",
        "opcoes": {
            "Explorar lugares novos": "Buzz Lightyear",
            "Cantar ou dançar": "Ariel",
            "Ficar sozinho(a) e refletir": "Elsa",
            "Proteger quem você ama": "Mulan",
            "Brincar com amigos": "Simba",
        }
    },
    {
        "pergunta": "Qual cor você mais gosta?",
        "opcoes": {
            "Azul": "Elsa",
            "Vermelho": "Mulan",
            "Amarelo": "Simba",
            "Turquesa": "Ariel",
            "Prata": "Buzz Lightyear",
        }
    },
    {
        "pergunta": "Se você tivesse um poder mágico, qual seria?",
        "opcoes": {
            "Controlar o gelo": "Elsa",
            "Respirar debaixo d'água": "Ariel",
            "Transformação": "Mulan",
            "Voar pelo espaço": "Buzz Lightyear",
            "Liderar e proteger": "Simba",
        }
    }
]

if "respostas" not in st.session_state:
    st.session_state.respostas = []
if "personagem_final" not in st.session_state:
    st.session_state.personagem_final = None

for i, p in enumerate(perguntas):
    if len(st.session_state.respostas) <= i:
        escolha = st.radio(p["pergunta"], list(p["opcoes"].keys()), key=f"q{i}")
        if st.button(f"Confirmar resposta {i+1}"):
            st.session_state.respostas.append(p["opcoes"][escolha])
        st.stop()

if len(st.session_state.respostas) == len(perguntas):
    contagem = Counter(st.session_state.respostas)
    personagem = contagem.most_common(1)[0][0]
    st.session_state.personagem_final = personagem

if st.session_state.personagem_final:
    st.success(f"🎉 Você seria o personagem **{st.session_state.personagem_final}** da Disney!")

    imagens = {
        "Elsa": "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Elsa_Frozen.png/220px-Elsa_Frozen.png",
        "Simba": "https://upload.wikimedia.org/wikipedia/en/thumb/3/3d/Simba_Pride_Lands.png/220px-Simba_Pride_Lands.png",
        "Buzz Lightyear": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/BuzzLightyear2.png/220px-BuzzLightyear2.png",
        "Mulan": "https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Mulan_%28Disney_character%29.png/220px-Mulan_%28Disney_character%29.png",
        "Ariel": "https://upload.wikimedia.org/wikipedia/en/thumb/6/69/Ariel_disney.png/220px-Ariel_disney.png"
    }

    url = imagens.get(st.session_state.personagem_final)
    if url:
        st.image(url, caption=st.session_state.personagem_final, use_container_width=True)
    else:
        st.write("Imagem do personagem não disponível.")

    if st.button("Refazer o teste 🔁"):
        st.session_state.respostas = []
        st.session_state.personagem_final = None
        st.experimental_rerun()

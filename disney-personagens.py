import streamlit as st
from collections import Counter

st.set_page_config(page_title="Qual Personagem da Disney é Você?", page_icon="🎭")

st.title("🎭 Qual Personagem da Disney é Você?")
st.write("Responda às perguntas e descubra qual personagem da Disney mais combina com você!")

# Perguntas e opções
perguntas = [
    {
        "pergunta": "Qual dessas qualidades mais te define?",
        "opcoes": {
            "Corajoso(a)": "Mulan",
            "Sonhador(a)": "Ariel",
            "Líder nato(a)": "Simba",
            "Independente": "Elsa",
            "Aventureiro(a)": "Buzz Lightyear",
            "Persistente": "Moana",
            "Leal": "Woody",
            "Determinado(a)": "Tiana",
            "Livre e curioso(a)": "Peter Pan",
            "Criativo(a)": "Rapunzel"
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
            "Navegar e sentir o vento": "Moana",
            "Organizar algo com propósito": "Tiana",
            "Cuidar dos outros": "Woody",
            "Sonhar acordado": "Peter Pan",
            "Criar algo com as mãos": "Rapunzel"
        }
    },
    {
        "pergunta": "Qual dessas frases mais combina com você?",
        "opcoes": {
            '"Ao infinito e além!"': "Buzz Lightyear",
            '"O amor é uma porta aberta."': "Elsa",
            '"Hakuna Matata!"': "Simba",
            '"Eu quero ser onde o povo está."': "Ariel",
            '"A coragem é o que nos define."': "Mulan",
            '"O oceano me chama."': "Moana",
            '"Nunca deixe de sonhar."': "Tiana",
            '"Você tem um amigo em mim."': "Woody",
            '"Nunca cresça!"': "Peter Pan",
            '"A vida começa quando meus sonhos começam."': "Rapunzel"
        }
    },
    {
        "pergunta": "Se você tivesse um poder mágico, qual seria?",
        "opcoes": {
            "Controlar o gelo": "Elsa",
            "Falar com animais": "Simba",
            "Respirar debaixo d'água": "Ariel",
            "Voar pelo espaço": "Buzz Lightyear",
            "Se transformar e se camuflar": "Mulan",
            "Comandar o oceano": "Moana",
            "Dar vida a brinquedos": "Woody",
            "Transformar realidade com trabalho duro": "Tiana",
            "Voar sem precisar de asas": "Peter Pan",
            "Fazer seu cabelo brilhar e curar": "Rapunzel"
        }
    }
]

# Inicializa pontuação
if "respostas" not in st.session_state:
    st.session_state.respostas = []
if "personagem_final" not in st.session_state:
    st.session_state.personagem_final = None

# Mostrar perguntas
for i, p in enumerate(perguntas):
    if len(st.session_state.respostas) <= i:
        escolha = st.radio(p["pergunta"], list(p["opcoes"].keys()), key=f"q{i}")
        if st.button(f"Confirmar resposta {i+1}"):
            st.session_state.respostas.append(p["opcoes"][escolha])
        st.stop()

# Calcular resultado
if len(st.session_state.respostas) == len(perguntas):
    contagem = Counter(st.session_state.respostas)
    personagem = contagem.most_common(1)[0][0]
    st.session_state.personagem_final = personagem

# Mostrar resultado final
if st.session_state.personagem_final:
    st.success(f"🎉 Você seria o personagem **{st.session_state.personagem_final}** da Disney!")

    imagens = {
        "Elsa": "https://lumiere-a.akamaihd.net/v1/images/elsa_frozen2_b4e5d185.jpeg",
        "Simba": "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-1t9up3l_4ffdc51d.jpeg",
        "Buzz Lightyear": "https://lumiere-a.akamaihd.net/v1/images/open-uri20150622-20810-19nh3dz_3173f790.jpeg",
        "Mulan": "https://lumiere-a.akamaihd.net/v1/images/pp_mulan_herobanner_mobile_19751_7b32b3d8.jpeg",
        "Ariel": "https://lumiere-a.akamaihd.net/v1/images/ariel_7d861cb0.jpeg",
        "Moana": "https://lumiere-a.akamaihd.net/v1/images/open-uri20160824-19296-1hmlmt1_2b0f3e1d.jpeg",
        "Woody": "https://lumiere-a.akamaihd.net/v1/images/woody_59a25f8f.jpeg",
        "Tiana": "https://lumiere-a.akamaihd.net/v1/images/pp_princessandthefrog_herobanner_mobile_19752_e278e9f7.jpeg",
        "Peter Pan": "https://lumiere-a.akamaihd.net/v1/images/pp_peterpan_herobanner_mobile_19744_927d0d1b.jpeg",
        "Rapunzel": "https://lumiere-a.akamaihd.net/v1/images/pp_tangled_herobanner_mobile_19755_3f45675f.jpeg"
    }

    if personagem in imagens:
        st.image(imagens[personagem], caption=personagem, use_container_width=True)

    if st.button("Refazer o teste 🔁"):
        st.session_state.respostas = []
        st.session_state.personagem_final = None
        st.experimental_rerun()

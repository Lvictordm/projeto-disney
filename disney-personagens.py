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
        "pergunta": "Qual dessas atividades você mais gosta?",
        "opcoes": {
            "Cozinhar ou experimentar comidas": "Tiana",
            "Viajar para lugares distantes": "Moana",
            "Liderar e tomar decisões": "Simba",
            "Desenhar, pintar ou criar": "Rapunzel",
            "Ficar perto da natureza": "Ariel",
            "Brincar ou rir com os amigos": "Woody",
            "Desafiar os próprios limites": "Mulan",
            "Sonhar com outros mundos": "Peter Pan",
            "Cuidar do que é importante para mim": "Elsa",
            "Explorar o desconhecido": "Buzz Lightyear"
        }
    },
    {
        "pergunta": "Qual cor você mais gosta?",
        "opcoes": {
            "Azul": "Elsa",
            "Vermelho": "Mulan",
            "Amarelo": "Simba",
            "Roxo": "Buzz Lightyear",
            "Verde": "Tiana",
            "Rosa": "Rapunzel",
            "Laranja": "Moana",
            "Branco": "Woody",
            "Turquesa": "Ariel",
            "Dourado": "Peter Pan"
        }
    },
    {
        "pergunta": "Com qual animal você mais se identifica?",
        "opcoes": {
            "Leão": "Simba",
            "Peixe": "Ariel",
            "Pássaro": "Peter Pan",
            "Rena ou animal do gelo": "Elsa",
            "Dragão": "Mulan",
            "Cavalo": "Woody",
            "Tartaruga do mar": "Moana",
            "Camaleão ou animal curioso": "Rapunzel",
            "Abelha ou formiga trabalhadora": "Tiana",
            "Animal do espaço (tipo alien ou robô)": "Buzz Lightyear"
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
        "Elsa": "https://upload.wikimedia.org/wikipedia/en/e/e0/Elsa_(Frozen).png",
        "Simba": "https://upload.wikimedia.org/wikipedia/en/9/9d/YoungSimba.png",
        "Buzz Lightyear": "https://upload.wikimedia.org/wikipedia/en/2/29/Buzz_Lightyear.png",
        "Mulan": "https://upload.wikimedia.org/wikipedia/en/4/4c/Mulan_disney.png",
        "Ariel": "https://upload.wikimedia.org/wikipedia/en/7/75/Ariel_disney.png",
        "Moana": "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_disney.png",
        "Woody": "https://upload.wikimedia.org/wikipedia/en/0/01/Woody_Woodpecker.png",
        "Tiana": "https://upload.wikimedia.org/wikipedia/en/8/80/Tiana_disney.png",
        "Peter Pan": "https://upload.wikimedia.org/wikipedia/en/d/d1/Peter_Pan_disney.png",
        "Rapunzel": "https://upload.wikimedia.org/wikipedia/en/a/a4/Rapunzel_disney.png"
    }

    if personagem in imagens:
        st.image(imagens[personagem], caption=personagem, use_container_width=True)

    if st.button("Refazer o teste 🔁"):
        st.session_state.respostas = []
        st.session_state.personagem_final = None
        st.experimental_rerun()

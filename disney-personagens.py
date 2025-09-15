import streamlit as st

st.set_page_config(page_title="Quiz Disney - Pontuação", page_icon="🎯")

st.title("🎯 Quiz Disney: Quanto você sabe sobre os filmes?")
st.write("Responda às perguntas e veja sua pontuação no final!")

perguntas = [
    {
        "pergunta": "Quem é o vilão no filme Aladdin?",
        "opcoes": ["Jafar", "Hades", "Gaston", "Úrsula"],
        "correta": "Jafar",
        "imagem": "https://imagem.natelinha.uol.com.br/original/Aladdin_88759a66acb08b6f9d2b3f3a411492538d613179.jpeg"
    },
    {
        "pergunta": "O que a Fera veste no baile com a Bela?",
        "opcoes": ["Terno azul", "Capa vermelha", "Armadura", "Vestido amarelo"],
        "correta": "Terno azul",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/f/fd/Beast_disney.png"
    },
    {
        "pergunta": "O que Ariel mais deseja?",
        "opcoes": ["Viver no mundo humano", "Ser princesa do mar", "Encontrar um gênio", "Aprender a lutar"],
        "correta": "Viver no mundo humano",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/7/75/Ariel_disney.png"
    },
    {
        "pergunta": "Qual objeto mágico aparece em Aladdin?",
        "opcoes": ["Tapete voador", "Tridente mágico", "Espada encantada", "Coração de Te Fiti"],
        "correta": "Tapete voador",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/5/58/Aladdin_disney.png"
    },
    {
        "pergunta": "Quem é o companheiro de Moana em sua jornada?",
        "opcoes": ["Maui", "Sebastião", "Fera", "Rajah"],
        "correta": "Maui",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_disney.png"
    },
    {
        "pergunta": "Qual é o disfarce de Mulan durante o treinamento?",
        "opcoes": ["Ela se veste como soldado", "Ela vira princesa", "Ela usa vestido mágico", "Ela se disfarça de pirata"],
        "correta": "Ela se veste como soldado",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/4/4c/Mulan_disney.png"
    },
    {
        "pergunta": "Qual desses itens representa melhor a Moana?",
        "opcoes": ["Oceano e canoa", "Espelho mágico", "Tridente do mar", "Espada e dragão"],
        "correta": "Oceano e canoa",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_disney.png"
    },
    {
        "pergunta": "Qual o nome do vilão de A Bela e a Fera?",
        "opcoes": ["Gaston", "Úrsula", "Jafar", "Malévola"],
        "correta": "Gaston",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/9/99/Gaston_disney.png"
    },
    {
        "pergunta": "O que Sebastian representa em A Pequena Sereia?",
        "opcoes": ["Um conselheiro real", "Um peixe curioso", "Um tritão inimigo", "Um pássaro maluco"],
        "correta": "Um conselheiro real",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/5/5e/Sebastian_the_crab.png"
    },
    {
        "pergunta": "Qual desses personagens é um semideus?",
        "opcoes": ["Maui", "Simba", "Hércules", "Buzz Lightyear"],
        "correta": "Maui",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/e/e4/Maui_disney.png"
    },
    {
        "pergunta": "Qual é o animal companheiro da Mulan?",
        "opcoes": ["Um dragão", "Um tigre", "Um macaco", "Um cachorro"],
        "correta": "Um dragão",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/2/23/Mushu_disney.png"
    },
    {
        "pergunta": "Qual o presente que a Fera dá para Bela que a encanta?",
        "opcoes": ["Uma biblioteca", "Um espelho mágico", "Um vestido encantado", "Uma rosa mágica"],
        "correta": "Uma biblioteca",
        "imagem": "https://upload.wikimedia.org/wikipedia/en/7/7c/Beautybeastposter.jpg"
    }
]

if "respostas" not in st.session_state:
    st.session_state.respostas = []
if "verificado" not in st.session_state:
    st.session_state.verificado = False


for i, p in enumerate(perguntas):
    if len(st.session_state.respostas) <= i:
        st.image(p["imagem"], width=250)
        escolha = st.radio(p["pergunta"], p["opcoes"], key=f"q{i}")
        if st.button(f"Confirmar resposta {i+1}"):
            st.session_state.respostas.append(escolha)
        st.stop()


if len(st.session_state.respostas) == len(perguntas) and not st.session_state.verificado:
    acertos = 0
    erros = 0
    for idx, p in enumerate(perguntas):
        if st.session_state.respostas[idx] == p["correta"]:
            acertos += 1
        else:
            erros += 1
    st.session_state.acertos = acertos
    st.session_state.erros = erros
    st.session_state.verificado = True


if st.session_state.verificado:
    st.markdown("## ✅ Resultado Final:")
    st.success(f"Você acertou {st.session_state.acertos} de {len(perguntas)} perguntas!")
    st.error(f"Você errou {st.session_state.erros} perguntas.")
    st.markdown(f"### 🎯 Pontuação final: **{st.session_state.acertos * 10} pontos**")

    if st.button("Refazer o quiz 🔁"):
        st.session_state.respostas = []
        st.session_state.verificado = False
        st.rerun()

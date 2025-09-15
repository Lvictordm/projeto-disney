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
        "imagem": "https://i.pinimg.com/736x/9f/3e/f2/9f3ef2f6ed2b32b6aed48d1917287c55.jpg"
    },
    {
        "pergunta": "O que Ariel mais deseja?",
        "opcoes": ["Viver no mundo humano", "Ser princesa do mar", "Encontrar um gênio", "Aprender a lutar"],
        "correta": "Viver no mundo humano",
        "imagem": "https://www.giraofertas.com.br/wp-content/uploads/2022/10/Ariel-Castle-Disney-Eau-de-Toilette-Infantil-06.jpg"
    },
    {
        "pergunta": "Qual objeto mágico aparece em Aladdin?",
        "opcoes": ["Tapete voador", "Tridente mágico", "Espada encantada", "Coração de Te Fiti"],
        "correta": "Tapete voador",
        "imagem": ""
    },
    {
        "pergunta": "Quem é o companheiro de Moana em sua jornada?",
        "opcoes": ["Maui", "Sebastião", "Fera", "Rajah"],
        "correta": "Maui",
        "imagem": "https://www.shutterstock.com/image-photo/create-amazing-moana-birthday-wallpaper-260nw-2577212925.jpg"
    },
    {
        "pergunta": "Qual é o disfarce de Mulan durante o treinamento?",
        "opcoes": ["Ela se veste como soldado", "Ela vira princesa", "Ela usa vestido mágico", "Ela se disfarça de pirata"],
        "correta": "Ela se veste como soldado",
        "imagem": "https://rollingstone.com.br/wp-content/uploads/mulan_reprod.jpg"
    },
    {
        "pergunta": "Qual desses itens representa melhor a Moana?",
        "opcoes": ["Oceano e canoa", "Espelho mágico", "Tridente do mar", "Espada e dragão"],
        "correta": "Oceano e canoa",
        "imagem": "https://lumiere-a.akamaihd.net/v1/images/g_moana_09_17699_064f5500_2f9ff275.jpeg"
    },
    {
        "pergunta": "Qual o nome do vilão de A Bela e a Fera?",
        "opcoes": ["Gaston", "Úrsula", "Jafar", "Malévola"],
        "correta": "Gaston",
        "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6BaPBq6NNdaYaoypkkPC3knT77xgEz9axww&s"
    },
    {
        "pergunta": "O que Sebastian representa em A Pequena Sereia?",
        "opcoes": ["Um conselheiro real", "Um peixe curioso", "Um tritão inimigo", "Um pássaro maluco"],
        "correta": "Um conselheiro real",
        "imagem": "https://recreio.com.br/wp-content/uploads/disney/sebastiao_capa.png"
    },
    {
        "pergunta": "Qual desses personagens é um semideus?",
        "opcoes": ["Maui", "Simba", "Hércules", "Buzz Lightyear"],
        "correta": "Maui",
        "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQu-myWZLYaaadxdU5p8K78C6a0blbRC-82FA&s"
    },
    {
        "pergunta": "Qual é o animal companheiro da Mulan?",
        "opcoes": ["Um dragão", "Um tigre", "Um macaco", "Um cachorro"],
        "correta": "Um dragão",
        "imagem": "https://i0.wp.com/cromossomonerd.com.br/wp-content/uploads/2016/10/imagem-destacada-mulan.png?fit=1068%2C600&ssl=1"
    },
    {
        "pergunta": "Qual o presente que a Fera dá para Bela que a encanta?",
        "opcoes": ["Uma biblioteca", "Um espelho mágico", "Um vestido encantado", "Uma rosa mágica"],
        "correta": "Uma biblioteca",
        "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlwfC-DZMR5qZQQq9HGtguVxub1skd9KAe6Q&s"
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

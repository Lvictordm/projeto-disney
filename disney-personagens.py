import streamlit as st

st.set_page_config(page_title="Quiz Disney - Pontuação", page_icon="🎯")

st.title("🎯 Quiz Disney: Quanto você sabe sobre os filmes?")
st.write("Responda às perguntas e veja sua pontuação no final!")

# Perguntas com resposta correta
perguntas = [
    {
        "pergunta": "Quem é o vilão no filme Aladdin?",
        "opcoes": ["Jafar", "Hades", "Gaston", "Úrsula"],
        "correta": "Jafar"
    },
    {
        "pergunta": "O que a Fera veste no baile com a Bela?",
        "opcoes": ["Terno azul", "Capa vermelha", "Armadura", "Vestido amarelo"],
        "correta": "Terno azul"
    },
    {
        "pergunta": "O que Ariel mais deseja?",
        "opcoes": ["Viver no mundo humano", "Ser princesa do mar", "Encontrar um gênio", "Aprender a lutar"],
        "correta": "Viver no mundo humano"
    },
    {
        "pergunta": "Qual objeto mágico aparece em Aladdin?",
        "opcoes": ["Tapete voador", "Tridente mágico", "Espada encantada", "Coração de Te Fiti"],
        "correta": "Tapete voador"
    },
    {
        "pergunta": "Quem é o companheiro de Moana em sua jornada?",
        "opcoes": ["Maui", "Sebastião", "Fera", "Rajah"],
        "correta": "Maui"
    },
    {
        "pergunta": "Qual é o disfarce de Mulan durante o treinamento?",
        "opcoes": ["Ela se veste como soldado", "Ela vira princesa", "Ela usa vestido mágico", "Ela se disfarça de pirata"],
        "correta": "Ela se veste como soldado"
    },
    {
        "pergunta": "Qual desses itens representa melhor a Moana?",
        "opcoes": ["Oceano e canoa", "Espelho mágico", "Tridente do mar", "Espada e dragão"],
        "correta": "Oceano e canoa"
    }
]

# Inicializar sessão
if "respostas" not in st.session_state:
    st.session_state.respostas = []
if "verificado" not in st.session_state:
    st.session_state.verificado = False

# Mostrar perguntas
for i, p in enumerate(perguntas):
    if len(st.session_state.respostas) <= i:
        escolha = st.radio(p["pergunta"], p["opcoes"], key=f"q{i}")
        if st.button(f"Confirmar resposta {i+1}"):
            st.session_state.respostas.append(escolha)
        st.stop()

# Verificar respostas
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

# Mostrar resultado final
if st.session_state.verificado:
    st.markdown("## ✅ Resultado Final:")
    st.success(f"Você acertou {st.session_state.acertos} de {len(perguntas)} perguntas!")
    st.error(f"Você errou {st.session_state.erros} perguntas.")
    st.markdown(f"### 🎯 Pontuação final: **{st.session_state.acertos * 10} pontos**")

    if st.button("Refazer o quiz 🔁"):
        st.session_state.respostas = []
        st.session_state.verificado = False
        st.experimental_rerun()

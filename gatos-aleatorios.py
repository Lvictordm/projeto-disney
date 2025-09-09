import streamlit as st
import requests
import random

st.set_page_config(page_title="Adivinhe o Gato!", page_icon="🐱")

st.title("🐱 Adivinhe a Raça do Gato!")
st.write("Uma imagem de um gato será exibida. Tente adivinhar a raça correta!")

# Traduções básicas (você pode expandir)
traducao_racas = {
    "Abyssinian": "Abissínio",
    "Bengal": "Bengal",
    "Birman": "Sagrado da Birmânia",
    "British Shorthair": "British de pelo curto",
    "Maine Coon": "Maine Coon",
    "Persian": "Persa",
    "Ragdoll": "Ragdoll",
    "Russian Blue": "Azul Russo",
    "Siamese": "Siamês",
    "Sphynx": "Sphynx"
}

# Funções de API
def buscar_racas():
    url = "https://api.thecatapi.com/v1/breeds"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    return []

def buscar_imagem_raca(raca_id):
    url = f"https://api.thecatapi.com/v1/images/search?breed_ids={raca_id}&limit=1"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        if dados:
            return dados[0]["url"]
    return None

# Carrega as raças uma única vez
if "racas" not in st.session_state:
    st.session_state.racas = buscar_racas()

# Função para iniciar novo desafio
def novo_desafio():
    if st.session_state.racas:
        raca_correta = random.choice(st.session_state.racas)
        nome_en = raca_correta["name"]
        nome_pt = traducao_racas.get(nome_en, nome_en)
        id_raca = raca_correta["id"]
        imagem = buscar_imagem_raca(id_raca)

        # Gera 3 opções falsas
        opcoes = [nome_pt]
        while len(opcoes) < 4:
            r = random.choice(st.session_state.racas)
            nome_fake = traducao_racas.get(r["name"], r["name"])
            if nome_fake not in opcoes:
                opcoes.append(nome_fake)
        random.shuffle(opcoes)

        st.session_state.desafio = {
            "nome_pt": nome_pt,
            "nome_en": nome_en,
            "imagem": imagem,
            "opcoes": opcoes,
            "respondido": False
        }

# Garante que temos um desafio ao carregar
if "desafio" not in st.session_state:
    novo_desafio()

# Mostra imagem e pergunta
desafio = st.session_state.desafio
st.image(desafio["imagem"], caption="Qual é a raça desse gato?", use_container_width=True)
escolha = st.selectbox("Escolha a raça:", desafio["opcoes"], key="selectbox")

# Botão para responder
if not desafio["respondido"]:
    if st.button("Responder"):
        if escolha == desafio["nome_pt"]:
            st.success("🎉 Acertou! Essa é a raça correta.")
        else:
            st.error(f"❌ Errou! A raça correta era: {desafio['nome_pt']} ({desafio['nome_en']})")

        st.session_state.desafio["respondido"] = True

# Após responder, botão para novo desafio
if desafio["respondido"]:
    if st.button("Próximo gato 🐾"):
        novo_desafio()
        st.experimental_rerun()

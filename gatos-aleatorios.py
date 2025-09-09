import streamlit as st
import requests
import random

st.set_page_config(page_title="Adivinhe o Gato!", page_icon="🐱")

st.title("🐱 Adivinhe a Raça do Gato!")
st.write("Vamos gerar a imagem de um gato aleatório e você precisa adivinhar a raça correta.")

# Dicionário com traduções (parcial - você pode expandir)
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
    # Adicione mais conforme desejar
}

def buscar_racas():
    url = "https://api.thecatapi.com/v1/breeds"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    return []

def buscar_imagem_raca(raca_id):
    url = f"https://api.thecatapi.com/v1/images/search?breed_ids={raca_id}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        if dados:
            return dados[0]["url"]
    return None

# Carregar raças (somente uma vez)
if "racas" not in st.session_state:
    st.session_state.racas = buscar_racas()

# Sortear desafio (somente uma vez)
if "desafio" not in st.session_state and st.session_state.racas:
    raca_correta = random.choice(st.session_state.racas)
    nome_original = raca_correta["name"]
    nome_pt = traducao_racas.get(nome_original, nome_original)
    id_raca = raca_correta["id"]
    imagem = buscar_imagem_raca(id_raca)

    # Opções aleatórias
    opcoes = [nome_pt]
    while len(opcoes) < 4:
        r = random.choice(st.session_state.racas)
        nome_op = traducao_racas.get(r["name"], r["name"])
        if nome_op not in opcoes:
            opcoes.append(nome_op)
    random.shuffle(opcoes)

    # Armazenar no estado
    st.session_state.desafio = {
        "nome_original": nome_original,
        "nome_pt": nome_pt,
        "id": id_raca,
        "imagem": imagem,
        "opcoes": opcoes
    }

# Mostrar desafio
if "desafio" in st.session_state:
    desafio = st.session_state.desafio
    st.image(desafio["imagem"], caption="Qual é a raça desse gato?", use_container_width=True)

    escolha = st.selectbox("Escolha a raça:", desafio["opcoes"])

    if st.button("Responder"):
        if escolha == desafio["nome_pt"]:
            st.success("🎉 Acertou! Essa é a raça correta.")
        else:
            st.error(f"❌ Errou! A raça correta era: {desafio['nome_pt']} ({desafio['nome_original']})")

        # Permitir novo jogo
        if st.button("Jogar novamente"):
            del st.session_state.desafio
            st.experimental_rerun()
else:
    st.error("Não foi possível carregar as raças de gatos.")

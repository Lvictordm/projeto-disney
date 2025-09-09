import streamlit as st
import requests
import random

st.set_page_config(page_title="Adivinhe o Gato!", page_icon="🐱")

st.title("🐱 Adivinhe a Raça do Gato!")
st.write("Vamos gerar imagens de gatos aleatórios e você precisa adivinhar a raça correta.")

# Tradução de algumas raças
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
    # Adicione mais se quiser
}

# Buscar todas as raças
def buscar_racas():
    url = "https://api.thecatapi.com/v1/breeds"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    return []

# Buscar várias imagens da mesma raça
def buscar_imagens_raca(raca_id, quantidade=3):
    url = f"https://api.thecatapi.com/v1/images/search?breed_ids={raca_id}&limit={quantidade}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return [item["url"] for item in dados if "url" in item]
    return []

# Carregar raças apenas uma vez
if "racas" not in st.session_state:
    st.session_state.racas = buscar_racas()

# Criar novo desafio apenas uma vez
if "desafio" not in st.session_state and st.session_state.racas:
    raca_correta = random.choice(st.session_state.racas)
    nome_original = raca_correta["name"]
    nome_pt = traducao_racas.get(nome_original, nome_original)
    id_raca = raca_correta["id"]
    imagens = buscar_imagens_raca(id_raca, quantidade=3)  # Pegando 3 imagens

    # Criar opções falsas
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
        "imagens": imagens,
        "opcoes": opcoes
    }

# Mostrar desafio
if "desafio" in st.session_state:
    desafio = st.session_state.desafio

    if desafio["imagens"]:
        st.subheader("Qual é a raça desses gatos?")
        st.image(desafio["imagens"], use_container_width=True)
    else:
        st.warning("Nenhuma imagem disponível para esta raça.")

    escolha = st.selectbox("Escolha a raça:", desafio["opcoes"])

    if st.button("Responder"):
        if escolha == desafio["nome_pt"]:
            st.success("🎉 Acertou! Essa é a raça correta.")
        else:
            st.error(f"❌ Errou! A raça correta era: {desafio['nome_pt']} ({desafio['nome_original']})")

        if st.button("Jogar novamente"):
            del st.session_state.desafio
            st.experimental_rerun()
else:
    st.error("Não foi possível carregar as raças de gatos.")

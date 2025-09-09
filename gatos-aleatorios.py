import streamlit as st
import requests
import random

st.set_page_config(page_title="Adivinhe o Gato!", page_icon="🐱")

# Traduções básicas
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

def novo_desafio():
    racas = st.session_state.racas
    raca = random.choice(racas)
    nome_en = raca["name"]
    nome_pt = traducao_racas.get(nome_en, nome_en)
    id_raca = raca["id"]
    imagem = buscar_imagem_raca(id_raca)

    # Opções
    opcoes = [nome_pt]
    while len(opcoes) < 4:
        r = random.choice(racas)
        nome_fake = traducao_racas.get(r["name"], r["name"])
        if nome_fake not in opcoes:
            opcoes.append(nome_fake)
    random.shuffle(opcoes)

    st.session_state.desafio = {
        "nome_pt": nome_pt,
        "nome_en": nome_en,
        "imagem": imagem,
        "opcoes": opcoes,
        "respondido": False,
        "resposta_certa": False
    }

def main():
    st.title("🐱 Adivinhe a Raça do Gato!")
    st.write("Uma imagem de um gato será exibida. Tente adivinhar a raça correta!")

    # Carregar raças uma vez
    if "racas" not in st.session_state:
        st.session_state.racas = buscar_racas()

    if not st.session_state.racas:
        st.error("Não foi possível carregar as raças de gatos.")
        return

    # Criar desafio se não existir
    if "desafio" not in st.session_state:
        novo_desafio()

    desafio = st.session_state.desafio

    # Exibir imagem
    st.image(desafio["imagem"], caption="Qual é a raça desse gato?", use_container_width=True)

    # Exibir opções
    escolha = st.selectbox("Escolha a raça:", desafio["opcoes"])

    # Botão para responder
    if not desafio["respondido"]:
        if st.button("Responder"):
            if escolha == desafio["nome_pt"]:
                st.success("🎉 Acertou! Essa é a raça correta.")
                st.session_state.desafio["resposta_certa"] = True
            else:
                st.error(f"❌ Errou! A raça correta era: {desafio['nome_pt']} ({desafio['nome_en']})")

            st.session_state.desafio["respondido"] = True

    # Se já respondeu, mostra botão para nova imagem
    if desafio["respondido"]:
        if st.button("Próximo gato 🐾"):
            # Remove o desafio atual e recarrega a página naturalmente
            del st.session_state.desafio

main()

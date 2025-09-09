import streamlit as st
import requests
import random


st.title(" adivinhe o gato!")
st.write("vamos gerar uma imagem de um gato aletorio e voce precisa adivinhar a raça")


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

st.title("🐱 Adivinhe a Raça do Gato")


racas = buscar_racas()


if racas:
    raca_correta = random.choice(racas)
    nome_raca_correta = raca_correta["name"]
    id_raca_correta = raca_correta["id"]
    imagem = buscar_imagem_raca(id_raca_correta)

    opcoes = [nome_raca_correta]
    while len(opcoes) < 4:
        r = random.choice(racas)
        if r["name"] not in opcoes:
            opcoes.append(r["name"])
    random.shuffle(opcoes)

    if imagem:
        st.image(imagem, caption="Qual é a raça desse gato?"use_container_width==True)
        escolha = st.selectbox("Escolha a raça:", opcoes)
        if st.button("Responder"):
            if escolha == nome_raca_correta:
                st.success("🎉 Acertou! Essa é a raça correta.")
            else:
                st.error(f"❌ Errou! A raça correta era: {nome_raca_correta}")
else:
    st.error("Não foi possível carregar as raças de gatos.")

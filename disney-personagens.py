import streamlit as st
import requests

# Definir a URL da API
API_URL = "https://api.disneyapi.dev/character"

# Função para pegar os personagens da API
def carregar_personagens():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Verifica se houve erro na requisição
        return response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao acessar a API: {e}")
        return []

# Carregar personagens
personagens = carregar_personagens()

# Verificar se a lista de personagens foi carregada
if len(personagens) == 0:
    st.error("Não foi possível carregar os personagens da Disney.")
else:
    # Exibir lista de personagens
    st.title("🌟 Personagens Disney")
    st.write("Aqui estão alguns personagens da Disney que você pode conhecer!")

    for personagem in personagens:
        # Mostrar as informações de cada personagem
        nome = personagem.get('name', 'Desconhecido')
        imagem_url = personagem.get('imageUrl', '')
        descricao = personagem.get('description', 'Descrição não disponível.')
        
        # Exibir as informações de cada personagem
        st.subheader(nome)
        if imagem_url:
            st.image(imagem_url, caption=nome, use_column_width=True)
        st.write(f"**Descrição:** {descricao}")
        st.write("---")

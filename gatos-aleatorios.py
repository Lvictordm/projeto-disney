import streamlit as st
import requests



st.title("the cat API")
st.write("Esse site gera imagens aleatorias de gatos, conforme a escolha do usuario")

def gato_aleatorio(): 
    url = "https://api.thecatapi.com/v1/imagens/search"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        return dados[0]['url']
    else:
        return None
    
if st.button("Mostrar gato aleatório"):
    imagem =  gato_aleatorio()

    if imagem:
        st.image(imagem, caption="Gato aleatório", use_column_width=True)
    else:
        st.error("Error ao buscar a imagem do gato aleatório")
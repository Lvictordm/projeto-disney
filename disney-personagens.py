import streamlit as st
import requests

st.set_page_config(page_title="Personagens da Disney", page_icon="🐭")

st.title("🐭 Personagens da Disney")
st.write("Explore personagens da Disney usando dados da API pública: [Disney API](https://api.disneyapi.dev/)")

# Campo de busca
personagem_nome = st.text_input("Digite o nome de um personagem da Disney:")

# Quando clicar em buscar
if st.button("Buscar"):
    if personagem_nome.strip() == "":
        st.warning("Por favor, digite um nome.")
    else:
        url = f"https://api.disneyapi.dev/character?name={personagem_nome}"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            resultados = dados.get("data", [])

            if not resultados:
                st.error("Nenhum personagem encontrado com esse nome.")
            else:
                for personagem in resultados:
                    st.subheader(personagem["name"])
                    
                    # Imagem (se existir)
                    if personagem.get("imageUrl"):
                        st.image(personagem["imageUrl"], width=200)

                    # Aparições
                    aparicoes = personagem.get("films", []) + personagem.get("tvShows", [])
                    aparicoes = list(set(aparicoes))  # remove duplicatas

                    if aparicoes:
                        st.markdown("**Apareceu em:**")
                        for a in aparicoes:
                            st.markdown(f"- {a}")
                    else:
                        st.markdown("*Sem informações de aparições*")

                    # Linha separadora
                    st.markdown("---")
        else:
            st.error("Erro ao buscar dados da API.")

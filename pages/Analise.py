# Importação das bibliotecas
import streamlit as st
import datetime
import pandas as pd
from PIL import Image
from auxiliar import apply_custom_style


# Configuração da página
st.set_page_config(page_title= 'ONG - Passos Mágicos', layout='wide', page_icon=':gem:')

if __name__ == '__main__':
        apply_custom_style()

#### Menu Superior
cols = st.columns(5, gap="large")
with cols[0]:
    st.image("images/pme.png")
with cols[1]:
    if st.button("Home"):
        st.switch_page("Home.py")
with cols[2]:
    if st.button("Análise"):
        st.switch_page("pages/Analise.py")
with cols[3]:
    if st.button("História"):
        st.switch_page("pages/Historia.py")
with cols[4]:
    if st.button("Sobre"):
        st.switch_page("pages/Sobre.py")
st.header("", divider="gray")

# Título do aplicativo
st.title("Upload de Arquivo Excel")

# Criando o widget de upload
uploaded_file = st.file_uploader("Faça upload do seu arquivo Excel", type=["xlsx"])

# Verifica se um arquivo foi enviado
if uploaded_file is not None:
    # Lendo o arquivo Excel como DataFrame
    df = pd.read_excel(uploaded_file)

    # Exibe o DataFrame
    st.write("### Dados do Arquivo:")
    st.dataframe(df)

    # Exibir estatísticas do DataFrame (opcional)
    st.write("### Estatísticas do DataFrame:")
    st.write(df.describe())
	
#Adicionando inputs do Usuario

fase = st.number_input("Insira um número 0 - 7", max_value=7, min_value=1)
ano_nascimento = st.number_input("Insira ano de Nascimento", value=2025, min_value=1900, max_value=2050)
genero = st.radio("Selecione o Genero", ["Masculino", "Feminino", "Prefiro não infomar"]) 
ano_ingresso = st.number_input("Insira ano de Ingresso", value=2025, min_value=1900, max_value=2050)
anos_pm = st.number_input("Insira ano PM", value=2025, min_value=1900, max_value=2050)
intituicao_ensino = st.selectbox("Selecione a Instituição de Ensino",["Escola Pública", "Escola Privada", "Já Formado", "Outro"])
pedra = st.selectbox("Selecione a Pedra",["Ametista", "Topázio", "Ágata", "Quartzo","Desconhecido"])
inde = st.number_input("INDE 0 - 10", max_value=10, min_value=1, step=float)
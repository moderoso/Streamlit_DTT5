# Importação das bibliotecas
import streamlit as st
from PIL import Image

# Configuração da página
st.set_page_config(page_title= 'ONG - Passos Mágicos', layout='wide', page_icon=':gem:')

# Título da página
#st.title('ONG - Passos Mágicos :woman-woman-girl-boy:✨')

# Carregando image
image = Image.open('images/pm.png')
st.image(image, width=200)

# Título da página
st.title('ONG - Passos Mágicos :woman-woman-girl-boy:✨')


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


side_bg = 'images/pm.png'
sidebar_bg(side_bg)

def sidebar_bg(side_bg):

   side_bg_ext = 'png'

   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )


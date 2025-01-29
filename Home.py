# Importação das bibliotecas
import streamlit as st
from PIL import Image
from auxiliar import apply_custom_style


if __name__ == '__main__':
        apply_custom_style()

# Configuração da página
#st.set_page_config(page_title= 'ONG - Passos Mágicos', layout='wide', page_icon=':gem:')




#### Páginas
cols = st.columns(6, gap="large")
with cols[0]:
    st.image("images/pm.png")
with cols[1]:
    if st.button("Home"):
        st.switch_page("Home.py")
with cols[2]:
    if st.button("PSE (2020)"):
        st.switch_page("pages/PSE (2020).py")
with cols[3]:
    if st.button("Sobre"):
        st.switch_page("pages/MVP (sobre).py")
with cols[4]:
    if st.button("Referências"):
        st.switch_page("pages/Sobre.py")

st.header("", divider="gray")

# Carregando top
top = Image.open('images/top.png')
st.image(top, width=200)

# Carregando image
image = Image.open('images/pm.png')
st.image(image, width=200)

# Carregando top
top2 = Image.open('images/top.png')
st.image(top2, width=200)




# Título da página
st.title('ONG - Passos Mágicos :woman-woman-girl-boy:✨')

    

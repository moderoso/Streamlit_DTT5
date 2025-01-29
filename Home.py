# Importação das bibliotecas
import streamlit as st
from PIL import Image
from auxiliar import apply_custom_style


# Configuração da página
#st.set_page_config(page_title= 'ONG - Passos Mágicos', layout='wide', page_icon=':gem:')
st.set_page_config(page_title= 'ONG - Passos Mágicos', layout='wide', page_icon=':gem:')

if __name__ == '__main__':
        apply_custom_style()

#### Menu Superior
cols = st.columns(6, gap="large")
with cols[0]:
    st.image("images/pm_top.png")
with cols[1]:
    if st.button("Home"):
        st.switch_page("Home.py")
with cols[2]:
    if st.button("Análise"):
        st.switch_page("pages/PSE (2020).py")
with cols[3]:
    if st.button("História"):
        st.switch_page("pages/MVP (sobre).py")
with cols[4]:
    if st.button("Sobre"):
        st.switch_page("pages/Sobre.py")
st.header("", divider="gray")

# Carregando top
#top = Image.open('images/top.png')
#st.image(top, width=200)

# Título da página
st.title('ONG - Passos Mágicos :woman-woman-girl-boy:✨')

### Título da Página Inicial
st.header(":footprints: ONG Passos Mágicos e seus principais indicadores")
st.markdown("#")

### Tabs da página inicial
#tabs_titles_2= ["Como funciona a Passos","Alunos impactados pela Passos","Indicadores"]
#tabs_2 = st.tabs(tabs_titles_2)

# Tab Como funciona a Passos
with tabs_2[0]: 
    st.markdown("")
    colunas_1 = st.columns(2)
    with colunas_1 [0]:

        with st.container(border=True):
            st.markdown("""
                        <p style='font-size:20px;'>A Passos Mágicos tem como objetivo acelerar a ascensão social de crianças e jovens do município de Embu Guaçu através da educação.   
                        <br><br>
                        Fornecendo aulas de português, matemática e inglês três vezes na semana, atividades extracurriculares de finais de semana e bolsas de estudos no colégio particular, em cursos técnicos
                        e de graduação.</p>""", unsafe_allow_html=True)

    with colunas_1 [1]:
                st.image("images/Ong-Passos-Magicos.jpeg",width=300)

    

# Importação das bibliotecas
import streamlit as st
from PIL import Image
from auxiliar import apply_custom_style


# Configuração da página
st.set_page_config(page_title= 'ONG - Passos Mágicos', layout='wide', page_icon=':gem:')

if __name__ == '__main__':
        apply_custom_style()

st.markdown("""<style>[data-testid="stSidebar"] {display: flex; align-items: center; margin-bottom: 20px;}.icon-container a {margin-right: 15px;}</style>""", unsafe_allow_html=True)
with st.sidebar:
    st.markdown('''<b><u>Equipe FIAP - 5DTAT - Grupo 79</u></b></font>''', unsafe_allow_html=True)
    st.markdown('''
                - Jhonny da Silva Mineu - RM 355135
                - Marina Mendez Araujo - RM 355100  
                - Volmir Moderoso Santos - RM 355589''')

#### Menu Superior
cols = st.columns(5, gap="large")
with cols[0]:
    st.image("images/pme.png")
#with cols[1]:
#    if st.button("Home"):
#        st.switch_page("Home.py")
#with cols[2]:
#    if st.button("Estudo"):
#        st.switch_page("pages/02 Estudo.py")
#with cols[3]:
#    if st.button("MVP"):
#        st.switch_page("pages/03 MVP.py")
#with cols[4]:
#    if st.button("Conclusão"):
#        st.switch_page("pages/05 Conclusao.py")
##with cols[5]:
    ##if st.button("Referências"):
        ##st.switch_page("pages/Referencias.py")
st.header("", divider="gray")


## Rodapé
st.markdown("---")

st.markdown('''<div class="center">
                    <a target="_self" href="#quem-somos">
                        <button class="back-to-top">
                            Voltar ao topo
                        </button>
                    </a>
                </div>''', unsafe_allow_html=True)


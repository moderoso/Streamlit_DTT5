# Importação das bibliotecas
import streamlit as st
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
    if st.button("Estudo"):
        st.switch_page("pages/Estudo.py")
with cols[3]:
    if st.button("MVP"):
        st.switch_page("pages/MVP.py")
with cols[4]:
    if st.button("Conclusão"):
        st.switch_page("pages/Conclusao.py")
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


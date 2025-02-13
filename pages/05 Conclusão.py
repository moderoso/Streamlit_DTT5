# Importação das bibliotecas
import streamlit as st
from PIL import Image
from auxiliar import apply_custom_style


# Configuração da página
st.set_page_config(page_title= 'ONG - Passos Mágicos', layout='wide', page_icon=':gem:')

with st.sidebar:
    st.markdown('''<b><u>Equipe FIAP - 5DTAT - Grupo 79</u></b></font>''', unsafe_allow_html=True)
    st.markdown('''
                - Jhonny da Silva Mineu - RM 355135
                - Marina Mendez Araujo - RM 355100  
                - Volmir Moderoso Santos - RM 355589''')

#### Menu Superior
cols = st.columns(6, gap="large")
with cols[0]:
    st.image("images/passos-magicos.png")
    st.markdown("  ")
with cols[1]:
    if st.button("Home"):
        st.switch_page("Home.py")
with cols[2]:
    if st.button("Estudo"):
        st.switch_page("pages/02 Estudo.py")
with cols[3]:
    if st.button("MVP"):
        st.switch_page("pages/03 MVP.py")
with cols[4]:
    if st.button("Conclusão"):
        st.switch_page("pages/05 Conclusão.py")
with cols[5]:
    if st.button("Referências"):
        st.switch_page("pages/06 Referencias.py")

st.header("", divider="gray")

st.markdown( '#### Conclusão')
st.markdown('<p style="text-align: justify;">Concluímos que baseados nos indicadores a instituição permanece evoluindo no critério pedagógico, porém, a taxa de evasão ainda é alta a partir de alunos com 12 anos ou mais de idade. A percepção é que a partir de 4 anos de participação é que existe um desinteresse como mostramos no dashboard. Em contrapartida houve também um avanço do IDA o que reflete uma melhora com o uso de programa de bolsa de estudos e o programa de aceleração do conhecimento.Um ponto bem importante é que os alunos que se mantiveram além do 4º ano conseguiram eliminar a defasagem de aprendizado como mostramos na IAN alcançando o ponto de equilíbrio no 7 ano.Outro ponto, deveria ser intensificada a parceria com escolas privadas, pois a aderência ainda é baixa em comparação a pública.<br><br></p>', unsafe_allow_html = True)





## Rodapé
st.markdown("---")

st.markdown('''<div class="center">
                    <a target="_self" href="#quem-somos">
                        <button class="back-to-top">
                            Voltar ao topo
                        </button>
                    </a>
                </div>''', unsafe_allow_html=True)


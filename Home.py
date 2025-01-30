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
    if st.button("Análise"):
        st.switch_page("pages/Analise.py")
with cols[3]:
    if st.button("História"):
        st.switch_page("pages/Historia.py")
with cols[4]:
    if st.button("Sobre"):
        st.switch_page("pages/Sobre.py")
st.header("", divider="gray")

# Carregando top
#top = Image.open('images/pme.png')
#st.image(top, width=200)

# Título da página
st.title('ONG - Passos Mágicos :woman-woman-girl-boy:✨')

### Título da Página Inicial
#st.header(":footprints: ONG Passos Mágicos e seus principais indicadores")
#st.markdown("#")

### Tabs da página inicial
tabs_titles_2= ["Como funciona a Passos","Alunos impactados pela Passos","Indicadores"]
tabs_2 = st.tabs(tabs_titles_2)

# Tab Como funciona a Passos
with tabs_2[0]: 
    st.markdown("")
    colunas_1 = st.columns(2)
    with colunas_1 [0]:

        with st.container(border=True):
            st.markdown("""
                        <p style='font-size:20px;'>A Passos Mágicos tem como objetivo acelerar a ascensão social de crianças e jovens do município de Embu Guaçu através da educação.
                         É efetuada um processo seletivo visando garantir a dignidade e a autoestima com o intuito de promover a inclusão social ativa. É efetuada a divulgação das vagas na comunidade, é aplicada uma prova de sondagem aos interessados, aos selecionados é feita uma entrevista com psicologos, pedagogos e assistentes sociais. Após deliberarem analisam o perfil socioeconomicos para direcionar o conteudo e por fim a matricula.</p>""", unsafe_allow_html=True)

    with colunas_1 [1]:
                st.image("images/borda.png",width=300)


    colunas_2 = st.columns(2, gap="large")

 

# TAB Alunos Impactados
with tabs_2[1]: 
    st.header("Alunos Impactados pela Passos Mágicos")

    st.markdown("""
                <p style='font-size:20px;'>A Passos Mágicos, no decorrer de sua trajetória, já impactou mais de 4.400 pessoas( considerando familiares). Vamos demostrar, logo abaixo, a quantidade de alunos
                 que fizeram parte do PAC (Programa de Aceleração de Conhecimento), o percentual de alunos por sexo e etnia e a sua faixa etária.
                <br><br>
                </p>""", unsafe_allow_html=True)

    colunas_3 = st.columns(2, gap="large")
    
    with colunas_3 [0]:
        st.markdown( """         
            <ul class="font-text-destaques">
                <br><br>
                <li> O gráfico ao lado demonstra a evolução do número de alunos impactados pelo sistema de aceleração de aprendizado da Passos Mágicos.
                </li>
                <li> Podemos notar que houve um crescimento exponencial chegando ao número de <b> 1.000 </b> alunos impactados pelo PAC da Passos no ano de 2022.
                </li>
            </ul>""",unsafe_allow_html=True)
    
# TAB de Indicadores      
with tabs_2[2]: 
    st.header("Indicadores Passos Mágicos")
    st.markdown('''<p style='font-size:20px;'>Os dados que serão mostrados abaixo tem a finalidade de demonstrar o impacto da Passos Mágicos no sistema educacional e nos jovens da região de Embu-Guaçu.
                <br><br>
                </p>''',unsafe_allow_html=True)
    colunas_3 = st.columns(2)
   with colunas_3 [0]:
        st.image("images/indicador_avaliacao.png",caption="Fonte:PEDE Pontos importantes", width=600)

       

    

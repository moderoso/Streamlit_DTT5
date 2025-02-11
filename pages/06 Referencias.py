# Importação da biblioteca streamlit
import streamlit as st
from auxiliar import apply_custom_style

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

# Título da página
st.title('Referências utilizadas para o projeto:')

#st.markdown('<p style="text-align: justify;"><br /><br /><br /><br /></p>', unsafe_allow_html = True)

st.write("### Fontes de dados")
st.write("Links acessado em 20 e 30 Janeiro 2025"

         "\n* OpenAI. “O Chat GPT é uma ferramenta de processamento de linguagem natural orientada por IA, que possibilita conversas semelhantes às humanas com o chatbot   https://openai.com/blog/chat-gpt-3-launch"
         "\n* Passos Mágicos. “ONG Passos Mágicos   https://passosmagicos.org.br/"
        "\n* Abandono escolar: entendendo as causas e buscando soluções. “Abandono Escolar  https://institutoayrtonsenna.org.br/abandono-escolar"
         "\n* Brazil and the OECD. “Brazil and the OECD   https://www.oecd.org/en/countries/brazil.html" 
		 "\n* Dois milhões de crianças e adolescentes de 11 a 19 anos não estão frequentando a escola no Brasil, “alerta a UNICEF   https://www.unicef.org/brazil/comunicados-de-imprensa/dois-milhoes-de-criancas-e-adolescentes-de-11-a-19-anos-nao-estao-frequentando-a-escola-no-brasil"
         "\n* Evasão escolar e o abandono: um guia para entender esses conceitos. “Evasão Escolar   https://observatoriodeeducacao.institutounibanco.org.br/em-debate/abandono-evasao-escolar/?gad_source=1&gclid=Cj0KCQiA4-y8BhC3ARIsAHmjC_EpA-7Air9ZuFjOOpgmc2-UwED_38gmL7qeBX7uX7Eufl1dEh__JZMaAifREALw_wcB"	
		 "\n* Relatório PEDE2021. “Disponível pela FIAP para Datathon" 		 
 		 )

st.markdown('<p style="text-align: justify;"><br /><br /><br /><br /></p>', unsafe_allow_html = True)


## Rodapé
st.markdown("---")

st.markdown('''<div class="center">
                    <a target="_self" href="#b3f7a5e4">
                        <button class="back-to-top">
                            Voltar ao topo
                        </button>
                    </a>
                </div>''', unsafe_allow_html=True)
		




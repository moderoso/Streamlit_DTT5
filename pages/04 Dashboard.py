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
tabs_titles_2= ["Dashboard e Storytelling","Análise e Insights"]
tabs_2 = st.tabs(tabs_titles_2)

with tabs_2[0]: 
    st.header("Dashboard e Storytelling")
    colunas_3 = st.columns(1, gap="large")
    powerbi_url = 'https://app.powerbi.com/view?r=eyJrIjoiZjI4NmNiN2QtNDMxOC00MmZjLTlkNWItN2FlMDdkMjZiOTRmIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9'
    st.components.v1.iframe(powerbi_url, width=1200, height=800)

with tabs_2[1]: 
    st.header("Análise e Insights")
    st.write("Com base nos dados encontrados, comprovamos que 78,98% da origem dos alunos são de escolas públicas, 10,21% escolas privadas e 10,81% são de outras origens. Dentre esse público pouco mais de 53% femininos e 46% masculinos e nos últimos 3 anos (2022, 2023 e 2024) foram atendidos 1661 alunos. E o maior faixa etária  de seus alunos possuem em média 12 anos de idade:")
    st.image("qtdeAlunosIdadeGen.png", width=500)


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
    st.image("images/qtdeAlunosIdadeGen.png", width=500)
    st.markdown('<p style="text-align: justify;">Baseado no indicador (INDE - Índice de Desenvolvimento Educacional 2,4 - 9,3) a média dos índices apurados foram em torno de 7 para os alunos que são atendidos pela Passos Mágicos, que por sua vez são classificados em  fases (0 - 9 e Alfa) e intervalos de classificação baseados pelo INDE e seguem a nomenclatura de pedras (Ametista, Ágata, Topázio, Quartzo e Sem Pedra):</p>', unsafe_allow_html = True)
    st.image("images/qtdeAlunosPedra.png", width=500)
    st.markdown('<p style="text-align: justify;">Diante dos dados apurados notamos que alguns índices tiveram pequenas variações conforme a estratégia educacional aplicada. Como segue:</p>', unsafe_allow_html = True)
    st.image("images/indices.png", width=500)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">IAA (Indicador de autoavaliação): </span>Se mantém alta conforme pesquisa de satisfação realizada com os alunos com 6 questões, relacionadas a si mesmo, família e a comunidade.</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">IAN (Indicador de defasagem de nível): </span>Houve uma ligeira melhora comparando com a média da instituição diante do aproveitamento dos alunos.</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">IDA (Indicador de desenvolvimento acadêmico): </span>Diante os esforços empregados nos anos analisados reflete um avanço na evolução do aproveitamento dos alunos.</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">IEG (Indicador de engajamento): </span>Conforme relatórios fornecidos vimos que em sua maioria (acima de 80%) do alunos fizeram todas as provas refletindo seu engajamento.</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">IPP (Indicador psicopedagógico): </span>Se manteve estável para a evolução cognitiva e pedagógica.</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">IPS (Indicador Psicossocial): </span>Houve uma queda em 2023, entretanto, após muito esforço foi otimizado o atendimento psicológico envolvendo o aluno e a sociedade que o rodeia.</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">IPV (Indicador ponto de virada): </span>Onde são observadas as aptidões dos alunos e manteve-se estável nos anos observados.</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<p style="text-align: justify;">Novamente nos dados obtidos evidenciam diversas amostras de evasão e seus fatores adversos, como descrevemos a seguir:</p>', unsafe_allow_html = True)    
    st.markdown('<p style="text-align: justify;">Vimos que a taxa de evasão é baixa dentre os alunos mais novos e se acentua até o ápice dos 13 anos</p>', unsafe_allow_html = True)
    st.image("images/evPorIdade.png", width=500)
    st.markdown('<p style="text-align: justify;">O gênero feminino é o que mais teve evasão nos programas da ONG, sendo reflexo de inúmeras causas que trouxemos ao longo do estudo.</p>', unsafe_allow_html = True)
    st.image("images/evPorGen.png", width=500)



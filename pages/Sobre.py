# Importação da biblioteca streamlit
import streamlit as st
from auxiliar import apply_custom_style


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
    if st.button("MVP"):
        st.switch_page("pages/MVP.py")
with cols[3]:
    if st.button("Conclusão"):
        st.switch_page("pages/Conclusao.py")
with cols[4]:
    if st.button("Sobre"):
        st.switch_page("pages/Sobre.py")
st.header("", divider="gray")

# Configuração da página
#st.set_page_config(page_title= 'Projeto ML preço do Petróleo', layout='wide', page_icon= '📊')

# Título da página
st.title('ONG - Passos Mágicos :woman-woman-girl-boy:')

# Descrição do projeto
st.markdown('### O Problema')
st.markdown('<p style="text-align: justify;">A ONG Passos Mágicos enfrenta um desafio delicado e crucial: como ampliar o impacto positivo em crianças e jovens em situação de vulnerabilidade, quando as dificuldades em medir de forma clara os efeitos de suas ações tornam esse processo complexo.<br />Cada aluno traz consigo uma realidade única, com diferentes contextos socioeconômicos e emocionais, o que torna difícil acompanhar seu progresso de maneira personalizada. Ela precisa de novas ferramentas para entender melhor os dados e ajustar suas estratégias, garantindo que cada criança receba o apoio e as oportunidades que merece, para que possa crescer e superar os obstáculos de sua jornada.</p>', unsafe_allow_html = True)
#st.markdown('- Análise Exploratória')
#st.markdown('- Desenvolvimento dashboard com os insights abaixo na ferramenta Streamlit')
#st.markdown('- Desenvolvimento de um modelo Machine Learning')
st.markdown('### Objetivo')
st.markdown('<p style="text-align: justify;">Este projeto visa utilizar análises preditivas para avaliar como as ações da ONG Passos Mágicos impactam o desempenho e o desenvolvimento dos estudantes.<br />O objetivo é identificar padrões e relações nos dados educacionais, socioeconômicos e comportamentais, para compreender como diferentes fatores influenciam tanto o sucesso quanto as dificuldades dos alunos.<br />Com esses insights, a ONG poderá aprimorar suas abordagens e programas, ajustando-os para atender de forma mais eficaz às necessidades individuais dos alunos e potencializar os benefícios em suas trajetórias educacionais.</p>', unsafe_allow_html = True)

# Visualização da fluxo de trabalho do projeto
#st.markdown('## Fluxo de Trabalho')
#miro_url = 'https://miro.com/app/live-embed/uXjVN1YW9H4=/?moveToViewport=-1349,-868,3306,1721&embedId=214115551426'
#st.markdown(f'<iframe width="80%" height="600" src="{miro_url}" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" #allowfullscreen></iframe>', unsafe_allow_html=True)

# Links
#st.markdown('## Links Úteis')
#st.markdown('##### Fontes de dados')
#st.markdown('Link acessado em 20 novembro 2024   ' '[A história do petróleo no Brasil](https://www.gov.br/anp/pt-br/acesso-a-informacao/institucional/historia-petroleo-brasil)')
#st.markdown('Link acessado em 20 novembro 2024   ' '[Qual é a origem do petróleo?](https://www.bbc.com/portuguese/articles/cnk0e0yydelo)')
#st.markdown('Link acessado em 20 novembro 2024   ' '[OPEC]( https://www.opec.org/opec_web/en/index.htm)')
#st.markdown('Link acessado em 20 novembro 2024   ' '[OpenAI. “O Chat GPT é uma ferramenta de processamento de linguagem natural orientada por IA, que possibilita conversas semelhantes às humanas com o #chatbot](https://openai.com/blog/chat-gpt-3-launch/)')
#st.markdown('Link acessado em 20 novembro 2024   ' '[Geopolítica do Petróleo](https://mundoeducacao.uol.com.br/geografia/geopolitica-petroleo.html)') 
#st.markdown('Link acessado em 20 novembro 2024   ' '[Nos Bastidores da Terra: Geóloga Explica a Formação do #Petróleo](https://super.abril.com.br/coluna/deriva-continental/nos-bastidores-da-terra-geologa-explica-a-formacao-do-petroleo#google_vignette)')
#st.markdown('Link acessado em 20 novembro 2024   ' '[Organização dos Países Exportadores de Petróleo](https://pt.wikipedia.org/wiki/Organiza%C3%A7%C3%A3o_dos_Pa%C3%ADses_Exportadores_de_Petr%C3%B3leo)')
#st.markdown('Link acessado em 20 novembro 2024   ' '[Agência Internacional de Energia](https://pt.wikipedia.org/wiki/Ag%C3%AAncia_Internacional_de_Energia)')  
#st.markdown('Link acessado em 20 novembro 2024   ' '[Oito motivos para a queda do preço do  petróleo](https://www.dw.com/pt-br/oito-motivos-para-a-queda-do-pre%C3%A7o-do-petr%C3%B3leo/a-19051686)') 

st.markdown('<p style="text-align: justify;"><br /><br /><br /><br /></p>', unsafe_allow_html = True)



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


# Equipe do projeto
st.write("### Equipe FIAP - 5DTAT - Grupo 79")
#st.markdown('<h5>Equipe FIAP - 5DTAT - Grupo 10</h5>', unsafe_allow_html = True)
st.markdown('#### Jhonny da Silva Mineu - RM 355135')
st.markdown('#### Marina Mendez Araujo - RM 355100')
st.markdown('#### Volmir Moderoso Santos - RM 355589')

## Rodapé
st.markdown("---")

st.markdown('''<div class="center">
                    <a target="_self" href="#286ba15e">
                        <button class="back-to-top">
                            Voltar ao topo
                        </button>
                    </a>
                </div>''', unsafe_allow_html=True)
		




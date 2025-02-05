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
tabs_titles_2= ["Como funciona a Passos","Evasão de alunos na Passos","Indicadores","Modelo"]
tabs_2 = st.tabs(tabs_titles_2)

# Tab Como funciona a Passos
with tabs_2[0]: 
    st.header("Como funciona a Passos Mágicos")
    st.markdown("")
    colunas_1 = st.columns(2)
    with colunas_1 [0]:

        with st.container(border=True):
            st.markdown("""
                        <p style='text-align: justify;'>A Passos Mágicos tem como objetivo acelerar a ascensão social de crianças e jovens do município de Embu Guaçu através da educação.
                         É efetuada um processo seletivo visando garantir a dignidade e a autoestima com o intuito de promover a inclusão social ativa. É efetuada a divulgação das vagas na comunidade, é aplicada uma prova de sondagem aos interessados, aos selecionados é feita uma entrevista com psicologos, pedagogos e assistentes sociais. Após deliberarem analisam o perfil socioeconomicos para direcionar o conteudo e por fim a matricula.</p>""", unsafe_allow_html=True)


    with colunas_1 [1]:
                st.image("images/borda.png",width=300)


    colunas_2 = st.columns(2, gap="large")

 

# TAB Alunos Impactados
with tabs_2[1]: 
    st.header("Evasão de alunos na Passos Mágicos")

    st.markdown("""
                <p style='text-align: justify;'>Com base na análise realizada, iniciamos nosso estudo com um panorama mais detalhado sobre os alunos da ONG Passos Mágicos
                <br><br>
                </p>""", unsafe_allow_html=True)

    colunas_3 = st.columns(2, gap="large")
    
    with colunas_3 [0]:
        st.markdown( '#### Faixa etária')
        st.markdown('<p style="text-align: justify;">Iniciando pela faixa etária, ao analisarmos a informação, o gráfico abaixo indica que a evasão é mais expressiva entre os alunos de 10 a 18 anos, com um aumento notável na faixa etária de 12 a 13 anos. A partir dos 14 anos, observa-se uma leve tendência de queda na taxa de evasão.<br><br></p>', unsafe_allow_html = True)
        st.image("images/ev_idade.png",caption="Evasão por Idade", width=600)

        st.markdown( '#### Gênero')
        st.markdown('<p style="text-align: justify;">Ao analisar o gênero dos alunos da ONG, representado por feminino e masculino, observa-se que as meninas apresentam uma taxa de evasão mais elevada em comparação aos meninos. Esse fenômeno pode ser atribuído a diversos fatores, como as responsabilidades domésticas e o cuidado com a família, o casamento precoce e a gravidez na adolescência, violência de gênero e o assédio escolar, entre outros aspectos.<br><br></p>', unsafe_allow_html = True)
        st.image("images/ev_genero.png",caption="Evasão por Gênero", width=600)		

        st.markdown( '#### Instituição de Ensino')
        st.markdown('<p style="text-align: justify;">A instituição de ensino é um fator crucial para a análise da evasão escolar. De acordo com os dados, as escolas públicas apresentam o maior número de alunos que abandonaram os estudos.<br><br></p>', unsafe_allow_html = True)
        st.image("images/ev_ensino.png",caption="Evasão por Instituição de ensino", width=600)

        st.markdown( '#### Permanência na Passos Mágicos')
        st.markdown('<p style="text-align: justify;">O tempo de permanência dos alunos na ONG Passos Mágicos também se revelou um dado importante para nossa análise, fornecendo informações valiosas para a instituição. Observamos que os maiores índices de evasão ocorrem entre os alunos que não completaram 1 ano, bem como entre aqueles com 1 e 3 anos de permanência. Por outro lado, alunos com 2 anos na Passos Mágicos apresentam uma taxa de evasão menor em comparação aos demais períodos.<br><br></p>', unsafe_allow_html = True)
        st.image("images/ev_tempo.png",caption="Evasão por Permanência no PM", width=600)	

        st.markdown( '#### Fase')
        st.markdown('<p style="text-align: justify;">A Fase está associada ao nível de aprendizado do aluno, com a fase 0 correspondendo à alfabetização e a fase 7 representando o 3º ano do ensino médio. Nesse contexto, as fases 2 e 3, que correspondem ao 5º ao 8º ano, apresentam o maior número de alunos desistentes de continuar no programa. Esse dado está relacionado ao primeiro gráfico apresentado, no qual observamos que a faixa etária de 10 a 13 anos é a que registra a maior taxa de evasão escolar.<br><br></p>', unsafe_allow_html = True)
        st.image("images/ev_fase.png",caption="Evasão por Fase", width=600)	
        st.markdown('<p style="text-align: justify;">Isso pode estar relacionado ao fato de que, entre os 10 e 13 anos, os alunos vivenciam uma fase de transição da infância para a adolescência, marcada por mudanças físicas e emocionais significativas. Esse processo pode gerar confusão e insegurança. A busca por identidade e a pressão para se encaixar socialmente podem resultar em desinteresse pela escola, especialmente se o ambiente escolar não oferecer o apoio necessário.Além disso, fatores como dificuldades de desafios acadêmicos, responsabilidades familiares e a falta de perspectivas de futuro também podem contribuir para a evasão nesse período.<br><br></p>', unsafe_allow_html = True)		
		
# TAB de Indicadores      
with tabs_2[2]: 
    st.header("Indicadores Passos Mágicos")
    st.markdown('''<p style='text-align: justify;'>Os dados que serão mostrados abaixo tem a finalidade de demonstrar o impacto da Passos Mágicos no sistema educacional e nos jovens da região de Embu-Guaçu.
                <br><br>
                </p>''',unsafe_allow_html=True)
    colunas_3 = st.columns(2)
    with colunas_3 [0]:
        st.image("images/indicador_avaliacao.png",caption="Indicadores de Avaliação, descrição e seus pesos - Fonte:PEDE Pontos importantes", width=600)
 #   with colunas_3 [1]:
        st.image("images/indicador_conselho.png",caption="Indicadores de Conselho, descrição e seus pesos - Fonte:PEDE Pontos importantes", width=600)
 #	with colunas_3 [2]:
    st.markdown('<p style="text-align: justify;">A pedra é a classificação do aluno, baseado no número do INDE (Índice do Desenvolvimento Educacional), que é uma métrica de processo avaliativo geral do aluno. O conceito de classificação é dado por:</p>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Quartzo – </span>2,405 a 5,506</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Ágata – </span>5,506 a 6,868</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Ametista – </span>6,868 a 8,230</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Topázio – </span>8,230 a 9,294</li></p></ul>', unsafe_allow_html = True)
    st.image("images/pedraINDE.png",caption="Faixas de desempenho Pedra-conceito INDE - Fonte:PEDE Pontos importantes", width=600)
    st.markdown('<p style="text-align: justify;">Essas quatro pedras, que simbolizam etapas de uma jornada de aprendizado e de desenvolvimento educacional, indicarão a posição de cada estudante em relação ao desempenho geral de todos na pesquisa avaliativa PEDE 2021.Analisando a evasão por Pedra, é possível identificar que a pedra Ametista e Ágata, são as que mais possuem alunos na situação de evasão, onde há alunos com valores na média do INDE.</p>', unsafe_allow_html = True)
    st.image("images/pedragrf.png",caption="Evasão por pedras", width=600)
	
# Tab Modelo
with tabs_2[0]: 
    st.header("Modelo")
    st.markdown("")
    colunas_1 = st.columns(2)
    with colunas_1 [0]:	
	
## Rodapé
st.markdown("---")

st.markdown('''<div class="center">
                    <a target="_self" href="#e0b3b9e8">
                        <button class="back-to-top">
                            Voltar ao topo
                        </button>
                    </a>
                </div>''', unsafe_allow_html=True)
		


       

    

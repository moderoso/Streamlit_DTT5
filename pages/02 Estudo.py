# Importação das bibliotecas
import streamlit as st
from datetime import datetime 
import pandas as pd
from PIL import Image
from auxiliar import apply_custom_style
import joblib

from Funcoes import rodando_modelo # type: ignore



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

### Tabs da página inicial
tabs_titles_2= ["Estudo Evasão de alunos na Passos","Modelo","Indicadores"]
tabs_2 = st.tabs(tabs_titles_2)


# TAB Evasão de alunos na Passos Mágicos
with tabs_2[0]: 
    st.header("Estudo Evasão de alunos na Passos Mágicos")
    st.markdown("""
                <p style='text-align: justify;'>Com base na análise realizada, iniciamos nosso estudo com um panorama mais detalhado sobre os alunos da ONG Passos Mágicos
                <br><br>
                </p>""", unsafe_allow_html=True)

    colunas_3 = st.columns(2, gap="large")
    
    with colunas_3 [0]:
        st.markdown( '#### Faixa etária')
        st.markdown('<p style="text-align: justify;">Iniciando pela faixa etária, ao analisarmos a informação, o gráfico abaixo indica que a evasão é mais expressiva entre os alunos de 10 a 18 anos, com um aumento notável na faixa etária de 12 a 13 anos. A partir dos 14 anos, observa-se uma leve tendência de queda na taxa de evasão.<br><br></p>', unsafe_allow_html = True)
        st.image("images/ev_idade.png",caption="Evasão por Idade", width=500)

        st.markdown( '#### Gênero')
        st.markdown('<p style="text-align: justify;">Ao analisar o gênero dos alunos da ONG, representado por feminino e masculino, observa-se que as meninas apresentam uma taxa de evasão mais elevada em comparação aos meninos. Esse fenômeno pode ser atribuído a diversos fatores, como as responsabilidades domésticas e o cuidado com a família, o casamento precoce e a gravidez na adolescência, violência de gênero e o assédio escolar, entre outros aspectos.<br><br></p>', unsafe_allow_html = True)
        st.image("images/ev_genero.png",caption="Evasão por Gênero", width=500)		

        st.markdown( '#### Instituição de Ensino')
        st.markdown('<p style="text-align: justify;">A instituição de ensino é um fator crucial para a análise da evasão escolar. De acordo com os dados, as escolas públicas apresentam o maior número de alunos que abandonaram os estudos.<br><br></p>', unsafe_allow_html = True)
        st.image("images/ev_ensino.png",caption="Evasão por Instituição de ensino", width=500)

        st.markdown( '#### Permanência na Passos Mágicos')
        st.markdown('<p style="text-align: justify;">O tempo de permanência dos alunos na ONG Passos Mágicos também se revelou um dado importante para nossa análise, fornecendo informações valiosas para a instituição. Observamos que os maiores índices de evasão ocorrem entre os alunos que não completaram 1 ano, bem como entre aqueles com 1 e 3 anos de permanência. Por outro lado, alunos com 2 anos na Passos Mágicos apresentam uma taxa de evasão menor em comparação aos demais períodos.<br><br></p>', unsafe_allow_html = True)
        st.image("images/ev_tempo.png",caption="Evasão por Permanência no PM", width=500)	

        st.markdown( '#### Fase')
        st.markdown('<p style="text-align: justify;">A Fase está associada ao nível de aprendizado do aluno, com a fase 0 correspondendo à alfabetização e a fase 7 representando o 3º ano do ensino médio. Nesse contexto, as fases 2 e 3, que correspondem ao 5º ao 8º ano, apresentam o maior número de alunos desistentes de continuar no programa. Esse dado está relacionado ao primeiro gráfico apresentado, no qual observamos que a faixa etária de 10 a 13 anos é a que registra a maior taxa de evasão escolar.<br><br></p>', unsafe_allow_html = True)
        st.image("images/ev_fase.png",caption="Evasão por Fase", width=500)	
        st.markdown('<p style="text-align: justify;">Isso pode estar relacionado ao fato de que, entre os 10 e 13 anos, os alunos vivenciam uma fase de transição da infância para a adolescência, marcada por mudanças físicas e emocionais significativas. Esse processo pode gerar confusão e insegurança. A busca por identidade e a pressão para se encaixar socialmente podem resultar em desinteresse pela escola, especialmente se o ambiente escolar não oferecer o apoio necessário.Além disso, fatores como dificuldades de desafios acadêmicos, responsabilidades familiares e a falta de perspectivas de futuro também podem contribuir para a evasão nesse período.<br><br></p>', unsafe_allow_html = True)		

	
# Tab Modelo
with tabs_2[1]: 
    st.header("Modelo")
    st.markdown("""
                <p style='text-align: justify;'>Para a construção da análise preditiva, foi escolhido dois modelos para serem treinados, o RandomForest e o XGBoost:
                <br></br>
                </p>""", unsafe_allow_html=True)

    colunas_3 = st.columns(2, gap="large")
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Random Forest: </span>Algoritmo de aprendizado de máquina baseado em conjuntos de árvores de decisão. Ele funciona criando várias árvores de decisão durante o treinamento e, em seguida, combinando suas previsões para melhorar a precisão do modelo e reduzir o risco de overfitting (ajuste excessivo aos dados).</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">XGBoost (Extreme Gradient Boosting): </span>É um algoritmo de aprendizado de máquina altamente eficiente e poderoso, utilizado principalmente para classificação e regressão. Ele é uma implementação otimizada do método de Gradient Boosting, que combina múltiplos modelos fracos (tipicamente árvores de decisão) para formar um modelo forte.</li></p></ul>', unsafe_allow_html = True)
    st.markdown( '#### Termos')
    st.markdown('<p style="text-align: justify;">Durante a análise dos modelos, iremos utilizar alguns termos e para facilitar o entendimento do que estamos descrevendo e abaixo há uma melhor explicação de cada termo:</p>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Precision: </span>A taxa de acerto entre as previsões positivas feitas pelo modelo e as reais positivas.</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Recall: </span>A taxa de acerto entre as reais positivas e as positivas corretamente identificadas pelo modelo.</li></p></ul>', unsafe_allow_html = True)	
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">F1-Score: </span>A média harmônica entre precisão e recall, usada para balancear esses dois aspectos.</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Support: </span> Quantidade de exemplos reais de cada classe no conjunto de dados de teste.</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Accuracy: </span> A proporção de acertos no total de previsões feitas.</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Macro Avg: </span>A média macro calcula a média simples de uma métrica (como precisão, recall ou F1-score) para todas as classes, sem levar em consideração o suporte de cada classe.</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Weighted Avg: </span>A média ponderada calcula a média das métricas (como precisão, recall ou F1-score), pesando cada classe de acordo com o número de exemplos (suporte) da classe no conjunto de teste.</li></p></ul>', unsafe_allow_html = True)	
	
    st.markdown( '#### Comparação dos modelos')
    st.markdown('<p style="text-align: justify;">Comparando o treinamento dos dois modelos, é possível obter as seguintes informações:</p>', unsafe_allow_html = True)	
    st.image("images/mod_random.png",caption="Modelo Random Forest", width=400)
    st.image("images/mod_XGBoost.png",caption="Modelo XGBoost", width=400)	
    st.markdown('<p style="text-align: justify;">O modelo RandomForest trouxe uma precisão, recall e f1-score de 93%, comparada com 78% do XGBoost, indicando que o RandomForest tem um bom equilíbrio entre precisão e recall, com uma média harmônica alta entre essas duas métricas. A pontuação sugere que o modelo é bastante eficiente em evitar erros (tanto falsos positivos quanto falsos negativos), e que está geralmente acertando nas suas previsões.</p>', unsafe_allow_html = True)
    st.image("images/mod_X_mod.png",caption="Modelo XGBoost x Modelo Random Forest", width=700)		


# TAB de Indicadores      
with tabs_2[2]: 
    st.header("Indicadores Passos Mágicos")
    st.markdown('''<p style='text-align: justify;'>Os dados que serão mostrados abaixo tem a finalidade de demonstrar o impacto da Passos Mágicos no sistema educacional e nos jovens da região de Embu-Guaçu.
                <br><br>
                </p>''',unsafe_allow_html=True)
    colunas_3 = st.columns(2)
    with colunas_3 [0]:
        st.image("images/indicador_avaliacao.png",caption="Indicadores de Avaliação, descrição e seus pesos - Fonte:PEDE Pontos importantes", width=500)
        st.image("images/indicador_conselho.png",caption="Indicadores de Conselho, descrição e seus pesos - Fonte:PEDE Pontos importantes", width=500)
    st.markdown('<p style="text-align: justify;">A pedra é a classificação do aluno, baseado no número do INDE (Índice do Desenvolvimento Educacional), que é uma métrica de processo avaliativo geral do aluno. O conceito de classificação é dado por:</p>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Quartzo – </span>2,405 a 5,506</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Ágata – </span>5,506 a 6,868</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Ametista – </span>6,868 a 8,230</li></p></ul>', unsafe_allow_html = True)
    st.markdown('<ul class="font-text-destaques"><p style="text-align: justify;"><li><span style="font-weight: bold">Topázio – </span>8,230 a 9,294</li></p></ul>', unsafe_allow_html = True)
    st.image("images/pedraINDE.png",caption="Faixas de desempenho Pedra-conceito INDE - Fonte:PEDE Pontos importantes", width=400)
    st.markdown('<p style="text-align: justify;">Essas quatro pedras, que simbolizam etapas de uma jornada de aprendizado e de desenvolvimento educacional, indicarão a posição de cada estudante em relação ao desempenho geral de todos na pesquisa avaliativa PEDE 2021.Analisando a evasão por Pedra, é possível identificar que a pedra Ametista e Ágata, são as que mais possuem alunos na situação de evasão, onde há alunos com valores na média do INDE.</p>', unsafe_allow_html = True)
    st.image("images/pedragrf.png",caption="Evasão por pedras", width=500)
	
## Rodapé
st.markdown("---")

st.markdown('''<div class="center">
                    <a target="_self" href="#e0b3b9e8">
                        <button class="back-to-top">
                            Voltar ao topo
                        </button>
                    </a>
                </div>''', unsafe_allow_html=True)
		

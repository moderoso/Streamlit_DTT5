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
    if st.button("MVP"):
        st.switch_page("pages/MVP.py")
with cols[3]:
    if st.button("Conclusão"):
        st.switch_page("pages/Conclusao.py")
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
tabs_titles_2= ["Quem Somos","Como funciona a Passos","Contexto","Modelo"]
tabs_2 = st.tabs(tabs_titles_2)


# TAB Quem Somos
with tabs_2[0]: 
    st.header("Quem Somos")
    st.markdown("")
    colunas_1 = st.columns(2)
    with colunas_1 [0]:
        with st.container(border=True):
            # Descrição Passos Magicos
            st.markdown('<p style="text-align: justify;">A Associação Passos Mágicos tem uma trajetória de 30 anos de atuação, trabalhando na transformação da vida de crianças e jovens de baixa renda os levando a melhores oportunidades de vida.A transformação, idealizada por Michelle Flues e Dimetri Ivanoff, começou em 1992, atuando dentro de orfanatos, no município de Embu-Guaçu.<br />Em 2016, depois de anos de atuação, decidem ampliar o programa para que mais jovens tivessem acesso a essa fórmula mágica para transformação que inclui: educação de qualidade, auxílio psicológico/psicopedagógico, ampliação de sua visão de mundo e protagonismo. Passaram então a atuar como um projeto social e educacional, criando assim a Associação Passos Mágicos.<br />A ONG Passos Mágicos é uma organização dedicada a transformar vidas por meio da educação e do acolhimento de crianças e jovens em situação de vulnerabilidade. Com um olhar atento às necessidades de cada estudante, a ONG oferece mais do que apenas ensino – ela proporciona um espaço seguro onde cada criança pode se sentir valorizada, respeitada e motivada a alcançar seu potencial.<br />A missão da Passos Mágicos é movida pela crença de que, para que um aluno realmente prospere, é necessário atender não só às suas necessidades acadêmicas, mas também ao seu bem-estar emocional, social e psicológico.<br /> A ONG se dedica a ser uma rede de apoio, não só no processo de aprendizagem, mas em todo o desenvolvimento do jovem, ajudando-o a superar desafios diários, sejam eles de ordem pessoal, familiar ou comunitária.<r />Em tempos de tantas desigualdades, a Passos Mágicos se destaca, oferecendo oportunidades para que cada criança e jovem possa dar os passos necessários para um futuro mais digno e promissor.Por isso, a Passos Mágicos busca entender e adaptar suas ações para apoiar de forma personalizada, promovendo um ambiente acolhedor onde a confiança e a autoestima possam florescer.</p>', unsafe_allow_html = True)		

    with colunas_1 [1]:
                st.image("images/borda.png",width=300)


    colunas_2 = st.columns(2, gap="large")




# Tab Como funciona a Passos
with tabs_2[1]: 
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

 

		
# TAB de Contexto 
with tabs_2[2]: 
    st.markdown("")
    colunas_1 = st.columns(2)
    with colunas_1 [0]:
        with st.container(border=True):
            st.markdown('### Contexto')
            st.markdown('<p style="text-align: justify;">O abandono escolar é uma realidade no Brasil, sendo um problema significativo, onde muitos jovens são afetados por diversos fatores, como por exemplo, problemas familiares, dificuldades financeiras, falta de motivação, falta de apoio educacional adequado, gravidez na adolescência, dificuldades de aprendizagem, violência nas comunidades, entre outros, especialmente em áreas rurais e periféricas.Segundo o censo de 2022 escolar do INEP (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira) de 2022, mostra que a situação é preocupante, com muitos jovens fora da escola e que não completaram seus estudos, principalmente nas faixas etárias mais altas. Alguns desses dados são:</p>', unsafe_allow_html = True)
            st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Evasão por nível de ensino:</span> Em 2021, a taxa de abandono escolar no Ensino Fundamental foi de cerca de 1,9% no Brasil. Já no Ensino Médio, a taxa de abandono é mais alarmante, onde no mesmo ano, cerca de 11,5% dos estudantes abandonaram a escola no Brasil. Este número é significativamente mais alto do que no Ensino Fundamental.</p>', unsafe_allow_html = True)
            st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Desigualdade Regional:</span> A evasão escolar no Brasil também varia bastante entre as regiões, com os estados do Norte (12%) e Nordeste (15%) enfrentando as maiores taxas de abandono no ensino médio, enquanto as regiões Sul (8%) e Sudeste (9%) apresentam índices mais baixos.</p>', unsafe_allow_html = True)
            st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Fortes impactos da Pandemia de COVID-19:</span> De acordo com o IBGE (Instituto Brasileiro de Geografia e Estatística), cerca de 1,4 milhão de alunos abandonaram a escola entre 2020 e 2021, com grande impacto nas áreas mais vulneráveis. O acesso desigual à tecnologia gerou um abismo ainda maior na permanência escolar, com jovens das classes mais baixas sendo os mais afetados.</p>', unsafe_allow_html = True)
            st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Taxas de Repetência: </span> A repetência escolar também tem uma relação direta com a evasão. Quando os alunos repetem o ano, muitos acabam desistindo de estudar, especialmente no Ensino Médio. O Brasil tem uma das maiores taxas de repetência da América Latina, com cerca de 13,6% no Ensino Médico em 2021.</p>', unsafe_allow_html = True)
            st.markdown('<p style="text-align: justify;">A situação tem causado um impacto significativo no futuro educacional e social desses jovens, demandando ações urgentes e políticas públicas voltadas à inclusão e à permanência escolar, áreas com as quais a ONG Passos Mágicos possui uma estreita conexão. Considerando a gravidade do tema, que pode acarretar consequências sérias tanto para os indivíduos quanto para o país, nosso objetivo é apresentar um modelo preditivo relacionado à evasão escolar, visando aprimorar as previsões e estratégias da ONG.</p>', unsafe_allow_html = True)

    with colunas_1 [1]:
                st.image("images/borda.png",width=300)


    colunas_2 = st.columns(2, gap="large")

	
# Tab Modelo
with tabs_2[3]: 
    st.header("Modelo")
    st.markdown("""
                <p style='text-align: justify;'>Para a construção da análise preditiva, foi escolhido dois modelos para serem treinados, o RandomForest e o XGBoost:
                <br><br>
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
	
## Rodapé
st.markdown("---")

st.markdown('''<div class="center">
                    <a target="_self" href="#e0b3b9e8">
                        <button class="back-to-top">
                            Voltar ao topo
                        </button>
                    </a>
                </div>''', unsafe_allow_html=True)
		


       

    

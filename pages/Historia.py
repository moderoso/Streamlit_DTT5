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
    if st.button("História"):
        st.switch_page("pages/Historia.py")
with cols[4]:
    if st.button("Sobre"):
        st.switch_page("pages/Sobre.py")
st.header("", divider="gray")

# Descrição Passos Magicos
st.markdown('### Quem Somos')
st.markdown('<p style="text-align: justify;">A Associação Passos Mágicos tem uma trajetória de 30 anos de atuação, trabalhando na transformação da vida de crianças e jovens de baixa renda os levando a melhores oportunidades de vida.A transformação, idealizada por Michelle Flues e Dimetri Ivanoff, começou em 1992, atuando dentro de orfanatos, no município de Embu-Guaçu.<br />Em 2016, depois de anos de atuação, decidem ampliar o programa para que mais jovens tivessem acesso a essa fórmula mágica para transformação que inclui: educação de qualidade, auxílio psicológico/psicopedagógico, ampliação de sua visão de mundo e protagonismo. Passaram então a atuar como um projeto social e educacional, criando assim a Associação Passos Mágicos.<br />A ONG Passos Mágicos é uma organização dedicada a transformar vidas por meio da educação e do acolhimento de crianças e jovens em situação de vulnerabilidade. Com um olhar atento às necessidades de cada estudante, a ONG oferece mais do que apenas ensino – ela proporciona um espaço seguro onde cada criança pode se sentir valorizada, respeitada e motivada a alcançar seu potencial.<br />A missão da Passos Mágicos é movida pela crença de que, para que um aluno realmente prospere, é necessário atender não só às suas necessidades acadêmicas, mas também ao seu bem-estar emocional, social e psicológico.<br /> A ONG se dedica a ser uma rede de apoio, não só no processo de aprendizagem, mas em todo o desenvolvimento do jovem, ajudando-o a superar desafios diários, sejam eles de ordem pessoal, familiar ou comunitária.<r />Em tempos de tantas desigualdades, a Passos Mágicos se destaca, oferecendo oportunidades para que cada criança e jovem possa dar os passos necessários para um futuro mais digno e promissor.Por isso, a Passos Mágicos busca entender e adaptar suas ações para apoiar de forma personalizada, promovendo um ambiente acolhedor onde a confiança e a autoestima possam florescer.</p>', unsafe_allow_html = True)

st.markdown('### Contexto')
st.markdown('<p style="text-align: justify;">O abandono escolar é uma realidade no Brasil, sendo um problema significativo, onde muitos jovens são afetados por diversos fatores, como por exemplo, problemas familiares, dificuldades financeiras, falta de motivação, falta de apoio educacional adequado, gravidez na adolescência, dificuldades de aprendizagem, violência nas comunidades, entre outros, especialmente em áreas rurais e periféricas.Segundo o censo de 2022 escolar do INEP (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira) de 2022, mostra que a situação é preocupante, com muitos jovens fora da escola e que não completaram seus estudos, principalmente nas faixas etárias mais altas. Alguns desses dados são:</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Evasão por nível de ensino:</span> Em 2021, a taxa de abandono escolar no Ensino Fundamental foi de cerca de 1,9% no Brasil. Já no Ensino Médio, a taxa de abandono é mais alarmante, onde no mesmo ano, cerca de 11,5% dos estudantes abandonaram a escola no Brasil. Este número é significativamente mais alto do que no Ensino Fundamental.</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Desigualdade Regional:</span> A evasão escolar no Brasil também varia bastante entre as regiões, com os estados do Norte (12%) e Nordeste (15%) enfrentando as maiores taxas de abandono no ensino médio, enquanto as regiões Sul (8%) e Sudeste (9%) apresentam índices mais baixos.</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Fortes impactos da Pandemia de COVID-19:</span> De acordo com o IBGE (Instituto Brasileiro de Geografia e Estatística), cerca de 1,4 milhão de alunos abandonaram a escola entre 2020 e 2021, com grande impacto nas áreas mais vulneráveis. O acesso desigual à tecnologia gerou um abismo ainda maior na permanência escolar, com jovens das classes mais baixas sendo os mais afetados.</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Taxas de Repetência: </span> A repetência escolar também tem uma relação direta com a evasão. Quando os alunos repetem o ano, muitos acabam desistindo de estudar, especialmente no Ensino Médio. O Brasil tem uma das maiores taxas de repetência da América Latina, com cerca de 13,6% no Ensino Médico em 2021.</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;">A situação tem causado um impacto significativo no futuro educacional e social desses jovens, demandando ações urgentes e políticas públicas voltadas à inclusão e à permanência escolar, áreas com as quais a ONG Passos Mágicos possui uma estreita conexão. Considerando a gravidade do tema, que pode acarretar consequências sérias tanto para os indivíduos quanto para o país, nosso objetivo é apresentar um modelo preditivo relacionado à evasão escolar, visando aprimorar as previsões e estratégias da ONG.</p>', unsafe_allow_html = True)

## Rodapé
st.markdown("---")

st.markdown('''<div class="center">
                    <a target="_self" href="#quem-somos">
                        <button class="back-to-top">
                            Voltar ao topo
                        </button>
                    </a>
                </div>''', unsafe_allow_html=True)


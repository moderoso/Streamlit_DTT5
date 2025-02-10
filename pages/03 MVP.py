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

# Título da página
#st.title('ONG - Passos Mágicos :woman-woman-girl-boy:✨')

### Tabs da página inicial
tabs_titles_2= ["Entradas de Dados"]
tabs_2 = st.tabs(tabs_titles_2)

# TAB Entrada de dados
with tabs_2[0]: 
    st.header("Entrada de Dados: Manual ou Upload de Arquivo")
    st.markdown("")
    colunas_3 = st.columns(1, gap="large")
    with colunas_3 [0]:
        scaler = joblib.load('db/scaler.pkl')
        modelo_carregado = joblib.load("db/modelo_evasao.pkl")
        # Criando um botão de escolha
        escolha = st.radio("Como deseja inserir os dados?", ("Upload de Excel", "Entrada Manual"))

        try:
            # Se o usuário escolher "Upload de Excel"
            if escolha == "Upload de Excel":
               ex = pd.read_excel('db/exemplo.xlsx',sheet_name='Planilha1')
               # Exibe o DataFrame
               st.write("### Exemplo de layout do arquivo:")

               st.markdown('<p style="text-align: justify;">A tabela abaixo é um exemplo de como os dados e quais colunas devem estar no arquivo para que o modelo consiga prever a probabilidade de evasão do aluno. O modelo retornará o mesmo arquivo passado, mas acrescentará duas colunas, de probabilidade de evasão e o resultado final da previsão ("Evadir" ou "Não evadir").</p>', unsafe_allow_html = True)
               st.dataframe(ex)
               # Título do aplicativo
               st.write("### Upload de Arquivo Excel:")

               # Criando o widget de upload
               uploaded_file = st.file_uploader("Faça upload do seu arquivo Excel", type=["xlsx"])

               # Verifica se um arquivo foi enviado
               if uploaded_file is not None:
                  # Lendo o arquivo Excel como DataFrame
                  df = pd.read_excel(uploaded_file)
   
                  # Exibe o DataFrame
                  st.write("### Resultado de Previsão:")

                  rodando_modelo(modelo_carregado,scaler,df,tipo='Massivo')
        
            # Se o usuário escolher "Entrada Manual"
            else:
                st.write("### Insira os dados manualmente:")

                ano_atual =  datetime.now().year

                #Adicionando inputs do Usuario
                fase = st.number_input("Insira um número 0 - 7", max_value=7, min_value=0)
                idade = st.slider("Insira a idade", value=10, min_value=6, max_value=26)
                genero = st.radio("Selecione o Genero", ["Masculino", "Feminino"]) 
                ano_pm = st.slider("Insira anos na Passos Mágicos", value=1, min_value=0, max_value=7)
                intituicao_ensino = st.selectbox("Selecione a Instituição de Ensino",["Escola Pública", "Escola Privada", "Já Formado", "Outro"])
                pedra = st.selectbox("Selecione a Pedra",["Ametista", "Topázio", "Ágata", "Quartzo","Outro"])
                inde = st.number_input("INDE 0 - 10", max_value=10.0, min_value=1.0, step=0.1, format="%.1f" )
                iaa = st.number_input("IAA 0 - 10",  max_value=10.0, min_value=1.0, step=0.1, format="%.1f" )
                ieg = st.number_input("IEG 0 - 10", max_value=10.0, min_value=1.0, step=0.1, format="%.1f" )
                ips = st.number_input("IPS 0 - 10", max_value=10.0, min_value=1.0, step=0.1, format="%.1f" )
                ida = st.number_input("IDA 0 - 10", max_value=10.0, min_value=1.0, step=0.1, format="%.1f" )
                ipv = st.number_input("IPV 0 - 10", max_value=10.0, min_value=1.0, step=0.1, format="%.1f" )
                ian = st.number_input("IAN 0 - 10", max_value=10.0, min_value=1.0, step=0.1, format="%.1f" )
                ipp = st.number_input("IPP 0 - 10", max_value=10.0, min_value=1.0, step=0.1, format="%.1f" )
                defas = st.selectbox("Nível defasagem",["Em Fase", "Moderada", "Severa"])

                respostas = {'Fase' : fase,
                        'Idade' : idade,
                            'Gênero' : genero,
                            'Anos PM': ano_pm,
                            'Instituição de Ensino': intituicao_ensino,
                            'Pedra': pedra,
                            'INDE': inde,
                            'IAA': iaa,
                            'IEG': ieg,
                            'IPS': ips,
                            'IDA': ida,
                            'IPV': ipv,
                            'IAN': ian,
                            'IPP': ipp,
                            'Defasagem': defas}
                df = pd.DataFrame(data=[respostas])

                print(df.info())

                if st.button("Prever"):
                    resultado = rodando_modelo(modelo_carregado, scaler, df, tipo='Manual')
        except:
            st.error('Ops, ocorreu um erro!', icon="🚨")
        		
## Rodapé
st.markdown("---")

st.markdown('''<div class="center">
                    <a target="_self" href="#entrada-de-dados-manual-ou-upload-de-arquivo">
                        <button class="back-to-top">
                            Voltar ao topo
                        </button>
                    </a>
                </div>''', unsafe_allow_html=True)
		


       

    




import pandas as pd
from datetime import datetime
import streamlit as st

def rodando_modelo(model,sc,df):
    ano_atual = datetime.now().year

    colunas_df = ['Fase', 'Ano Nascimento', 'Idade', 'Ano Ingresso', 'Anos PM', 'INDE',
       'IAA', 'IEG', 'IPS', 'IDA', 'IPV', 'IAN', 'IPP', 'Gênero_Feminino',
       'Gênero_Masculino', 'Instituição de Ensino_Desconhecido',
       'Instituição de Ensino_Escola Privada',
       'Instituição de Ensino_Escola Pública',
       'Instituição de Ensino_Já formado', 'Instituição de Ensino_Outro',
       'Pedra_Ametista', 'Pedra_Desconhecido', 'Pedra_Quartzo',
       'Pedra_Topázio', 'Pedra_Ágata', 'Defasagem_Em Fase',
       'Defasagem_Moderada', 'Defasagem_Severa']
    
    # Criando coluna categorica com base na defasagem do aluno
    df['Idade'] = ano_atual - df['Ano Nascimento']
    df['Anos PM'] = ano_atual - df['Ano Ingresso']
    df['Defasagem'] = df['Defas'].apply(lambda x: "Em Fase" if x >= 0 else ("Moderada" if x < 0 and x <= -2 else "Severa"))
    df = df.drop(columns=['Defas','STATUS'])

    # Obtendo coluna de valores numéricos e categóricos
    colunas_numericas = df.select_dtypes(include=['number'])
    colunas_categoricas = df.select_dtypes(include=['object'])

    # Preenchendo os valores nulos nas colunas numéricas com a média
    df[colunas_categoricas.columns] = df[colunas_categoricas.columns].fillna('Desconhecido')
    df[colunas_numericas.columns] = df[colunas_numericas.columns].fillna(df[colunas_numericas.columns].mean())

    # Normalizando as colunas númericas do dataframe
    df[colunas_numericas.columns] = sc.transform(df[colunas_numericas.columns])

    # Aplicando o enconding nas colunas categoricas
    df = pd.get_dummies(df, columns=colunas_categoricas.columns, drop_first=False)

    df = df.reindex(columns=colunas_df, fill_value=False)

    previsao = model.predict(df)
    if previsao[0] == 0:
        print("🔹 Previsão: Não evadiu")
    else:
        print("🔹 Previsão: Evadiu")

def exibindo():
    st.warning('Prevendo', icon="⚠️")
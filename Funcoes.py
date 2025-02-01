import pandas as pd
from datetime import datetime
import streamlit as st
import io

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

    df_copy = df.copy(deep=True)
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

    if len(df['Fase']) > 1:
        df_copy = pd.concat([df, pd.Series(previsao, name='Previsao')], axis=1)
        df_copy['Previsao'] = df_copy['Previsao'].apply(lambda x: "Não evadiu" if x == 1 else "Evadiu")
 
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df_copy.to_excel(writer, index=False, sheet_name="Previsao")
        
        output.seek(0)  # Voltando ao início do buffer

        # Botão para download do arquivo Excel
        st.download_button(
            label="📥 Baixar Resultado Previsão",
            data=output,
            file_name="Previsao_Evasao.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
 
 
    else:
        if previsao[0] == 0:
            st.success("🔹 Previsão: Não evadiu")
        else:
            st.error("🔹 Previsão: Evadiu")

def exportando_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Previsao")
    
    output.seek(0)  # Voltando ao início do buffer

    # Botão para download do arquivo Excel
    st.download_button(
        label="📥 Baixar Resultado Previsão",
        data=output,
        file_name="Previsao_Evasao.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
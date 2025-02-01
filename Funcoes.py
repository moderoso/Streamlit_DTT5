import pandas as pd
from datetime import datetime
import streamlit as st
import io

def valid_model(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Previsao")
    
    output.seek(0)  # Voltando ao início do buffer

    # Botão para download do arquivo Excel
    st.download_button(
        label="📥 Baixar Resultado Previsão",
        data=output,
        file_name="Validacao_Modelo.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)


def rodando_modelo(model,sc,df,tipo):
    colunas_df = ['Fase', 'Ano Nascimento', 'Idade', 'Ano Ingresso', 'Anos PM', 'INDE',
       'IAA', 'IEG', 'IPS', 'IDA', 'IPV', 'IAN', 'IPP', 'Gênero_Feminino',
       'Gênero_Masculino', 'Instituição de Ensino_Desconhecido',
       'Instituição de Ensino_Escola Privada',
       'Instituição de Ensino_Escola Pública',
       'Instituição de Ensino_Já formado', 'Instituição de Ensino_Outro',
       'Pedra_Ametista', 'Pedra_Desconhecido', 'Pedra_Quartzo',
       'Pedra_Topázio', 'Pedra_Ágata', 'Defasagem_Em Fase',
       'Defasagem_Moderada', 'Defasagem_Severa']

    if tipo == 'Manual':
        ano_atual = datetime.now().year
        
        df['Idade'] = ano_atual - df['Ano Nascimento']
        df['Anos PM'] = ano_atual - df['Ano Ingresso']

        colunas_num = ['Fase', 'Ano Nascimento', 'Idade', 'Ano Ingresso', 'Anos PM', 'INDE',
       'IAA', 'IEG', 'IPS', 'IDA', 'IPV', 'IAN', 'IPP']

        for coluna in colunas_num:
            df[coluna] = pd.to_numeric(df[coluna], errors='coerce')

        #df = df.reindex(columns=colunas_num)

        # Separando colunas por tipo de dado
        colunas_numericas = df.select_dtypes(include=['number'])
        colunas_categoricas = df.select_dtypes(include=['object'])
        
        # Normalizando as colunas númericas do dataframe
        df[colunas_numericas.columns] = sc.transform(df[colunas_numericas.columns])

        df = pd.get_dummies(df, columns=colunas_categoricas.columns, drop_first=False)
        df = df.reindex(columns=colunas_df, fill_value=False)
        
        print(df)
        # Prenvendo o valor
        previsao = model.predict(df)
        st.dataframe(df)

        valid_model(df)


        st.dataframe(previsao)
        if previsao[0] == 1:
            st.success("🔹 Previsão: Não evadiu")
        else:
            st.error("🔹 Previsão: Evadiu")
    
    else:
        df_copy = df.copy(deep=True)

        # Separando colunas por tipo de dado
        colunas_numericas = df.select_dtypes(include=['number'])
        colunas_categoricas = df.select_dtypes(include=['object'])

        # Normalizando as colunas númericas do dataframe
        df[colunas_numericas.columns] = sc.transform(df[colunas_numericas.columns])

        # Aplicando o enconding nas colunas categoricas e preenchendo false nas demais
        df = pd.get_dummies(df, columns=colunas_categoricas.columns, drop_first=False)
        df = df.reindex(columns=colunas_df, fill_value=False)

        # Prenvendo o valor
        previsao = model.predict(df)

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









    
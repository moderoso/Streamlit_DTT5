import pandas as pd
import streamlit as st
import io
from sklearn.ensemble import RandomForestClassifier

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
    colunas_df = ['Fase', 'Idade', 'Anos PM', 'INDE',
       'IAA', 'IEG', 'IPS', 'IDA', 'IPV', 'IAN', 'IPP', 'Gênero_Feminino',
       'Gênero_Masculino', 'Instituição de Ensino_Escola Privada',
       'Instituição de Ensino_Escola Pública','Instituição de Ensino_Já formado', 
       'Instituição de Ensino_Outro',
       'Pedra_Ametista', 'Pedra_Outro', 'Pedra_Quartzo',
       'Pedra_Topázio', 'Pedra_Ágata', 'Defasagem_Em Fase',
       'Defasagem_Moderada', 'Defasagem_Severa']

    if tipo == 'Manual':

        # Definição das colunas numéricas
        colunas_num = ['Fase', 'Idade', 'Anos PM', 'INDE',
                    'IAA', 'IEG', 'IPS', 'IDA', 'IPV', 'IAN', 'IPP']

        # Convertendo as colunas numéricas para garantir o tipo correto
        for coluna in colunas_num:
            df[coluna] = pd.to_numeric(df[coluna], errors='coerce')

        # Separando colunas por tipo de dado
        colunas_numericas = df[colunas_num]  # Apenas as colunas numéricas definidas
        colunas_categoricas = df.select_dtypes(include=['object'])  # Pegando colunas categóricas

        # Aplicando normalização às colunas numéricas
        df[colunas_numericas.columns] = sc.transform(colunas_numericas)

        # Criando colunas dummies para as variáveis categóricas
        df = pd.get_dummies(df, columns=colunas_categoricas.columns, drop_first=False)

        # Garantindo que o DataFrame final tenha todas as colunas esperadas (preenchendo ausentes com False)
        df = df.reindex(columns=colunas_df, fill_value=False)

        # Fazendo a previsão e probabilidade de evasão
        probabilidades = model.predict_proba(df)[:, 1]
        previsao = model.predict(df)
        
        # Exibindo resultado da previsão
        if previsao[0] == 0:
            st.success(f"🔹 Previsão: Não evadir (Probabilidade de evasão: {probabilidades[0]*100:.2f}%)")
        else:
            st.error(f"🔹 Previsão: Evadir (Probabilidade de evasão: {probabilidades[0]*100:.2f}%)")
    
    else:
        df_copy = df.copy(deep=True)

        # Separando colunas por tipo de dado
        colunas_numericas = df_copy.select_dtypes(include=['number'])
        colunas_categoricas = df_copy.select_dtypes(include=['object'])

        # Normalizando as colunas númericas do dataframe
        df_copy[colunas_numericas.columns] = sc.transform(df_copy[colunas_numericas.columns])

        # Aplicando o enconding nas colunas categoricas e preenchendo false nas demais
        df_copy = pd.get_dummies(df_copy, columns=colunas_categoricas.columns, drop_first=False)
        df_copy = df_copy.reindex(columns=colunas_df, fill_value=False)

        # Fazendo a previsão e probabilidade de evasão
        probabilidades = model.predict_proba(df_copy)[:, 1]
        previsao = model.predict(df_copy)

        df = df.assign(ProbabilidadeEvasao=probabilidades,Previsao=previsao)
        df['Previsao'] = df['Previsao'].apply(lambda x: "Não evadir" if x == 0 else "Evadir")
        df['ProbabilidadeEvasao'] = df['ProbabilidadeEvasao'] * 100
        df['ProbabilidadeEvasao'] = df['ProbabilidadeEvasao'].apply(lambda x: f'{x:.1f}%')

        st.dataframe(df)
 
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









    
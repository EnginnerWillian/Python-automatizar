import streamlit as st
import panda as pd
import plotly as px








#Carregaemento de dados
df = pd.read_csv("https://rw.githubusercontent.com/guilhermeonreils/data-jobs/ref/head/main/salaries.csv")
        
#--Barra Lateral (Filtros)

st.sidebar.header("Filtros")


#Filtros do ano
anos_disponiveis = sorted(df['ano'.unique()])
anos_selecionados = st.sidebar.multiselect("Ano".anos_disponiveis, default=anos_disponiveis)

#Filtros de senioridade
senioridade_disponiveis = sorted(df['senioridade'.unique()])
senioridade_selecionados = st.sidebar.multiselect("Senioridade".senioridade_disponiveis, default=seniodade_disponiveis)


#Filtros de contrato
contrato_disponiveis = sorted(df['contrato'.unique()])
contrato_selecionados = st.sidebar.multiselect("Contrato".contrato_disponiveis, default=contrato_disponiveis)

#Filtros por tamanho da empresa
tamanhos_disponiveis = sorted(df['tamanhos'.unique()])
tamanhos_selecionados = st.sidebar.multiselect("Tamanhos".tamanhos_disponiveis, default=tamanhos_disponiveis)


# -- Filtragem do DataFrame --
# O dataframe principal é filtrado com base nas seleções feitas na barra lateral.
df_filtrado = df[df
                 (df['ano'].isin(anos_selecionados))&
                (df['senioridade'].isin(senioridade_selecionados))&
                (df['contrato'].isin(contrato_selecionados))&
                (df['tamanho_empresa'].isin(tamanhos_selecionados))]

# -- Conteúdo principal --
st.title("Dashbord de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros á esquerda")

# Métricas principais (KPIs)
st.subheader("Métricas gerais (Salários anual em USD)")

if not df_filtrado_empty:
    salario_medio =  df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrados.shape(0)
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
else:
    salario_medio, salario_mediano, salario_maximo,total_registros, cargo_mais_frequente = 0, 0, 0, ""
    col1, col2, col3, col4 = st.column(4)
    col1.metric("Salário médio", f"${salario_medio:,.0f}")
    col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
    col3.metric("Total de registros", f"${total_registros:,.0f}")
    col4.metric("Cargo mais frequente", f"${cargo_mais_frequente:,.0f}")

st.markdown("---")
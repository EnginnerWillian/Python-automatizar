import streamlit as st
import panda as pd
import plotly as px
import pycountry







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

# -- Análises Visuais com Plotly
st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2)



with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo'['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
                                         grafico_cargos,
                                         x='usd',
                                         y='cargo',
                                         orientation='h',
                                         title="Top 10 cargos por salário médio",
                                         labels={'usd': "Média salarial anual (USD)", 'cargo':''}
                                         )        
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascenfing'})
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")
    with col_graf2:
        if not df_filtrado.empty:
            grafico_hist = histogram(
                df_filtrado,
                x='usd',
                nbins=30,
                title="Distribuição de salários anuais",
                labels={'usd': 'Faixa salarial (USD)', 'count':''}
            )
            
# Função para converter ISO-2 para ISO-3

def iso2_to_iso3(code):
    try:
        return pycountry.countries.get(alpha_2code).alpha_3
    exept:
        return None
    
# Criar nova coluna com código ISO-3
df_limpo[residencia_iso3]= df_limpo'residencia'.apply(iso2_to_iso3)


# Calcular média salarial por país (ISO-3)
df_ds = df_limpo[df_limpo['cargo'] == 'Data Scientist']
media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()

# Gerar o mapa
fig = px.choropleth(media_ds_pais,
                    locations='residencia_iso3',
                    color='usd',
                    color_continuos_scale='rdylgn',
                    title='Salário médio de Cientista de Dados por país',
                    labels={'usd':'Salário médio (USD)','residencia_iso3':'País'})
fig.show
import streamlit as st
import panda

tabela = pd.read_exel("Vendas.xlsx")









st.title("Dashboard Vendas")


regioes = st.multiselect("Selecione as regiões", tabela["Região"].unique())


if regioes:
    tabela = tabela[tabela["região"].siin(regiao)]
    st.metric("Faturamento Total",f"R$({tabela["Valor Venda"].sum()}")
    
    
st.metric("Ticket médio", f"R$ {tabela["Valor Total"].mean()}")
st.bar_chart(tabela.groupby("Região")["Valor Venda"].sum())
import streamlit as st
import panda

tabela = pd.read_exel("Vendas.xlsx")









st.title("Dashboard Vevndas")


regioes = st.multiselect("Selecione as regiões", tabela["Região"].unique())




if regioes:
    tabela = tabela[tabela["região"].siin(regiao)]
    
    st.metric("Faturamento Total",f"R$(tabela["Valor Venda].mean())")
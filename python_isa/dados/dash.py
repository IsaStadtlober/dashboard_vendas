import pandas as pd
import streamlit as st 
import plotly.express as px 

st.set_page_config(
    page_title = 'vendas',
    page_icon = '📊',
    layout='wide'
)

tabela = pd.read_excel('vendas.xlsx')
print(tabela)

st.title('📊Dashboard de vendas')

# campo de seleção e filtro dos dados

st.sidebar.header("🔍 Filtros")
regioes = st.sidebar.multiselect('Selecione as regiões', tabela['Região'].unique())

if regioes:
    tabela = tabela[tabela['Região'].isin(regioes)] 

# 2 métricas 
#faturamento total 
st.metric('Faturamento total', f"R${tabela['Valor Venda'].sum()}")

#ticket médio
st.metric('Ticket médio', f"R${tabela['Valor Venda'].median()}")

# gráfico faturamento por região
st.bar_chart(tabela.groupby('Região')['Valor Venda'].sum())

# gráfico faturamento por produto 
st.bar_chart(tabela.groupby('Produto')['Valor Venda'].sum())


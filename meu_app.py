import streamlit as st
import pandas as pd
st.set_page_config(page_title="Meu site Streamlit")

with st.container():
    st.subheader("Meu primeiro site com Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações sobre os contratos fechados pela empresa")
import streamlit as st 

st.write("Acesse nosso site [Aqui](http://www.utfpr.edu.br/)")

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

with st.container():
    st.write("___")
    qtde_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D"])
    num_dias =int(qtde_dias.replace("D", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    
    st.area_chart(dados, x="Data", y="Contratos")


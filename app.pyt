import streamlit as st
st.title("Quiz interativo de ciências!!")
st.write("cada pergunta vale 1 ponto")
pergunta1 = st.radio(
"Qual é o resultado de um Oxigênio e 2 Hidrogênios?", 
("água", "combustível de foguete", "gas carbonico", "ar respirável"),
index=None,
key="pergunta1"
)                      
if pergunta1 is not None:
    if pergunta1 == "água": 
        st.success("Resposta correta! Você ganhou 1 ponto.")
    else: 
        st.error("Resposta incorreta! A resposta correta é água.")
# procoding 
# vou  usar a biblioteca
import streamlit as st


st.title('CALCULADORA...')


n1  = st.number_input('numero:', )
n2  = st.number_input('numero:', value = 0.0)


soma, sub, div, mult = st.columns(4)
if soma.button('Soma'):
    calcular   =  n1  + n2 
    st.success(calcular)
elif sub.button('subtração'):    
    calcular   =  n1  - n2 
    st.success(calcular)    
elif div.button('Divisão'):    
    calcular   =  n1  / n2 
    st.success(calcular)       
elif mult.button('Multiplicação'):    
    calcular   =  n1  * n2 
    st.success(calcular)
 #-------------------------------------------------------------------------------------------------

st.title('Desafio 1: Cartão de visitas Digital')

st.header('CARTÃO DE VISITA')

st.text('Isso é um texto streamlit')

#--------------------------------------------------------------------------------------------------

st.title('Desafio 2: Formulário de Cadastro de Usuário')

st.text_input('Nome: ')

st.number_input("Idade: ",value=None, placeholder="Digite sua idade...")

st.checkbox('Booleano')

st.button('Enviar')

#---------------------------------------------------------------------------------------------------

st.title('Desafio 3: O Seletor de Cursos')

st.selectbox('Escolha apenas um curso', ('Python', 'Web'))

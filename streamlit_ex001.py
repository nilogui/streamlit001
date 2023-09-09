# https://www.tabnews.com.br/LucasEd/um-breve-guia-de-como-usar-o-streamlit

import streamlit as st

st.title("Meu primeiro aplicativo Streamlit")

if st.button("Clique aqui"):
  st.write("Voce clicou no botao!")

# Adicionar uma caixa de selecao
opcoes = ["Opcao 1", "Opcao 2", "Opcao 3"]
escolha = st.selectbox("Escolha uma opcao:", opcoes)
st.write("Voce escolheu: ", escolha)

# Adicionar um campo de entrada de texto
nome = st.text_input("Qual e o seu nome?")
st.write("Ola, ", nome)

# Adicionar um grafico
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4])
# st.pyplot()

# fig, ax = plt.subplots()
# ax.scatter([1, 2, 3], [1, 2, 3])
# ... other plotting actions ...
# st.pyplot(fig)

# https://docs.streamlit.io/library/get-started/main-concepts
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

import numpy as np

st.write("Another example:")
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

st.write("More One:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

st.write("last One:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

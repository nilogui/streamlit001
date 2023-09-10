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

st.write("Last One:")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

st.write("Draw a line chart right now:")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write("Plot a map:")
map_data = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.write("A Slider:")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.write("A Text:")
import streamlit as st
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

st.write("A Dataframe:")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

st.write("A selectbox:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

# https://docs.streamlit.io/library/api-reference/charts/st.area_chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['col1', 'col2', 'col3'])

st.area_chart(
    chart_data,
    x='col1',
    y=['col2', 'col3'],
    color=['#FF0000','#0000FF']  # Optional
)




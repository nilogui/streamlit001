import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

import pandas as pd
import numpy as np
# https://mainpagepy-hmtjm6tcqjuyqe5kbuamnj.streamlit.app/
chart_data = pd.DataFrame({
    'col1' : np.random.randn(20),
    'col2' : np.random.randn(20),
    'col3' : np.random.choice(['A','B','C'],20)
})

st.bar_chart(
    chart_data,
    x='col1',
    y='col2',
    color='col3'
)



import matplotlib.pyplot as plt

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)


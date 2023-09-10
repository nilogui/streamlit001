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





import altair as alt

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)




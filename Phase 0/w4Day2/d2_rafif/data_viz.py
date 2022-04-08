import streamlit as st
import numpy as np

def app():
    st.title('Data Visualization')

    st.header('Section 1')

    st.markdown('Demo Page for Data Visualization')

    st.header('Columns using ratio partitioning')
    col1, col2 = st.columns([3, 1])
    data = np.random.randn(10, 1)

    col1.subheader("A wide column with a chart")
    col1.line_chart(data)

    col2.subheader("A narrow column with the data")
    col2.write(data)

st.header('This is outside function')